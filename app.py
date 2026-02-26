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
    One-Tailed &amp; Two-Tailed Tests — Concepts, Visuals &amp; Real-World Finance Examples
  </p>
  <p style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;
            font-family:{FB};font-size:0.85rem;font-style:italic">
    The Mountain Path – World of Finance &nbsp;|&nbsp; Prof. V. Ravichandran
  </p>
</div>
""")

tabs = st.tabs(["📐 Overview","→ One-Tailed","↔ Two-Tailed","⚖ Comparison","💹 Finance Examples","🐍 Python Code"])
with tabs[0]: tab_overview()
with tabs[1]: tab_one_tailed()
with tabs[2]: tab_two_tailed()
with tabs[3]: tab_comparison()
with tabs[4]: tab_finance_examples()
with tabs[5]: tab_python_code()

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
