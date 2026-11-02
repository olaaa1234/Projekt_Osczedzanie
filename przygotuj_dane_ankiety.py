from pathlib import Path
from functools import lru_cache
import pandas as pd

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "odpowiedzi_ankieta.xlsx"
OUTPUT = BASE / "odpowiedzi_ankieta_przygotowane.xlsx"

MULTI_OPTIONS = {'Na jaki cel najchętniej odkładał(a)byś pieniądze?': ['Poduszka finansowa na nieprzewidziane wydatki.', 'Zakup mieszkania lub domu.', 'Samochód lub inny większy zakup.', 'Wakacje i przyjemności.', 'Emerytura i zabezpieczenie przyszłości.', 'Edukacja lub rozwój.', 'Nie mam konkretnego celu.'], 'Co najbardziej utrudnia Ci regularne oszczędzanie?': ['Zbyt niskie dochody w stosunku do wydatków.', 'Wysokie koszty życia i bieżące zobowiązania.', 'Brak odpowiedniego nawyku i systematyczności.', 'Brak konkretnego celu oszczędzania.', 'Wolę korzystać z pieniędzy teraz niż odkładać je na przyszłość.', 'Nie wiem, jak najlepiej zacząć oszczędzać.', 'Obawiam się utraty zgromadzonych pieniędzy.', 'Nie widzę wystarczających korzyści z oszczędzania.'], 'Które z poniższych form oszczędzania/ inwestowania znasz?': ['Gotówka przechowywana w domu.', 'Zwykłe konto osobiste (ROR).', 'Konto oszczędnościowe.', 'Lokata bankowa.', 'Obligacje skarbowe.', 'Fundusze inwestycyjne.', 'Akcje i ETF-y.', 'PPK lub PPE.', 'IKE lub IKZE.', 'Nie znam żadnej z powyższych form.'], 'Z których form oszczędzania lub inwestowania obecnie korzystasz?': ['Gotówka w domu.', 'Zwykłe konto osobiste (ROR).', 'Konto oszczędnościowe.', 'Lokata bankowa.', 'Obligacje skarbowe.', 'Fundusze inwestycyjne.', 'Akcje lub ETF-y.', 'PPK lub PPE.', 'IKE lub IKZE.', 'Nie korzystam z żadnej z powyższych form.'], 'Jeśli nie korzystasz z takich kalkulatorów lub robisz to rzadko, dlaczego?': ['Nie wiedziałem(-am), że takie narzędzia istnieją.', 'Nie wiem, gdzie znaleźć wiarygodny kalkulator.', 'Nie mam potrzeby korzystania z takich narzędzi.', 'Są dla mnie zbyt skomplikowane.', 'Nie wiem, jakie dane należy wprowadzić.', 'Nie ufam otrzymywanym wynikom.', 'Wolę samodzielnie obliczać lub planować oszczędności.', 'Nie mam wystarczającej wiedzy finansowej.'], 'Co najbardziej zachęciłoby Cię do korzystania z kalkulatora oszczędności?': ['Prosty i intuicyjny sposób obsługi.', 'Wizualizacja wzrostu oszczędności na wykresie.', 'Możliwość porównania różnych form oszczędzania.', 'Pokazanie wpływu inflacji na realną wartość pieniędzy.', 'Możliwość sprawdzenia, ile mogę zgromadzić, odkładając niewielkie kwoty.', 'Gotowe przykłady i podpowiedzi dla początkujących.', 'Wiarygodne źródła i wyjaśnienie sposobu obliczeń.', 'Możliwość korzystania bez rejestracji i podawania danych osobowych.', 'Nic – nie jestem zainteresowany(-a) takimi narzędziami.'], 'Które funkcje cyfrowego narzędzia do planowania oszczędności i zarządzania pieniędzmi byłyby dla Ciebie najbardziej przydatne?': ['Kalkulator pokazujący przyszłą wartość oszczędności.', 'Wykres pokazujący, jak rosną oszczędności w czasie.', 'Porównanie oszczędzania na koncie, lokacie i w obligacjach.', 'Pokazanie, jak inflacja zmniejsza siłę nabywczą pieniędzy.', 'Wyznaczanie celu i miesięcznej kwoty do odłożenia.', 'Przypomnienia o regularnym oszczędzaniu.', 'Symulacja automatycznego odkładania niewielkich kwot.', 'Fikcyjny portfel finansowy, w którym można testować przykładowe sposoby lokowania środków bez używania prawdziwych pieniędzy.', 'Podpowiedzi, jak podzielić i zdywersyfikować środki w zależności od celu, planowanego czasu oszczędzania i akceptowanego ryzyka.', 'Krótkie wyjaśnienia i wskazówki dotyczące finansów.', 'Żadna z powyższych funkcji.']}

