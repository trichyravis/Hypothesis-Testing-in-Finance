"""
tab_non_finance.py — Everyday (Non-Finance) Hypothesis Testing Examples
Six real-world cases from medicine, education, manufacturing, psychology, 
agriculture, and quality control. Same z/t framework, different domains.
"""
import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from components import (
    render_card, ib, render_ib, fml, bdg,
    hl, gt, rt2, vf, vr, lb_t, mut_t, txt_s, p,
    steps_html, two_col, three_col, table_html,
    metric_row, section_heading,
    S, FH, FB, FM, TXT, NO_SEL,
)
from tab_explainers import explainer_non_finance
from tabs import _plot_test

# ── Local helpers ─────────────────────────────────────────────────
def _f(t): return f'<span style="font-family:{FM};color:#64ffda;-webkit-text-fill-color:#64ffda">{t}</span>'
def _hdr(icon, title, color):
    return (f'<div style="font-family:{FH};font-size:1.05rem;color:{color};'
            f'-webkit-text-fill-color:{color};margin:0 0 7px 0;font-weight:700">{icon} {title}</div>')

def _case_header(num, domain, title, test_type, badge_variant):
    return (
        f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;{NO_SEL}">'
        f'<span style="background:#003366;color:#FFD700;-webkit-text-fill-color:#FFD700;'
        f'font-family:{FH};font-size:1.1rem;font-weight:700;padding:4px 12px;'
        f'border-radius:6px">Case {num}</span>'
        f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;'
        f'font-family:{FB};font-size:.82rem;font-weight:600">{domain}</span>'
        f'<span style="flex:1"></span>'
        f'{bdg(test_type, badge_variant)}</div>'
        f'<div style="font-family:{FH};font-size:1.05rem;color:#FFD700;'
        f'-webkit-text-fill-color:#FFD700;margin-bottom:10px">{title}</div>'
    )

def _result_badge(rej):
    if rej:
        return f'<span style="color:#dc3545;-webkit-text-fill-color:#dc3545;font-weight:700;font-size:1rem">🔴 REJECT H₀</span>'
    return f'<span style="color:#28a745;-webkit-text-fill-color:#28a745;font-weight:700;font-size:1rem">🟢 FAIL TO REJECT H₀</span>'


# ═══════════════════════════════════════════════════════════
# CASE STUDY FUNCTIONS
# ═══════════════════════════════════════════════════════════

