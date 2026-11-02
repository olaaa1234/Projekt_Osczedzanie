import streamlit as st

st.set_page_config(page_title="Dlaczego nie oszczędzamy?", page_icon="🌱", layout="wide")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Manrope:wght@500;600;700;800&display=swap');
html, body, [class*="css"] {font-family:'DM Sans',sans-serif}
.stApp{background:radial-gradient(ellipse at 4% 0%,rgba(185,225,137,.27),transparent 34%),radial-gradient(ellipse at 100% 8%,rgba(130,196,155,.18),transparent 30%),#eef5e9;color:#173b34}
[data-testid="stHeader"]{background:transparent}
[data-testid="stSidebar"]{background:#123f38}
[data-testid="stSidebar"] *{color:#eef8e9!important}
.block-container{padding-top:2rem;padding-bottom:3rem;max-width:1450px}
.brand{display:flex;align-items:center;gap:10px;padding:8px 2px 20px}.brand-icon{background:linear-gradient(135deg,#cce66d,#8fbd62);border-radius:13px;padding:10px;font-size:23px}.brand-title{font:800 17px Manrope;color:white}.brand-sub{font-size:10px;letter-spacing:1.5px;color:#c4d9c9;text-transform:uppercase}
.hero{background:linear-gradient(118deg,#123f38 0%,#17574a 65%,#24745b 100%);border-radius:25px;padding:35px 38px;color:#f4faed;margin:5px 0 24px;box-shadow:0 16px 38px #184b3b22}.kicker{color:#d7ec87;font-size:10px;letter-spacing:2.2px;font-weight:800;text-transform:uppercase}.hero h1{font:800 clamp(28px,3.5vw,43px)/1.15 Manrope;color:white;margin:12px 0}.hero p{color:#d5e8dc;max-width:780px;line-height:1.7;margin:0}.chip{display:inline-block;margin-top:17px;padding:7px 12px;border-radius:30px;background:#dcef971c;border:1px solid #dcef973b;color:#e5f3b1;font-size:11px}
.section{font:800 22px Manrope;color:#173f35;margin:15px 0 5px}.lead{color:#6b8578;font-size:13px;margin-bottom:16px}.card{background:#ffffffc9;border:1px solid #dce9d9;border-radius:17px;padding:19px 20px;margin:10px 0;box-shadow:0 7px 22px #224e390a}.card h3{font:800 16px Manrope;color:#174b3e;margin:0 0 8px}.card-link-title{font:800 21px Manrope;color:#174b3e;margin:2px 0 10px;line-height:1.25}.card p{color:#536e60;line-height:1.65;font-size:15px;margin:0}.card-link-title{font-size:21px!important}.tag{display:inline-block;background:#e4efdc;color:#47704e;border-radius:20px;padding:5px 9px;font-size:10px;font-weight:800;margin-bottom:8px}.note{background:#e4efdc;border-left:4px solid #9cbd4f;border-radius:9px;padding:13px 16px;color:#496553;font-size:12px;line-height:1.6;margin:14px 0}.stButton>button{background:#cce66d;color:#244333;border:0;border-radius:30px;font-weight:800}.stButton>button:hover{background:#d8ef83;color:#173b34;border:0}
#MainMenu,footer{visibility:hidden}
</style>
""", unsafe_allow_html=True)
with st.sidebar:
    st.markdown('<div class="brand"><div class="brand-icon">🌱</div><div><div class="brand-title">Oszczędzanie bez tajemnic</div><div class="brand-sub">Wiedza · zachowania · decyzje</div></div></div>',unsafe_allow_html=True)
    st.caption("PROJEKT EDUKACYJNO-BADAWCZY")
    st.markdown("---")
    st.markdown("Poznaj bariery oszczędzania, sprawdź wyniki badania i zobacz, jak może pracować regularna wpłata.")
    st.markdown("---")
    st.caption("Projekt studencki · Materiał edukacyjny")

home=st.Page("pages/0_start.py",title="Wprowadzenie",default=True)
theory=st.Page("pages/2_dlaczego_nie_oszczedzamy.py",title="Dlaczego nie oszczędzamy?")
calculator=st.Page("pages/1_kalkulator_oszczednosci.py",title="Kalkulator oszczędności")
survey=st.Page("pages/3_wyniki_ankiety.py",title="Ankieta i wyniki")
nav=st.navigation({"PROJEKT":[home,theory,survey],"NARZĘDZIE PRAKTYCZNE":[calculator]},position="sidebar")
nav.run()
