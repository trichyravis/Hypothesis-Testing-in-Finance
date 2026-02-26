"""
styles.py — CSS injection for Mountain Path design theme
Colors: darkblue #003366 | midblue #004d80 | gold #FFD700
        cardBg #112240 | bgDark #0a1628 | lightblue #ADD8E6
Fonts: Playfair Display (headings) + Source Sans Pro (body) + JetBrains Mono (code)
"""

import streamlit as st


def inject_css():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Source+Sans+Pro:wght@300;400;600&family=JetBrains+Mono:wght@400;600&display=swap');

/* ── Root Variables ── */
:root {
    --dark:    #0a1628;
    --card:    #112240;
    --blue:    #003366;
    --mid:     #004d80;
    --gold:    #FFD700;
    --lb:      #ADD8E6;
    --grn:     #28a745;
    --red:     #dc3545;
    --txt:     #e6f1ff;
    --mut:     #8892b0;
    --acc:     #64ffda;
}

/* ── App Background ── */
.stApp {
    background: linear-gradient(135deg, #1a2332, #243447, #2a3f5f) !important;
    font-family: 'Source Sans Pro', sans-serif !important;
}

/* ── Hide default Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1rem !important; max-width: 1200px; }

/* ── Header ── */
.mp-header {
    text-align: center;
    padding: 28px 20px 14px;
    border-bottom: 2px solid var(--gold);
    margin-bottom: 24px;
}
.mp-header h1 {
    font-family: 'Playfair Display', serif !important;
    font-size: 2.15rem !important;
    color: var(--gold) !important;
    letter-spacing: 1px;
    margin-bottom: 6px;
}
.mp-header .subtitle { color: var(--mut); font-size: 1rem; margin-bottom: 4px; }
.mp-header .brand { font-size: 0.85rem; color: var(--lb); font-style: italic; }

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: var(--card) !important;
    border-radius: 8px;
    padding: 4px;
    gap: 4px;
    border: 1px solid #1e3a5f;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: var(--mut) !important;
    font-family: 'Source Sans Pro', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    border-radius: 6px !important;
    padding: 8px 16px !important;
    border: none !important;
    transition: all 0.25s !important;
}
.stTabs [data-baseweb="tab"]:hover {
    color: var(--gold) !important;
    background: rgba(0,77,128,0.3) !important;
}
.stTabs [aria-selected="true"] {
    background: var(--blue) !important;
    color: var(--gold) !important;
    border: 1px solid var(--gold) !important;
}
.stTabs [data-baseweb="tab-border"] { display: none !important; }
.stTabs [data-baseweb="tab-panel"] { padding-top: 16px !important; }

/* ── Cards ── */
.mp-card {
    background: var(--card);
    border: 1px solid #1e3a5f;
    border-radius: 10px;
    padding: 22px;
    margin-bottom: 18px;
}
.mp-card h2 {
    font-family: 'Playfair Display', serif;
    font-size: 1.35rem;
    color: var(--gold);
    border-bottom: 1px solid #1e3a5f;
    padding-bottom: 8px;
    margin-bottom: 14px;
}
.mp-card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.05rem;
    color: var(--lb);
    margin: 12px 0 7px;
}
.mp-card p { line-height: 1.7; color: var(--txt); margin-bottom: 7px; }

/* ── Info Boxes ── */
.ib {
    border-radius: 8px;
    padding: 13px 15px;
    margin: 10px 0;
    border-left: 4px solid;
    line-height: 1.65;
}
.ib p { margin-bottom: 4px; color: var(--txt); }
.ib-blue  { background: rgba(0,51,102,0.45);  border-color: var(--lb);  }
.ib-gold  { background: rgba(255,215,0,0.1);  border-color: var(--gold); }
.ib-green { background: rgba(40,167,69,0.15); border-color: var(--grn); }
.ib-red   { background: rgba(220,53,69,0.15); border-color: var(--red); }

/* ── Formula Box ── */
.fml {
    background: #0d1f3a;
    border-left: 4px solid var(--gold);
    border-radius: 6px;
    padding: 13px 17px;
    margin: 10px 0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.88rem;
    color: var(--acc);
    line-height: 1.85;
    white-space: pre-wrap;
    overflow-x: auto;
}