def _case_drug_trial(alpha):
    """Case 1 — Medicine: Drug efficacy test"""
    xb, mu0, sigma, n = 138.5, 140.0, 8.0, 64
    se = sigma / np.sqrt(n)
    z  = (xb - mu0) / se
    zc = stats.norm.ppf(alpha)           # left-tailed
    pv = stats.norm.cdf(z)
    rej = z < zc

    render_card("💊 Case 1 — Medicine: Blood Pressure Drug Trial",
        ib(_case_header("1", "🏥 Clinical Medicine", "Does the new drug lower blood pressure?",
                         "Left-Tailed z-test", "red"),
           "gold") +
        p(f'A pharmaceutical company tests a new antihypertensive drug. '
          f'Before treatment, patients averaged {hl("140 mmHg")} systolic BP (σ = 8 mmHg, known from large prior studies). '
          f'After administering the drug to {hl("n = 64 patients")}, the sample mean drops to {hl("138.5 mmHg")}. '
          f'Does the drug significantly reduce blood pressure?') +
        two_col(
            ib(f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">Hypotheses</span><br>'
               + p(f'{lb_t("<strong>H₀:</strong>")} μ ≥ 140 mmHg (drug has no effect or worsens)'
                   f'<br>{lb_t("<strong>H₁:</strong>")} μ < 140 mmHg (drug lowers BP)'
                   f'<br>{bdg("Left-Tailed Test", "red")} — we predict a decrease'), "blue"),
            ib(f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">Why left-tailed?</span><br>'
               + p('We specifically predict the drug <em>reduces</em> BP — we are not merely asking '
                   'if BP changed. The directional prediction concentrates all rejection power '
                   'in the left tail, making the test more sensitive to reduction.'), "gold"),
        ) +
        fml(f'SE  = σ/√n = {sigma}/√{n} = {se:.4f}\n'
            f'z   = (x̄ − μ₀)/SE = ({xb} − {mu0})/{se:.4f} = {hl(f"{z:.4f}")}\n'
            f'z_crit (α={alpha}, left) = {hl(f"{zc:.3f}")}\n'
            f'p-value = P(Z < {z:.4f}) = {hl(f"{pv:.4f}")}')
    )

    metric_row([
        ("z-statistic", f"{z:.4f}", None),
        (f"z-critical (α={alpha})", f"{zc:.3f}", None),
        ("p-value", f"{pv:.4f}", None),
        ("Decision", "REJECT H₀ 🔴" if rej else "FAIL TO REJECT 🟢", None),
    ])

    ssteps = [
        ("Set hypotheses", f'H₀: μ ≥ 140 &nbsp;|&nbsp; H₁: μ < 140 → {bdg("Left-Tailed","red")}'),
        ("Compute SE",     fml(f'SE = {sigma}/√{n} = {se:.4f} mmHg')),
        ("Compute z",      fml(f'z = ({xb} − {mu0}) / {se:.4f} = {hl(f"{z:.4f}")}')),
        ("Find z_crit",    txt_s(f'Left-tail α={alpha}: z_crit = {hl(f"{zc:.3f}")}')),
        ("Decision",       _result_badge(rej) + txt_s(f' — z = {z:.4f} vs z_crit = {zc:.3f}') +
                           p(f'p-value = {pv:.4f} {"< α → Statistically significant drug effect" if pv < alpha else "> α → Insufficient evidence"}')),
    ]
    render_ib(
        f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">Step-by-Step Solution:</span>'
        f'<div style="margin-top:10px">{steps_html(ssteps)}</div>', "gold"
    )
    render_ib(
        f'<span style="color:#28a745;-webkit-text-fill-color:#28a745;font-weight:600">Real-World Interpretation: </span>'
        + txt_s(f'{"The drug shows a statistically significant reduction in blood pressure at the chosen significance level. The FDA would require additional trials, but this is a promising result." if rej else "The reduction in mean blood pressure (1.5 mmHg) is not statistically significant at the chosen level — it could easily be due to random sampling variation. More subjects or a larger dose may be needed."}'),
        "green"
    )
    fig = _plot_test(z, alpha, "left", f"Drug Trial: BP Reduction Test | α={alpha}")
    st.pyplot(fig, use_container_width=True); plt.close(fig)


