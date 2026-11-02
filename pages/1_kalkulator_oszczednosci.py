import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ---------------------------------------------------------
# Wygląd – jasna mięta, głęboka zieleń i limonkowe akcenty
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Manrope:wght@500;600;700;800&display=swap');

    .stApp {
        background:
          radial-gradient(ellipse at 4% 0%, rgba(185,225,137,.30), transparent 34%),
          radial-gradient(ellipse at 100% 8%, rgba(130,196,155,.20), transparent 30%),
          #eef5e9;
        color: #173b34;
    }
    html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stSidebar"] { background: #123f38; }
    [data-testid="stSidebar"] * { color: #eef8e9 !important; }

    .block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1500px; }

    .hero-panel {
        background: linear-gradient(118deg, #123f38 0%, #17574a 65%, #24745b 100%);
        border-radius: 25px;
        padding: 30px 34px;
        color: #f4faed;
        margin: 0 0 22px 0;
        box-shadow: 0 16px 38px rgba(24,75,59,.15);
        position: relative;
        overflow: hidden;
    }
    .hero-panel:after {
        content: ""; position: absolute; width: 260px; height: 260px;
        border: 1px solid rgba(226,244,165,.17); border-radius: 50%;
        right: -55px; top: -130px;
        box-shadow: 0 0 0 28px rgba(226,244,165,.035), 0 0 0 58px rgba(226,244,165,.025);
    }
    .hero-kicker { color: #d7ec87; font-size: 10px; letter-spacing: 2.3px; font-weight: 800; text-transform: uppercase; }
    .hero-title { color: #fff; font: 800 clamp(28px,3.5vw,42px)/1.12 'Manrope',sans-serif; letter-spacing: -1.3px; margin: 10px 0 9px; }
    .hero-copy { color: #d5e8dc; font-size: 14px; line-height: 1.65; max-width: 700px; margin: 0; }
    .hero-chip { display: inline-block; margin-top: 17px; padding: 6px 11px; border-radius: 30px; background: rgba(220,240,151,.13); border: 1px solid rgba(220,240,151,.23); color: #e5f3b1; font-size: 11px; }

    .section-label { color: #43816a; font-size: 10px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; margin: 2px 0 5px; }
    .section-title { color: #173f35; font: 800 21px 'Manrope',sans-serif; letter-spacing: -.5px; margin: 0 0 4px; }
    .section-subtitle { color: #6b8578; font-size: 12px; margin: 0 0 16px; }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255,255,255,.78);
        border: 1px solid #dce9d9 !important;
        border-radius: 19px !important;
        box-shadow: 0 7px 22px rgba(34,78,57,.045);
    }
    [data-testid="stMetric"] {
        background: #f5f9ef; border: 1px solid #e2ecd8;
        padding: 13px 14px; border-radius: 14px;
    }
    [data-testid="stMetricLabel"] { color: #6b8578 !important; font-size: 11px !important; }
    [data-testid="stMetricValue"] { color: #174b3e !important; font-family: 'Manrope',sans-serif; font-size: 23px !important; font-weight: 800 !important; }

    [data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {
        background: #cce66d !important; border: 2px solid #ffffff !important;
        box-shadow: 0 1px 7px rgba(47,91,50,.22) !important;
    }
    [data-testid="stSlider"] [data-baseweb="slider"] > div > div {
        background: #b9d95a !important;
    }
    [data-testid="stSlider"] [data-baseweb="slider"] > div:first-child {
        background: #dce8d4 !important;
    }
    [data-testid="stNumberInput"] input, [data-testid="stSelectbox"] [data-baseweb="select"] > div {
        background: #f7faf4 !important; border-color: #dce8d7 !important;
        border-radius: 10px !important; color: #23483d !important;
    }
    [data-testid="stRadio"] label, [data-testid="stCheckbox"] label { color: #34594c !important; font-size: 12px; }
    .stButton > button {
        background: #cce66d; color: #244333; border: 0; border-radius: 30px;
        font-weight: 800; padding: 9px 20px;
    }
    .stButton > button:hover { background: #d8ef83; color: #173b34; border: 0; }
    .small-help { color: #71877a; font-size: 11px; line-height: 1.55; }
    .result-highlight {
        background: linear-gradient(120deg,#174d40,#216a54);
        color: #f4faed; border-radius: 17px; padding: 17px 19px; margin-bottom: 13px;
    }
    .result-highlight .label { color: #d0e4b0; font-size: 11px; }
    .result-highlight .value { color: #d8ed7b; font: 800 29px 'Manrope',sans-serif; margin-top: 3px; }
    .result-highlight .hint { color: #d1e3d8; font-size: 10px; margin-top: 4px; }
    .note-box { background: #e4efdc; border-left: 4px solid #9cbd4f; border-radius: 9px; padding: 12px 15px; color: #496553; font-size: 11px; line-height: 1.6; }
    div[data-testid="stDataFrame"] { border: 1px solid #dce9d9; border-radius: 12px; overflow: hidden; }
    #MainMenu, footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Nagłówek
# ---------------------------------------------------------
st.markdown(
    """
    <div class="hero-panel">
      <div class="hero-kicker">Finansowy Kompas · Narzędzie edukacyjne</div>
      <div class="hero-title">Zaplanuj swoje oszczędności.</div>
      <p class="hero-copy">
        Sprawdź, jak regularne wpłaty, oprocentowanie i czas mogą pomóc Ci
        zbudować kapitał. Dostosuj założenia i obserwuj wyniki na bieżąco.
      </p>
      <span class="hero-chip">✦ Twój plan · Twoje parametry · Twoja symulacja</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# Synchroniczne pola: suwak do szybkiej zmiany i pole liczbowe do dokładnego wpisania.
def _sync_control(key: str, source: str):
    if source == "slider":
        st.session_state[f"{key}_number"] = st.session_state[f"{key}_slider"]
    else:
        st.session_state[f"{key}_slider"] = st.session_state[f"{key}_number"]

def amount_control(label, key, minimum, maximum, default, step, suffix="", help_text=None):
    slider_key = f"{key}_slider"
    number_key = f"{key}_number"
    if slider_key not in st.session_state:
        st.session_state[slider_key] = default
    if number_key not in st.session_state:
        st.session_state[number_key] = default

    st.markdown(f"**{label}**")
    a, b = st.columns([1.65, 1], vertical_alignment="center")
    with a:
        st.slider(
            label, min_value=minimum, max_value=maximum, step=step,
            key=slider_key, label_visibility="collapsed",
            on_change=_sync_control, args=(key, "slider"), help=help_text
        )
    with b:
        st.number_input(
            f"Wpisz {label.lower()}",
            min_value=minimum, max_value=maximum, step=step,
            key=number_key, label_visibility="collapsed",
            on_change=_sync_control, args=(key, "number"), help=help_text
        )
    value = st.session_state[number_key]
    if suffix:
        st.caption(f"Aktualna wartość: **{value:,.{1 if isinstance(value, float) else 0}f} {suffix}**".replace(",", " "))
    return value

# ---------------------------------------------------------
# Parametry i wyniki
# ---------------------------------------------------------
left, right = st.columns([0.92, 1.28], gap="large")

with left:
    with st.container(border=True):
        st.markdown('<div class="section-label">01 / Ustawienia</div><div class="section-title">Twój plan oszczędzania</div><div class="section-subtitle">Zmieniaj suwaki lub wpisuj własne wartości.</div>', unsafe_allow_html=True)

        st.markdown("####  Kapitał i wpłaty")
        initial_capital = amount_control("Kapitał początkowy", "initial", 0, 500000, 5000, 500, "zł")
        monthly_payment = amount_control("Miesięczna wpłata", "monthly", 0, 20000, 500, 50, "zł")
        years = amount_control("Okres oszczędzania", "years", 1, 40, 10, 1, "lat")

        st.markdown("---")
        st.markdown("####  Oprocentowanie")
        annual_rate = amount_control("Oprocentowanie nominalne", "rate", 0.0, 20.0, 5.0, 0.1, "%")
        capitalization = st.selectbox(
            "Częstotliwość kapitalizacji",
            ["Miesięczna", "Kwartalna", "Półroczna", "Roczna"],
            index=0
        )
        payment_timing = st.radio(
            "Kiedy wpłacasz pieniądze?",
            ["Na początku miesiąca", "Na końcu miesiąca"],
            horizontal=True
        )

        with st.expander("Więcej ustawień", expanded=False):
            increase_payments = st.checkbox("Zwiększaj miesięczną wpłatę raz w roku", value=False)
            annual_payment_growth = 0.0
            if increase_payments:
                annual_payment_growth = st.slider("Roczny wzrost wpłaty", 1.0, 30.0, 5.0, 0.5, format="%.1f%%")

            deduct_tax = st.checkbox("Uwzględnij 19% podatek od zysków kapitałowych", value=True)
            include_inflation = st.checkbox("Pokaż wpływ inflacji na realną wartość", value=True)
            inflation_rate = 3.0
            if include_inflation:
                inflation_rate = st.slider("Średnia roczna inflacja", 0.0, 20.0, 3.0, 0.1, format="%.1f%%")

        st.markdown('<div class="small-help">Wskazówka: przetestuj różne okresy i wysokości wpłat, aby sprawdzić, które parametry najmocniej wpływają na końcowy kapitał.</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="section-label">02 / Rezultat</div><div class="section-title">Zobacz, jak rosną Twoje oszczędności</div><div class="section-subtitle"></div>', unsafe_allow_html=True)

    capitalization_months = {"Miesięczna": 1, "Kwartalna": 3, "Półroczna": 6, "Roczna": 12}[capitalization]
    tax_rate = 0.19

    def simulate_savings():
        months = int(years * 12)
        balance = float(initial_capital)
        paid_in = float(initial_capital)
        accrued_interest = 0.0
        total_tax = 0.0
        rows = []
        # Wartość gotówki/konta 0% w cenach z końca danego miesiąca.
        # Każda wpłata jest pomniejszana o inflację tylko za okres,
        # przez który faktycznie pozostawała bez oprocentowania.
        cash_deposits = [(0, float(initial_capital))]

        for month in range(1, months + 1):
            payment_year = (month - 1) // 12
            current_payment = float(monthly_payment) * (
                (1 + annual_payment_growth / 100) ** payment_year if increase_payments else 1
            )

            if payment_timing == "Na początku miesiąca":
                balance += current_payment
                paid_in += current_payment
                cash_deposits.append((month - 1, current_payment))

            accrued_interest += balance * (annual_rate / 100) / 12

            if payment_timing == "Na końcu miesiąca":
                balance += current_payment
                paid_in += current_payment
                cash_deposits.append((month, current_payment))

            if month % capitalization_months == 0 or month == months:
                tax = accrued_interest * tax_rate if deduct_tax else 0.0
                balance += accrued_interest - tax
                total_tax += tax
                accrued_interest = 0.0

            real_balance = (
                balance / ((1 + inflation_rate / 100) ** (month / 12))
                if include_inflation else np.nan
            )
            cash_real_balance = (
                sum(amount / ((1 + inflation_rate / 100) ** ((month - deposit_month) / 12))
                    for deposit_month, amount in cash_deposits)
                if include_inflation else np.nan
            )
            rows.append({
                "Miesiąc": month,
                "Rok": (month - 1) // 12 + 1,
                "Saldo nominalne": balance,
                "Wpłacony kapitał": paid_in,
                "Wartość realna": real_balance,
                "Siła nabywcza gotówki (0%)": cash_real_balance,
            })

        return pd.DataFrame(rows), paid_in, balance, total_tax

    df, total_paid, final_balance, total_tax = simulate_savings()
    net_gain = final_balance - total_paid
    real_final = final_balance / ((1 + inflation_rate / 100) ** years) if include_inflation else None

    def money(value):
        return f"{value:,.2f} zł".replace(",", " ")

    st.markdown(
        f'<div class="result-highlight"><div class="label">Szacowana wartość oszczędności po {years} latach</div><div class="value">{money(final_balance)}</div><div class="hint">Przy założonym oprocentowaniu {annual_rate:.1f}% i kapitalizacji {capitalization.lower()}</div></div>',
        unsafe_allow_html=True
    )

    k1, k2 = st.columns(2)
    k1.metric("Łączna suma wpłat", money(total_paid))
    k2.metric("Zysk po podatku", money(net_gain))
    k3, k4 = st.columns(2)
    k3.metric("Podatek od zysków", money(total_tax))
    if include_inflation:
        k4.metric("Wartość realna", money(real_final))
    else:
        k4.metric("Efektywne oprocentowanie", f"{annual_rate:.1f}%")

    st.markdown("<br>", unsafe_allow_html=True)
    chart_mode = st.radio(
        "Wizualizacja",
        ["Wzrost oszczędności", "Struktura końcowej kwoty"],
        horizontal=True,
        label_visibility="collapsed"
    )

    if chart_mode == "Wzrost oszczędności":
        fig = go.Figure()
        x = df["Miesiąc"] / 12
        fig.add_trace(go.Scatter(
            x=x, y=df["Saldo nominalne"], name="Saldo",
            mode="lines", line=dict(color="#75a83e", width=3),
            fill="tozeroy", fillcolor="rgba(174,211,100,.17)",
            hovertemplate="Rok %{x:.1f}<br>Saldo: %{y:,.2f} zł<extra></extra>"
        ))
        fig.add_trace(go.Scatter(
            x=x, y=df["Wpłacony kapitał"], name="Suma wpłat",
            mode="lines", line=dict(color="#477f72", width=2, dash="dash"),
            hovertemplate="Rok %{x:.1f}<br>Wpłaty: %{y:,.2f} zł<extra></extra>"
        ))
        if include_inflation:
            fig.add_trace(go.Scatter(
                x=x, y=df["Wartość realna"], name="Wartość realna oszczędności",
                mode="lines", line=dict(color="#d2a84c", width=2, dash="dot"),
                hovertemplate="Rok %{x:.1f}<br>Realna wartość oszczędności: %{y:,.2f} zł<extra></extra>"
            ))
            fig.add_trace(go.Scatter(
                x=x, y=df["Siła nabywcza gotówki (0%)"],
                name="Gotówka / konto 0% – siła nabywcza",
                mode="lines", line=dict(color="#c46f5b", width=2.5, dash="dash"),
                hovertemplate="Rok %{x:.1f}<br>Siła nabywcza gotówki: %{y:,.2f} zł<extra></extra>"
            ))
        fig.update_layout(
            height=350, margin=dict(l=5, r=10, t=20, b=5),
            hovermode="x unified", plot_bgcolor="rgba(255,255,255,0)",
            paper_bgcolor="rgba(255,255,255,0)",
            font=dict(family="DM Sans", color="#476557", size=10),
            legend=dict(orientation="h", y=1.13, x=0),
            xaxis=dict(title="Lata oszczędzania", range=[0, years], dtick=1, gridcolor="#e2ebdc", zeroline=False),
            yaxis=dict(title="Wartość (zł)", tickformat=",.0f", gridcolor="#e2ebdc", zeroline=False),
        )
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
        if include_inflation:
            st.markdown(
                '<div class="note-box"><b>Jak czytać linię gotówki?</b> Pokazuje szacowaną siłę nabywczą '
                'tych samych wpłat, gdyby były odkładane w gotówce lub na nieoprocentowanym koncie (0%). '
                'Inflacja stopniowo zmniejsza ich realną wartość. Każda wpłata jest korygowana tylko za okres '
                'od momentu jej odłożenia, dlatego późniejsze wpłaty nie są traktowane tak, jakby leżały '
                'bezczynnie od początku całego okresu.</div>',
                unsafe_allow_html=True
            )
    else:
        interest = max(final_balance - total_paid, 0)
        fig = go.Figure(go.Bar(
            x=["Końcowa wartość"], y=[total_paid], name="Wpłacony kapitał",
            marker_color="#477f72", text=[money(total_paid)], textposition="inside",
            hovertemplate="Wpłacony kapitał: %{y:,.2f} zł<extra></extra>"
        ))
        fig.add_trace(go.Bar(
            x=["Końcowa wartość"], y=[interest], name="Zysk po podatku",
            marker_color="#c7df69", text=[money(interest)], textposition="inside",
            hovertemplate="Zysk: %{y:,.2f} zł<extra></extra>"
        ))
        fig.update_layout(
            barmode="stack", height=350, margin=dict(l=5, r=10, t=20, b=5),
            plot_bgcolor="rgba(255,255,255,0)", paper_bgcolor="rgba(255,255,255,0)",
            font=dict(family="DM Sans", color="#476557", size=10),
            legend=dict(orientation="h", y=1.13, x=0),
            yaxis=dict(title="Wartość (zł)", tickformat=",.0f", gridcolor="#e2ebdc"),
        )
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# ---------------------------------------------------------
# Zestawienie roczne – rozwijana tabela
# ---------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)

with st.container(key="annual-table-panel", border=True):
    st.markdown(
        '<div class="section-label">03 / Szczegółowe zestawienie</div>'
        '<div class="section-title">Wyniki rok po roku</div>'
        '<div class="section-subtitle">Rozwiń tabelę, aby sprawdzić saldo, sumę wpłat i realną wartość oszczędności w każdym roku.</div>',
        unsafe_allow_html=True
    )

    with st.expander("Pokaż / ukryj zestawienie roczne", expanded=False):
        annual = df.groupby("Rok", as_index=False).last()
        annual_display = annual[["Rok", "Saldo nominalne", "Wpłacony kapitał"]].copy()
        if include_inflation:
            annual_display["Wartość realna"] = annual["Wartość realna"]
            annual_display["Siła nabywcza gotówki (0%)"] = annual["Siła nabywcza gotówki (0%)"]
        annual_display = annual_display.rename(columns={
            "Rok": "Rok oszczędzania",
            "Saldo nominalne": "Saldo nominalne (zł)",
            "Wpłacony kapitał": "Suma wpłat (zł)",
            "Wartość realna": "Wartość realna oszczędności (zł)",
            "Siła nabywcza gotówki (0%)": "Gotówka / konto 0% – realnie (zł)",
        })
        formatters = {
            c: (lambda x: f"{x:,.2f} zł".replace(",", " "))
            for c in annual_display.columns if c != "Rok oszczędzania"
        }
        green_table = (
            annual_display.style
            .format(formatters)
            .set_table_styles([
                {
                    "selector": "th",
                    "props": [
                        ("background-color", "#dcebd2"),
                        ("color", "#245342"),
                        ("font-weight", "700"),
                        ("border-bottom", "1px solid #c7ddbd"),
                        ("padding", "12px 14px"),
                        ("text-align", "left"),
                    ],
                },
                {
                    "selector": "td",
                    "props": [
                        ("color", "#355c4b"),
                        ("border-bottom", "1px solid #e6eee1"),
                        ("padding", "10px 14px"),
                    ],
                },
                {
                    "selector": "tbody tr:nth-child(odd)",
                    "props": [("background-color", "#fbfdf9")],
                },
                {
                    "selector": "tbody tr:nth-child(even)",
                    "props": [("background-color", "#f0f6eb")],
                },
                {
                    "selector": "tbody tr:hover",
                    "props": [("background-color", "#e5f0d9")],
                },
            ])
        )
        st.dataframe(
            green_table,
            use_container_width=True,
            hide_index=True,
            height=min(460, 42 + 36 * (len(annual_display) + 1))
        )


    with st.expander("Jak obliczane są wyniki?", expanded=False):
        st.markdown(
            f"""
            - **Wpłaty:** {payment_timing.lower()}, {monthly_payment:,.0f} zł miesięcznie.
            - **Oprocentowanie:** stałe nominalne {annual_rate:.1f}% rocznie, naliczane w modelu miesięcznym.
            - **Kapitalizacja:** {capitalization.lower()}.
            - **Podatek:** {'19% od kapitalizowanych odsetek' if deduct_tax else 'pominięty'}.
            - **Inflacja:** {'średnio ' + format(inflation_rate, '.1f') + '% rocznie' if include_inflation else 'pominięta'}.
            - **Zmiana wpłat:** {'wzrost o ' + format(annual_payment_growth, '.1f') + '% rocznie' if increase_payments else 'stała miesięczna wpłata'}.

            Model ma charakter edukacyjny i upraszcza zasady naliczania odsetek oraz podatku.
            Nie uwzględnia opłat, limitów ani zmienności oprocentowania konkretnego produktu.
            """
        )

# ---------------------------------------------------------
# Porównanie scenariuszy oprocentowania
# ---------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)

with st.container(border=True):
    st.markdown(
        '<div class="section-label">04 / Porównanie</div>'
        '<div class="section-title">Jak oprocentowanie wpływa na oszczędności?</div>'
        '<div class="section-subtitle">Porównaj trzy warianty przy identycznych wpłatach, okresie i pozostałych założeniach.</div>',
        unsafe_allow_html=True
    )

    st.markdown("**Ustaw różnicę oprocentowania względem wariantu podstawowego**")
    rate_col1, rate_col2 = st.columns(2)

    with rate_col1:
        lower_difference = st.slider(
            "Obniżenie oprocentowania",
            min_value=0.0,
            max_value=5.0,
            value=1.0,
            step=0.1,
            format="%.1f p.p.",
            key="comparison_lower_difference"
        )

    with rate_col2:
        higher_difference = st.slider(
            "Podwyższenie oprocentowania",
            min_value=0.0,
            max_value=5.0,
            value=1.0,
            step=0.1,
            format="%.1f p.p.",
            key="comparison_higher_difference"
        )

    lower_rate = max(0.0, float(annual_rate) - lower_difference)
    higher_rate = min(20.0, float(annual_rate) + higher_difference)

    st.caption(
        f"Porównywane oprocentowanie: {lower_rate:.1f}% (niższe) · "
        f"{annual_rate:.1f}% (podstawowe) · {higher_rate:.1f}% (wyższe). "
        "Pozostałe parametry pozostają bez zmian."
    )

    def simulate_rate_for_comparison(rate):
        """Oblicza saldo na koniec każdego roku dla wskazanej stopy procentowej."""
        balance = float(initial_capital)
        accrued_interest = 0.0
        annual_rows = []

        for month in range(1, int(years) * 12 + 1):
            payment_year = (month - 1) // 12
            current_payment = float(monthly_payment) * (
                (1 + annual_payment_growth / 100) ** payment_year
                if increase_payments else 1
            )

            if payment_timing == "Na początku miesiąca":
                balance += current_payment

            accrued_interest += balance * (rate / 100) / 12

            if payment_timing == "Na końcu miesiąca":
                balance += current_payment

            if month % capitalization_months == 0 or month == int(years) * 12:
                tax = accrued_interest * tax_rate if deduct_tax else 0.0
                balance += accrued_interest - tax
                accrued_interest = 0.0

            if month % 12 == 0:
                annual_rows.append({
                    "Rok": month // 12,
                    "Saldo": balance
                })

        return pd.DataFrame(annual_rows)

    lower_df = simulate_rate_for_comparison(lower_rate)
    base_df = simulate_rate_for_comparison(float(annual_rate))
    higher_df = simulate_rate_for_comparison(higher_rate)

    comparison_fig = go.Figure()
    comparison_series = [
        (lower_df, f"{lower_rate:.1f}% – niższe", "#9BBE63"),
        (base_df, f"{annual_rate:.1f}% – podstawowe", "#477F72"),
        (higher_df, f"{higher_rate:.1f}% – wyższe", "#C5D95F"),
    ]

    for scenario_df, scenario_name, scenario_color in comparison_series:
        comparison_fig.add_trace(go.Bar(
            x=scenario_df["Rok"],
            y=scenario_df["Saldo"],
            name=scenario_name,
            marker_color=scenario_color,
            marker_line_width=0,
            hovertemplate=(
                "Rok: %{x}<br>"
                "Końcowe saldo: %{y:,.2f} zł"
                "<extra>" + scenario_name + "</extra>"
            )
        ))

    comparison_fig.update_layout(
        barmode="group",
        height=390,
        margin=dict(l=8, r=12, t=22, b=8),
        plot_bgcolor="rgba(255,255,255,0)",
        paper_bgcolor="rgba(255,255,255,0)",
        font=dict(family="DM Sans", color="#476557", size=10),
        legend=dict(orientation="h", y=1.13, x=0),
        xaxis=dict(
            title="Rok oszczędzania",
            tickmode="linear",
            dtick=max(1, int(years) // 12),
            range=[0.4, int(years) + 0.6],
            gridcolor="#e2ebdc",
            zeroline=False
        ),
        yaxis=dict(
            title="Wartość oszczędności (zł)",
            tickformat=",.0f",
            gridcolor="#e2ebdc",
            zeroline=False
        ),
        bargap=0.22,
        bargroupgap=0.08,
        hovermode="x"
    )
    st.plotly_chart(
        comparison_fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

    low_end = float(lower_df.iloc[-1]["Saldo"])
    base_end = float(base_df.iloc[-1]["Saldo"])
    high_end = float(higher_df.iloc[-1]["Saldo"])
    delta_cols = st.columns(3)
    delta_cols[0].metric("Wariant niższy", money(low_end))
    delta_cols[1].metric("Wariant podstawowy", money(base_end))
    delta_cols[2].metric("Wariant wyższy", money(high_end))

    st.caption(
        "Wykres pokazuje saldo na koniec każdego roku. Podatek, kapitalizacja, moment wpłaty "
        "i ewentualny coroczny wzrost wpłat są takie same jak w głównej symulacji."
    )


st.markdown(
    '<div class="note-box"><b>Ważne:</b> Finansowy Kompas ma charakter edukacyjny. Wyniki symulacji zależą od przyjętych założeń i nie stanowią oferty banku, gwarancji zysku ani indywidualnej rekomendacji finansowej.</div>',
    unsafe_allow_html=True
)
