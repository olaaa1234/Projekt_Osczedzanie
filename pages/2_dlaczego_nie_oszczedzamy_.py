import streamlit as st

# ============================================================
# WPROWADZENIE
# ============================================================

st.markdown(
    """
    <div class="hero">
        <div class="kicker">Część 01 · Diagnoza problemu</div>
        <h1>Dlaczego oszczędzanie bywa trudne?</h1>
        <p>
            Nie istnieje jedna przyczyna. Decyzje finansowe są wynikiem
            ograniczeń budżetowych, wiedzy, emocji, nawyków oraz zaufania
            do dostępnych narzędzi.
        </p>
        <span class="chip">Bariery ekonomiczne · psychologiczne · informacyjne</span>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# SKALA ZJAWISKA – DANE Z BADANIA BANKU MILLENNIUM
# ============================================================

st.markdown(
    '<div class="section">Jak wygląda oszczędzanie i inwestowanie w Polsce?</div>',
    unsafe_allow_html=True
)

source_url = "https://www.bankmillennium.pl/o-banku/centrum-prasowe/informacje-prasowe/-/news/finanse-polakow-co-piaty-z-nas-nie-ma-zadnych-oszczednosci?id=33798636"

# Wskaźniki dotyczące oszczędzania – baza: wszyscy respondenci
row1 = st.columns(3)

with row1[0]:
    st.metric("Zbyt niskie zarobki jako powód nieoszczędzania", "48%")
    st.caption("Wśród osób, które nie oszczędzają i wskazały powód.")

with row1[1]:
    st.metric("Nie ma żadnych oszczędności", "18%")
    st.caption("Wszyscy respondenci.")

with row1[2]:
    st.metric("Stara się oszczędzać regularnie", "35%")
    st.caption("Wszyscy respondenci.")

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

row2 = st.columns(4)

with row2[0]:
    st.metric("Oszczędza co miesiąc lub częściej", "64%")
    st.caption("Wśród osób oszczędzających.")

with row2[1]:
    st.metric("Konta oszczędnościowe i lokaty", "64%")
    st.caption("Wśród oszczędzających, którzy wskazali formę.")

with row2[2]:
    st.metric("Obligacje Skarbu Państwa", "8%")
    st.caption("Wśród oszczędzających, którzy wskazali formę.")

with row2[3]:
    st.metric("Akcje", "6%")
    st.caption("Wśród oszczędzających, którzy wskazali formę.")



st.markdown(
    f"**Źródło:** Bank Millennium, *Finanse Polaków* (badanie z 6–12 czerwca 2025 r.), "
    f"Ogólnopolski Panel Badawczy Ariadna, reprezentatywna próba 1046 dorosłych osób. "
    f"[Otwórz pełne wyniki badania]({source_url})"
)

st.caption(
    "Uwaga: wartości mają różne podstawy procentowania. 48% dotyczy osób "
    "nieoszczędzających, które wskazały przyczynę; 64% dotyczące częstotliwości "
    "oraz form przechowywania oszczędności odnoszą się do osób oszczędzających. "
    "Pozostałe wskaźniki dotyczą wszystkich respondentów. Wyników nie należy "
    "sumować ani bezpośrednio porównywać."
)

# ============================================================
# BARIERY EKONOMICZNE
# ============================================================

st.markdown(
    '<div class="section">1. Bariery ekonomiczne</div>'
    '<div class="lead">Nie każdy brak oszczędności wynika z braku motywacji.</div>',
    unsafe_allow_html=True
)

a, b = st.columns(2)

with a:
    st.markdown(
        """
        <div class="card">
            <div class="tag">MOŻLIWOŚCI FINANSOWE</div>
            <h3>Niski dochód i wysokie koszty życia</h3>
            <p>
                Jeżeli większość dochodu pochłaniają mieszkanie, żywność,
                transport i zobowiązania, przestrzeń do odkładania pieniędzy
                jest ograniczona. W takiej sytuacji rada „po prostu oszczędzaj”
                może być niewystarczająca.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with b:
    st.markdown(
        """
        <div class="card">
            <div class="tag">NIEPEWNOŚĆ</div>
            <h3>Nieregularne dochody i nieprzewidziane wydatki</h3>
            <p>
                Zmienne zarobki, naprawy, leczenie czy inne nagłe koszty
                utrudniają utrzymanie stałej kwoty wpłat. Oszczędności bywają
                wtedy wykorzystywane do bieżącego łatania budżetu.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# BARIERY PSYCHOLOGICZNE
# ============================================================

st.markdown(
    '<div class="section">2. Bariery psychologiczne i behawioralne</div>',
    unsafe_allow_html=True
)

a, b, c = st.columns(3)

for col, title, desc in [
    (
        a,
        "Preferencja teraźniejszości",
        "Natychmiastowa korzyść z wydania pieniędzy może wydawać się bardziej atrakcyjna niż odległy efekt regularnego oszczędzania."
    ),
    (
        b,
        "Brak konkretnego celu",
        "Ogólne postanowienie „będę oszczędzać” jest mniej motywujące niż mierzalny cel, kwota i termin."
    ),
    (
        c,
        "Brak nawyku",
        "Jeśli odkładanie nie jest zautomatyzowane ani wpisane w miesięczny budżet, łatwo o nim zapomnieć lub przesunąć je na później."
    )
]:
    with col:
        st.markdown(
            f'<div class="card"><h3>{title}</h3><p>{desc}</p></div>',
            unsafe_allow_html=True
        )

# ============================================================
# BARIERY WIEDZY I NARZĘDZI
# ============================================================

st.markdown(
    '<div class="section">3. Bariery wiedzy i korzystania z narzędzi</div>',
    unsafe_allow_html=True
)

a, b = st.columns(2)

with a:
    st.markdown(
        """
        <div class="card">
            <h3>Niska pewność w podejmowaniu decyzji</h3>
            <p>
                Nieznajomość procentu składanego, podatków, inflacji czy różnic
                między produktami może powodować odkładanie decyzji.
                Ważne jest jednak odróżnienie braku wiedzy od braku środków.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with b:
    st.markdown(
        """
        <div class="card">
            <h3>Niedopasowane lub niezrozumiałe kalkulatory</h3>
            <p>
                Zbyt wiele pól, niezrozumiałe pojęcia, brak wyjaśnienia założeń
                albo obawa o wiarygodność wyniku mogą zniechęcać do użycia
                narzędzia. Prostota i przejrzystość mają znaczenie.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# DODATKOWE RAPORTY I ŹRÓDŁA
# ============================================================

st.markdown(
    '<div class="section">Co jeszcze mówią badania?</div>'
    '<div class="lead">Raporty i opracowania, które pomagają zrozumieć '
    'zachowania finansowe, poziom wiedzy i sytuację gospodarstw domowych.</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="card">
        <div class="tag">FUNDACJA THINK! · 2024</div>
        <h3>Postawy Polaków wobec finansów</h3>
        <p>
            Badanie Katarzyny Sekścińskiej przeprowadzone we wrześniu 2024 r.
            metodą CAWI na reprezentatywnej próbie 1182 dorosłych Polaków.
            Raport opisuje m.in. zachowania oszczędnościowe, inwestowanie,
            poczucie bezpieczeństwa finansowego i wiedzę finansową.
        </p>
        <a href="https://rozwijamy.edu.pl/wp-content/uploads/2024/10/Raport_Postawy_Polakow_wobec_finansow_2024.pdf" target="_blank">Otwórz raport (PDF)</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="card">
        <div class="tag">OECD · 2023</div>
        <h3>Krajowa Strategia Edukacji Finansowej dla Polski</h3>
        <p>
            Opracowanie przedstawia wyzwania związane z edukacją finansową
            w Polsce oraz wskazuje obszary, w których rozwijanie kompetencji
            finansowych może wspierać codzienne decyzje gospodarstw domowych.
        </p>
        <a href="https://www.oecd.org/pl/publications/2023/04/national-strategy-for-financial-education-for-poland_6fd5288f.html" target="_blank">Otwórz raport OECD</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="card">
        <div class="tag">GUS · 2026</div>
        <h3>Sytuacja gospodarstw domowych w 2025 r.</h3>
        <p>
            Publikacja GUS przedstawia dochody, wydatki i zróżnicowanie
            sytuacji materialnej gospodarstw domowych. To ważny kontekst
            do oceny, ile środków może pozostawać na oszczędności.
        </p>
        <a href="https://stat.gov.pl/obszary-tematyczne/warunki-zycia/dochody-wydatki-i-warunki-zycia-ludnosci/sytuacja-gospodarstw-domowych-w-2025-r-w-swietle-badania-budzetow-gospodarstw-domowych%2C3%2C25.html" target="_blank">Otwórz publikację GUS</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="card">
        <div class="tag">NBP · 2025</div>
        <h3>Financial System in Poland 2023</h3>
        <p>
            Raport opisuje polski system finansowy, w tym aktywa finansowe
            gospodarstw domowych i uwarunkowania wyboru form lokowania środków.
        </p>
        <a href="https://nbp.pl/wp-content/uploads/2025/03/Financial-System-in-Poland-2023.pdf" target="_blank">Otwórz raport NBP (PDF)</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="note">
        <b>Wniosek dla projektu:</b> kalkulator może pomóc zrozumieć wpływ
        regularności, czasu i oprocentowania, ale nie rozwiąże problemu
        zbyt niskich dochodów. Dlatego wyniki ankiety należy analizować
        z uwzględnieniem sytuacji materialnej respondentów.
    </div>
    """,
    unsafe_allow_html=True
)