def _case_exam_scores(alpha):
    """Case 2 — Education: Did new teaching method improve scores?"""
    xb, mu0, s, n = 72.4, 68.0, 14.0, 49
    se = s / np.sqrt(n)
    t  = (xb - mu0) / se
    df = n - 1
    tc = stats.t.ppf(1 - alpha, df)   # right-tailed
    pv = 1 - stats.t.cdf(t, df)
    rej = t > tc

    render_card("📚 Case 2 — Education: New Teaching Method Test",
        ib(_case_header("2", "🏫 Education Research", "Did the new teaching method improve exam scores?",
                         "Right-Tailed t-test", "gold"),
           "gold") +
        p(f'A university introduces a {hl("flipped classroom")} teaching method. '
          f'Historically, the average exam score was {hl("68 marks")} (out of 100). '
          f'A sample of {hl("n = 49 students")} taught with the new method scored a mean of {hl("72.4")} '
          f'(sample std dev = 14.0). Did the new method improve scores?') +
        two_col(
            ib(f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">Hypotheses</span><br>'
               + p(f'{lb_t("<strong>H₀:</strong>")} μ ≤ 68 (no improvement or worse)'
                   f'<br>{lb_t("<strong>H₁:</strong>")} μ > 68 (scores improved)'
                   f'<br>{bdg("Right-Tailed t-test", "gold")} — σ unknown, use t-distribution'), "blue"),
            ib(f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">Why t-test?</span><br>'
               + p('Population σ is unknown — we only have the sample std dev s. '
                   'The t-distribution has heavier tails than normal, making it harder to reject H₀, '
                   f'which is appropriate. With df = {df} and large n, t ≈ z.'), "gold"),
        ) +
        fml(f'SE     = s/√n = {s}/√{n} = {se:.4f}\n'
            f't      = (x̄ − μ₀)/SE = ({xb} − {mu0})/{se:.4f} = {hl(f"{t:.4f}")}\n'
            f'df     = n−1 = {df}\n'
            f't_crit (α={alpha}, df={df}, right) = {hl(f"{tc:.3f}")}\n'
            f'p-value = P(T > {t:.4f}) = {hl(f"{pv:.4f}")}')
    )

    metric_row([
        ("t-statistic", f"{t:.4f}", None),
        (f"t-critical (df={df}, α={alpha})", f"{tc:.3f}", None),
        ("p-value", f"{pv:.4f}", None),
        ("Decision", "REJECT H₀ 🔴" if rej else "FAIL TO REJECT 🟢", None),
    ])

    render_ib(
        f'<span style="color:#28a745;-webkit-text-fill-color:#28a745;font-weight:600">Real-World Interpretation: </span>'
        + txt_s(f'{"The improvement of 4.4 marks is statistically significant — the flipped classroom method genuinely raised scores. The university should consider adopting it widely." if rej else "The 4.4-mark improvement is not statistically significant at this level — it could reflect sampling variation. The university should test with a larger cohort before adopting the method."}'),
        "green"
    )
    fig = _plot_test(t, alpha, "right", f"Teaching Method: Score Improvement Test | α={alpha}, df={df}")
    st.pyplot(fig, use_container_width=True); plt.close(fig)


def _case_factory_weight(alpha):
    """Case 3 — Manufacturing: Quality control on cereal box weight"""
    xb, mu0, sigma, n = 499.1, 500.0, 4.0, 100
    se = sigma / np.sqrt(n)
    z  = (xb - mu0) / se
    zc = stats.norm.ppf(1 - alpha / 2)   # two-tailed
    pv = 2 * (1 - stats.norm.cdf(abs(z)))
    rej = abs(z) > zc

    render_card("🏭 Case 3 — Manufacturing: Cereal Box Weight QC",
        ib(_case_header("3", "⚙ Quality Control", "Is the filling machine still calibrated correctly?",
                         "Two-Tailed z-test", "blue"),
           "blue") +
        p(f'A cereal factory calibrates its filling machine to {hl("500g per box")} (σ = 4g). '
          f'A quality inspector samples {hl("n = 100 boxes")} and finds a mean weight of {hl("499.1g")}. '
          f'Is the machine out of calibration — in either direction?') +
        two_col(
            ib(f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">Hypotheses</span><br>'
               + p(f'{lb_t("<strong>H₀:</strong>")} μ = 500g (machine correctly calibrated)'
                   f'<br>{lb_t("<strong>H₁:</strong>")} μ ≠ 500g (machine drifted — either direction)'
                   f'<br>{bdg("Two-Tailed Test", "blue")} — drift could be over- or under-filling'), "blue"),
            ib(f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">Why two-tailed?</span><br>'
               + p('The inspector does not predict which direction the machine drifted. '
                   'Under-filling cheats consumers (legal risk). Over-filling wastes product (cost risk). '
                   'Both matter equally — so α is split across both tails.'), "gold"),
        ) +
        fml(f'SE     = σ/√n = {sigma}/√{n} = {se:.4f}\n'
            f'z      = ({xb} − {mu0})/{se:.4f} = {hl(f"{z:.4f}")}\n'
            f'z_crit (α/2 = {alpha/2:.3f}) = ±{hl(f"{zc:.3f}")}\n'
            f'p-value = 2×P(Z > |{z:.4f}|) = {hl(f"{pv:.4f}")}')
    )

    metric_row([
        ("z-statistic", f"{z:.4f}", None),
        (f"z-critical (±, α={alpha})", f"±{zc:.3f}", None),
        ("p-value", f"{pv:.4f}", None),
        ("Decision", "REJECT H₀ 🔴" if rej else "FAIL TO REJECT 🟢", None),
    ])

    render_ib(
        f'<span style="color:#28a745;-webkit-text-fill-color:#28a745;font-weight:600">Real-World Interpretation: </span>'
        + txt_s(f'{"The weight deviation is statistically significant — the machine has drifted and needs recalibration. The under-fill of 0.9g may seem small, but across millions of boxes this represents significant material loss or regulatory risk." if rej else "The 0.9g under-fill is within normal sampling variation at this significance level. No immediate recalibration is required, but the inspector should increase monitoring frequency."}'),
        "green"
    )
    fig = _plot_test(z, alpha, "two", f"QC: Box Weight Calibration Test | α={alpha}")
    st.pyplot(fig, use_container_width=True); plt.close(fig)


