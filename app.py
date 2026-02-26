"""
Hypothesis Testing in Finance — One-Tailed & Two-Tailed Tests
The Mountain Path – World of Finance
Prof. V. Ravichandran
"""

import streamlit as st
from styles import inject_css
from tabs import (
    tab_overview,
    tab_one_tailed,
    tab_two_tailed,
    tab_comparison,
    tab_finance_examples,
    tab_python_code,
)

st.set_page_config(
    page_title="Hypothesis Testing in Finance",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_css()

# ── Header ──────────────────────────────────────────────────────────
st.markdown("""
<div class="mp-header">
    <h1>Hypothesis Testing in Finance</h1>
    <p class="subtitle">One-Tailed &amp; Two-Tailed Tests — Concepts, Visuals &amp; Real-World Finance Examples</p>
    <p class="brand">The Mountain Path – World of Finance &nbsp;|&nbsp; Prof. V. Ravichandran</p>
</div>
""", unsafe_allow_html=True)

# ── Tab Navigation ───────────────────────────────────────────────────
TABS = [
    "📐 Overview",
    "→ One-Tailed",
    "↔ Two-Tailed",
    "⚖ Comparison",
    "💹 Finance Examples",
    "🐍 Python Code",
]

tabs = st.tabs(TABS)

with tabs[0]:
    tab_overview()
with tabs[1]:
    tab_one_tailed()
with tabs[2]:
    tab_two_tailed()
with tabs[3]:
    tab_comparison()
with tabs[4]:
    tab_finance_examples()
with tabs[5]:
    tab_python_code()

# ── Footer ───────────────────────────────────────────────────────────
st.markdown("""
<div class="mp-footer">
    <strong style="color:#FFD700">The Mountain Path – World of Finance</strong><br>
    <a href="https://www.linkedin.com/in/trichyravis" target="_blank">LinkedIn</a>
    &nbsp;|&nbsp;
    <a href="https://github.com/trichyravis" target="_blank">GitHub</a><br>
    <span style="color:#8892b0">Prof. V. Ravichandran &nbsp;|&nbsp;
    28+ Years Corporate Finance &amp; Banking &nbsp;|&nbsp;
    10+ Years Academic Excellence</span>
</div>
""", unsafe_allow_html=True)
