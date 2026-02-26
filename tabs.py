"""
tabs.py — All six tab content functions for the Hypothesis Testing app
"""

import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import io

from components import (
    card, info_box, formula_box, badge, steps_html,
    two_col_html, three_col_html, table_html, metric_row,
)
from charts import (
    normal_curve_overview, right_tailed_chart, left_tailed_chart,
    two_tailed_chart, comparison_chart,
)


# ═══════════════════════════════════════════════════════════════════
# TAB 1 — OVERVIEW
# ═══════════════════════════════════════════════════════════════════

def tab_overview():
    st.markdown(f"""
<div class="mp-card">
  <h2>📐 Foundation: What is Hypothesis Testing?</h2>
  <p>Hypothesis testing is a statistical decision framework using sample data to make
  inferences about population parameters. In finance it answers: <em>"Does this fund
  generate alpha?"</em> or <em>"Has market risk increased after a policy change?"</em></p>
  {two_col_html(
      info_box("<h3>Null Hypothesis (H₀)</h3><p>The <strong>default assumption</strong> — "
               "'no change', 'no effect', 'equals benchmark'. We assume H₀ is true and "
               "look for evidence to reject it.</p>"
               "<p><span class='hl'>Example:</span> μ = 12% (fund matches market)</p>",
               "blue"),
      info_box("<h3>Alternative Hypothesis (H₁)</h3><p>The <strong>claim under test</strong>. "
               "Its direction (&gt;, &lt;, or ≠) determines one-tailed vs two-tailed test.</p>"
               "<p><span class='hl'>Example:</span> μ &gt; 12% (fund outperforms)</p>",
               "gold"),
  )}
  {normal_curve_overview()}
  {three_col_html(
      info_box("<strong style='color:#ADD8E6'>α — Significance Level</strong><br>"
               "P(Type I Error). Probability of rejecting a true H₀.<br>"
               f"{badge('Common: 1%, 5%, 10%','gold')}", "blue"),
      info_box("<strong style='color:#FFD700'>p-value</strong><br>"
               "P(observing data at least this extreme | H₀ true).<br>"
               f"{badge('p &lt; α → Reject H₀','red')} {badge('p ≥ α → Fail to Reject','green')}",
               "gold"),
      info_box("<strong style='color:#28a745'>Critical Region</strong><br>"
               "Values of test statistic that trigger rejection of H₀, set by α.<br>"
               f"{badge('z-stat or t-stat','blue')}", "green"),
  )}
</div>
""", unsafe_allow_html=True)

    st.markdown(f"""
<div class="mp-card">
  <h2>🗺 Decision Guide: Which Test?</h2>
  {table_html(
      ["Research Question", "H₁", "Test", "Critical Region"],
      [
          ["Did returns <strong>change</strong> (either direction)?", "μ ≠ μ₀",
           badge("Two-Tailed","blue"), "Both tails (α/2 each)"],
          ["Did returns <strong>increase</strong>?", "μ &gt; μ₀",
           badge("Right-Tailed","gold"), "Right tail only (full α)"],
          ["Did risk <strong>worsen / increase</strong>?", "μ &gt; μ₀",
           badge("Right-Tailed","red"), "Right tail only (full α)"],
      ]
  )}
</div>
""", unsafe_allow_html=True)

    # Interactive concept widget
    st.markdown('<div class="mp-card"><h2>🔢 Key Constants at a Glance</h2>', unsafe_allow_html=True)
    metric_row([
        ("One-Tail α=5%", "z = 1.645", None),
        ("Two-Tail α=5%", "z = ±1.960", None),
        ("One-Tail α=1%", "z = 2.326", None),
        ("Two-Tail α=1%", "z = ±2.576", None),
    ])
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# TAB 2 — ONE-TAILED TESTS
# ═══════════════════════════════════════════════════════════════════