def _case_sleep_study(alpha):
    """Case 4 — Psychology: Sleep deprivation and reaction time"""
    xb, mu0, s, n = 285.0, 270.0, 40.0, 25
    se = s / np.sqrt(n)
    t  = (xb - mu0) / se
    df = n - 1
    tc = stats.t.ppf(1 - alpha, df)   # right-tailed (we predict increase)
    pv = 1 - stats.t.cdf(t, df)
    rej = t > tc

    render_card("🧠 Case 4 — Psychology: Sleep Deprivation & Reaction Time",
        ib(_case_header("4", "🧬 Behavioural Science", "Does sleep deprivation worsen reaction time?",
                         "Right-Tailed t-test", "red"),
           "red") +
        p(f'A sleep researcher studies the effect of 24-hour sleep deprivation. '
          f'Normal reaction time for adults averages {hl("270 ms")}. '
          f'After keeping {hl("n = 25 volunteers")} awake for 24 hours, '
          f'mean reaction time = {hl("285 ms")} (s = 40 ms). '
          f'Does sleep deprivation significantly worsen (increase) reaction time?') +
        two_col(
            ib(f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">Hypotheses</span><br>'
               + p(f'{lb_t("<strong>H₀:</strong>")} μ ≤ 270 ms (no worsening)'
                   f'<br>{lb_t("<strong>H₁:</strong>")} μ > 270 ms (reaction time worsened)'
                   f'<br>{bdg("Right-Tailed t-test", "red")} — n=25, σ unknown'), "blue"),
            ib(f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">Small Sample Note</span><br>'
               + p(f'With only n = 25, the Central Limit Theorem gives weaker assurance. '
                   f'The t-distribution with df = {df} has heavier tails, appropriately accounting for '
                   f'greater uncertainty with small samples.'), "gold"),
        ) +
        fml(f'SE     = s/√n = {s}/√{n} = {se:.4f}\n'
            f't      = ({xb} − {mu0})/{se:.4f} = {hl(f"{t:.4f}")}\n'
            f'df     = {df}\n'
            f't_crit (α={alpha}, right) = {hl(f"{tc:.3f}")}\n'
            f'p-value = {hl(f"{pv:.4f}")}')
    )

    metric_row([
        ("t-statistic", f"{t:.4f}", None),
        (f"t-critical (df={df})", f"{tc:.3f}", None),
        ("p-value", f"{pv:.4f}", None),
        ("Decision", "REJECT H₀ 🔴" if rej else "FAIL TO REJECT 🟢", None),
    ])

    render_ib(
        f'<span style="color:#28a745;-webkit-text-fill-color:#28a745;font-weight:600">Real-World Interpretation: </span>'
        + txt_s(f'{"The 15 ms increase in reaction time is statistically significant. Sleep deprivation measurably impairs response time — consistent with extensive neuroscience literature. A 15 ms delay can be safety-critical in driving or surgery." if rej else "The 15 ms increase is not statistically significant at this level with n = 25. A larger sample is likely needed — the small n gives low power to detect modest effects."}'),
        "green"
    )
    fig = _plot_test(t, alpha, "right", f"Sleep Study: Reaction Time Test | α={alpha}, df={df}")
    st.pyplot(fig, use_container_width=True); plt.close(fig)


