"""
tabs.py — All six tab functions using st.html() with 100% inline styles.
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
from tab_explainers import (
    explainer_overview, explainer_one_tailed, explainer_two_tailed,
    explainer_comparison, explainer_finance, explainer_python,
)
from charts import (
    normal_curve_overview, right_tailed_chart, left_tailed_chart,
    two_tailed_chart, comparison_chart,
)

# ═══════════════════════════════════════════════════════════════════
# TAB 1 — OVERVIEW
# ═══════════════════════════════════════════════════════════════════
def tab_overview():
    render_card("📐 Foundation: What is Hypothesis Testing?",
        p("Hypothesis testing is a statistical decision framework using sample data to make "
          "inferences about population parameters. In finance: "
          "<em>\"Does this fund generate alpha?\"</em> or "
          "<em>\"Has market risk increased after a policy change?\"</em>") +
        two_col(
            ib(f'<div style="font-family:{FH};font-size:1.05rem;color:#ADD8E6;'
               f'-webkit-text-fill-color:#ADD8E6;margin:0 0 7px 0">Null Hypothesis (H₀)</div>'
               + p(f'The <span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">default assumption</span> — '
                   f'"no change", "no effect", "equals benchmark". We assume H₀ is true.')
               + p(f'{hl("Example:")} μ = 12% (fund matches market)'),
               "blue"),
            ib(f'<div style="font-family:{FH};font-size:1.05rem;color:#FFD700;'
               f'-webkit-text-fill-color:#FFD700;margin:0 0 7px 0">Alternative Hypothesis (H₁)</div>'
               + p(f'The <span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">claim under test</span>. '
                   f'Its direction (&gt;, &lt;, ≠) determines one-tailed vs two-tailed test.')
               + p(f'{hl("Example:")} μ &gt; 12% (fund outperforms)'),
               "gold"),
        ) +
        normal_curve_overview() +
        three_col(
            ib(f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">α — Significance Level</span><br>'
               + p("P(Type I Error). Probability of rejecting a true H₀.")
               + bdg("Common: 1%, 5%, 10%","gold"),
               "blue"),
            ib(f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">p-value</span><br>'
               + p("P(data at least this extreme | H₀ true).")
               + bdg("p &lt; α → Reject H₀","red") + " " + bdg("p ≥ α → Fail to Reject","green"),
               "gold"),
            ib(f'<span style="color:#28a745;-webkit-text-fill-color:#28a745;font-weight:600">Critical Region</span><br>'
               + p("Values of test statistic that trigger rejection of H₀.")
               + bdg("z-stat or t-stat","blue"),
               "green"),
        )
    )

    explainer_overview()
    render_card("🗺 Decision Guide: Which Test?",
        table_html(
            ["Research Question","H₁","Test","Critical Region"],
            [
                [txt_s("Did returns <strong>change</strong> (either direction)?"), txt_s("μ ≠ μ₀"), bdg("Two-Tailed","blue"), txt_s("Both tails (α/2 each)")],
                [txt_s("Did returns <strong>increase</strong>?"),                  txt_s("μ &gt; μ₀"), bdg("Right-Tailed","gold"), txt_s("Right tail only (full α)")],
                [txt_s("Did risk <strong>worsen/increase</strong>?"),              txt_s("μ &gt; μ₀"), bdg("Right-Tailed","red"),  txt_s("Right tail only (full α)")],
            ]
        )
    )

    render_card("🔢 Key Constants at a Glance",
        p("The four anchor critical values that cover 90% of all finance hypothesis tests:")
    )
    metric_row([
        ("One-Tail α=5%", "z = 1.645", None),
        ("Two-Tail α=5%", "z = ±1.960", None),
        ("One-Tail α=1%", "z = 2.326", None),
        ("Two-Tail α=1%", "z = ±2.576", None),
    ])


# ═══════════════════════════════════════════════════════════════════
# TAB 2 — ONE-TAILED
# ═══════════════════════════════════════════════════════════════════
def tab_one_tailed():
    render_card("→ One-Tailed Tests: Right-Tailed & Left-Tailed",
        p(f'Used when there is a {lb_t("<strong>directional hypothesis</strong>")}. '
          f'All α is concentrated in ONE tail, giving more power to detect effects in that direction.') +
        two_col(
            ib(f'<div style="font-family:{FH};font-size:1.05rem;color:#FFD700;-webkit-text-fill-color:#FFD700;margin:0 0 7px 0">▶ Right-Tailed Test</div>'
               + p(f'{lb_t("<strong>H₀:</strong>")} μ ≤ μ₀ &nbsp;|&nbsp; {lb_t("<strong>H₁:</strong>")} μ &gt; μ₀')
               + p(f'Reject H₀ if statistic in the {hl("RIGHT tail")}')
               + p(f'{gt("Finance use:")} Fund return exceeds benchmark?')
               + right_tailed_chart()
               + fml(f'z = (x̄ − μ₀) / (σ/√n)\nReject if z > z_α\nα=5%: z > {hl("+1.645")}\nα=1%: z > {hl("+2.326")}'),
               "gold"),
            ib(f'<div style="font-family:{FH};font-size:1.05rem;color:#dc3545;-webkit-text-fill-color:#dc3545;margin:0 0 7px 0">◀ Left-Tailed Test</div>'
               + p(f'{lb_t("<strong>H₀:</strong>")} μ ≥ μ₀ &nbsp;|&nbsp; {lb_t("<strong>H₁:</strong>")} μ &lt; μ₀')
               + p(f'Reject H₀ if statistic in the {rt2("LEFT tail")}')
               + p(f'{gt("Finance use:")} Portfolio losses worsened?')
               + left_tailed_chart()
               + fml(f'z = (x̄ − μ₀) / (σ/√n)\nReject if z < −z_α\nα=5%: z < {hl("−1.645")}\nα=1%: z < {hl("−2.326")}'),
               "red"),
        )
    )

    render_card("📊 Worked Example — Portfolio Alpha Test (Interactive)",
        ib(f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">Scenario:</span> '
           + txt_s(' A fund claims returns <em>greater than</em> the market return. '
                   'Sample of n months: mean return x̄, σ known. Test at chosen α.'),
           "gold")
    )

    explainer_one_tailed()
    c1, c2, c3, c4 = st.columns(4)
    x_bar = c1.number_input("Sample Mean (x̄) %", value=13.5, step=0.1, key="ot_xb")
    mu_0  = c2.number_input("Pop. Mean (μ₀) %",   value=12.0, step=0.1, key="ot_mu")
    sigma = c3.number_input("Std Dev (σ) %", value=6.0, min_value=0.1, step=0.1, key="ot_sg")
    n     = c4.number_input("Sample Size (n)", value=36, min_value=1, step=1, key="ot_n")

    alpha_c = st.select_slider("Significance Level α", options=[0.10,0.05,0.025,0.01], value=0.05, key="ot_a")
    tail_c  = st.radio("Test Direction",
                       ["Right-Tailed (H₁: μ > μ₀)","Left-Tailed (H₁: μ < μ₀)"],
                       horizontal=True, key="ot_t")
    tail = "right" if "Right" in tail_c else "left"

    se = sigma / np.sqrt(n)
    z_stat = (x_bar - mu_0) / se
    if tail == "right":
        z_crit = stats.norm.ppf(1-alpha_c); p_val = 1-stats.norm.cdf(z_stat); rej = z_stat > z_crit
    else:
        z_crit = stats.norm.ppf(alpha_c);   p_val = stats.norm.cdf(z_stat);   rej = z_stat < z_crit

    metric_row([
        ("z-statistic",    f"{z_stat:.4f}", None),
        ("Critical Value", f"{z_crit:.3f}", None),
        ("p-value",        f"{p_val:.4f}",  None),
        ("Decision", "REJECT H₀ 🔴" if rej else "FAIL TO REJECT 🟢", None),
    ])
    fig = _plot_test(z_stat, alpha_c, tail, f"One-Tailed ({tail}) | α={alpha_c}")
    st.pyplot(fig, use_container_width=True); plt.close(fig)

    render_ib(
        f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">Key Insight:</span> '
        + txt_s(' All α is concentrated in one tail → more power to detect effects in the stated direction. '
                'Direction must be decided <em>before</em> data collection to avoid p-hacking.'),
        "blue"
    )


# ═══════════════════════════════════════════════════════════════════
# TAB 3 — TWO-TAILED
# ═══════════════════════════════════════════════════════════════════
def tab_two_tailed():
    render_card("↔ Two-Tailed Test: Testing for Any Difference",
        p(f'Used for {lb_t("<strong>non-directional hypotheses</strong>")} — detecting a difference in '
          f'<em>either direction</em>. α is split equally (α/2 per tail), requiring more extreme '
          f'test statistics to reject H₀.') +
        two_tailed_chart() +
        fml(f'H₀: μ = μ₀  |  H₁: μ ≠ μ₀\n\nReject H₀ if |z| > z_{{α/2}}\n\n'
            f'α = 5%:  |z| > {hl("1.960")}\nα = 1%:  |z| > {hl("2.576")}\nα = 10%: |z| > {hl("1.645")}\n\n'
            f'p-value (two-tailed) = 2 × P(Z > |z|)') +
        ib(f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">Why split α?</span> '
           + txt_s(' Each tail gets α/2 = 2.5%, so critical values are more extreme (±1.96 vs ±1.645) — '
                   'making two-tailed tests more conservative but directionally unbiased.'),
           "blue")
    )

    render_card("📊 Worked Example — VaR Change Test (Interactive)",
        ib(f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">Scenario:</span> '
           + txt_s(' Historical daily VaR = ₹50 Lakhs. After a system upgrade, 64 days show '
                   'mean loss = ₹47.5L, σ = ₹12L. Has VaR <em>changed?</em>'),
           "gold")
    )

    explainer_two_tailed()
    c1, c2, c3, c4 = st.columns(4)
    x_bar = c1.number_input("Sample Mean (x̄)", value=47.5, step=0.5, key="tt_xb")
    mu_0  = c2.number_input("Pop. Mean (μ₀)",   value=50.0, step=0.5, key="tt_mu")
    sigma = c3.number_input("Std Dev (σ)",       value=12.0, min_value=0.1, step=0.5, key="tt_sg")
    n     = c4.number_input("Sample Size (n)",   value=64,   min_value=1,   step=1,   key="tt_n")

    alpha_c = st.select_slider("Significance Level α", options=[0.10,0.05,0.025,0.01], value=0.05, key="tt_a")

    se     = sigma / np.sqrt(n)
    z_stat = (x_bar - mu_0) / se
    z_crit = stats.norm.ppf(1 - alpha_c/2)
    p_val  = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    rej    = abs(z_stat) > z_crit

    metric_row([
        ("z-statistic",    f"{z_stat:.4f}",  None),
        ("Critical Value", f"±{z_crit:.3f}", None),
        ("p-value",        f"{p_val:.4f}",   None),
        ("Decision", "REJECT H₀ 🔴" if rej else "FAIL TO REJECT 🟢", None),
    ])
    fig = _plot_test(z_stat, alpha_c, "two", f"Two-Tailed | α={alpha_c}")
    st.pyplot(fig, use_container_width=True); plt.close(fig)

    ssteps = [
        ("Hypotheses",     f'H₀: μ = {mu_0} | H₁: μ ≠ {mu_0} → {bdg("Two-Tailed","blue")}'),
        ("Critical value", f'α/2 = {alpha_c/2:.3f} per tail → z_crit = {hl(f"±{z_crit:.3f}")}'),
        ("Test statistic", fml(f'z = ({x_bar} − {mu_0}) / ({sigma}/√{n})\n  = {x_bar-mu_0:.1f} / {se:.4f} = {hl(f"{z_stat:.4f}")}')),
        ("Decision",       (vr("REJECT H₀") if rej else vf("FAIL TO REJECT H₀")) +
                           txt_s(f' — |z| = {abs(z_stat):.4f} {">" if rej else "<"} {z_crit:.3f}')),
        ("p-value",        txt_s(f'2 × P(Z &lt; -{abs(z_stat):.4f}) = ') + hl(f"{p_val:.4f}") +
                           txt_s(f' {"&lt; α → Reject" if p_val < alpha_c else "&gt; α → Fail to Reject"}')),
    ]
    render_ib(
        f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">Step-by-Step:</span>'
        f'<div style="margin-top:10px">{steps_html(ssteps)}</div>',
        "gold"
    )

    otc = stats.norm.ppf(alpha_c)
    render_ib(
        f'<span style="color:#dc3545;-webkit-text-fill-color:#dc3545;font-weight:600">⚠ Critical Insight:</span> '
        + txt_s(f' If we wrongly used a left-tailed test: z = {z_stat:.4f} vs z_crit = {otc:.4f}. '
                f'We {"WOULD" if z_stat < otc else "would NOT"} reject H₀ — '
                f'showing why test direction must be set BEFORE data collection!'),
        "red"
    )


# ═══════════════════════════════════════════════════════════════════
# TAB 4 — COMPARISON
# ═══════════════════════════════════════════════════════════════════
def tab_comparison():
    render_card("⚖ One-Tailed vs Two-Tailed: Complete Comparison",
        comparison_chart() +
        table_html(
            ["Feature","One-Tailed","Two-Tailed"],
            [
                [txt_s("H₁ direction"),         txt_s("Directional (&gt; or &lt;)"),       txt_s("Non-directional (≠)")],
                [txt_s("Critical region"),       txt_s("One tail"),                          txt_s("Both tails (α/2 each)")],
                [txt_s("Critical z (α=5%)"),     gt("±1.645"),                               rt2("±1.960")],
                [txt_s("Critical z (α=1%)"),     gt("±2.326"),                               rt2("±2.576")],
                [txt_s("Statistical power"),     gt("Higher (in stated direction)"),          rt2("Lower")],
                [txt_s("p-value formula"),       txt_s("P(Z&gt;z) or P(Z&lt;z)"),           txt_s("2 × P(Z &gt; |z|)")],
                [txt_s("When to use"),           txt_s("Prior directional belief"),           txt_s("Direction unknown / safer")],
                [txt_s("Risk"),                  txt_s("Misleading if direction wrong"),      txt_s("Conservative but safer")],
            ]
        )
    )

    explainer_comparison()
    render_card("🎯 Type I & Type II Errors",
        two_col(
            ib(f'<span style="color:#dc3545;-webkit-text-fill-color:#dc3545;font-weight:600">'
               f'Type I Error (α) — False Positive</span><br>'
               + p("Reject H₀ when it is actually TRUE.")
               + p(mut_t("<em>Finance: Declaring a fund has alpha when it doesn't.</em>"))
               + bdg("Controlled by significance level α","red"),
               "red"),
            ib(f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">'
               f'Type II Error (β) — False Negative</span><br>'
               + p("Fail to reject H₀ when it is actually FALSE.")
               + p(mut_t("<em>Finance: Missing a fund that truly outperforms.</em>"))
               + bdg("Power = 1 − β (maximize this)","gold"),
               "gold"),
        ) +
        ib(txt_s("One-tailed tests have higher power (lower β) for a given directional effect — "
                 "making them preferred when directional theory is well-established. "
                 "Two-tailed tests reduce risk of false positives from wrong direction assumptions."),
           "green")
    )

    render_card("🔭 Critical Value Explorer",
        p("Select α and test type to explore critical values and rejection regions dynamically.")
    )
    col1, col2 = st.columns(2)
    alpha_e   = col1.select_slider("α", options=[0.10,0.05,0.025,0.01,0.005], value=0.05, key="cmp_a")
    test_type = col2.radio("Test Type", ["One-Tailed","Two-Tailed"], horizontal=True, key="cmp_t")

    if test_type == "One-Tailed":
        zc = stats.norm.ppf(1-alpha_e)
        tc30 = stats.t.ppf(1-alpha_e, 30); tc60 = stats.t.ppf(1-alpha_e, 60)
        label = f"One-Tail (α={alpha_e})"; tail_p = "right"
    else:
        zc = stats.norm.ppf(1-alpha_e/2)
        tc30 = stats.t.ppf(1-alpha_e/2, 30); tc60 = stats.t.ppf(1-alpha_e/2, 60)
        label = f"Two-Tail (α={alpha_e})"; tail_p = "two"

    metric_row([
        (f"z-critical ({label})", f"±{zc:.3f}", None),
        ("t-critical (df=30)",    f"±{tc30:.3f}", None),
        ("t-critical (df=60)",    f"±{tc60:.3f}", None),
        ("t-critical (df=∞)",     f"±{zc:.3f}", None),
    ])
    fig2 = _plot_test(0, alpha_e, tail_p, f"Critical Region | {label}")
    st.pyplot(fig2, use_container_width=True); plt.close(fig2)


# ═══════════════════════════════════════════════════════════════════
# TAB 5 — FINANCE EXAMPLES
# ═══════════════════════════════════════════════════════════════════
def tab_finance_examples():
    def ex_box(num, title, badge_txt, badge_var, h0, h1, note, variant):
        return ib(
            f'<div style="font-family:{FH};font-size:1.05rem;color:{S[badge_var if badge_var!="red" else "red"]};'
            f'-webkit-text-fill-color:{S[badge_var if badge_var!="red" else "red"]};margin:0 0 6px 0">'
            f'{num}. {title}</div>'
            + bdg(badge_txt, badge_var)
            + p(f'{lb_t("<strong>H₀:</strong>")} {h0} &nbsp;|&nbsp; {lb_t("<strong>H₁:</strong>")} {h1}')
            + p(note),
            variant
        )

    render_card("💹 Real-World Finance & Risk Applications",
        two_col(
            ex_box("1","Portfolio Alpha (Jensen's α)","Right-Tailed","gold","α ≤ 0","α &gt; 0","t = α_hat / SE(α_hat) from regression","gold"),
            ex_box("2","CAPM Beta Neutrality","Two-Tailed","blue","β = 1","β ≠ 1","t = (β_hat − 1) / SE(β_hat)","blue"),
        ) +
        two_col(
            ex_box("3","VaR Backtesting (Kupiec)","Right-Tailed","red","exceedance = 5%","&gt; 5%","Binomial test on number of VaR breaches","red"),
            ex_box("4","Credit Default Rate","Right-Tailed","gold","default rate ≤ 2%","&gt; 2%","Monitor loan portfolio risk deterioration","gold"),
        ) +
        two_col(
            ex_box("5","Bond Portfolio Duration","Two-Tailed","blue","D = 7 yrs","D ≠ 7 yrs","Post-rebalancing duration shift check","blue"),
            ex_box("6","Sharpe Ratio Test","Right-Tailed","gold","SR ≤ 0.5","SR &gt; 0.5","Jobson-Korkie test for risk-adjusted performance","gold"),
        )
    )

    explainer_finance()
    render_card("📋 Solved: Bond Portfolio Duration Test (t-test)",
        ib(f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">Scenario:</span> '
           + txt_s(' Target modified duration = 7 years. After restructuring, 49 bonds: '
                   'mean = 7.84 yrs, s = 2.94 yrs. Has duration changed? α = 1%.'),
           "gold")
    )

    xb, mu, sb, nb, ab = 7.84, 7.0, 2.94, 49, 0.01
    se_b   = sb / np.sqrt(nb); t_stat = (xb-mu)/se_b; df = nb-1
    t_crit = stats.t.ppf(1-ab/2, df); p_b = 2*(1-stats.t.cdf(abs(t_stat), df))
    rej_b  = abs(t_stat) > t_crit

    metric_row([
        ("t-statistic",                  f"{t_stat:.4f}",  None),
        ("Critical Value (df=48, α=1%)", f"±{t_crit:.3f}", None),
        ("p-value",                      f"{p_b:.4f}",     None),
        ("Decision", "REJECT H₀ 🔴" if rej_b else "FAIL TO REJECT 🟢", None),
    ])

    ssteps = [
        ("Hypotheses",     f'H₀: μ = {mu} | H₁: μ ≠ {mu} → {bdg("Two-Tailed t-test","blue")}'),
        ("Critical value", f'df = {df}, α = {ab} → t_crit = {hl(f"±{t_crit:.3f}")}'),
        ("Test statistic", fml(f't = ({xb} − {mu}) / ({sb}/√{nb})\n  = {xb-mu:.2f} / {se_b:.4f} = {hl(f"{t_stat:.4f}")}')),
        ("Decision",       (vr("REJECT H₀") if rej_b else vf("FAIL TO REJECT H₀")) +
                           txt_s(f' at α={ab}')),
        ("Note",           txt_s(f'At α=5% (t_crit=±{stats.t.ppf(0.975,df):.3f}): also fail to reject. '
                                 f'p-value = {p_b:.4f} (borderline).')),
    ]
    st.html(f'<div style="margin-top:14px;{NO_SEL}">{steps_html(ssteps)}</div>')

    fig3 = _plot_test(t_stat, ab, "two", "Bond Duration Test (t-distribution, df=48)")
    st.pyplot(fig3, use_container_width=True); plt.close(fig3)


# ═══════════════════════════════════════════════════════════════════
# TAB 6 — PYTHON CODE
# ═══════════════════════════════════════════════════════════════════
def tab_python_code():
    render_card("🐍 Python Implementation", "")
    explainer_python()

    st.code('''import numpy as np
import scipy.stats as stats

def z_test(sample_mean, pop_mean, pop_std, n, alpha=0.05, tail="two"):
    se     = pop_std / np.sqrt(n)
    z_stat = (sample_mean - pop_mean) / se
    if tail == "right":
        z_crit  = stats.norm.ppf(1 - alpha)
        p_value = 1 - stats.norm.cdf(z_stat)
        reject  = z_stat > z_crit
    elif tail == "left":
        z_crit  = stats.norm.ppf(alpha)
        p_value = stats.norm.cdf(z_stat)
        reject  = z_stat < z_crit
    else:
        z_crit  = stats.norm.ppf(1 - alpha / 2)
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
        reject  = abs(z_stat) > z_crit
    cv = f"±{z_crit:.3f}" if tail == "two" else f"{z_crit:.3f}"
    print(f"z={z_stat:.4f} | z_crit={cv} | p={p_value:.4f} | {'REJECT' if reject else 'FAIL TO REJECT'}")
    return z_stat, p_value, reject

# Examples
z_test(13.5, 12, 6, 36,  alpha=0.05, tail="right")  # Fund alpha
z_test(47.5, 50, 12, 64, alpha=0.05, tail="two")    # VaR change


def t_test_one_sample(data, pop_mean, alpha=0.05, tail="two"):
    n, x_bar, s = len(data), np.mean(data), np.std(data, ddof=1)
    t_stat = (x_bar - pop_mean) / (s / np.sqrt(n)); df = n - 1
    if tail == "right":
        t_crit = stats.t.ppf(1-alpha, df);   p_value = 1-stats.t.cdf(t_stat, df)
    elif tail == "left":
        t_crit = stats.t.ppf(alpha, df);     p_value = stats.t.cdf(t_stat, df)
    else:
        t_crit = stats.t.ppf(1-alpha/2, df); p_value = 2*(1-stats.t.cdf(abs(t_stat), df))
    cv = f"±{t_crit:.3f}" if tail == "two" else f"{t_crit:.3f}"
    print(f"t={t_stat:.4f} | t_crit={cv} | p={p_value:.4f}")
    return t_stat, p_value

# Critical values reference
for a in [0.10, 0.05, 0.01]:
    print(f"α={a}: 1-tail z={stats.norm.ppf(1-a):.3f} | 2-tail z=±{stats.norm.ppf(1-a/2):.3f}")
''', language="python")

    render_card("▶ Live Code Runner",
        ib(f'<span style="color:#e6f1ff;-webkit-text-fill-color:#e6f1ff">'
           f'Adjust parameters and click Run to execute a live z-test.</span>', "blue")
    )

    c1, _ = st.columns([1, 1])
    with c1:
        section_heading("Z-Test Parameters")
        xb  = st.number_input("Sample Mean",     value=13.5, key="py_xb")
        mu  = st.number_input("Population Mean", value=12.0, key="py_mu")
        sig = st.number_input("Std Dev",         value=6.0,  min_value=0.01, key="py_sg")
        nn  = st.number_input("n",               value=36,   min_value=1,    key="py_n")
        alp = st.select_slider("α", options=[0.10,0.05,0.01], value=0.05, key="py_a")
        tl  = st.radio("Tail", ["right","left","two"], horizontal=True, key="py_t")

    if st.button("▶ Run Z-Test", key="run_zt"):
        se  = sig / np.sqrt(nn); zs = (xb - mu) / se
        if   tl == "right": zc = stats.norm.ppf(1-alp);   pv = 1-stats.norm.cdf(zs);          rej = zs > zc
        elif tl == "left":  zc = stats.norm.ppf(alp);      pv = stats.norm.cdf(zs);             rej = zs < zc
        else:               zc = stats.norm.ppf(1-alp/2);  pv = 2*(1-stats.norm.cdf(abs(zs)));  rej = abs(zs) > zc
        cv_s = f"±{zc:.3f}" if tl == "two" else f"{zc:.3f}"
        dtxt = "REJECT H₀" if rej else "FAIL TO REJECT H₀"; dcol = "#dc3545" if rej else "#28a745"
        render_ib(
            f'<span style="font-family:{FM};font-size:.9rem;color:#e6f1ff;-webkit-text-fill-color:#e6f1ff">'
            f'z-stat = {hl(f"{zs:.4f}")} &nbsp;|&nbsp; z_crit = {hl(cv_s)} &nbsp;|&nbsp; p = {hl(f"{pv:.4f}")}</span><br>'
            f'<span style="color:{dcol};-webkit-text-fill-color:{dcol};font-size:1.1rem;font-weight:700">{dtxt}</span>',
            "gold"
        )
        fig4 = _plot_test(zs, alp, tl, f"z={zs:.3f} | α={alp}")
        st.pyplot(fig4, use_container_width=True); plt.close(fig4)

    section_heading("🔢 Critical Values Reference Table")
    rows = []
    for a in [0.10, 0.05, 0.025, 0.01, 0.005]:
        rows.append([
            txt_s(f"{a:.3f}"),
            hl(f"{stats.norm.ppf(1-a):.3f}"),
            hl(f"{stats.norm.ppf(1-a/2):.3f}"),
            txt_s(f"{stats.t.ppf(1-a/2,30):.3f}"),
            txt_s(f"{stats.t.ppf(1-a/2,60):.3f}"),
        ])
    st.html(table_html(["α","One-Tail z","Two-Tail z (±)","t (df=30)","t (df=60)"], rows))

    render_ib(
        f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">Memory Anchor:</span> '
        + txt_s(' ') + hl("1.645 → 1.96 → 2.33 → 2.576") +
        txt_s(' — One-tail 5%, Two-tail 5%, One-tail 1%, Two-tail 1%. '
              'These four values cover 90% of all finance hypothesis tests!'),
        "blue"
    )


# ═══════════════════════════════════════════════════════════════════
# SHARED PLOT HELPER
# ═══════════════════════════════════════════════════════════════════
def _plot_test(z_stat, alpha, tail, title=""):
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor("#0a1628"); ax.set_facecolor("#112240")
    x = np.linspace(-4, 4, 600); y = stats.norm.pdf(x)
    ax.plot(x, y, color="#ADD8E6", lw=2.5, zorder=3)
    ax.fill_between(x, y, alpha=0.22, color="#004d80")

    def shade(xl): ax.fill_between(xl, stats.norm.pdf(xl), color="#dc3545", alpha=0.72, zorder=2)

    if tail == "two":
        zc = stats.norm.ppf(1-alpha/2)
        shade(np.linspace(zc,4.05,150)); shade(np.linspace(-4.05,-zc,150))
        ax.axvline(zc,  color="#dc3545", ls="--", lw=1.8, label=f"z_crit=±{zc:.3f}")
        ax.axvline(-zc, color="#dc3545", ls="--", lw=1.8)
    elif tail == "right":
        zc = stats.norm.ppf(1-alpha)
        shade(np.linspace(zc,4.05,150))
        ax.axvline(zc, color="#dc3545", ls="--", lw=1.8, label=f"z_crit=+{zc:.3f}")
    else:
        zc = stats.norm.ppf(alpha)
        shade(np.linspace(-4.05,zc,150))
        ax.axvline(zc, color="#dc3545", ls="--", lw=1.8, label=f"z_crit={zc:.3f}")

    if z_stat != 0:
        ax.axvline(z_stat, color="#FFD700", lw=2.5, zorder=4, label=f"z_stat={z_stat:.4f}")
        ax.scatter([z_stat],[stats.norm.pdf(z_stat)], color="#FFD700", s=80, zorder=5)
        rej = ((tail=="two"   and abs(z_stat) > stats.norm.ppf(1-alpha/2)) or
               (tail=="right" and z_stat      > stats.norm.ppf(1-alpha))   or
               (tail=="left"  and z_stat      < stats.norm.ppf(alpha)))
        ax.text(0.5, 0.92, "REJECT H₀" if rej else "FAIL TO REJECT H₀",
                transform=ax.transAxes, ha="center", fontsize=13, fontweight="bold",
                color="#dc3545" if rej else "#28a745")

    ax.set_title(title, color="#FFD700", fontsize=11, pad=8)
    ax.set_xlabel("Standard Deviations from Mean", color="#8892b0", fontsize=9)
    ax.set_ylabel("Density", color="#8892b0", fontsize=9)
    ax.tick_params(colors="#8892b0", labelsize=8)
    ax.legend(facecolor="#112240", labelcolor="#e6f1ff", fontsize=9, edgecolor="#1e3a5f")
    for sp in ax.spines.values(): sp.set_color("#1e3a5f")
    ax.grid(axis="y", color="#1e3a5f", alpha=0.4, lw=0.5)
    plt.tight_layout(pad=1.2)
    return fig
