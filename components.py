"""
components.py — Reusable HTML helper functions for Mountain Path design system
"""

import streamlit as st


def card_open(title: str = "") -> str:
    h = f'<h2>{title}</h2>' if title else ''
    return f'<div class="mp-card">{h}'


def card_close() -> str:
    return '</div>'


def card(title: str, body: str):
    """Render a full card with title and HTML body."""
    st.markdown(f'<div class="mp-card"><h2>{title}</h2>{body}</div>',
                unsafe_allow_html=True)


def info_box(content: str, variant: str = "blue") -> str:
    """variant: blue | gold | green | red"""
    cls = {"blue": "ib-blue", "gold": "ib-gold",
           "green": "ib-green", "red": "ib-red"}.get(variant, "ib-blue")
    return f'<div class="ib {cls}">{content}</div>'


def formula_box(content: str) -> str:
    return f'<div class="fml">{content}</div>'


def badge(text: str, variant: str = "blue") -> str:
    cls = {"blue": "bdg-blue", "gold": "bdg-gold",
           "green": "bdg-green", "red": "bdg-red"}.get(variant, "bdg-blue")
    return f'<span class="bdg {cls}">{text}</span>'


def steps_html(steps: list) -> str:
    """steps: list of (title, body_html) tuples"""
    html = ""
    for i, (title, body) in enumerate(steps, 1):
        html += f"""
<div class="step-row">
  <div class="step-num">{i}</div>
  <div class="step-body"><strong>{title}</strong><br>{body}</div>
</div>"""
    return html


def two_col_html(left: str, right: str) -> str:
    return f"""
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:10px 0">
  <div>{left}</div>
  <div>{right}</div>
</div>"""


def three_col_html(a: str, b: str, c: str) -> str:
    return f"""
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin:10px 0">
  <div>{a}</div><div>{b}</div><div>{c}</div>
</div>"""


def table_html(headers: list, rows: list) -> str:
    th = "".join(f"<th>{h}</th>" for h in headers)
    tr = "".join(
        "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>"
        for row in rows
    )
    return f'<table class="mp-table"><tr>{th}</tr>{tr}</table>'


def metric_row(metrics: list) -> None:
    """metrics: list of (label, value, delta=None)"""
    cols = st.columns(len(metrics))
    for col, (label, value, *rest) in zip(cols, metrics):
        delta = rest[0] if rest else None
        col.metric(label, value, delta)