def _case_crop_yield(alpha):
    """Case 5 — Agriculture: New fertiliser crop yield"""
    xb, mu0, sigma, n = 52.8, 50.0, 7.5, 36
    se = sigma / np.sqrt(n)
    z  = (xb - mu0) / se
    zc = stats.norm.ppf(1 - alpha)   # right-tailed
    pv = 1 - stats.norm.cdf(z)
    rej = z > zc

    render_card("🌾 Case 5 — Agriculture: Fertiliser Yield Test",
        ib(_case_header("5", "🌱 Agricultural Research", "Does the new fertiliser increase crop yield?",
                         "Right-Tailed z-test", "green"),
           "green") +
        p(f'An agricultural research station tests a new nitrogen-rich fertiliser. '
          f'The standard variety yields {hl("50 kg/plot")} on average (σ = 7.5 kg, known from historical records). '
          f'Testing on {hl("n = 36 plots")} with the new fertiliser gives mean = {hl("52.8 kg/plot")}. '
          f'Is this a genuine improvement?') +
        two_col(
            ib(f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">Hypotheses</span><br>'
               + p(f'{lb_t("<strong>H₀:</strong>")} μ ≤ 50 kg (no improvement)'
                   f'<br>{lb_t("<strong>H₁:</strong>")} μ > 50 kg (yield improved)'
                   f'<br>{bdg("Right-Tailed z-test", "green")} — σ known from records'), "blue"),
            ib(f'<span style="color:#28a745;-webkit-text-fill-color:#28a745;font-weight:600">Practical Significance</span><br>'
               + p('Statistical significance alone is not enough. A 2.8 kg increase per plot '
                   'across thousands of hectares represents significant commercial value. '
                   'But if the new fertiliser costs much more, the farmer must weigh '
                   'statistical vs <em>economic</em> significance.'), "green"),
        ) +
        fml(f'SE     = σ/√n = {sigma}/√{n} = {se:.4f}\n'
            f'z      = ({xb} − {mu0})/{se:.4f} = {hl(f"{z:.4f}")}\n'
            f'z_crit (α={alpha}, right) = {hl(f"{zc:.3f}")}\n'
            f'p-value = P(Z > {z:.4f}) = {hl(f"{pv:.4f}")}')
    )

    metric_row([
        ("z-statistic", f"{z:.4f}", None),
        (f"z-critical (α={alpha})", f"{zc:.3f}", None),
        ("p-value", f"{pv:.4f}", None),
        ("Decision", "REJECT H₀ 🔴" if rej else "FAIL TO REJECT 🟢", None),
    ])

    render_ib(
        f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">Statistical vs Economic Significance: </span>'
        + txt_s('Statistical significance tells you the effect is real. Economic significance tells you '
                'if it is big enough to matter. A 2.8 kg/plot increase is statistically significant, '
                'but the farmer must also ask: does the cost of the new fertiliser justify this gain?'),
        "blue"
    )
    fig = _plot_test(z, alpha, "right", f"Crop Yield: Fertiliser Test | α={alpha}")
    st.pyplot(fig, use_container_width=True); plt.close(fig)


