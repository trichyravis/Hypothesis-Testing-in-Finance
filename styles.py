"""
styles.py — Minimal CSS injection for Mountain Path theme.
Only handles Streamlit native widgets (tabs, metrics, inputs).
All custom HTML now goes through st.html() to bypass Streamlit style injection.
"""
import streamlit as st

# ── Design Tokens (used by both CSS and inline HTML) ──────────────
C = {
    "dark":    "#0a1628",
    "card":    "#112240",
    "blue":    "#003366",
    "mid":     "#004d80",
    "gold":    "#FFD700",
    "lb":      "#ADD8E6",
    "grn":     "#28a745",
    "red":     "#dc3545",
    "txt":     "#e6f1ff",
    "mut":     "#8892b0",
    "acc":     "#64ffda",
    "bg":      "#1e2d45",
}

def inject_css():
    st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Source+Sans+Pro:wght@300;400;600&family=JetBrains+Mono:wght@400;600&display=swap');

/* App background */
.stApp {{
    background: linear-gradient(135deg,#1a2332,#243447,#2a3f5f) !important;
    font-family: 'Source Sans Pro', sans-serif !important;
}}
#MainMenu, footer, header {{ visibility: hidden; }}
.block-container {{ padding-top: 1rem !important; max-width: 1200px; }}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {{
    background: {C['card']} !important;
    border-radius: 8px; padding: 4px; gap: 4px;
    border: 1px solid #1e3a5f;
}}
.stTabs [data-baseweb="tab"] {{
    background: transparent !important;
    color: {C['mut']} !important;
    font-family: 'Source Sans Pro', sans-serif !important;
    font-weight: 600 !important; font-size: .88rem !important;
    border-radius: 6px !important; padding: 8px 16px !important;
    border: none !important; transition: all .25s !important;
}}
.stTabs [data-baseweb="tab"]:hover {{
    color: {C['gold']} !important;
    background: rgba(0,77,128,.3) !important;
}}
.stTabs [aria-selected="true"] {{
    background: {C['blue']} !important;
    color: {C['gold']} !important;
    border: 1px solid {C['gold']} !important;
}}
.stTabs [data-baseweb="tab-border"] {{ display:none !important; }}
.stTabs [data-baseweb="tab-panel"] {{ padding-top: 14px !important; }}

/* Metrics */
div[data-testid="stMetric"] {{
    background: {C['card']} !important;
    border: 1px solid #1e3a5f !important;
    border-radius: 8px !important; padding: 14px !important;
}}
div[data-testid="stMetric"] label {{
    color: {C['lb']} !important; font-weight: 600 !important;
}}
div[data-testid="stMetric"] [data-testid="stMetricValue"] {{
    color: {C['gold']} !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 1.4rem !important;
}}

/* Inputs */
.stSelectbox label, .stSlider label,
.stRadio label, .stNumberInput label {{
    color: {C['lb']} !important; font-weight: 600 !important;
}}
.stSelectbox [data-baseweb="select"] > div {{
    background: {C['card']} !important;
    border-color: #1e3a5f !important; color: {C['txt']} !important;
}}
.stSelectbox [data-baseweb="select"] span {{ color: {C['txt']} !important; }}
.stRadio [data-testid="stMarkdownContainer"] p {{ color: {C['txt']} !important; }}
.stRadio div[role="radiogroup"] label span {{ color: {C['txt']} !important; }}
.stSlider p {{ color: {C['lb']} !important; }}
.stNumberInput input {{
    background: {C['card']} !important;
    color: {C['txt']} !important; border-color: #1e3a5f !important;
}}
.stButton button {{
    background: {C['blue']} !important; color: {C['gold']} !important;
    border: 2px solid {C['gold']} !important;
    font-weight: 700 !important; border-radius: 6px !important;
}}
.stButton button:hover {{ background: {C['mid']} !important; }}
.stCodeBlock pre {{ background: #0d1f3a !important; }}
.stCodeBlock code {{ color: {C['acc']} !important; }}

/* st.html iframe sizing */
iframe {{ border: none !important; }}
</style>
""", unsafe_allow_html=True)
