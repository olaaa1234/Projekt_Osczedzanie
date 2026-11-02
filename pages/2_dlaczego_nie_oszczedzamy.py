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

# Wskaźniki w formie wyróżnionych kart – zmieniono wyłącznie sposób prezentacji.
st.markdown(
    """
    <style>
    .savings-kpi-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 14px;
        margin: 18px 0 22px 0;
    }

    .savings-kpi-grid.secondary {
        grid-template-columns: repeat(4, minmax(0, 1fr));
        margin-top: 0;
    }

    .savings-kpi {
        min-height: 178px;
        box-sizing: border-box;
        padding: 20px 18px;
        border-radius: 18px;
        background: linear-gradient(145deg, #348d43 0%, #14552c 100%);
        color: #f5ffe9;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 4px 12px rgba(20, 85, 44, 0.12);
        border: 1px solid rgba(255,255,255,0.18);
    }

    .savings-kpi .value {
        color: #f5ffe9;
        font-size: clamp(2.5rem, 5vw, 3.8rem);
        line-height: 1;
        font-weight: 800;
        letter-spacing: -2px;
        margin-bottom: 13px;
    }

    .savings-kpi .label {
        color: #ffffff;
        font-size: 1rem;
        line-height: 1.35;
        font-weight: 650;
        margin-bottom: 8px;
    }

    .savings-kpi .basis {
        color: #d9f0d9;
        font-size: 0.78rem;
        line-height: 1.3;
        opacity: 0.95;
    }

    @media (max-width: 850px) {
        .savings-kpi-grid, .savings-kpi-grid.secondary {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
    }

    @media (max-width: 520px) {
        .savings-kpi-grid, .savings-kpi-grid.secondary {
            grid-template-columns: 1fr;
        }

        .savings-kpi { min-height: 145px; }
    }
    </style>

    <div class="savings-kpi-grid">
        <div class="savings-kpi">
            <div class="value">48%</div>
            <div class="label">Zbyt niskie zarobki jako powód nieoszczędzania</div>
            <div class="basis">Wśród osób nieoszczędzających, które wskazały powód</div>
        </div>
        <div class="savings-kpi">
            <div class="value">18%</div>
            <div class="label">Nie ma żadnych oszczędności</div>
            <div class="basis">Wszyscy respondenci</div>
        </div>
        <div class="savings-kpi">
            <div class="value">35%</div>
            <div class="label">Stara się oszczędzać regularnie</div>
            <div class="basis">Wszyscy respondenci</div>
        </div>
    </div>

    <div class="savings-kpi-grid secondary">
        <div class="savings-kpi">
            <div class="value">64%</div>
            <div class="label">Oszczędza co miesiąc lub częściej</div>
            <div class="basis">Wśród osób oszczędzających</div>
        </div>
        <div class="savings-kpi">
            <div class="value">64%</div>
            <div class="label">Wybiera konta oszczędnościowe i lokaty</div>
            <div class="basis">Wśród oszczędzających, którzy wskazali formę</div>
        </div>
        <div class="savings-kpi">
            <div class="value">8%</div>
            <div class="label">Wybiera obligacje Skarbu Państwa</div>
            <div class="basis">Wśród oszczędzających, którzy wskazali formę</div>
        </div>
        <div class="savings-kpi">
            <div class="value">6%</div>
            <div class="label">Wybiera akcje</div>
            <div class="basis">Wśród oszczędzających, którzy wskazali formę</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    f"**Źródło:** Bank Millennium, *Finanse Polaków* (badanie z 6–12 czerwca 2025 r.), "
    f"Ogólnopolski Panel Badawczy Ariadna, reprezentatywna próba 1046 dorosłych osób. "
    f"[Otwórz pełne wyniki badania]({source_url})"
)


# ============================================================
# DODATKOWE WSKAŹNIKI – DWA NAJNOWSZE BADANIA (2025–2026)
# ============================================================

think_url = "https://www.think.org.pl/wp-content/uploads/2025/10/Raport_Postawy-Polakow-wobec-finansow_2025_www_v1.pdf"

# Wspólna sekcja danych – bez dodatkowego nagłówka

st.markdown(
    """
    <style>
    .recent-kpi-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 14px;
        margin: 18px 0 18px 0;
    }

    .recent-kpi-grid.wib-kpi-grid {
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 12px;
    }

    .recent-kpi-grid.wib-kpi-grid .recent-kpi {
        min-height: 160px;
        padding: 16px 15px;
    }

    .recent-kpi-grid.wib-kpi-grid .value {
        font-size: clamp(2rem, 3.2vw, 3rem);
        margin-bottom: 10px;
    }

    .recent-kpi-grid.wib-kpi-grid .label {
        font-size: 0.92rem;
        line-height: 1.3;
    }

    .recent-kpi-grid.wib-kpi-grid .basis {
        font-size: 0.72rem;
    }

    .recent-kpi {
        min-height: 178px;
        box-sizing: border-box;
        padding: 20px 18px;
        border-radius: 18px;
        background: linear-gradient(145deg, #347f78 0%, #174e4b 100%);
        color: #f1fffc;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 4px 12px rgba(23, 78, 75, 0.13);
        border: 1px solid rgba(255,255,255,0.2);
    }

    /* Karty badania WIB/GPW – nowy odcień zieleni.
       Karty Fundacji Think! zachowują wcześniejszy kolor. */
    .recent-kpi.wib-kpi {
        background: linear-gradient(145deg, #6F9F63 0%, #3F7548 100%);
        color: #F7FFF3;
        box-shadow: 0 4px 12px rgba(63, 117, 72, 0.18);
    }

    .recent-kpi.wib-kpi .value {
        color: #F7FFF3;
    }

    .recent-kpi.wib-kpi .basis {
        color: #E3F2DC;
    }

    .recent-kpi .value {
        color: #f1fffc;
        font-size: clamp(2.5rem, 5vw, 3.8rem);
        line-height: 1;
        font-weight: 800;
        letter-spacing: -2px;
        margin-bottom: 13px;
    }

    .recent-kpi .label {
        color: #ffffff;
        font-size: 1rem;
        line-height: 1.35;
        font-weight: 650;
        margin-bottom: 8px;
    }

    .recent-kpi .basis {
        color: #d7f0eb;
        font-size: 0.78rem;
        line-height: 1.3;
        opacity: 0.97;
    }

    @media (max-width: 850px) {
        .recent-kpi-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
    }

    @media (max-width: 520px) {
        .recent-kpi-grid {
            grid-template-columns: 1fr;
        }

        .recent-kpi {
            min-height: 145px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# BADANIE FUNDACJI THINK! – 2025
# ============================================================

st.markdown(
    """
    <div class="recent-kpi-grid">
        <div class="recent-kpi">
            <div class="value">30%</div>
            <div class="label">Czuje się bezpiecznie finansowo</div>
            <div class="basis">Wszyscy respondenci · N = 1037 · osoby 18–74 lata</div>
        </div>
        <div class="recent-kpi">
            <div class="value">37%</div>
            <div class="label">Deklaruje, że inwestuje swoje pieniądze</div>
            <div class="basis">Wszyscy respondenci · N = 1037 · osoby 18–74 lata</div>
        </div>
        <div class="recent-kpi">
            <div class="value">21%</div>
            <div class="label">Aktywnie szuka informacji o oszczędzaniu i inwestowaniu</div>
            <div class="basis">Wszyscy respondenci · N = 1037 · osoby 18–74 lata</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"**Źródło:** Fundacja Think!, *Postawy Polaków wobec finansów* (październik 2025). "
    f"Badanie CAWI na Ogólnopolskim Panelu Badawczym Ariadna, reprezentatywna ogólnopolska próba dorosłych Polaków w wieku 18–74 lata, N = 1037; realizacja: 25 września–5 października 2025 r. "
    f"[Otwórz pełny raport]({think_url})",
    unsafe_allow_html=True
)

# ============================================================
# BADANIE WIB / FUNDACJA GPW – 2026
# ============================================================

st.markdown(
    """
    <div class="recent-kpi-grid wib-kpi-grid">
        <div class="recent-kpi wib-kpi">
            <div class="value">50%</div>
            <div class="label">Oszczędza pieniądze</div>
            <div class="basis">Wszyscy respondenci · N = 1099 · osoby 18–65 lat</div>
        </div>
        <div class="recent-kpi wib-kpi">
            <div class="value">26%</div>
            <div class="label">Nie oszczędza ani nie inwestuje</div>
            <div class="basis">Wszyscy respondenci · N = 1099 · osoby 18–65 lat</div>
        </div>
        <div class="recent-kpi wib-kpi">
            <div class="value">41%</div>
            <div class="label">Czuje się bezpiecznie finansowo</div>
            <div class="basis">Wszyscy respondenci · N = 1099 · osoby 18–65 lat</div>
        </div>
        <div class="recent-kpi wib-kpi">
            <div class="value">52%</div>
            <div class="label">Nie podejmuje celowych działań, by poszerzać wiedzę finansową</div>
            <div class="basis">Wskaźnik uśredniony dla analizowanych obszarów · N = 1099 · osoby 18–65 lat</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "**Źródło:** Fundacja Warszawski Instytut Bankowości i Fundacja GPW, "
    "*Poziom wiedzy finansowej Polaków 2026*. Badanie CAWI, 19–22 lutego 2026 r., "
    "ogólnopolska próba N = 1099; badani w wieku 18–65 lat, dobór warstwowy według płci, wieku i klasy miejscowości. "
    "[Otwórz pełny raport](https://www.zbp.pl/getContentAsset/dc75b940-f471-45ba-9cc8-2f3d5fe867c3/1b52933d-ceff-4d97-bee2-094d491a3634/AKTUALNE_badanie_kee_2026__compressed-skompresowany.pdf?language=pl)",
    unsafe_allow_html=True
)



# Karty w każdym wierszu rozciągają się na całą szerokość kolumny.
# Dzięki temu przy dwóch kartach zajmują po połowie dostępnego miejsca,
# a przy trzech – po jednej trzeciej. Wysokość kart w wierszu jest wyrównana.
st.markdown(
    """
    <style>
    div[data-testid="stHorizontalBlock"] {
        align-items: stretch !important;
        gap: 1.25rem !important;
    }

    div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
        display: flex !important;
        min-width: 0 !important;
    }

    div[data-testid="stHorizontalBlock"] > div[data-testid="column"] > div {
        display: flex !important;
        flex: 1 1 auto !important;
        width: 100% !important;
        min-width: 0 !important;
    }

    div[data-testid="stHorizontalBlock"] div[data-testid="stMarkdownContainer"] {
        width: 100% !important;
        min-width: 0 !important;
    }

    div[data-testid="stHorizontalBlock"] .card {
        width: 100% !important;
        max-width: none !important;
        /* Karta rośnie wraz z treścią – tekst nie nachodzi na kolejną sekcję. */
        height: auto !important;
        min-height: 235px !important;
        box-sizing: border-box !important;
        display: flex !important;
        flex-direction: column !important;
        overflow: visible !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# MOŻLIWE BARIERY OSZCZĘDZANIA I INWESTOWANIA
# ============================================================

st.markdown(
    """
    <div class="section">Co może powstrzymywać przed oszczędzaniem i inwestowaniem?</div>
    <div class="lead">
        Poniższe punkty przedstawiają ogólne wnioski dotyczące najczęstszych
        trudności, które mogą utrudniać budowanie oszczędności i podejmowanie
        decyzji inwestycyjnych. Nie każda bariera dotyczy każdej osoby – ich
        znaczenie zależy od indywidualnej sytuacji i doświadczeń.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 1. BARIERY EKONOMICZNE
# ============================================================

st.markdown(
    '<div class="section">1. Bariery ekonomiczne</div>'
    '<div class="lead">Ograniczone dochody i wysokie koszty życia mogą utrudniać wygospodarowanie pieniędzy na przyszłość.</div>',
    unsafe_allow_html=True
)

a, b, c = st.columns(3)

with a:
    st.markdown(
        """
        <div class="card">
            <div class="tag">DOCHODY</div>
            <h3>Zbyt niskie dochody lub ich brak</h3>
            <p>
                Gdy większość dochodów przeznaczana jest na podstawowe potrzeby,
                trudno wygospodarować nadwyżkę, którą można regularnie odkładać.
                Przy niestabilnych lub niskich zarobkach oszczędzanie często
                schodzi na dalszy plan.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with b:
    st.markdown(
        """
        <div class="card">
            <div class="tag">WYDATKI</div>
            <h3>Bieżące i nieprzewidziane wydatki</h3>
            <p>
                Rachunki, codzienne zakupy i rosnące koszty utrzymania mogą
                pochłaniać znaczną część budżetu. Dodatkowo nagłe wydatki,
                takie jak naprawa samochodu czy sprzętu, często zmuszają
                do wykorzystania zgromadzonych pieniędzy.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c:
    st.markdown(
        """
        <div class="card">
            <div class="tag">PODUSZKA FINANSOWA</div>
            <h3>Brak kapitału na początek</h3>
            <p>
                Osoby, które nie mają oszczędności na nieprzewidziane sytuacje,
                mogą nie czuć się gotowe do lokowania pieniędzy w inwestycje.
                Najpierw potrzebują zabezpieczenia podstawowych potrzeb
                i poczucia finansowej stabilności.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# 2. BARIERY PSYCHOLOGICZNE I BEHAWIORALNE
# ============================================================

st.markdown(
    '<div class="section">2. Bariery psychologiczne i behawioralne</div>'
    '<div class="lead">Nawet przy dostępnych środkach emocje, przyzwyczajenia i sposób postrzegania ryzyka wpływają na decyzje finansowe.</div>',
    unsafe_allow_html=True
)

a, b, c = st.columns(3)

with a:
    st.markdown(
        """
        <div class="card">
            <div class="tag">OBAWA PRZED STRATĄ</div>
            <h3>Lęk przed ryzykiem inwestycyjnym</h3>
            <p>
                Możliwość utraty części zgromadzonych pieniędzy może zniechęcać
                do inwestowania. Szczególnie trudno zaakceptować ryzyko osobom,
                które długo odkładały swoje oszczędności i traktują je jako
                zabezpieczenie na przyszłość.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with b:
    st.markdown(
        """
        <div class="card">
            <div class="tag">PREFERENCJA BEZPIECZEŃSTWA</div>
            <h3>Wybór bezpiecznych i płynnych form</h3>
            <p>
                Wiele osób ceni przede wszystkim pewność i łatwy dostęp do
                pieniędzy. Może to skłaniać do wybierania prostych, dobrze
                znanych rozwiązań zamiast produktów, które dają szansę na
                wyższy zysk, ale wiążą się z większym ryzykiem.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c:
    st.markdown(
        """
        <div class="card">
            <div class="tag">MOTYWACJA I NAWYKI</div>
            <h3>Trudność z rozpoczęciem oszczędzania</h3>
            <p>
                Odkładanie pieniędzy wymaga systematyczności i zmiany
                codziennych przyzwyczajeń. Bez konkretnego celu, planu
                i wypracowanej rutyny łatwo odkładać decyzję o oszczędzaniu
                na później.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# 3. BARIERY WIEDZY I KORZYSTANIA Z NARZĘDZI
# ============================================================

st.markdown(
    '<div class="section">3. Bariery wiedzy i korzystania z narzędzi</div>'
    '<div class="lead">Brak orientacji w dostępnych rozwiązaniach może utrudniać ocenę możliwości i rozpoczęcie inwestowania.</div>',
    unsafe_allow_html=True
)

a, b, c = st.columns(3)

with a:
    st.markdown(
        """
        <div class="card">
            <div class="tag">BRAK WIEDZY</div>
            <h3>Niewystarczająca wiedza o inwestowaniu</h3>
            <p>
                Niepewność dotycząca zasad działania rynku, ryzyka i możliwych
                wyników może powodować obawę przed popełnieniem błędu.
                Bez podstawowej wiedzy trudno samodzielnie ocenić, które
                rozwiązanie odpowiada własnym potrzebom.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with b:
    st.markdown(
        """
        <div class="card">
            <div class="tag">EDUKACJA FINANSOWA</div>
            <h3>Brak systematycznego poszerzania wiedzy</h3>
            <p>
                Wiedza finansowa często rozwijana jest dopiero wtedy, gdy
                pojawia się konkretna potrzeba. Brak regularnego uczenia się
                utrudnia porównywanie ofert, rozumienie kosztów i podejmowanie
                przemyślanych decyzji.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c:
    st.markdown(
        """
        <div class="card">
            <div class="tag">ZŁOŻONOŚĆ PRODUKTÓW</div>
            <h3>Niska znajomość instrumentów finansowych</h3>
            <p>
                Nazwy i mechanizmy działania takich produktów jak ETF-y,
                obligacje czy akcje mogą być dla początkujących niezrozumiałe.
                Duża liczba dostępnych możliwości utrudnia wybór i może
                prowadzić do rezygnacji z inwestowania.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# DODATKOWE MATERIAŁY UZUPEŁNIAJĄCE
# ============================================================

st.markdown(
    '<div class="section">Materiały uzupełniające</div>'
    ,
    unsafe_allow_html=True
)

st.markdown(
    """
<style>
.extra-source-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin:14px 0 20px;align-items:stretch}
.extra-source-card{box-sizing:border-box;min-width:0;padding:16px 17px;border:1px solid #d9e8d5;border-radius:15px;background:rgba(255,255,255,.82);box-shadow:0 3px 10px rgba(30,75,40,.045);display:flex;flex-direction:column;gap:8px}
.extra-source-tag{display:inline-block;width:fit-content;padding:5px 9px;border-radius:20px;background:#e5efdc;color:#27613c;font-size:.63rem;line-height:1.2;font-weight:750;letter-spacing:.02em}
.extra-source-card h3{margin:2px 0 0;color:#123d36;font-size:.98rem;line-height:1.3}
.extra-source-card p{margin:0;color:#46615b;font-size:.82rem;line-height:1.48;flex:1 1 auto}
.extra-source-card a{width:fit-content;font-size:.82rem;font-weight:650}
@media(max-width:850px){.extra-source-grid{grid-template-columns:1fr}}
</style>
<div class="extra-source-grid"><div class="extra-source-card"><div class="extra-source-tag">KOMISJA EUROPEJSKA · 2023</div><h3>Monitoring poziomu wiedzy finansowej w UE</h3><p>Europejskie badanie porównujące wiedzę, zachowania i postawy finansowe mieszkańców państw Unii. Pozwala umieścić polskie decyzje finansowe w szerszym kontekście europejskim.</p><a href="https://op.europa.eu/en/publication-detail/-/publication/b54cefd6-409f-11ee-952f-01aa75ed71a1/language-en" target="_blank">Otwórz publikację</a></div><div class="extra-source-card"><div class="extra-source-tag">ARTYKUŁ NAUKOWY · 2023</div><h3>Motywy oszczędzania gospodarstw domowych</h3><p>Analiza pokazuje, jak cele oszczędzania wiążą się z cechami społeczno-ekonomicznymi gospodarstw, m.in. ich strukturą, wiekiem i poziomem posiadanych aktywów.</p><a href="https://pressto.amu.edu.pl/index.php/rpeis/article/view/38119" target="_blank">Otwórz artykuł naukowy</a></div><div class="extra-source-card"><div class="extra-source-tag">UNIWERSYTET WARSZAWSKI · 2025</div><h3>Unikanie wiedzy finansowej i oszczędzanie długoterminowe</h3><p>Badanie 1200 dorosłych mieszkańców Polski analizuje, czy unikanie informacji finansowych i emerytalnych wiąże się z gotowością do odkładania pieniędzy na przyszłość.</p><a href="https://press.wz.uw.edu.pl/jbfe/vol2025/iss1/5/" target="_blank">Otwórz artykuł naukowy</a></div></div>
    """,
    unsafe_allow_html=True
)

