from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# ============================================================
# DASHBOARD WYNIKÓW ANKIETY
# Plik przeznaczony do umieszczenia w folderze pages/
# Wymagany plik danych: odpowiedzi_ankieta_przygotowane.xlsx
# ============================================================

# Kolory zgodne z zieloną stylistyką projektu
GREEN = "#16845B"
DARK = "#123B2D"
LIGHT_GREEN = "#EAF5EF"
TEXT = "#23352D"

st.markdown(
    """
    <style>
    .block-container {padding-top: 2rem; padding-bottom: 3rem; max-width: 1500px;}
    [data-testid="stMetric"] {
        background: #F1F7F3; border: 1px solid #DCEBE1;
        padding: 17px 19px; border-radius: 14px;
    }
    [data-testid="stMetricLabel"] {color: #557064 !important;}
    [data-testid="stMetricValue"] {color: #123B2D !important;}
    div[data-testid="stMultiSelect"] label {font-weight: 600;}
    .section-note {color: #60756A; font-size: 0.92rem; margin-top: -8px;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Ścieżka jest wyznaczana względem folderu projektu, a nie bieżącego katalogu.
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "odpowiedzi_ankieta_przygotowane.xlsx"

# Jeśli plik strony zostanie uruchomiony bezpośrednio z folderu głównego,
# sprawdź również lokalizację obok skryptu.
if not DATA_PATH.exists():
    DATA_PATH = Path(__file__).resolve().parent / "odpowiedzi_ankieta_przygotowane.xlsx"


@st.cache_data
def load_data(path: str, modified: float):
    respondents = pd.read_excel(path, sheet_name="Respondenci")
    multiple = pd.read_excel(path, sheet_name="Odpowiedzi_wielokrotne")

    respondents["ID_respondenta"] = respondents["ID_respondenta"].astype(str)
    multiple["ID_respondenta"] = multiple["ID_respondenta"].astype(str)

    # Usunięcie przypadkowych spacji z pól tekstowych.
    for frame in (respondents, multiple):
        for col in frame.select_dtypes(include=["object"]).columns:
            frame[col] = frame[col].map(
                lambda value: value.strip() if isinstance(value, str) else value
            )
    return respondents, multiple


if not DATA_PATH.exists():
    st.error(
        "Nie znaleziono pliku odpowiedzi_ankieta_przygotowane.xlsx. "
        "Umieść go w głównym folderze projektu, obok app.py."
    )
    st.stop()

try:
    respondents, multiple = load_data(str(DATA_PATH), DATA_PATH.stat().st_mtime)
except Exception as exc:
    st.error(f"Nie udało się wczytać danych ankiety: {exc}")
    st.stop()

# Nazwy pytań w arkuszu Respondenci
AGE = "W jakim jesteś przedziale wiekowym?"
REGULAR = "Czy obecnie regularnie odkładasz część swoich pieniędzy?"
CALCULATOR = "Czy kiedykolwiek korzystałeś(-aś) z internetowego kalkulatora oszczędności lub kalkulatora finansowego?"
CURRENT_FORMS = "Z których form oszczędzania lub inwestowania obecnie korzystasz?"
GOALS = "Na jaki cel najchętniej odkładał(a)byś pieniądze?"
BARRIERS = "Co najbardziej utrudnia Ci regularne oszczędzanie?"
KNOWN_FORMS = "Które z poniższych form oszczędzania/ inwestowania znasz?"
EXTRA_500 = "Wyobraź sobie, że każdego miesiąca dysponujesz dodatkową kwotą 500 zł, której nie musisz przeznaczać na bieżące wydatki. Co najprawdopodobniej byś z nią zrobił(a)?"
PREFERRED_FORM = "Gdybyś miał(a) dziś odłożyć pieniądze na okres około 2–3 lat, którą formę najchętniej byś wybrał(a)?"
KNOWLEDGE_1 = "8. W jakim celu można nabyć obligacje skarbowe?"
KNOWLEDGE_2 = "Co oznacza kapitalizacja odsetek?"
KNOWLEDGE_3 = "Jeśli inflacja wynosi 5% rocznie, a pieniądze na koncie nie są oprocentowane, co dzieje się z ich siłą nabywczą?"
CALC_BARRIERS = "Jeśli nie korzystasz z takich kalkulatorów lub robisz to rzadko, dlaczego?"
CALC_ENCOURAGE = "Co najbardziej zachęciłoby Cię do korzystania z kalkulatora oszczędności?"
AUTOMATION = "Czy automatyzacja oszczędzania, np. automatyczne przelewanie określonej kwoty na konto oszczędnościowe po otrzymaniu wynagrodzenia, pomogłaby Ci oszczędzać regularniej?"
DIGITAL_FEATURES = "Które funkcje cyfrowego narzędzia do planowania oszczędności i zarządzania pieniędzmi byłyby dla Ciebie najbardziej przydatne?"

st.title("Wyniki ankiety")
st.caption("Analiza odpowiedzi respondentów dotyczących oszczędzania, inwestowania i narzędzi finansowych.")

# Callback uruchamia się przed ponownym utworzeniem widgetów,
# dzięki czemu można bezpiecznie wyczyścić ich stan.
def clear_survey_filters():
    for key in ("survey_age", "survey_regular", "survey_calculator", "survey_forms"):
        st.session_state[key] = []


# ----------------------- FILTRY -------------------------------

st.markdown("### Filtry")
st.markdown(
    '<p class="section-note">Brak wyboru w danym filtrze oznacza uwzględnienie wszystkich odpowiedzi.</p>',
    unsafe_allow_html=True,
)

st.button(
    "Wyczyść wszystkie filtry",
    type="secondary",
    on_click=clear_survey_filters,
)

f1, f2, f3, f4 = st.columns(4)

def options_for(column):
    if column not in respondents.columns:
        return []
    values = respondents[column].dropna().astype(str).unique().tolist()
    return sorted(values)

with f1:
    selected_age = st.multiselect("Grupa wiekowa", options_for(AGE), key="survey_age")
with f2:
    selected_regular = st.multiselect("Regularne oszczędzanie", options_for(REGULAR), key="survey_regular")
with f3:
    selected_calculator = st.multiselect("Korzystanie z kalkulatorów", options_for(CALCULATOR), key="survey_calculator")

# Filtr form obecnie wykorzystywanych jest pobierany z tabeli odpowiedzi wielokrotnych.
form_options = []
if "Pytanie" in multiple.columns and "Odpowiedz" in multiple.columns:
    form_options = sorted(
        multiple.loc[multiple["Pytanie"] == CURRENT_FORMS, "Odpowiedz"]
        .dropna().astype(str).unique().tolist()
    )
with f4:
    selected_forms = st.multiselect("Obecnie używane formy", form_options, key="survey_forms")

# Pusta lista = brak filtrowania. Filtry łączą się warunkiem AND.
filtered = respondents.copy()

if selected_age and AGE in filtered.columns:
    filtered = filtered[filtered[AGE].astype(str).isin(selected_age)]

if selected_regular and REGULAR in filtered.columns:
    filtered = filtered[filtered[REGULAR].astype(str).isin(selected_regular)]

if selected_calculator and CALCULATOR in filtered.columns:
    filtered = filtered[filtered[CALCULATOR].astype(str).isin(selected_calculator)]

if selected_forms:
    form_ids = multiple.loc[
        (multiple["Pytanie"] == CURRENT_FORMS)
        & (multiple["Odpowiedz"].astype(str).isin(selected_forms)),
        "ID_respondenta",
    ].dropna().astype(str).unique()
    filtered = filtered[filtered["ID_respondenta"].isin(form_ids)]

filtered_ids = set(filtered["ID_respondenta"].astype(str))
filtered_multiple = multiple[multiple["ID_respondenta"].isin(filtered_ids)].copy()

st.caption(f"Zakres analizy: **{len(filtered):,} z {len(respondents):,} respondentów**".replace(",", " "))

st.divider()

# ----------------------- KPI ----------------------------------

def share_text(numerator, denominator):
    if denominator == 0:
        return "—"
    return f"{numerator / denominator:.1%}".replace(".", ",")

n = len(filtered)
regular_yes = 0
if REGULAR in filtered.columns:
    regular_yes = filtered[REGULAR].astype(str).str.startswith("Tak", na=False).sum()

calculator_yes = 0
if CALCULATOR in filtered.columns:
    calculator_yes = filtered[CALCULATOR].astype(str).str.startswith("Tak", na=False).sum()

k1, k2, k3 = st.columns(3)
k1.metric("Liczba respondentów", f"{n:,}".replace(",", " "))
k2.metric("Regularnie oszczędzający", share_text(regular_yes, n), f"{regular_yes} osób")
k3.metric("Korzystający z kalkulatorów", share_text(calculator_yes, n), f"{calculator_yes} osób")

if n == 0:
    st.warning("Wybrane filtry nie zwróciły żadnych respondentów. Zmień lub wyczyść filtry.")
    st.stop()


# ----------------------- FUNKCJE WYKRESÓW ---------------------

def render_fixed_pie(data, label_col, value_col, title):
    """
    Rysuje wykresy o stałej wielkości. Legendę renderujemy poza Plotly,
    aby liczba pozycji legendy nie zmieniała średnicy koła.
    """
    import plotly.graph_objects as go

    labels = data[label_col].astype(str).tolist()
    values = data[value_col].tolist()
    palette = px.colors.qualitative.Set2
    colors = [palette[i % len(palette)] for i in range(len(labels))]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.38,
                sort=False,
                direction="clockwise",
                marker=dict(colors=colors, line=dict(color="rgba(0,0,0,0)", width=0)),
                textposition="inside",
                textinfo="percent",
                insidetextfont=dict(color="#FFFFFF", size=12),
                hovertemplate="<b>%{label}</b><br>Liczba: %{value}<br>Udział: %{percent}<extra></extra>",
                showlegend=False,
                domain=dict(x=[0.16, 0.84], y=[0.02, 0.98]),
            )
        ]
    )

    fig.update_layout(
        title=dict(text=title, x=0.02, xanchor="left", y=0.98, yanchor="top"),
        height=330,
        margin=dict(l=8, r=8, t=48, b=8),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=TEXT),
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    # Własna legenda HTML nie wpływa na rozmiar wykresu kołowego.
    legend_items = []
    for label, color, value in zip(labels, colors, values):
        safe_label = (
            str(label).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;")
        )
        legend_items.append(
            f'<div style="display:flex;align-items:flex-start;gap:8px;'
            f'margin:3px 0;font-size:12px;line-height:1.35;color:{TEXT};">'
            f'<span style="display:inline-block;flex:0 0 10px;width:10px;height:10px;'
            f'margin-top:3px;border-radius:2px;background:{color};"></span>'
            f'<span>{safe_label}</span></div>'
        )
    st.markdown(
        '<div style="display:grid;grid-template-columns:1fr;gap:1px;'
        'padding:0 8px 8px 8px;">' + "".join(legend_items) + "</div>",
        unsafe_allow_html=True,
    )


def single_chart(frame, column, title, horizontal=True, top_n=None):
    if column not in frame.columns:
        st.info(f"Brak kolumny: {column}")
        return
    data = (
        frame[column].dropna().astype(str)
        .value_counts().rename_axis("Odpowiedź")
        .reset_index(name="Liczba")
    )
    if top_n:
        data = data.head(top_n)
    if data.empty:
        st.info("Brak danych dla tego pytania.")
        return
    render_fixed_pie(data, "Odpowiedź", "Liczba", title)


def multiple_chart(frame, question, title, top_n=None):
    data = frame.loc[frame["Pytanie"] == question].copy()
    if data.empty:
        st.info("Brak odpowiedzi dla tego pytania w wybranej grupie.")
        return

    # Liczymy unikalnych respondentów dla każdej opcji.
    data = (
        data.groupby("Odpowiedz")["ID_respondenta"]
        .nunique().sort_values(ascending=False)
        .reset_index(name="Respondenci")
    )
    if top_n:
        data = data.head(top_n)
    render_fixed_pie(data, "Odpowiedz", "Respondenci", title)


# ----------------------- ZAKŁADKI -----------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "Oszczędzanie",
    "Wiedza finansowa",
    "Kalkulatory i narzędzia",
    "Preferencje",
])

with tab1:
    st.subheader("Nawyki i bariery oszczędzania")
    a, b = st.columns(2)
    with a:
        single_chart(filtered, REGULAR, "Czy respondenci regularnie oszczędzają?")
    with b:
        multiple_chart(filtered_multiple, BARRIERS, "Największe bariery oszczędzania")
    a, b = st.columns(2)
    with a:
        multiple_chart(filtered_multiple, GOALS, "Cele oszczędzania")
    with b:
        single_chart(filtered, EXTRA_500, "Co respondenci zrobiliby z dodatkowymi 500 zł?")

with tab2:
    st.subheader("Poziom wiedzy finansowej")
    a, b = st.columns(2)
    with a:
        single_chart(filtered, KNOWLEDGE_1, "Wiedza o obligacjach skarbowych")
        single_chart(filtered, KNOWLEDGE_2, "Rozumienie kapitalizacji odsetek")
    with b:
        single_chart(filtered, KNOWLEDGE_3, "Rozumienie wpływu inflacji")

    st.divider()
    st.subheader("Udział prawidłowych odpowiedzi według wieku")
    st.caption(
        "Dla każdego pytania pokazany jest odsetek prawidłowych odpowiedzi "
        "wśród wszystkich ważnych odpowiedzi udzielonych przez daną grupę wiekową."
    )

    correct_answers = {
        KNOWLEDGE_1: "Aby pożyczyć pieniądze państwu, które zobowiązuje się do ich zwrotu na określonych warunkach.",
        KNOWLEDGE_2: "Dopisywanie naliczonych odsetek do kapitału, od którego mogą być naliczane kolejne odsetki.",
        KNOWLEDGE_3: "Spada, ponieważ za tę samą kwotę można kupić mniej.",
    }

    question_labels = {
        KNOWLEDGE_1: "Obligacje skarbowe",
        KNOWLEDGE_2: "Kapitalizacja odsetek",
        KNOWLEDGE_3: "Wpływ inflacji",
    }

    age_results = []
    if AGE in filtered.columns:
        for question, correct_answer in correct_answers.items():
            if question not in filtered.columns:
                continue

            question_data = filtered[[AGE, question]].dropna().copy()
            question_data[AGE] = question_data[AGE].astype(str).str.strip()
            question_data[question] = question_data[question].astype(str).str.strip()

            # Odrzucamy puste wartości i ewentualny powtórzony tekst nagłówka,
            # który może pojawić się w danych jako odpowiedź.
            question_data = question_data[
                (question_data[AGE] != "")
                & (question_data[question] != "")
                & (question_data[question] != question)
            ]

            if question_data.empty:
                continue

            grouped = question_data.groupby(AGE)[question].agg(
                liczba_odpowiedzi="count",
                liczba_poprawnych=lambda values: values.eq(correct_answer).sum(),
            ).reset_index()

            grouped["Udział prawidłowych odpowiedzi"] = (
                grouped["liczba_poprawnych"] / grouped["liczba_odpowiedzi"] * 100
            )
            grouped["Pytanie"] = question_labels[question]
            age_results.append(
                grouped[[AGE, "Pytanie", "Udział prawidłowych odpowiedzi", "liczba_odpowiedzi"]]
            )

    if age_results:
        age_chart_data = pd.concat(age_results, ignore_index=True)

        # Zachowaj kolejność grup wiekowych występującą w danych.
        age_order = respondents[AGE].dropna().astype(str).drop_duplicates().tolist()
        age_order = [age for age in age_order if age in age_chart_data[AGE].unique()]

        fig_age = px.bar(
            age_chart_data,
            x=AGE,
            y="Udział prawidłowych odpowiedzi",
            color="Pytanie",
            barmode="group",
            category_orders={AGE: age_order},
            text=age_chart_data["Udział prawidłowych odpowiedzi"].map(
                lambda value: f"{value:.1f}%".replace(".", ",")
            ),
            color_discrete_sequence=["#62BFA4", "#FF916B", "#8EA4D2"],
            hover_data={"liczba_odpowiedzi": True, "Udział prawidłowych odpowiedzi": ":.1f"},
        )
        fig_age.update_layout(
            height=470,
            margin=dict(l=15, r=20, t=35, b=20),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color=TEXT),
            xaxis_title="Grupa wiekowa",
            yaxis_title="Udział prawidłowych odpowiedzi",
            yaxis=dict(range=[0, 100], ticksuffix="%", gridcolor="rgba(80,110,90,0.12)"),
            legend_title_text="",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        )
        fig_age.update_traces(textposition="outside", cliponaxis=False)
        st.plotly_chart(fig_age, use_container_width=True)
    else:
        st.info("Nie udało się obliczyć udziału prawidłowych odpowiedzi dla grup wiekowych.")

with tab3:
    st.subheader("Korzystanie z kalkulatorów i potrzeby użytkowników")
    a, b = st.columns(2)
    with a:
        single_chart(filtered, CALCULATOR, "Czy respondenci korzystali z kalkulatorów?")
        multiple_chart(filtered_multiple, CALC_BARRIERS, "Dlaczego respondenci nie korzystają z kalkulatorów?")
    with b:
        multiple_chart(filtered_multiple, CALC_ENCOURAGE, "Co zachęciłoby do korzystania z kalkulatora?")
        single_chart(filtered, AUTOMATION, "Czy automatyzacja pomagałaby oszczędzać?")

with tab4:
    st.subheader("Znajomość i wybór form oszczędzania")
    a, b = st.columns(2)
    with a:
        multiple_chart(filtered_multiple, KNOWN_FORMS, "Znane formy oszczędzania i inwestowania")
    with b:
        multiple_chart(filtered_multiple, CURRENT_FORMS, "Obecnie wykorzystywane formy")
    a, b = st.columns(2)
    with a:
        single_chart(filtered, PREFERRED_FORM, "Preferowana forma na okres 2–3 lat")
    with b:
        multiple_chart(filtered_multiple, DIGITAL_FEATURES, "Najbardziej przydatne funkcje narzędzia cyfrowego")

with st.expander("Pokaż tabelę respondentów uwzględnionych w analizie"):
    st.dataframe(filtered, use_container_width=True, hide_index=True)

st.caption("W pytaniach wielokrotnego wyboru jedna osoba może wskazać kilka opcji. Wykresy pokazują liczbę unikalnych respondentów dla każdej opcji; sumy mogą przekraczać 100%.")