def _case_call_centre(alpha):
    """Case 6 — Operations: Call centre response time"""
    xb, mu0, s, n = 4.6, 5.0, 1.8, 81
    se = s / np.sqrt(n)
    t  = (xb - mu0) / se
    df = n - 1
    tc_two = stats.t.ppf(1 - alpha / 2, df)
    pv = 2 * (1 - stats.t.cdf(abs(t), df))
    rej = abs(t) > tc_two

    render_card("📞 Case 6 — Operations: Call Centre Response Time",
        ib(_case_header("6", "🏢 Operations Management", "Has average call handling time changed?",
                         "Two-Tailed t-test", "blue"),
           "blue") +
        p(f'A telecom company sets a target call handling time of {hl("5.0 minutes")}. '
          f'After a new CRM software rollout, {hl("n = 81 calls")} are monitored: '
          f'mean = {hl("4.6 min")}, s = 1.8 min. '
          f'Has the average handling time changed (either direction — faster or slower)?') +
        two_col(
            ib(f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">Hypotheses</span><br>'
               + p(f'{lb_t("<strong>H₀:</strong>")} μ = 5.0 min (time unchanged)'
                   f'<br>{lb_t("<strong>H₁:</strong>")} μ ≠ 5.0 min (time changed)'
                   f'<br>{bdg("Two-Tailed t-test", "blue")} — could be faster or slower'), "blue"),
            ib(f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">Management Implication</span><br>'
               + p('A significant <em>decrease</em> in time could mean improved efficiency OR '
                   'rushed service (quality risk). A significant <em>increase</em> means bottlenecks. '
                   'Either direction matters — hence two-tailed. The direction of the result '
                   'guides the management response.'), "gold"),
        ) +
        fml(f'SE     = s/√n = {s}/√{n} = {se:.4f}\n'
            f't      = ({xb} − {mu0})/{se:.4f} = {hl(f"{t:.4f}")}\n'
            f'df     = {df}\n'
            f't_crit (α/2={alpha/2:.3f}, df={df}) = ±{hl(f"{tc_two:.3f}")}\n'
            f'p-value = 2×P(T > |{t:.4f}|) = {hl(f"{pv:.4f}")}')
    )

    metric_row([
        ("t-statistic", f"{t:.4f}", None),
        (f"t-critical (±, df={df})", f"±{tc_two:.3f}", None),
        ("p-value", f"{pv:.4f}", None),
        ("Decision", "REJECT H₀ 🔴" if rej else "FAIL TO REJECT 🟢", None),
    ])

    render_ib(
        f'<span style="color:#28a745;-webkit-text-fill-color:#28a745;font-weight:600">Real-World Interpretation: </span>'
        + txt_s(f'{"The 0.4-minute reduction in handling time is statistically significant. The CRM software measurably changed call handling. Management should now investigate whether this reflects genuine efficiency gains or compromised service quality." if rej else "The 0.4-minute reduction is not statistically significant. The new CRM has not measurably changed average call time — observed differences are within normal random variation."}'),
        "green"
    )
    fig = _plot_test(t, alpha, "two", f"Call Centre: Handling Time Test | α={alpha}, df={df}")
    st.pyplot(fig, use_container_width=True); plt.close(fig)


# ═══════════════════════════════════════════════════════════
# MAIN TAB
# ═══════════════════════════════════════════════════════════

