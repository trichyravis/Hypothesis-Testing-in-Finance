"""
components.py — All HTML uses st.html() with 100% inline styles.
user-select:none prevents browser auto-selection highlights.
"""
import streamlit as st

# ── Design tokens ─────────────────────────────────────────────────
S = {
    "txt":  "#e6f1ff",
    "gold": "#FFD700",
    "lb":   "#ADD8E6",
    "grn":  "#28a745",
    "red":  "#dc3545",
    "acc":  "#64ffda",
    "mut":  "#8892b0",
    "card": "#112240",
    "blue": "#003366",
    "mid":  "#004d80",
    "dark": "#0a1628",
    "bdr":  "#1e3a5f",
}
FH = "'Playfair Display',serif"
FB = "'Source Sans Pro',sans-serif"
FM = "'JetBrains Mono',monospace"

# Base text style applied to every text-bearing element
TXT = f"color:#e6f1ff;font-family:{FB};line-height:1.65;-webkit-text-fill-color:#e6f1ff"
# Prevent browser selection blue highlight on static content
NO_SEL = "user-select:none;-webkit-user-select:none"


# ── Card ──────────────────────────────────────────────────────────
def render_card(title: str, body_html: str):
    h2 = (f'<h2 style="font-family:{FH};font-size:1.35rem;color:#FFD700;'
          f'-webkit-text-fill-color:#FFD700;border-bottom:1px solid #1e3a5f;'
          f'padding-bottom:8px;margin:0 0 14px 0;{NO_SEL}">{title}</h2>')
    html = (f'<div style="background:#112240;border:1px solid #1e3a5f;border-radius:10px;'
            f'padding:22px;margin-bottom:18px;{TXT};{NO_SEL}">'
            f'{h2}{body_html}</div>')
    st.html(html)


# ── Info Box (returns HTML string for embedding) ──────────────────
_IB_BORDERS = {
    "blue":  ("rgba(0,51,102,0.6)",  "#ADD8E6"),
    "gold":  ("rgba(255,215,0,0.13)","#FFD700"),
    "green": ("rgba(40,167,69,0.2)", "#28a745"),
    "red":   ("rgba(220,53,69,0.2)", "#dc3545"),
}

def ib(content: str, variant: str = "blue") -> str:
    bg, bc = _IB_BORDERS.get(variant, _IB_BORDERS["blue"])
    return (
        f'<div style="background:{bg};border-left:4px solid {bc};border-radius:8px;'
        f'padding:13px 15px;margin:10px 0;{TXT};{NO_SEL}">'
        f'{content}'
        f'</div>'
    )

def render_ib(content: str, variant: str = "blue"):
    """Render standalone info box via st.html()."""
    st.html(ib(content, variant))


# ── Inline text spans (all carry explicit color + no-select) ──────
def hl(t):  return f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">{t}</span>'
def gt(t):  return f'<span style="color:#28a745;-webkit-text-fill-color:#28a745;font-weight:600">{t}</span>'
def rt2(t): return f'<span style="color:#dc3545;-webkit-text-fill-color:#dc3545;font-weight:600">{t}</span>'
def vf(t):  return f'<span style="color:#28a745;-webkit-text-fill-color:#28a745;font-weight:700">{t}</span>'
def vr(t):  return f'<span style="color:#dc3545;-webkit-text-fill-color:#dc3545;font-weight:700">{t}</span>'
def lb_t(t):return f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6">{t}</span>'
def mut_t(t):return f'<span style="color:#8892b0;-webkit-text-fill-color:#8892b0">{t}</span>'
def txt_s(t):return f'<span style="color:#e6f1ff;-webkit-text-fill-color:#e6f1ff">{t}</span>'

def p(content: str) -> str:
    """Paragraph with forced light text."""
    return f'<p style="{TXT};margin-bottom:7px">{content}</p>'


# ── Formula Box ───────────────────────────────────────────────────
def fml(content: str) -> str:
    return (f'<div style="background:#0d1f3a;border-left:4px solid #FFD700;border-radius:6px;'
            f'padding:13px 17px;margin:10px 0;font-family:{FM};font-size:.88rem;'
            f'color:#64ffda;-webkit-text-fill-color:#64ffda;line-height:1.85;'
            f'white-space:pre-wrap;overflow-x:auto;{NO_SEL}">{content}</div>')


# ── Badge ─────────────────────────────────────────────────────────
_BADGE = {
    "blue":  ("#004d80","#ffffff"),
    "gold":  ("#FFD700","#0a1628"),
    "green": ("#28a745","#ffffff"),
    "red":   ("#dc3545","#ffffff"),
}

def bdg(text: str, variant: str = "blue") -> str:
    bg, fg = _BADGE.get(variant, _BADGE["blue"])
    return (f'<span style="background:{bg};color:{fg};-webkit-text-fill-color:{fg};'
            f'display:inline-block;padding:2px 10px;border-radius:20px;font-size:.77rem;'
            f'font-weight:700;margin:2px;font-family:{FB};{NO_SEL}">{text}</span>')


# ── Steps ─────────────────────────────────────────────────────────
def steps_html(steps: list) -> str:
    rows = ""
    for i, (title, body) in enumerate(steps, 1):
        rows += (
            f'<div style="display:flex;gap:12px;margin-bottom:12px;align-items:flex-start;{NO_SEL}">'
            f'<div style="background:#FFD700;color:#0a1628;-webkit-text-fill-color:#0a1628;'
            f'border-radius:50%;min-width:28px;height:28px;display:flex;align-items:center;'
            f'justify-content:center;font-weight:700;font-size:.85rem;font-family:{FB}">{i}</div>'
            f'<div style="{TXT};flex:1">'
            f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">{title}</span><br>'
            f'<span style="color:#e6f1ff;-webkit-text-fill-color:#e6f1ff">{body}</span>'
            f'</div></div>'
        )
    return rows


# ── Grid Layouts ──────────────────────────────────────────────────
def two_col(left: str, right: str) -> str:
    return (f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:10px 0">'
            f'<div>{left}</div><div>{right}</div></div>')

def three_col(a: str, b: str, c: str) -> str:
    return (f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin:10px 0">'
            f'<div>{a}</div><div>{b}</div><div>{c}</div></div>')


# ── Table ─────────────────────────────────────────────────────────
def table_html(headers: list, rows: list) -> str:
    ths = "".join(
        f'<th style="background:#003366;color:#FFD700;-webkit-text-fill-color:#FFD700;'
        f'padding:9px 12px;text-align:left;font-weight:600;font-family:{FB}">{h}</th>'
        for h in headers
    )
    trs = ""
    for row in rows:
        tds = "".join(
            f'<td style="padding:8px 12px;border-bottom:1px solid #1e3a5f;'
            f'color:#e6f1ff;-webkit-text-fill-color:#e6f1ff;font-family:{FB}">{c}</td>'
            for c in row
        )
        trs += f'<tr>{tds}</tr>'
    return (f'<table style="width:100%;border-collapse:collapse;margin:12px 0;'
            f'font-size:.88rem;{NO_SEL}"><tr>{ths}</tr>{trs}</table>')


# ── Section heading ───────────────────────────────────────────────
def section_heading(title: str):
    st.html(f'<h3 style="font-family:{FH};color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;'
            f'font-size:1.1rem;margin:18px 0 8px 0;{NO_SEL}">{title}</h3>')


# ── Metric Row (Streamlit native) ─────────────────────────────────
def metric_row(metrics: list):
    cols = st.columns(len(metrics))
    for col, (label, value, *rest) in zip(cols, metrics):
        col.metric(label, value, rest[0] if rest else None)