/* ── Steps ── */
.step-row {
    display: flex;
    gap: 12px;
    margin-bottom: 12px;
    align-items: flex-start;
}
.step-num {
    background: var(--gold);
    color: var(--dark);
    border-radius: 50%;
    width: 28px; height: 28px;
    display: flex; align-items: center; justify-content: center;
    font-weight: 700; font-size: 0.85rem;
    flex-shrink: 0;
    font-family: 'Source Sans Pro', sans-serif;
}
.step-body { flex: 1; color: var(--txt); line-height: 1.65; }
.step-body strong { color: var(--lb); }

/* ── Badges ── */
.bdg {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 20px;
    font-size: 0.77rem;
    font-weight: 700;
    margin: 2px;
    font-family: 'Source Sans Pro', sans-serif;
}
.bdg-blue  { background: var(--mid);  color: white; }
.bdg-gold  { background: var(--gold); color: var(--dark); }
.bdg-green { background: var(--grn);  color: white; }
.bdg-red   { background: var(--red);  color: white; }

/* ── Tables ── */
.mp-table {
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 0.88rem;
    font-family: 'Source Sans Pro', sans-serif;
}
.mp-table th {
    background: var(--blue);
    color: var(--gold);
    padding: 9px 12px;
    text-align: left;
    font-weight: 600;
}
.mp-table td {
    padding: 8px 12px;
    border-bottom: 1px solid #1e3a5f;
    color: var(--txt);
}
.mp-table tr:hover td { background: rgba(0,77,128,0.2); }
.hl  { color: var(--gold); font-weight: 600; }
.gt  { color: var(--grn);  font-weight: 600; }
.rt  { color: var(--red);  font-weight: 600; }
.vf  { color: var(--grn);  font-weight: 700; }
.vr  { color: var(--red);  font-weight: 700; }

/* ── Code Block ── */
.code-block {
    background: #0d1f3a;
    border: 1px solid #1e3a5f;
    border-radius: 8px;
    padding: 18px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.79rem;
    line-height: 1.65;
    overflow-x: auto;
    white-space: pre;
    color: var(--acc);
    margin-top: 8px;
}
.cc { color: #8892b0; }
.ck { color: #FFD700; }
.cf { color: #28a745; }
.cs { color: #ff9f43; }
.cn { color: #ADD8E6; }

/* ── Streamlit widgets overrides ── */
.stMarkdown p { color: var(--txt) !important; }
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
    font-family: 'Playfair Display', serif !important;
    color: var(--gold) !important;
}
div[data-testid="stMetric"] {
    background: var(--card) !important;
    border: 1px solid #1e3a5f !important;
    border-radius: 8px !important;
    padding: 14px !important;
}
div[data-testid="stMetric"] label { color: var(--lb) !important; font-weight:600 !important; }
div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: var(--gold) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 1.4rem !important;
}

/* ── Selectbox / slider overrides ── */
.stSelectbox label, .stSlider label, .stRadio label {
    color: var(--lb) !important;
    font-weight: 600 !important;
    font-family: 'Source Sans Pro', sans-serif !important;
}
.stSelectbox [data-baseweb="select"] > div {
    background: var(--card) !important;
    border-color: #1e3a5f !important;
    color: var(--txt) !important;
}
.stSlider [data-testid="stTickBar"] { color: var(--mut) !important; }
.stRadio [data-testid="stMarkdownContainer"] p { color: var(--txt) !important; }

/* ── Expander ── */
.streamlit-expanderHeader {
    background: var(--card) !important;
    color: var(--lb) !important;
    font-weight: 600 !important;
    border: 1px solid #1e3a5f !important;
    border-radius: 6px !important;
}
.streamlit-expanderContent {
    background: rgba(17,34,64,0.7) !important;
    border: 1px solid #1e3a5f !important;
}

/* ── Footer ── */
.mp-footer {
    text-align: center;
    padding: 18px;
    color: var(--mut);
    font-size: 0.84rem;
    border-top: 1px solid #1e3a5f;
    margin-top: 28px;
    line-height: 1.9;
}
.mp-footer a { color: var(--gold); text-decoration: none; }
.mp-footer a:hover { text-decoration: underline; }
</style>
""", unsafe_allow_html=True)