def tab_non_finance():
    explainer_non_finance()

    render_card("🌍 Everyday Hypothesis Testing — Six Real-World Cases",
        p(f'The same z-test and t-test framework used in finance applies to '
          f'{hl("medicine")}, {hl("education")}, {hl("manufacturing")}, '
          f'{hl("psychology")}, {hl("agriculture")}, and {hl("operations management")}. '
          f'Master the pattern here — and every finance test becomes intuitive.') +
        three_col(
            ib(f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">6 Case Studies</span><br>'
               + p('Drug trial, teaching method, factory QC, sleep study, crop yield, call centre'), "gold"),
            ib(f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">All 3 Test Types</span><br>'
               + p('Left-tailed, right-tailed, two-tailed — z-test and t-test both covered'), "blue"),
            ib(f'<span style="color:#28a745;-webkit-text-fill-color:#28a745;font-weight:600">Interactive α</span><br>'
               + p('Adjust significance level for all cases simultaneously'), "green"),
        )
    )

    # Global alpha selector
    col1, _ = st.columns([1, 2])
    alpha = col1.select_slider(
        "Significance Level α (applies to all cases)",
        options=[0.10, 0.05, 0.025, 0.01], value=0.05, key="nf_alpha"
    )

    # Overview table
    section_heading("📋 Case Study Overview")
    st.html(table_html(
        ["#", "Domain", "Question", "Test Type", "H₀", "H₁"],
        [
            [bdg("1","red"),    txt_s("Medicine"),      txt_s("Drug lowers BP?"),           bdg("Left z","red"),     txt_s("μ ≥ 140"),  txt_s("μ < 140")],
            [bdg("2","gold"),   txt_s("Education"),     txt_s("Teaching method improves?"), bdg("Right t","gold"),   txt_s("μ ≤ 68"),   txt_s("μ > 68")],
            [bdg("3","blue"),   txt_s("Manufacturing"), txt_s("Machine calibrated?"),       bdg("Two-tail z","blue"),txt_s("μ = 500g"), txt_s("μ ≠ 500g")],
            [bdg("4","red"),    txt_s("Psychology"),    txt_s("Sleep worsens RT?"),         bdg("Right t","red"),    txt_s("μ ≤ 270"),  txt_s("μ > 270")],
            [bdg("5","green"),  txt_s("Agriculture"),   txt_s("Fertiliser increases yield?"),bdg("Right z","green"), txt_s("μ ≤ 50"),   txt_s("μ > 50")],
            [bdg("6","blue"),   txt_s("Operations"),    txt_s("Call time changed?"),        bdg("Two-tail t","blue"),txt_s("μ = 5.0"),  txt_s("μ ≠ 5.0")],
        ]
    ))

    # Case selector
    cases = [
        "💊 Case 1 — Drug Trial (Medicine)",
        "📚 Case 2 — Teaching Method (Education)",
        "🏭 Case 3 — Factory QC (Manufacturing)",
        "🧠 Case 4 — Sleep Study (Psychology)",
        "🌾 Case 5 — Fertiliser Yield (Agriculture)",
        "📞 Case 6 — Call Centre (Operations)",
    ]
    case = st.radio("Select Case Study", cases, horizontal=True, key="nf_case")

    st.markdown("---")

    if   "Case 1" in case: _case_drug_trial(alpha)
    elif "Case 2" in case: _case_exam_scores(alpha)
    elif "Case 3" in case: _case_factory_weight(alpha)
    elif "Case 4" in case: _case_sleep_study(alpha)
    elif "Case 5" in case: _case_crop_yield(alpha)
    elif "Case 6" in case: _case_call_centre(alpha)

    # Cross-domain comparison
    section_heading("🔄 The Universal Pattern")
    render_ib(
        ib(f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">Every test follows this identical 5-step script:</span>'
           f'<div style="margin-top:10px">'
           + steps_html([
               ("State H₀ and H₁", "Null = status quo. Alternative = the claim. Direction determines test type."),
               ("Choose α",        "Significance level = your tolerance for a false alarm. 5% is standard."),
               ("Compute the test statistic", "z = (x̄ − μ₀)/(σ/√n) if σ known. t = (x̄ − μ₀)/(s/√n) if σ unknown."),
               ("Find critical value",  "Look up z or t from tables based on α, tail direction, and df."),
               ("Compare and conclude", "stat > critical → Reject H₀. Interpret in domain context."),
           ]) + '</div>',
           "gold"),
        "gold"
    )
