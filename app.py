"""
Hypothesis Testing in Finance — Streamlit App
The Mountain Path – World of Finance | Prof. V. Ravichandran
"""
import streamlit as st
from styles import inject_css
from tabs import (
    tab_overview, tab_one_tailed, tab_two_tailed,
    tab_comparison, tab_finance_examples, tab_python_code,
)
from tab_non_finance import tab_non_finance
from tab_edu_hub     import tab_edu_hub

st.set_page_config(
    page_title="Hypothesis Testing in Finance",
    page_icon="📐", layout="wide",
    initial_sidebar_state="collapsed",
)
inject_css()

NO_SEL = "user-select:none;-webkit-user-select:none"
FH = "'Playfair Display',serif"
FB = "'Source Sans Pro',sans-serif"

st.html(f"""
<div style="text-align:center;padding:28px 20px 14px;
            border-bottom:2px solid #FFD700;margin-bottom:24px;{NO_SEL}">
  <h1 style="font-family:{FH};font-size:2.15rem;color:#FFD700;
             -webkit-text-fill-color:#FFD700;letter-spacing:1px;margin-bottom:6px">
    Hypothesis Testing in Finance
  </h1>
  <p style="color:#8892b0;-webkit-text-fill-color:#8892b0;
            font-family:{FB};font-size:1rem;margin-bottom:4px">
    One-Tailed &amp; Two-Tailed Tests — Concepts, Visuals &amp; Real-World Examples
  </p>
  <p style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;
            font-family:{FB};font-size:0.85rem;font-style:italic">
    The Mountain Path – World of Finance &nbsp;|&nbsp; Prof. V. Ravichandran
  </p>
  <div style="display:flex;justify-content:center;gap:10px;margin-top:12px;flex-wrap:wrap">
    <span style="background:rgba(0,51,102,0.6);color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;
                 padding:3px 12px;border-radius:20px;font-size:.78rem;font-family:{FB};
                 border:1px solid #1e3a5f">z-Test &amp; t-Test</span>
    <span style="background:rgba(255,215,0,0.12);color:#FFD700;-webkit-text-fill-color:#FFD700;
                 padding:3px 12px;border-radius:20px;font-size:.78rem;font-family:{FB};
                 border:1px solid #FFD700">Fund Alpha Testing</span>
    <span style="background:rgba(40,167,69,0.18);color:#28a745;-webkit-text-fill-color:#28a745;
                 padding:3px 12px;border-radius:20px;font-size:.78rem;font-family:{FB};
                 border:1px solid #28a745">VaR Backtesting</span>
    <span style="background:rgba(255,159,67,0.15);color:#ff9f43;-webkit-text-fill-color:#ff9f43;
                 padding:3px 12px;border-radius:20px;font-size:.78rem;font-family:{FB};
                 border:1px solid #ff9f43">Bond Duration</span>
    <span style="background:rgba(162,155,254,0.15);color:#a29bfe;-webkit-text-fill-color:#a29bfe;
                 padding:3px 12px;border-radius:20px;font-size:.78rem;font-family:{FB};
                 border:1px solid #a29bfe">6 Non-Finance Cases</span>
  </div>
</div>
""")

tabs = st.tabs([
    "📐 Overview",
    "→ One-Tailed",
    "↔ Two-Tailed",
    "⚖ Comparison",
    "💹 Finance Examples",
    "🌍 Everyday Examples",
    "📚 Education Hub",
    "🐍 Python Code",
])

with tabs[0]: tab_overview()
with tabs[1]: tab_one_tailed()
with tabs[2]: tab_two_tailed()
with tabs[3]: tab_comparison()
with tabs[4]: tab_finance_examples()
with tabs[5]: tab_non_finance()
with tabs[6]: tab_edu_hub()
with tabs[7]: tab_python_code()

st.html(f"""
<div style="text-align:center;padding:18px;color:#8892b0;-webkit-text-fill-color:#8892b0;
            font-family:{FB};font-size:.84rem;border-top:1px solid #1e3a5f;
            margin-top:28px;line-height:1.9;{NO_SEL}">
  <strong style="color:#FFD700;-webkit-text-fill-color:#FFD700">
    The Mountain Path – World of Finance
  </strong><br>
  <a href="https://www.linkedin.com/in/trichyravis" target="_blank"
     style="color:#FFD700;-webkit-text-fill-color:#FFD700;text-decoration:none">LinkedIn</a>
  &nbsp;|&nbsp;
  <a href="https://github.com/trichyravis" target="_blank"
     style="color:#FFD700;-webkit-text-fill-color:#FFD700;text-decoration:none">GitHub</a><br>
  <span style="color:#8892b0;-webkit-text-fill-color:#8892b0">
    Prof. V. Ravichandran &nbsp;|&nbsp;
    28+ Years Corporate Finance &amp; Banking &nbsp;|&nbsp;
    10+ Years Academic Excellence
  </span>
</div>
""")
