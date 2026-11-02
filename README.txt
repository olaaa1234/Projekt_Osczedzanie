PROJEKT: OSZCZĘDZANIE BEZ TAJEMNIC

Uruchomienie w Windows / PowerShell:
1. Otwórz folder projektu w VS Code.
2. W terminalu wykonaj:
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   python -m streamlit run app.py

Strony projektu:
- Wprowadzenie
- Dlaczego nie oszczędzamy? (teoria i źródła)
- Ankieta i wyniki (pytania ankietowe oraz import CSV/XLSX)
- Kalkulator oszczędności (przeniesiony z zielonej wersji poprzedniego projektu)

Ankieta:
Pytania można przenieść do Google Forms lub Microsoft Forms. Po zebraniu odpowiedzi wyeksportuj je do CSV/XLSX i wczytaj na stronie „Ankieta i wyniki”. Każdy wiersz powinien odpowiadać jednemu respondentowi.

Uwaga:
Projekt ma charakter edukacyjny. Kalkulator nie stanowi rekomendacji ani oferty produktu finansowego. Wyniki ankiety należy opisać zgodnie z rzeczywistą metodą doboru próby; mała próba wygodna nie jest reprezentatywna dla całej Polski.