def tab_one_tailed():
    st.markdown(f"""
<div class="mp-card">
  <h2>→ One-Tailed Tests: Right-Tailed &amp; Left-Tailed</h2>
  <p>Used when there is a <strong>directional hypothesis</strong>. All of the significance
  level α is concentrated in ONE tail, giving more statistical power to detect effects
  in that specific direction.</p>
  {two_col_html(
      info_box("<h3 style='color:#FFD700'>▶ Right-Tailed Test</h3>"
               "<p><strong>H₀:</strong> μ ≤ μ₀ &nbsp;|&nbsp; <strong>H₁:</strong> μ &gt; μ₀</p>"
               "<p>Reject H₀ if statistic in the <span class='hl'>RIGHT tail</span></p>"
               "<p><span class='gt'>Finance use:</span> Fund return exceeds benchmark?</p>"
               + right_tailed_chart()
               + formula_box("z = (x̄ − μ₀) / (σ/√n)\nReject H₀ if z > z_α\nα=5%: z > <span class='hl'>+1.645</span>\nα=1%: z > <span class='hl'>+2.326</span>"),
               "gold"),
      info_box("<h3 style='color:#dc3545'>◀ Left-Tailed Test</h3>"
               "<p><strong>H₀:</strong> μ ≥ μ₀ &nbsp;|&nbsp; <strong>H₁:</strong> μ &lt; μ₀</p>"
               "<p>Reject H₀ if statistic in the <span class='rt'>LEFT tail</span></p>"
               "<p><span class='gt'>Finance use:</span> Portfolio losses worsened (VaR up)?</p>"
               + left_tailed_chart()
               + formula_box("z = (x̄ − μ₀) / (σ/√n)\nReject H₀ if z < −z_α\nα=5%: z < <span class='hl'>−1.645</span>\nα=1%: z < <span class='hl'>−2.326</span>"),
               "red"),
  )}
</div>
""", unsafe_allow_html=True)

    # Interactive one-tailed example
    st.markdown('<div class="mp-card"><h2>📊 Worked Example — Portfolio Alpha Test (Interactive)</h2>',
                unsafe_allow_html=True)
    st.markdown(info_box("<strong>Scenario:</strong> A fund claims returns <em>greater than</em> the market "
                         "return. Sample of n months shows mean return x̄, σ known. Test at chosen α.", "gold"),
                unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    x_bar   = c1.number_input("Sample Mean (x̄) %", value=13.5, step=0.1, key="ot_xbar")
    mu_0    = c2.number_input("Population Mean (μ₀) %", value=12.0, step=0.1, key="ot_mu0")
    sigma   = c3.number_input("Std Dev (σ) %", value=6.0, min_value=0.1, step=0.1, key="ot_sig")
    n       = c4.number_input("Sample Size (n)", value=36, min_value=1, step=1, key="ot_n")

    alpha_choice = st.select_slider("Significance Level α",
                                    options=[0.10, 0.05, 0.025, 0.01],
                                    value=0.05, key="ot_alpha")
    tail_choice = st.radio("Test Direction", ["Right-Tailed (H₁: μ > μ₀)", "Left-Tailed (H₁: μ < μ₀)"],
                            horizontal=True, key="ot_tail")
    tail = "right" if "Right" in tail_choice else "left"

    se     = sigma / np.sqrt(n)
    z_stat = (x_bar - mu_0) / se

    if tail == "right":
        z_crit  = stats.norm.ppf(1 - alpha_choice)
        p_value = 1 - stats.norm.cdf(z_stat)
        reject  = z_stat > z_crit
    else:
        z_crit  = stats.norm.ppf(alpha_choice)
        p_value = stats.norm.cdf(z_stat)
        reject  = z_stat < z_crit

    # Results metrics
    st.markdown("---")
    metric_row([
        ("z-statistic", f"{z_stat:.4f}", None),
        ("Critical Value", f"{z_crit:.3f}", None),
        ("p-value", f"{p_value:.4f}", None),
        ("Decision", "REJECT H₀ 🔴" if reject else "FAIL TO REJECT 🟢", None),
    ])

    # Plot
    fig = _plot_test(z_stat, alpha_choice, tail,
                     title=f"One-Tailed ({tail.capitalize()}) | α={alpha_choice}")
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    st.markdown("""
<div class="ib ib-blue">
  <strong>Key Insight:</strong> All α is concentrated in one tail, giving more power
  to detect effects in the stated direction — but the direction must be decided
  <em>before</em> data collection to avoid p-hacking.
</div></div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# TAB 3 — TWO-TAILED TESTS
# ═══════════════════════════════════════════════════════════════════

def tab_two_tailed():
    st.markdown(f"""
<div class="mp-card">
  <h2>↔ Two-Tailed Test: Testing for Any Difference</h2>
  <p>Used for <strong>non-directional hypotheses</strong> — detecting a difference in
  <em>either direction</em>. The α is split equally: α/2 per tail, requiring more
  extreme test statistics to reject H₀.</p>
  {two_tailed_chart()}
  {formula_box("Two-Tailed: H₀: μ = μ₀  |  H₁: μ ≠ μ₀\n\nReject H₀ if |z| > z_{α/2}\n\nα = 5%:  |z| > <span class='hl'>1.960</span>  (±1.960)\nα = 1%:  |z| > <span class='hl'>2.576</span>  (±2.576)\nα = 10%: |z| > <span class='hl'>1.645</span>  (±1.645)\n\np-value (two-tailed) = 2 × P(Z > |z|)")}
  {info_box("<strong>Why split α?</strong> We're open to deviation in either direction. Each tail "
            "gets only α/2 = 2.5%, so critical values are more extreme (±1.96 vs ±1.645) — "
            "making two-tailed tests more conservative but directionally unbiased.", "blue")}
</div>
""", unsafe_allow_html=True)

    # Interactive two-tailed example
    st.markdown('<div class="mp-card"><h2>📊 Worked Example — VaR Change Test (Interactive)</h2>',
                unsafe_allow_html=True)
    st.markdown(info_box("<strong>Scenario:</strong> Historical daily VaR = ₹50 Lakhs. After a system "
                         "upgrade, 64 days show mean loss = ₹47.5L, σ = ₹12L. Has VaR <em>changed</em>?",
                         "gold"), unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    x_bar   = c1.number_input("Sample Mean (x̄)", value=47.5, step=0.5, key="tt_xbar")
    mu_0    = c2.number_input("Population Mean (μ₀)", value=50.0, step=0.5, key="tt_mu0")
    sigma   = c3.number_input("Std Dev (σ)", value=12.0, min_value=0.1, step=0.5, key="tt_sig")
    n       = c4.number_input("Sample Size (n)", value=64, min_value=1, step=1, key="tt_n")

    alpha_choice = st.select_slider("Significance Level α",
                                    options=[0.10, 0.05, 0.025, 0.01],
                                    value=0.05, key="tt_alpha")

    se      = sigma / np.sqrt(n)
    z_stat  = (x_bar - mu_0) / se
    z_crit  = stats.norm.ppf(1 - alpha_choice / 2)
    p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    reject  = abs(z_stat) > z_crit

    st.markdown("---")
    metric_row([
        ("z-statistic", f"{z_stat:.4f}", None),
        ("Critical Value", f"±{z_crit:.3f}", None),
        ("p-value", f"{p_value:.4f}", None),
        ("Decision", "REJECT H₀ 🔴" if reject else "FAIL TO REJECT 🟢", None),
    ])

    fig = _plot_test(z_stat, alpha_choice, "two",
                     title=f"Two-Tailed | α={alpha_choice}")
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    # Steps breakdown
    steps = [
        ("Hypotheses", f"H₀: μ = {mu_0} &nbsp;|&nbsp; H₁: μ ≠ {mu_0} → {badge('Two-Tailed','blue')}"),
        ("Critical value", f"α/2 = {alpha_choice/2:.3f} per tail → z_crit = <span class='hl'>±{z_crit:.3f}</span>"),
        ("Test statistic",
         f"<div class='fml'>z = ({x_bar} − {mu_0}) / ({sigma}/√{n}) = {x_bar-mu_0:.1f} / {se:.4f} = <span class='hl'>{z_stat:.4f}</span></div>"),
        ("Decision",
         f"|z| = {abs(z_stat):.4f} {'>' if reject else '<'} {z_crit:.3f} → "
         f"<span class='{'vr' if reject else 'vf'}'>{'REJECT H₀' if reject else 'FAIL TO REJECT H₀'}</span>"),
        ("p-value",
         f"2 × P(Z &lt; -{abs(z_stat):.4f}) = <span class='hl'>{p_value:.4f}</span> "
         f"{'< α → Reject' if p_value < alpha_choice else '> α → Fail to Reject'}"),
    ]
    st.markdown(f"""
<div class='ib ib-gold' style='margin-top:14px'>
  <strong>Step-by-Step Breakdown:</strong>
  <div style="margin-top:10px">{steps_html(steps)}</div>
</div>""", unsafe_allow_html=True)

    st.markdown(f"""
{info_box("<strong>⚠ Critical Insight:</strong> If we wrongly used a left-tailed test here: "
          f"z = {z_stat:.4f} and z_crit = {-stats.norm.ppf(1-alpha_choice):.3f}. "
          f"{'We WOULD reject H₀ — showing how test direction critically affects conclusions!' if z_stat < -stats.norm.ppf(1-alpha_choice) else 'We still would not reject — but the threshold changes to a less strict value!'}", "red")}
</div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# TAB 4 — COMPARISON
# ═══════════════════════════════════════════════════════════════════

def tab_comparison():
    st.markdown(f"""
<div class="mp-card">
  <h2>⚖ One-Tailed vs Two-Tailed: Complete Comparison</h2>
  {comparison_chart()}
  {table_html(
      ["Feature", "One-Tailed", "Two-Tailed"],
      [
          ["H₁ direction", "Directional (&gt; or &lt;)", "Non-directional (≠)"],
          ["Critical region", "One tail", "Both tails (α/2 each)"],
          ["Critical z (α=5%)", "<span class='gt'>±1.645</span>", "<span class='rt'>±1.960</span>"],
          ["Critical z (α=1%)", "<span class='gt'>±2.326</span>", "<span class='rt'>±2.576</span>"],
          ["Statistical power", "<span class='gt'>Higher (in stated direction)</span>", "<span class='rt'>Lower</span>"],
          ["p-value formula", "P(Z&gt;z) or P(Z&lt;z)", "2 × P(Z &gt; |z|)"],
          ["When to use", "Prior directional belief", "Direction unknown"],
          ["Risk of misuse", "Misleading if direction wrong", "Conservative but safer"],
      ]
  )}
</div>
""", unsafe_allow_html=True)

    # Type I & II errors
    st.markdown(f"""
<div class="mp-card">
  <h2>🎯 Type I &amp; Type II Errors</h2>
  {two_col_html(
      info_box("<strong style='color:#dc3545'>Type I Error (α) — False Positive</strong><br>"
               "Reject H₀ when it is actually TRUE.<br>"
               "<em>Finance:</em> Declaring a fund has alpha when it doesn't.<br>"
               f"{badge('Controlled by significance level α','red')}", "red"),
      info_box("<strong style='color:#FFD700'>Type II Error (β) — False Negative</strong><br>"
               "Fail to reject H₀ when it is actually FALSE.<br>"
               "<em>Finance:</em> Missing a fund that truly outperforms.<br>"
               f"{badge('Power = 1 − β (maximize this)','gold')}", "gold"),
  )}
  {info_box("One-tailed tests have higher power (lower β) for a given directional effect — "
            "making them preferred when directional theory is well-established. Two-tailed tests "
            "reduce risk of false positives from wrong direction assumptions.", "green")}
</div>
""", unsafe_allow_html=True)

    # Interactive critical value explorer
    st.markdown('<div class="mp-card"><h2>🔭 Critical Value Explorer</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    alpha_exp = col1.select_slider("α", options=[0.10, 0.05, 0.025, 0.01, 0.005], value=0.05, key="cmp_alpha")
    test_type = col2.radio("Test Type", ["One-Tailed", "Two-Tailed"], horizontal=True, key="cmp_type")

    if test_type == "One-Tailed":
        zc = stats.norm.ppf(1 - alpha_exp)
        tc30 = stats.t.ppf(1 - alpha_exp, df=30)
        tc60 = stats.t.ppf(1 - alpha_exp, df=60)
        label = f"One-Tail (α={alpha_exp})"
    else:
        zc = stats.norm.ppf(1 - alpha_exp / 2)
        tc30 = stats.t.ppf(1 - alpha_exp / 2, df=30)
        tc60 = stats.t.ppf(1 - alpha_exp / 2, df=60)
        label = f"Two-Tail (α={alpha_exp})"

    metric_row([
        (f"z-critical ({label})", f"±{zc:.3f}", None),
        ("t-critical (df=30)", f"±{tc30:.3f}", None),
        ("t-critical (df=60)", f"±{tc60:.3f}", None),
        ("t-critical (df=∞)", f"±{zc:.3f}", None),
    ])

    fig2 = _plot_test(0, alpha_exp,
                      "two" if test_type == "Two-Tailed" else "right",
                      title=f"Critical Region | {label}")
    st.pyplot(fig2, use_container_width=True)
    plt.close(fig2)
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# TAB 5 — FINANCE EXAMPLES
# ═══════════════════════════════════════════════════════════════════

def tab_finance_examples():
    st.markdown(f"""
<div class="mp-card">
  <h2>💹 Real-World Finance &amp; Risk Applications</h2>
  {two_col_html(
      info_box("<h3>1. Portfolio Alpha (Jensen's α)</h3>"
               f"{badge('Right-Tailed','gold')}"
               "<p><strong>H₀:</strong> α ≤ 0 &nbsp;|&nbsp; <strong>H₁:</strong> α &gt; 0</p>"
               "<p>t = α_hat / SE(α_hat) from regression</p>", "gold"),
      info_box("<h3>2. CAPM Beta Neutrality</h3>"
               f"{badge('Two-Tailed','blue')}"
               "<p><strong>H₀:</strong> β = 1 &nbsp;|&nbsp; <strong>H₁:</strong> β ≠ 1</p>"
               "<p>t = (β_hat − 1) / SE(β_hat)</p>", "blue"),
  )}
  {two_col_html(
      info_box("<h3>3. VaR Backtesting (Kupiec)</h3>"
               f"{badge('Right-Tailed','red')}"
               "<p><strong>H₀:</strong> exceedance = 5% &nbsp;|&nbsp; <strong>H₁:</strong> &gt; 5%</p>"
               "<p>Binomial test on number of VaR breaches</p>", "red"),
      info_box("<h3>4. Credit Default Rate</h3>"
               f"{badge('Right-Tailed','gold')}"
               "<p><strong>H₀:</strong> default rate ≤ 2% &nbsp;|&nbsp; <strong>H₁:</strong> &gt; 2%</p>"
               "<p>Monitoring loan portfolio risk deterioration</p>", "gold"),
  )}
  {two_col_html(
      info_box("<h3>5. Bond Portfolio Duration</h3>"
               f"{badge('Two-Tailed','blue')}"
               "<p><strong>H₀:</strong> D = 7 yrs &nbsp;|&nbsp; <strong>H₁:</strong> D ≠ 7 yrs</p>"
               "<p>Post-rebalancing duration shift check</p>", "blue"),
      info_box("<h3>6. Sharpe Ratio Test</h3>"
               f"{badge('Right-Tailed','gold')}"
               "<p><strong>H₀:</strong> SR ≤ 0.5 &nbsp;|&nbsp; <strong>H₁:</strong> SR &gt; 0.5</p>"
               "<p>Jobson-Korkie test for risk-adjusted performance</p>", "gold"),
  )}
</div>
""", unsafe_allow_html=True)

    # Solved bond duration example
    st.markdown('<div class="mp-card"><h2>📋 Solved: Bond Portfolio Duration Test (t-test)</h2>',
                unsafe_allow_html=True)
    st.markdown(info_box("<strong>Scenario:</strong> Target modified duration = 7 years. After "
                         "restructuring, 49 bonds: mean = 7.84 yrs, s = 2.94 yrs. "
                         "Has duration changed? α = 1%.", "gold"), unsafe_allow_html=True)

    x_bar_b, mu_0_b, s_b, n_b, alpha_b = 7.84, 7.0, 2.94, 49, 0.01
    se_b    = s_b / np.sqrt(n_b)
    t_stat  = (x_bar_b - mu_0_b) / se_b
    df_b    = n_b - 1
    t_crit  = stats.t.ppf(1 - alpha_b / 2, df=df_b)
    p_val_b = 2 * (1 - stats.t.cdf(abs(t_stat), df=df_b))
    reject_b = abs(t_stat) > t_crit

    metric_row([
        ("t-statistic", f"{t_stat:.4f}", None),
        ("Critical Value (df=48, α=1%)", f"±{t_crit:.3f}", None),
        ("p-value", f"{p_val_b:.4f}", None),
        ("Decision", "REJECT H₀ 🔴" if reject_b else "FAIL TO REJECT 🟢", None),
    ])

    steps_b = [
        ("Hypotheses", f"H₀: μ = {mu_0_b} &nbsp;|&nbsp; H₁: μ ≠ {mu_0_b} → {badge('Two-Tailed t-test','blue')}"),
        ("Critical value",
         f"df = {df_b}, α = {alpha_b}, two-tailed → t_crit = <span class='hl'>±{t_crit:.3f}</span>"),
        ("Test statistic",
         f"<div class='fml'>t = ({x_bar_b} − {mu_0_b}) / ({s_b}/√{n_b}) = {x_bar_b - mu_0_b:.2f} / {se_b:.4f} = <span class='hl'>{t_stat:.4f}</span></div>"),
        ("Decision",
         f"|t| = {abs(t_stat):.4f} {'>' if reject_b else '<'} {t_crit:.3f} → "
         f"<span class='{'vr' if reject_b else 'vf'}'>{'REJECT H₀' if reject_b else 'FAIL TO REJECT H₀'}</span> at α={alpha_b}"),
        ("Note", f"At α=5% (t_crit = ±{stats.t.ppf(0.975, df=df_b):.3f}): also fail to reject. p-value = {p_val_b:.4f} (borderline)."),
    ]
    st.markdown(f'<div style="margin-top:14px">{steps_html(steps_b)}</div>',
                unsafe_allow_html=True)

    fig3 = _plot_test(t_stat, alpha_b, "two", title="Bond Duration Test (t-distribution, df=48)")
    st.pyplot(fig3, use_container_width=True)
    plt.close(fig3)
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# TAB 6 — PYTHON CODE
# ═══════════════════════════════════════════════════════════════════

def tab_python_code():
    st.markdown('<div class="mp-card"><h2>🐍 Python Implementation</h2>', unsafe_allow_html=True)

    python_code = '''import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# ============================================================
# 1. REUSABLE Z-TEST FUNCTION (population std known)
# ============================================================
def z_test(sample_mean, pop_mean, pop_std, n, alpha=0.05, tail='two'):
    """Z-test when population std is known."""
    se = pop_std / np.sqrt(n)
    z_stat = (sample_mean - pop_mean) / se

    if tail == 'right':
        z_crit = stats.norm.ppf(1 - alpha)
        p_value = 1 - stats.norm.cdf(z_stat)
        reject = z_stat > z_crit
    elif tail == 'left':
        z_crit = stats.norm.ppf(alpha)
        p_value = stats.norm.cdf(z_stat)
        reject = z_stat < z_crit
    else:  # two-tailed
        z_crit = stats.norm.ppf(1 - alpha / 2)
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
        reject = abs(z_stat) > z_crit

    cv = f"±{z_crit:.3f}" if tail == 'two' else f"{z_crit:.3f}"
    print(f"\\nZ-Test ({tail}-tailed) | α={alpha}")
    print(f"  z-stat={z_stat:.4f} | z_crit={cv} | p={p_value:.4f}")
    print(f"  → {'REJECT H₀' if reject else 'FAIL TO REJECT H₀'}")
    return z_stat, p_value, reject

# Example 1: Portfolio alpha test (right-tailed)
z_test(sample_mean=13.5, pop_mean=12, pop_std=6, n=36, alpha=0.05, tail='right')
# Output: z=1.5000 | z_crit=1.645 | p=0.0668 → FAIL TO REJECT H₀

# Example 2: VaR change test (two-tailed)
z_test(sample_mean=47.5, pop_mean=50, pop_std=12, n=64, alpha=0.05, tail='two')
# Output: z=-1.6667 | z_crit=±1.960 | p=0.0956 → FAIL TO REJECT H₀


# ============================================================
# 2. ONE-SAMPLE T-TEST (σ unknown — most common in finance)
# ============================================================
def t_test_one_sample(data, pop_mean, alpha=0.05, tail='two'):
    """One-sample t-test when population std is unknown."""
    n     = len(data)
    x_bar = np.mean(data)
    s     = np.std(data, ddof=1)
    t_stat = (x_bar - pop_mean) / (s / np.sqrt(n))
    df    = n - 1

    if tail == 'right':
        t_crit  = stats.t.ppf(1 - alpha, df)
        p_value = 1 - stats.t.cdf(t_stat, df)
        reject  = t_stat > t_crit
    elif tail == 'left':
        t_crit  = stats.t.ppf(alpha, df)
        p_value = stats.t.cdf(t_stat, df)
        reject  = t_stat < t_crit
    else:
        t_crit  = stats.t.ppf(1 - alpha / 2, df)
        p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))
        reject  = abs(t_stat) > t_crit

    cv = f"±{t_crit:.3f}" if tail == 'two' else f"{t_crit:.3f}"
    print(f"\\nT-Test ({tail}-tailed) | df={df} | α={alpha}")
    print(f"  x̄={x_bar:.3f} | s={s:.3f} | t={t_stat:.4f} | t_crit={cv} | p={p_value:.4f}")
    print(f"  → {'REJECT H₀' if reject else 'FAIL TO REJECT H₀'}")
    return t_stat, p_value

# Bond duration test (two-tailed, α=1%)
np.random.seed(42)
bond_durations = np.random.normal(loc=7.84, scale=2.94, size=49)
t_test_one_sample(bond_durations, pop_mean=7, alpha=0.01, tail='two')


# ============================================================
# 3. VISUALIZATION
# ============================================================
def plot_test(z_stat, alpha=0.05, tail='two', title=''):
    """Plot normal distribution with rejection region and test statistic."""
    fig, ax = plt.subplots(figsize=(10, 4.5))
    fig.patch.set_facecolor('#0a1628')
    ax.set_facecolor('#112240')

    x = np.linspace(-4, 4, 500)
    y = stats.norm.pdf(x)
    ax.plot(x, y, color='#ADD8E6', lw=2.5)
    ax.fill_between(x, y, alpha=0.2, color='#004d80')

    def shade(xl):
        ax.fill_between(xl, stats.norm.pdf(xl), color='#dc3545', alpha=0.7)

    if tail == 'two':
        zc = stats.norm.ppf(1 - alpha / 2)
        shade(np.linspace(zc, 4, 100))
        shade(np.linspace(-4, -zc, 100))
        ax.axvline(zc, color='#dc3545', ls='--', lw=1.5,
                   label=f'z_crit = ±{zc:.3f}')
        ax.axvline(-zc, color='#dc3545', ls='--', lw=1.5)
    elif tail == 'right':
        zc = stats.norm.ppf(1 - alpha)
        shade(np.linspace(zc, 4, 100))
        ax.axvline(zc, color='#dc3545', ls='--', lw=1.5,
                   label=f'z_crit = +{zc:.3f}')
    else:
        zc = stats.norm.ppf(alpha)
        shade(np.linspace(-4, zc, 100))
        ax.axvline(zc, color='#dc3545', ls='--', lw=1.5,
                   label=f'z_crit = {zc:.3f}')

    ax.axvline(z_stat, color='#FFD700', lw=2.5, label=f'z_stat = {z_stat:.3f}')
    ax.scatter([z_stat], [stats.norm.pdf(z_stat)], color='#FFD700', s=80, zorder=5)

    ax.set_title(f'{tail.capitalize()}-tailed | {title} | α={alpha}',
                 color='#FFD700', fontsize=12)
    ax.set_xlabel('Standard Deviations', color='#8892b0')
    ax.tick_params(colors='#8892b0')
    ax.legend(facecolor='#112240', labelcolor='#e6f1ff')
    for sp in ax.spines.values():
        sp.set_color('#1e3a5f')
    plt.tight_layout()
    return fig


# ============================================================
# 4. CRITICAL VALUES TABLE
# ============================================================
print("\\nCRITICAL VALUES REFERENCE")
print(f"{'α':>6} | {'1-tail z':>10} | {'2-tail z':>10} | {'2-tail t(df=30)':>16}")
for a in [0.10, 0.05, 0.025, 0.01, 0.005]:
    z1 = stats.norm.ppf(1 - a)
    z2 = stats.norm.ppf(1 - a / 2)
    t2 = stats.t.ppf(1 - a / 2, df=30)
    print(f"{a:>6.3f} | {z1:>10.3f} | {z2:>10.3f} | {t2:>16.3f}")
'''

    st.code(python_code, language="python")
    st.markdown('</div>', unsafe_allow_html=True)

    # Live Python runner
    st.markdown('<div class="mp-card"><h2>▶ Live Code Runner</h2>', unsafe_allow_html=True)
    st.markdown(info_box("Run hypothesis tests live. Adjust parameters and click Run.", "blue"),
                unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Z-Test Parameters**")
        xb   = st.number_input("Sample Mean", value=13.5, key="py_xb")
        mu   = st.number_input("Population Mean", value=12.0, key="py_mu")
        sig  = st.number_input("Std Dev", value=6.0, min_value=0.01, key="py_sig")
        nn   = st.number_input("n", value=36, min_value=1, key="py_n")
        alp  = st.select_slider("α", options=[0.10, 0.05, 0.01], value=0.05, key="py_a")
        tl   = st.radio("Tail", ["right", "left", "two"], horizontal=True, key="py_tl")

    if st.button("▶ Run Z-Test", key="run_zt"):
        se     = sig / np.sqrt(nn)
        zs     = (xb - mu) / se
        if tl == "right":
            zc = stats.norm.ppf(1 - alp); pv = 1 - stats.norm.cdf(zs); rej = zs > zc
        elif tl == "left":
            zc = stats.norm.ppf(alp); pv = stats.norm.cdf(zs); rej = zs < zc
        else:
            zc = stats.norm.ppf(1 - alp / 2); pv = 2 * (1 - stats.norm.cdf(abs(zs))); rej = abs(zs) > zc

        cv_str = f"±{zc:.3f}" if tl == "two" else f"{zc:.3f}"
        result_color = "#dc3545" if rej else "#28a745"
        decision_txt = "REJECT H₀" if rej else "FAIL TO REJECT H₀"

        st.markdown(f"""
<div class='ib ib-gold' style='font-family:JetBrains Mono,monospace;font-size:.9rem'>
  z-stat = <span class='hl'>{zs:.4f}</span>
  &nbsp;|&nbsp; z_crit = <span class='hl'>{cv_str}</span>
  &nbsp;|&nbsp; p-value = <span class='hl'>{pv:.4f}</span><br>
  Decision: <strong style='color:{result_color};font-size:1.1rem'>{decision_txt}</strong>
</div>""", unsafe_allow_html=True)

        fig4 = _plot_test(zs, alp, tl, title=f"z={zs:.3f} | α={alp}")
        st.pyplot(fig4, use_container_width=True)
        plt.close(fig4)

    # Critical values table
    st.markdown('<h3 style="color:#ADD8E6;font-family:Playfair Display,serif;margin-top:20px">🔢 Critical Values Reference</h3>',
                unsafe_allow_html=True)
    rows = []
    for a in [0.10, 0.05, 0.025, 0.01, 0.005]:
        z1 = stats.norm.ppf(1 - a)
        z2 = stats.norm.ppf(1 - a / 2)
        t30 = stats.t.ppf(1 - a / 2, df=30)
        t60 = stats.t.ppf(1 - a / 2, df=60)
        rows.append([f"{a:.3f}",
                     f"<span class='hl'>{z1:.3f}</span>",
                     f"<span class='hl'>{z2:.3f}</span>",
                     f"{t30:.3f}",
                     f"{t60:.3f}"])

    st.markdown(table_html(
        ["α", "One-Tail z", "Two-Tail z (±)", "Two-Tail t (df=30)", "Two-Tail t (df=60)"],
        rows
    ), unsafe_allow_html=True)

    st.markdown(info_box("<strong>Memory Anchor:</strong> "
                         "<span class='hl'>1.645 → 1.96 → 2.33 → 2.576</span> — "
                         "One-tail 5%, Two-tail 5%, One-tail 1%, Two-tail 1%. "
                         "These four values cover 90% of all finance hypothesis tests!", "blue"),
                unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# SHARED PLOT HELPER
# ═══════════════════════════════════════════════════════════════════

def _plot_test(z_stat: float, alpha: float, tail: str, title: str = "") -> plt.Figure:
    """Generate a styled matplotlib figure showing the rejection region."""
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor("#0a1628")
    ax.set_facecolor("#112240")

    x = np.linspace(-4, 4, 600)
    y = stats.norm.pdf(x)
    ax.plot(x, y, color="#ADD8E6", lw=2.5, zorder=3)
    ax.fill_between(x, y, alpha=0.22, color="#004d80")

    def shade(xl):
        ax.fill_between(xl, stats.norm.pdf(xl), color="#dc3545", alpha=0.72, zorder=2)

    if tail == "two":
        zc = stats.norm.ppf(1 - alpha / 2)
        shade(np.linspace(zc, 4.05, 150))
        shade(np.linspace(-4.05, -zc, 150))
        ax.axvline(zc,  color="#dc3545", ls="--", lw=1.8, label=f"z_crit = ±{zc:.3f}")
        ax.axvline(-zc, color="#dc3545", ls="--", lw=1.8)
        ax.text(zc  + 0.12, 0.02, f"+{zc:.2f}", color="#dc3545", fontsize=9)
        ax.text(-zc - 0.55, 0.02, f"-{zc:.2f}", color="#dc3545", fontsize=9)
    elif tail == "right":
        zc = stats.norm.ppf(1 - alpha)
        shade(np.linspace(zc, 4.05, 150))
        ax.axvline(zc, color="#dc3545", ls="--", lw=1.8, label=f"z_crit = +{zc:.3f}")
        ax.text(zc + 0.1, 0.02, f"+{zc:.2f}", color="#dc3545", fontsize=9)
    else:
        zc = stats.norm.ppf(alpha)
        shade(np.linspace(-4.05, zc, 150))
        ax.axvline(zc, color="#dc3545", ls="--", lw=1.8, label=f"z_crit = {zc:.3f}")
        ax.text(zc - 0.65, 0.02, f"{zc:.2f}", color="#dc3545", fontsize=9)

    if z_stat != 0:
        ax.axvline(z_stat, color="#FFD700", lw=2.5, zorder=4, label=f"z_stat = {z_stat:.4f}")
        ax.scatter([z_stat], [stats.norm.pdf(z_stat)], color="#FFD700", s=80, zorder=5)

    # Shading label
    reject_z = (tail == "two"    and abs(z_stat) > stats.norm.ppf(1 - alpha / 2)) or \
               (tail == "right"  and z_stat > stats.norm.ppf(1 - alpha)) or \
               (tail == "left"   and z_stat < stats.norm.ppf(alpha))

    if z_stat != 0:
        decision = "REJECT H₀" if reject_z else "FAIL TO REJECT H₀"
        d_color = "#dc3545" if reject_z else "#28a745"
        ax.text(0.5, 0.92, decision, transform=ax.transAxes,
                ha="center", fontsize=13, fontweight="bold",
                color=d_color, family="DejaVu Sans")

    ax.set_title(title, color="#FFD700", fontsize=11, pad=8, family="DejaVu Sans")
    ax.set_xlabel("Standard Deviations from Mean", color="#8892b0", fontsize=9)
    ax.set_ylabel("Density", color="#8892b0", fontsize=9)
    ax.tick_params(colors="#8892b0", labelsize=8)
    ax.legend(facecolor="#112240", labelcolor="#e6f1ff", fontsize=9,
              framealpha=0.8, edgecolor="#1e3a5f")
    for sp in ax.spines.values():
        sp.set_color("#1e3a5f")
    ax.grid(axis="y", color="#1e3a5f", alpha=0.4, lw=0.5)
    plt.tight_layout(pad=1.2)
    return fig