def parse_multi_answer(value, allowed_options):
    if pd.isna(value) or not str(value).strip():
        return [], []
    text = " ".join(str(value).strip().split())
    ordered_options = sorted(allowed_options, key=len, reverse=True)

    @lru_cache(None)
    def walk(position):
        if position >= len(text):
            return ([], [])
        candidates = []
        for option in ordered_options:
            end = position + len(option)
            if text[position:end].casefold() == option.casefold():
                if end == len(text):
                    candidates.append(([option], []))
                elif text.startswith(", ", end):
                    next_options, next_other = walk(end + 2)
                    candidates.append(([option] + next_options, next_other))
        if candidates:
            return min(candidates, key=lambda result: (sum(map(len, result[1])), -len(result[0])))
        return ([], [text[position:].strip()])
    return walk(0)

def main():
    if not SOURCE.exists():
        raise FileNotFoundError(f"Nie znaleziono pliku źródłowego: {SOURCE}")

    df = pd.read_excel(SOURCE)
    df.columns = [str(c).strip() for c in df.columns]

    respondents = df.copy()
    respondents.insert(0, "ID_respondenta", range(1, len(respondents) + 1))
    for col in respondents.select_dtypes(include=["object"]).columns:
        respondents[col] = respondents[col].map(
            lambda x: " ".join(x.split()) if isinstance(x, str) else x
        )

    long_rows, parse_audit = [], []
    for question, allowed in MULTI_OPTIONS.items():
        if question not in respondents.columns:
            raise ValueError(f"Brak kolumny w Excelu: {question}")
        matched_count = custom_count = blank_count = 0
        for _, row in respondents.iterrows():
            raw_value = row[question]
            if pd.isna(raw_value) or not str(raw_value).strip():
                blank_count += 1
                continue
            matched, custom = parse_multi_answer(raw_value, allowed)
            for answer in matched:
                long_rows.append({
                    "ID_respondenta": row["ID_respondenta"],
                    "Pytanie": question,
                    "Odpowiedz": answer,
                    "Rodzaj_odpowiedzi": "Opcja z formularza",
                    "Odpowiedz_oryginalna": raw_value,
                })
                matched_count += 1
            for answer in custom:
                if answer:
                    long_rows.append({
                        "ID_respondenta": row["ID_respondenta"],
                        "Pytanie": question,
                        "Odpowiedz": answer,
                        "Rodzaj_odpowiedzi": "Odpowiedź własna / spoza słownika",
                        "Odpowiedz_oryginalna": raw_value,
                    })
                    custom_count += 1
        parse_audit.append({
            "Pytanie": question,
            "Liczba respondentów": len(respondents),
            "Brak odpowiedzi": blank_count,
            "Liczba rozpoznanych wskazań": matched_count,
            "Liczba odpowiedzi własnych / nierozpoznanych": custom_count,
            "Liczba opcji w słowniku": len(allowed),
        })

    long_df = pd.DataFrame(long_rows)
    audit_df = pd.DataFrame([
        {
            "Kolumna": col,
            "Liczba odpowiedzi": int(df[col].notna().sum()),
            "Braki": int(df[col].isna().sum()),
            "Liczba unikalnych wartości": int(df[col].nunique(dropna=True)),
        }
        for col in df.columns
    ])
    quality_summary = pd.DataFrame([
        {"Metryka": "Liczba respondentów", "Wartość": len(df)},
        {"Metryka": "Liczba kolumn", "Wartość": len(df.columns)},
        {"Metryka": "Duplikaty całych rekordów", "Wartość": int(df.duplicated().sum())},
        {"Metryka": "Liczba pytań wielokrotnego wyboru", "Wartość": len(MULTI_OPTIONS)},
        {"Metryka": "Liczba wierszy w tabeli odpowiedzi wielokrotnych", "Wartość": len(long_df)},
        {"Metryka": "Braki odpowiedzi łącznie", "Wartość": int(df.isna().sum().sum())},
    ])
    dictionary_df = pd.DataFrame([
        {"Pytanie": q, "Opcja": option}
        for q, opts in MULTI_OPTIONS.items() for option in opts
    ])

    with pd.ExcelWriter(OUTPUT, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Oryginalne_dane", index=False)
        respondents.to_excel(writer, sheet_name="Respondenci", index=False)
        long_df.to_excel(writer, sheet_name="Odpowiedzi_wielokrotne", index=False)
        quality_summary.to_excel(writer, sheet_name="Podsumowanie_audytu", index=False)
        audit_df.to_excel(writer, sheet_name="Audyt_kolumn", index=False)
        pd.DataFrame(parse_audit).to_excel(writer, sheet_name="Audyt_wielokrotnego", index=False)
        dictionary_df.to_excel(writer, sheet_name="Slownik_opcji", index=False)

    print(f"Zapisano przygotowane dane: {OUTPUT}")

if __name__ == "__main__":
    main()
