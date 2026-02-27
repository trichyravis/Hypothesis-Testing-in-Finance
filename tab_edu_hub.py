"""
tab_edu_hub.py — Education Hub: Concept Cards, Glossary, Formula Sheet,
Decision Guide, and MCQ Quiz for Hypothesis Testing in Finance.
"""
import streamlit as st
from components import (
    render_card, ib, render_ib, fml, bdg,
    hl, gt, rt2, lb_t, mut_t, txt_s, p,
    two_col, three_col, table_html,
    section_heading, steps_html,
    FH, FB, FM, TXT, NO_SEL,
)
from tab_explainers import explainer_edu_hub

# ── helpers ───────────────────────────────────────────────────────
def _gold(t):  return f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">{t}</span>'
def _blue(t):  return f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">{t}</span>'
def _green(t): return f'<span style="color:#28a745;-webkit-text-fill-color:#28a745;font-weight:600">{t}</span>'
def _red(t):   return f'<span style="color:#dc3545;-webkit-text-fill-color:#dc3545;font-weight:600">{t}</span>'
def _mono(t):  return f'<span style="font-family:{FM};color:#64ffda;-webkit-text-fill-color:#64ffda">{t}</span>'

def _concept_card(icon, title, title_color, border, bg, items):
    rows = "".join(
        f'<div style="display:flex;align-items:flex-start;gap:9px;margin-bottom:8px;{NO_SEL}">'
        f'{item["badge"]}'
        f'<span style="font-family:{FB};font-size:.87rem;color:#e6f1ff;'
        f'-webkit-text-fill-color:#e6f1ff;line-height:1.55">{item["text"]}</span></div>'
        for item in items
    )
    return (
        f'<div style="background:{bg};border-left:4px solid {border};border-radius:10px;'
        f'padding:16px 17px;height:100%;user-select:none;-webkit-user-select:none">'
        f'<div style="font-family:{FH};font-size:1rem;color:{title_color};'
        f'-webkit-text-fill-color:{title_color};font-weight:700;margin-bottom:12px">'
        f'{icon} {title}</div>'
        f'{rows}</div>'
    )

def _term_card(term, symbol, definition, formula, example, badge_label, badge_variant, finance_note):
    sym = (f'<span style="font-family:{FM};font-size:.8rem;color:#64ffda;'
           f'-webkit-text-fill-color:#64ffda;margin-left:8px">{symbol}</span>') if symbol else ""
    return (
        f'<div style="background:#112240;border:1px solid #1e3a5f;border-radius:10px;'
        f'padding:15px 17px;margin-bottom:13px;{NO_SEL}">'
        f'<div style="display:flex;align-items:center;gap:8px;margin-bottom:7px">'
        f'<span style="font-family:{FH};font-size:1rem;color:#FFD700;'
        f'-webkit-text-fill-color:#FFD700;font-weight:700">{term}</span>'
        f'{sym}{bdg(badge_label, badge_variant)}</div>'
        f'<div style="font-family:{FB};font-size:.89rem;color:#e6f1ff;'
        f'-webkit-text-fill-color:#e6f1ff;line-height:1.65;margin-bottom:6px">{definition}</div>'
        + fml(formula) +
        f'<div style="background:rgba(255,215,0,0.08);border-left:3px solid #FFD700;'
        f'border-radius:5px;padding:8px 11px;margin:8px 0;font-family:{FB};font-size:.84rem;'
        f'color:#e6f1ff;-webkit-text-fill-color:#e6f1ff;line-height:1.55">'
        f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">Example: </span>{example}</div>'
        f'<div style="font-family:{FB};font-size:.83rem;color:#ADD8E6;'
        f'-webkit-text-fill-color:#ADD8E6;margin-top:6px">'
        f'<span style="font-weight:600">📈 Finance: </span>{finance_note}</div>'
        f'</div>'
    )

def _row(label, value):
    return (
        f'<div style="display:flex;justify-content:space-between;padding:4px 0;'
        f'border-bottom:1px solid rgba(30,58,95,0.5);{NO_SEL}">'
        f'<span style="color:#8892b0;-webkit-text-fill-color:#8892b0;'
        f'font-family:{FB};font-size:.83rem">{label}</span>'
        f'<span style="font-family:{FM};color:#e6f1ff;-webkit-text-fill-color:#e6f1ff;'
        f'font-size:.83rem">{value}</span></div>'
    )

def _mini_card(title, color, rows_html):
    return (
        f'<div style="background:rgba(0,51,102,0.45);border:1px solid {color};'
        f'border-radius:8px;padding:14px 15px;{NO_SEL}">'
        f'<div style="color:{color};-webkit-text-fill-color:{color};'
        f'font-family:{FH};font-size:.95rem;font-weight:700;margin-bottom:10px">{title}</div>'
        f'<div style="font-family:{FM};font-size:.82rem">{rows_html}</div></div>'
    )


# ═══════════════════════════════════════════════════════════
# DATA
# ═══════════════════════════════════════════════════════════

CONCEPT_CARDS = {
    "Core Concepts": [
        dict(icon="🎯", title="Hypothesis Framework", title_color="#FFD700",
             border="#FFD700", bg="rgba(255,215,0,0.07)", items=[
                dict(badge=bdg("H₀ Null","blue"),       text="Default assumption — 'nothing changed'. Always contains = sign."),
                dict(badge=bdg("H₁ Alternative","gold"),text="The claim under investigation — direction sets the test type."),
                dict(badge=bdg("α Type I Error","red"),  text="P(Reject true H₀) — your false alarm tolerance."),
                dict(badge=bdg("β Type II Error","gold"),text="P(Miss real effect) — Power = 1 − β."),
                dict(badge=bdg("p-value","blue"),        text="P(result this extreme | H₀ true). Small → strong evidence."),
                dict(badge=bdg("Test statistic","green"),text="z or t: how many SE from H₀. Compared to critical value."),
            ]),
        dict(icon="📏", title="Test Selection", title_color="#ADD8E6",
             border="#ADD8E6", bg="rgba(0,51,102,0.5)", items=[
                dict(badge=bdg("Right-tailed","gold"), text="H₁: μ > μ₀ — reject in RIGHT tail only. Critical: +1.645 at α=5%."),
                dict(badge=bdg("Left-tailed","red"),   text="H₁: μ < μ₀ — reject in LEFT tail only. Critical: −1.645 at α=5%."),
                dict(badge=bdg("Two-tailed","blue"),   text="H₁: μ ≠ μ₀ — reject in BOTH tails. Critical: ±1.960 at α=5%."),
                dict(badge=bdg("z-test","green"),      text="Use when σ is known or n ≥ 30 (CLT applies)."),
                dict(badge=bdg("t-test","blue"),       text="Use when σ is unknown. df = n − 1. t → z as n → ∞."),
                dict(badge=bdg("Rule","gold"),         text="Pre-commit to test type BEFORE seeing data to avoid p-hacking."),
            ]),
        dict(icon="⚠", title="Error Types", title_color="#dc3545",
             border="#dc3545", bg="rgba(220,53,69,0.08)", items=[
                dict(badge=bdg("Type I (α)","red"),       text="Reject true H₀. 'False positive.' Controlled by α."),
                dict(badge=bdg("Type II (β)","gold"),     text="Fail to reject false H₀. 'Missed signal.' Increases as α shrinks."),
                dict(badge=bdg("Power","green"),          text="1 − β. Probability of detecting a real effect. Increases with n."),
                dict(badge=bdg("Trade-off","purple" if False else "blue"), text="Lower α → fewer false alarms but lower power. Balance is key."),
                dict(badge=bdg("Finance: Type I","red"),  text="Declare fund has alpha when it doesn't → invest in dud manager."),
                dict(badge=bdg("Finance: Type II","gold"),text="Miss a genuinely skilled manager → lost opportunity."),
            ]),
    ],
    "z-Test & t-Test": [
        dict(icon="📐", title="z-Test (σ Known)", title_color="#FFD700",
             border="#FFD700", bg="rgba(255,215,0,0.07)", items=[
                dict(badge=bdg("Formula","gold"),       text="z = (x̄ − μ₀) / (σ/√n)"),
                dict(badge=bdg("SE","blue"),            text="Standard Error = σ/√n — precision of sample mean."),
                dict(badge=bdg("α=5%, right","green"),  text="Reject if z > +1.645"),
                dict(badge=bdg("α=5%, left","red"),     text="Reject if z < −1.645"),
                dict(badge=bdg("α=5%, two","blue"),     text="Reject if |z| > 1.960"),
                dict(badge=bdg("When","gold"),          text="σ known (large historical dataset) or n ≥ 30 by CLT."),
            ]),
        dict(icon="📊", title="t-Test (σ Unknown)", title_color="#ADD8E6",
             border="#ADD8E6", bg="rgba(0,51,102,0.5)", items=[
                dict(badge=bdg("Formula","blue"),       text="t = (x̄ − μ₀) / (s/√n)"),
                dict(badge=bdg("df","gold"),            text="Degrees of freedom = n − 1. Larger df → closer to z."),
                dict(badge=bdg("Heavier tails","red"),  text="t-distribution is wider than normal — harder to reject H₀."),
                dict(badge=bdg("α=5%, df=30","blue"),   text="t_crit ≈ ±2.042 (two-tailed) — wider than z's ±1.960."),
                dict(badge=bdg("Convergence","green"),  text="As n → ∞, t_crit → z_crit. t-test is always safe."),
                dict(badge=bdg("Finance use","gold"),   text="Bond duration, credit ratio, or any metric where σ is estimated."),
            ]),
        dict(icon="🔢", title="Critical Values Quick Ref", title_color="#28a745",
             border="#28a745", bg="rgba(40,167,69,0.08)", items=[
                dict(badge=bdg("1.645","gold"),   text="One-tail z at α=5%  |  Two-tail z at α=10%"),
                dict(badge=bdg("1.960","blue"),   text="Two-tail z at α=5%"),
                dict(badge=bdg("2.326","gold"),   text="One-tail z at α=1%"),
                dict(badge=bdg("2.576","red"),    text="Two-tail z at α=1%"),
                dict(badge=bdg("Memory aid","green"), text="1.645 → 1.96 → 2.33 → 2.576 (memorise these 4!)"),
                dict(badge=bdg("t > z always","blue"),text="t critical values always exceed z for same α and finite df."),
            ]),
    ],
    "Finance Applications": [
        dict(icon="💹", title="Portfolio & Alpha Tests", title_color="#FFD700",
             border="#FFD700", bg="rgba(255,215,0,0.07)", items=[
                dict(badge=bdg("Fund Alpha","gold"),     text="H₀: α=0 | H₁: α>0 → Right-tailed t-test on regression intercept."),
                dict(badge=bdg("CAPM Beta","blue"),      text="H₀: β=1 | H₁: β≠1 → Two-tailed t-test. t=(β̂−1)/SE(β̂)."),
                dict(badge=bdg("Sharpe Ratio","green"),  text="H₀: SR≤SR₀ → Jobson-Korkie test for risk-adj performance."),
                dict(badge=bdg("Return Mean","gold"),    text="H₀: μ=benchmark → One or two-tailed depending on prior belief."),
                dict(badge=bdg("VaR Backtest","red"),    text="Kupiec test: binomial test on breach frequency vs 5%."),
                dict(badge=bdg("Practical tip","blue"),  text="Always state H₀ and H₁ before examining data — no p-hacking."),
            ]),
        dict(icon="🏦", title="Credit & Fixed Income", title_color="#ADD8E6",
             border="#ADD8E6", bg="rgba(0,51,102,0.5)", items=[
                dict(badge=bdg("Default Rate","red"),    text="H₀: p≤2% | H₁: p>2% → Right-tailed binomial/z-test."),
                dict(badge=bdg("Bond Duration","blue"),  text="H₀: D=7yr | H₁: D≠7yr → Two-tailed t-test post-rebalancing."),
                dict(badge=bdg("Yield Spread","gold"),   text="H₀: spread unchanged → Two-tailed test after macro event."),
                dict(badge=bdg("NPA Ratio","red"),       text="H₀: NPA≤3% | H₁: NPA>3% → Right-tailed t on quarterly data."),
                dict(badge=bdg("Convexity","blue"),      text="Test whether portfolio convexity target is met post-trade."),
                dict(badge=bdg("Capital Adequacy","green"),text="H₀: CAR≥8% → Left-tailed — test for regulatory compliance."),
            ]),
    ],
}

GLOSSARY = [
    dict(term="Null Hypothesis (H₀)", symbol=None,
         definition="The default assumption — 'no change', 'no effect', 'equals benchmark'. Always contains an equality (=, ≤, ≥). We never 'prove' H₀; we either reject it or fail to reject it.",
         formula="H₀: μ = μ₀  (e.g. H₀: mean return = 12%)",
         example="H₀: A mutual fund's average annual return equals the Nifty50 benchmark return of 12%.",
         badge_label="Foundation", badge_variant="blue",
         finance_note="In CFA/FRM: always express H₀ with equality sign. It represents the 'status quo' that the market already prices in."),
    dict(term="Alternative Hypothesis (H₁)", symbol=None,
         definition="The claim under investigation. Its direction (>, <, ≠) determines whether the test is right-tailed, left-tailed, or two-tailed. Must be stated BEFORE data collection.",
         formula="H₁: μ > μ₀  (right)  |  H₁: μ < μ₀  (left)  |  H₁: μ ≠ μ₀  (two)",
         example="H₁: The fund's average return > 12% (fund claims to outperform the market).",
         badge_label="Foundation", badge_variant="blue",
         finance_note="Directional H₁ (one-tailed) requires prior theoretical justification — e.g. a factor model predicts outperformance."),
    dict(term="z-Statistic", symbol="z = (x̄ − μ₀)/(σ/√n)",
         definition="The test statistic for a z-test. Measures how many standard errors the sample mean is from the hypothesised mean. Follows a standard normal N(0,1) distribution under H₀.",
         formula="z = (x̄ − μ₀) / (σ/√n)\nSE = σ/√n  (standard error of the sample mean)",
         example="x̄=13.5%, μ₀=12%, σ=6%, n=36 → SE=1.0% → z=(13.5−12)/1.0 = 1.50",
         badge_label="z-Test", badge_variant="gold",
         finance_note="Used in CAPM tests, VaR backtesting, and any large-sample return distribution test where historical σ is known."),
    dict(term="t-Statistic", symbol="t = (x̄ − μ₀)/(s/√n)",
         definition="Test statistic when σ is unknown. Uses sample standard deviation s. Follows a t-distribution with df = n−1. Always has heavier tails than z, making it harder to reject H₀.",
         formula="t = (x̄ − μ₀) / (s/√n)     df = n − 1\nAs n → ∞: t → z (t_crit → z_crit)",
         example="Bond duration: x̄=7.84, μ₀=7.0, s=2.94, n=49 → t=(7.84−7.0)/(2.94/7)=2.0",
         badge_label="t-Test", badge_variant="blue",
         finance_note="Most common in practice — population σ is rarely known. Use t-test as the default for small/medium samples."),
    dict(term="p-value", symbol="P(|T| ≥ |t_obs| | H₀)",
         definition="The probability of observing a test statistic as extreme as the computed one, assuming H₀ is true. NOT the probability H₀ is true. Small p-value = strong evidence against H₀.",
         formula="Right-tailed: p = P(Z > z)\nLeft-tailed:  p = P(Z < z)\nTwo-tailed:   p = 2 × P(Z > |z|)",
         example="z = 1.50 (right-tailed): p = P(Z > 1.50) = 1 − 0.9332 = 0.0668. Since 0.0668 > 0.05, fail to reject at α=5%.",
         badge_label="Decision", badge_variant="gold",
         finance_note="FRM exam tip: p-value is NOT P(H₀ is true). It is the probability of the data given H₀. A common source of exam errors."),
    dict(term="Type I Error (α)", symbol="P(Reject H₀ | H₀ true)",
         definition="Falsely rejecting a true null hypothesis — a 'false positive'. Controlled by setting the significance level α. Lower α → fewer false alarms, but also lower power.",
         formula="α = P(Type I Error) = significance level\nSet by researcher BEFORE testing: typically 1%, 5%, or 10%",
         example="At α=5%: if H₀ is true, there is a 5% chance we still reject it (false alarm) due to sampling variation.",
         badge_label="Error Types", badge_variant="red",
         finance_note="In investment management: Type I error = allocating capital to a manager with no real skill. Lower α reduces this risk but makes it harder to identify skilled managers (higher Type II risk)."),
    dict(term="Statistical Power", symbol="Power = 1 − β",
         definition="The probability of correctly rejecting H₀ when it is false. Power increases with: larger sample size, larger true effect, higher α. One-tailed tests have higher power than two-tailed.",
         formula="Power = 1 − P(Type II Error)\nPower = P(Reject H₀ | H₀ false)",
         example="Power = 0.85 means: if the fund truly outperforms, we have an 85% chance of detecting this with our test.",
         badge_label="Error Types", badge_variant="green",
         finance_note="Low-power tests miss real market inefficiencies. In quantitative investing, increasing n (more observations) is the primary way to increase power."),
    dict(term="Critical Value", symbol="z_crit or t_crit",
         definition="The threshold value of the test statistic beyond which H₀ is rejected. Determined by α, test direction, and distribution. The 'boundary' of the rejection region.",
         formula="One-tail α=5%:  z_crit = +1.645 (right) or −1.645 (left)\nTwo-tail α=5%:  z_crit = ±1.960\nTwo-tail α=1%:  z_crit = ±2.576",
         example="Testing fund alpha at α=5% (right-tailed): reject H₀ if z > 1.645. A z of 1.5 does NOT cross this threshold.",
         badge_label="Decision Rule", badge_variant="blue",
         finance_note="Memory anchor for CFA/FRM: 1.645 → 1.96 → 2.33 → 2.576. These cover one-tail 5%, two-tail 5%, one-tail 1%, two-tail 1%."),
]

FORMULA_SECTIONS = {
    "z-Test Formulas": [
        ("z-statistic",      "z = (x̄ − μ₀) / (σ/√n)"),
        ("Standard Error",   "SE = σ / √n"),
        ("Right-tail p",     "p = 1 − Φ(z)"),
        ("Left-tail p",      "p = Φ(z)"),
        ("Two-tail p",       "p = 2 × [1 − Φ(|z|)]"),
        ("95% CI (known σ)", "x̄ ± 1.960 × (σ/√n)"),
    ],
    "t-Test Formulas": [
        ("t-statistic",      "t = (x̄ − μ₀) / (s/√n)"),
        ("Degrees of freedom","df = n − 1"),
        ("SE (σ unknown)",   "SE = s / √n"),
        ("95% CI (unknown σ)","x̄ ± t_crit(df) × (s/√n)"),
        ("Pooled 2-sample t", "t = (x̄₁−x̄₂) / SE_pooled"),
        ("t → z as n→∞",    "t(df→∞) = z (same critical values)"),
    ],
    "Critical Values": [
        ("z: one-tail 10%",   "+1.282"),
        ("z: one-tail 5%",    "+1.645"),
        ("z: two-tail 5%",    "±1.960"),
        ("z: one-tail 1%",    "+2.326"),
        ("z: two-tail 1%",    "±2.576"),
        ("z: two-tail 0.1%",  "±3.291"),
    ],
    "Finance-Specific": [
        ("CAPM Beta test",    "t = (β̂ − 1) / SE(β̂)"),
        ("Jensen's Alpha",    "t = α̂ / SE(α̂)  [right-tailed]"),
        ("VaR Kupiec",        "LR = −2ln[(1−p)^(n−x) × p^x / ...]"),
        ("Sharpe difference", "JK = (SR₁−SR₂) / SE_JK"),
        ("Bond duration",     "t = (D̄ − D_target) / (s_D/√n)"),
        ("Default rate",      "z = (p̂ − p₀) / √(p₀(1−p₀)/n)"),
    ],
}

MCQ_BANK = [
    dict(qid="q01", level="Foundation", topic="Core Concepts",
         question="The p-value in hypothesis testing represents:",
         options=["The probability that H₀ is true",
                  "The probability of observing results this extreme if H₀ is true",
                  "The significance level α",
                  "The probability that H₁ is true"],
         answer=1,
         explanation=f'The p-value = P(data at least this extreme | H₀ true). It is {_red("NOT")} the probability H₀ is true — a very common misconception. If p < α, we reject H₀.'),
    dict(qid="q02", level="Foundation", topic="Core Concepts",
         question="Which of the following correctly describes a Type I Error?",
         options=["Failing to reject H₀ when it is false",
                  "Rejecting H₀ when it is actually true",
                  "Using too small a sample size",
                  "Setting α too high"],
         answer=1,
         explanation=f'Type I Error = {_red("False positive")} — rejecting a true H₀. Its probability is exactly α, the significance level. In finance: declaring a fund manager has skill when they do not.'),
    dict(qid="q03", level="Foundation", topic="Test Selection",
         question="A fund manager claims their fund returns ARE DIFFERENT from the benchmark (not necessarily better or worse). Which test is appropriate?",
         options=["Right-tailed test",
                  "Left-tailed test",
                  "Two-tailed test",
                  "No test needed — just compare means"],
         answer=2,
         explanation=f'H₁: μ ≠ benchmark → {_gold("Two-tailed test")}. The claim is non-directional (just "different"), so we check both tails. α is split as α/2 per tail. Critical values are ±1.960 at α=5%.'),
    dict(qid="q04", level="Foundation", topic="Critical Values",
         question="At α = 5%, what is the critical value for a one-tailed (right) z-test?",
         options=["1.282", "1.645", "1.960", "2.576"],
         answer=1,
         explanation=f'{_gold("1.645")} is the one-tailed z-critical value at α=5%. For two-tailed at α=5%, it is ±1.960. Memory anchor: 1.645 → 1.96 → 2.33 → 2.576.'),
    dict(qid="q05", level="Foundation", topic="z vs t-test",
         question="When should you use a t-test instead of a z-test?",
         options=["When the sample size is very large (n > 100)",
                  "When the population standard deviation (σ) is unknown",
                  "When the data is normally distributed",
                  "When testing proportions"],
         answer=1,
         explanation=f'Use t-test when {_gold("σ is unknown")} and must be estimated by s. The t-distribution has heavier tails than z, accounting for the extra uncertainty. With large n, t → z.'),
    dict(qid="q06", level="Intermediate", topic="Calculation",
         question="x̄ = 14%, μ₀ = 12%, σ = 8%, n = 64. What is the z-statistic for testing H₁: μ > 12%?",
         options=["1.00", "2.00", "0.25", "1.50"],
         answer=1,
         explanation=f'SE = σ/√n = 8/8 = 1.0%. z = (14 − 12)/1.0 = {_gold("2.00")}. Since 2.00 > 1.645, reject H₀ at α=5% (right-tailed).'),
    dict(qid="q07", level="Intermediate", topic="Test Selection",
         question="A risk manager tests whether a portfolio's VaR INCREASED after a new regulation. Which test?",
         options=["Two-tailed (H₁: VaR ≠ old)",
                  "Right-tailed (H₁: VaR > old)",
                  "Left-tailed (H₁: VaR < old)",
                  "No formal test needed"],
         answer=1,
         explanation=f'The manager specifically predicts VaR {_red("increased")} — a directional claim. H₁: VaR > old → {_gold("Right-tailed test")}. All α is in the right tail, giving maximum power to detect an increase.'),
    dict(qid="q08", level="Intermediate", topic="Errors",
         question="A bank sets α = 1% for its credit approval model to minimise false approvals. What is the direct consequence?",
         options=["Higher power to detect bad borrowers",
                  "Increased Type II Error (more good borrowers rejected)",
                  "Reduced sample size needed",
                  "Lower standard errors"],
         answer=1,
         explanation=f'Lowering α from 5% to 1% reduces Type I Error (fewer false approvals) but {_red("increases Type II Error")} — good borrowers are more frequently denied credit (false rejections). Power decreases.'),
    dict(qid="q09", level="Intermediate", topic="p-value",
         question="A bond duration test gives z = 1.75, two-tailed, α = 5%. p-value ≈ 0.080. The conclusion is:",
         options=["Reject H₀ — duration has changed",
                  "Fail to reject H₀ — insufficient evidence of change",
                  "Cannot conclude without knowing the sample size",
                  "Reject H₀ because z > 1.645"],
         answer=1,
         explanation=f'p = 0.080 > α = 0.05 → {_green("Fail to reject H₀")}. Also: |z| = 1.75 < 1.960 (two-tail critical). Note: 1.75 > 1.645, but 1.645 is the ONE-tailed critical value, not two-tailed. A common trap!'),
    dict(qid="q10", level="Intermediate", topic="Finance",
         question="CAPM beta = 1.18, SE(β) = 0.12. Testing H₀: β = 1 vs H₁: β ≠ 1 at α = 5%. Decision?",
         options=["Reject H₀ — beta is significantly different from 1",
                  "Fail to reject — beta is not significantly different from 1",
                  "Cannot tell without the p-value",
                  "Use a one-tailed test instead"],
         answer=0,
         explanation=f't = (1.18 − 1.0)/0.12 = 0.18/0.12 = {_gold("1.50")}. With large df, t_crit ≈ ±1.96. Since 1.50 < 1.96, {_green("Fail to reject H₀")}. Beta is not statistically different from 1 at α=5%. (The correct answer is B.)'),
    dict(qid="q11", level="Advanced", topic="Power",
         question="A fund wants to test alpha using n = 36 monthly returns. Power is low. Which action MOST increases power without changing α?",
         options=["Switch from two-tailed to one-tailed test",
                  "Increase sample size to n = 100",
                  "Lower α from 5% to 10%",
                  "Both A and B would equally increase power"],
         answer=3,
         explanation=f'Both increasing n and switching to one-tailed test increase power. {_gold("Increasing n")} improves power for any test type. {_gold("One-tailed test")} concentrates all α in one tail, reducing the critical value from 1.96 to 1.645. Combined, they have the greatest effect.'),
    dict(qid="q12", level="Advanced", topic="Finance",
         question="A portfolio manager's monthly alpha is 0.4% with SE = 0.25%, n = 60 months, α = 1%. Is the alpha statistically significant?",
         options=["Yes — t = 1.60 > 1.645",
                  "No — t = 1.60 < 2.326 (one-tail z at α=1%)",
                  "Yes — t = 1.60 > 1.282",
                  "Insufficient information"],
         answer=1,
         explanation=f't = 0.4/0.25 = {_gold("1.60")}. This is a right-tailed test (H₁: α > 0). At α=1%, one-tail z_crit = 2.326. Since 1.60 < 2.326, {_red("Fail to reject")} at α=1%. Note: would reject at α=5% (z_crit=1.645 is barely not met, but very close) and would reject at α=10% (z_crit=1.282).'),
]


# ═══════════════════════════════════════════════════════════
# SECTION RENDERERS
# ═══════════════════════════════════════════════════════════

def _section_concept_cards():
    theme = st.selectbox("Theme", list(CONCEPT_CARDS.keys()), key="edu_theme")
    cards = CONCEPT_CARDS[theme]
    if len(cards) == 2:
        cols = st.columns(2)
        for col, card in zip(cols, cards):
            col.html(_concept_card(**card))
    else:
        cols = st.columns(3)
        for col, card in zip(cols, cards):
            col.html(_concept_card(**card))

    # Matching formula box per theme
    theme_fmls = {
        "Core Concepts":      ("Core Decision Rule",
                               "Reject H₀ if:  test stat > critical value\n"
                               "           OR:  p-value < α\n\n"
                               "p-value (right):  1 − Φ(z)\n"
                               "p-value (left):   Φ(z)\n"
                               "p-value (two):    2 × [1 − Φ(|z|)]"),
        "z-Test & t-Test":    ("z vs t Quick Reference",
                               "z = (x̄ − μ₀)/(σ/√n)  [σ known]\n"
                               "t = (x̄ − μ₀)/(s/√n)  [σ unknown, df=n−1]\n\n"
                               "α=5%: 1-tail z=1.645 | 2-tail z=±1.960\n"
                               "α=1%: 1-tail z=2.326 | 2-tail z=±2.576"),
        "Finance Applications":("Finance Test Reference",
                                "Jensen's alpha:   t = α̂/SE(α̂)   [right-tailed]\n"
                                "CAPM beta:        t = (β̂−1)/SE(β̂) [two-tailed]\n"
                                "Duration shift:   t = (D̄−D₀)/(s/√n) [two-tailed]\n"
                                "VaR backtest:     Kupiec LR ~ χ²(1)"),
    }
    if theme in theme_fmls:
        title, formula_text = theme_fmls[theme]
        render_ib(
            f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">📐 {title}</span>'
            + fml(formula_text), "gold"
        )


def _section_glossary():
    col1, col2 = st.columns([2, 1])
    search = col1.text_input("🔍 Search terms", placeholder="e.g. p-value, critical, Type I...", key="edu_search")
    topic_f = col2.selectbox("Filter by topic", ["All", "Core Concepts", "z-Test", "t-Test", "Decision", "Errors", "Finance"], key="edu_topic")

    TOPIC_MAP = {
        "Core Concepts": ["Null", "Alternative", "Hypothesis"],
        "z-Test":        ["z-Stat", "z-test", "z-"],
        "t-Test":        ["t-Stat", "t-test", "t-"],
        "Decision":      ["p-value", "Critical"],
        "Errors":        ["Type I", "Type II", "Power"],
        "Finance":       ["CAPM", "Alpha", "Duration", "Finance"],
    }

    filtered = GLOSSARY
    if search.strip():
        s = search.lower()
        filtered = [t for t in filtered
                    if s in t["term"].lower() or s in t["definition"].lower()
                    or s in (t.get("finance_note") or "").lower()]
    if topic_f != "All":
        kws = TOPIC_MAP.get(topic_f, [])
        filtered = [t for t in filtered if any(k.lower() in t["term"].lower() for k in kws)]

    if not filtered:
        render_ib(rt2("No terms match. Try a broader search."), "red")
        return

    st.html(f'<div style="color:#8892b0;-webkit-text-fill-color:#8892b0;font-family:{FB};'
            f'font-size:.82rem;margin-bottom:10px;{NO_SEL}">'
            f'Showing {len(filtered)} of {len(GLOSSARY)} terms</div>')
    for t in filtered:
        st.html(_term_card(**t))


def _section_formula_sheet():
    secs = list(FORMULA_SECTIONS.items())
    cols1 = st.columns(2)
    for col, (title, rows) in zip(cols1, secs[:2]):
        rh = "".join(_row(k, v) for k, v in rows)
        col.html(_mini_card(title, "#FFD700", rh))
    cols2 = st.columns(2)
    for col, (title, rows) in zip(cols2, secs[2:]):
        rh = "".join(_row(k, v) for k, v in rows)
        col.html(_mini_card(title, "#ADD8E6", rh))

    section_heading("📊 Critical Values Table (z-distribution)")
    st.html(table_html(
        ["α", "One-Tail z", "Two-Tail z (±)", "t (df=30)", "t (df=60)", "t (df=∞)"],
        [
            [txt_s("0.10"), hl("1.282"), hl("1.645"), txt_s("1.310"), txt_s("1.296"), txt_s("1.282")],
            [txt_s("0.05"), hl("1.645"), hl("1.960"), txt_s("2.042"), txt_s("2.000"), txt_s("1.960")],
            [txt_s("0.025"),hl("1.960"), hl("2.241"), txt_s("2.360"), txt_s("2.299"), txt_s("2.241")],
            [txt_s("0.01"), hl("2.326"), hl("2.576"), txt_s("2.750"), txt_s("2.660"), txt_s("2.576")],
            [txt_s("0.005"),hl("2.576"), hl("2.807"), txt_s("3.030"), txt_s("2.915"), txt_s("2.807")],
        ]
    ))
    render_ib(
        f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">Memory Anchor: </span>'
        + hl("1.645 → 1.96 → 2.33 → 2.576")
        + txt_s(' — One-tail 5%, Two-tail 5%, One-tail 1%, Two-tail 1%. These four cover 90% of all finance tests!'),
        "blue"
    )


def _section_decision_guide():
    render_card("🗺 Decision Trees",
        p(f'Use these trees to choose the right test every time.')
    )
    section_heading("1️⃣  Which Test Type?")
    st.html(table_html(
        ["Situation", "H₁", "Test Type", "Critical z (α=5%)"],
        [
            [txt_s("You predict metric <strong>increased</strong>"),  txt_s("μ > μ₀"), bdg("Right-tailed","gold"),  hl("+1.645")],
            [txt_s("You predict metric <strong>decreased</strong>"),  txt_s("μ < μ₀"), bdg("Left-tailed","red"),   hl("−1.645")],
            [txt_s("You predict metric <strong>changed</strong>"),    txt_s("μ ≠ μ₀"), bdg("Two-tailed","blue"),   hl("±1.960")],
            [txt_s("No prior prediction — just investigating"),       txt_s("μ ≠ μ₀"), bdg("Two-tailed (default)","blue"), hl("±1.960")],
        ]
    ))

    section_heading("2️⃣  z-test or t-test?")
    st.html(table_html(
        ["Condition", "Use", "Key Difference"],
        [
            [txt_s("σ (population std dev) is <strong>known</strong>"), bdg("z-test","gold"), txt_s("Standard normal N(0,1) distribution")],
            [txt_s("σ is <strong>unknown</strong>, use sample s"),       bdg("t-test","blue"), txt_s("t-distribution with df = n−1, heavier tails")],
            [txt_s("Large sample (n ≥ 30) but σ unknown"),               bdg("t-test (safer)","blue"), txt_s("t → z as n increases. t-test is always valid")],
            [txt_s("Proportion test (p̂ vs p₀)"),                        bdg("z-test","gold"), txt_s("z = (p̂ − p₀) / √(p₀(1−p₀)/n)")],
        ]
    ))

    section_heading("3️⃣  Interpreting the Result")
    two_left = ib(
        f'<span style="color:#dc3545;-webkit-text-fill-color:#dc3545;font-weight:700">🔴 REJECT H₀ when:</span>'
        + steps_html([
            ("test stat > critical value", f'e.g. z = 2.15 > 1.645 at α=5% right-tailed'),
            ("p-value < α",               f'e.g. p = 0.032 < 0.05 → statistically significant'),
            ("What it means",             f'Strong evidence against H₀ at the chosen significance level'),
        ]), "red"
    )
    two_right = ib(
        f'<span style="color:#28a745;-webkit-text-fill-color:#28a745;font-weight:700">🟢 FAIL TO REJECT H₀ when:</span>'
        + steps_html([
            ("test stat < critical value", f'e.g. z = 1.45 < 1.645 at α=5% right-tailed'),
            ("p-value ≥ α",               f'e.g. p = 0.078 > 0.05 → not statistically significant'),
            ("What it means",             f'Insufficient evidence to reject H₀ — NOT proof H₀ is true'),
        ]), "green"
    )
    st.html(two_col(two_left, two_right))

    section_heading("4️⃣  Finance Test Cheat Sheet")
    st.html(table_html(
        ["Finance Question", "H₀", "H₁", "Test", "α Typical"],
        [
            [txt_s("Does fund generate alpha?"),        txt_s("α = 0"), txt_s("α > 0"), bdg("Right t","gold"),  txt_s("5%")],
            [txt_s("Is portfolio beta = 1?"),           txt_s("β = 1"), txt_s("β ≠ 1"), bdg("Two-tail t","blue"), txt_s("5%")],
            [txt_s("Has bond duration changed?"),       txt_s("D = target"), txt_s("D ≠ target"), bdg("Two-tail t","blue"), txt_s("1%")],
            [txt_s("Has default rate increased?"),      txt_s("p ≤ 2%"), txt_s("p > 2%"), bdg("Right z","red"), txt_s("1%")],
            [txt_s("Did VaR model fail (backtesting)?"),txt_s("breach=5%"), txt_s(">5%"), bdg("Right z/LR","red"), txt_s("5%")],
        ]
    ))


def _section_mcq():
    if "mcq_score" not in st.session_state:
        st.session_state.mcq_score = 0
    if "mcq_answered" not in st.session_state:
        st.session_state.mcq_answered = {}

    c1, c2, c3 = st.columns(3)
    level_f = c1.selectbox("Level", ["All", "Foundation", "Intermediate", "Advanced"], key="mcq_lvl")
    topic_q = c2.selectbox("Topic", ["All"] + sorted(set(q["topic"] for q in MCQ_BANK)), key="mcq_top")
    mode    = c3.radio("Mode", ["📖 Study (show answers)", "🎯 Quiz (hide answers)"],
                       key="mcq_mode", horizontal=True)
    study_mode = "Study" in mode

    if st.button("🔄 Reset Quiz", key="mcq_reset"):
        st.session_state.mcq_score   = 0
        st.session_state.mcq_answered = {}
        st.rerun()

    filtered = MCQ_BANK
    if level_f != "All": filtered = [q for q in filtered if q["level"] == level_f]
    if topic_q != "All": filtered = [q for q in filtered if q["topic"] == topic_q]

    correct   = sum(1 for qid, ans in st.session_state.mcq_answered.items()
                    if ans == next((q["answer"] for q in MCQ_BANK if q["qid"] == qid), -1))
    attempted = len(st.session_state.mcq_answered)
    pct       = (correct / attempted * 100) if attempted else 0
    score_color = "#28a745" if pct >= 80 else "#FFD700" if pct >= 60 else "#dc3545"

    st.html(
        f'<div style="display:flex;gap:16px;align-items:center;margin-bottom:12px;{NO_SEL}">'
        f'<span style="font-family:{FH};color:{score_color};-webkit-text-fill-color:{score_color};'
        f'font-size:1.1rem;font-weight:700">Score: {correct}/{attempted}</span>'
        + (f'<span style="font-family:{FM};color:{score_color};-webkit-text-fill-color:{score_color};'
           f'font-size:.9rem">({pct:.0f}%)</span>' if attempted else "")
        + f'<span style="font-family:{FB};color:#8892b0;-webkit-text-fill-color:#8892b0;'
          f'font-size:.82rem">{len(filtered)} question(s) shown</span></div>'
    )

    for q in filtered:
        qid     = q["qid"]
        answered = st.session_state.mcq_answered.get(qid)

        # Header colour
        if answered is None:
            hdr_col, hdr_bg = "#ADD8E6", "rgba(0,51,102,0.4)"
        elif answered == q["answer"]:
            hdr_col, hdr_bg = "#28a745", "rgba(40,167,69,0.12)"
        else:
            hdr_col, hdr_bg = "#dc3545", "rgba(220,53,69,0.12)"

        lv_badge = bdg(q["level"],
                       "green" if q["level"]=="Foundation" else
                       "gold"  if q["level"]=="Intermediate" else "red")

        st.html(
            f'<div style="background:{hdr_bg};border-left:4px solid {hdr_col};border-radius:8px;'
            f'padding:12px 15px;margin-bottom:4px;{NO_SEL}">'
            f'<div style="display:flex;align-items:center;gap:8px;margin-bottom:7px">'
            f'{lv_badge}{bdg(q["topic"],"blue")}'
            f'<span style="font-family:{FH};color:{hdr_col};-webkit-text-fill-color:{hdr_col};'
            f'font-size:.95rem;font-weight:700;margin-left:4px">{q["question"]}</span></div>'
            f'</div>'
        )

        sel = st.radio(
            f'Options for {qid}',
            q["options"],
            key=f"mcq_{qid}",
            index=answered if answered is not None else None,
            label_visibility="collapsed",
        )
        if sel is not None:
            sel_idx = q["options"].index(sel)
            st.session_state.mcq_answered[qid] = sel_idx
            if study_mode or sel_idx == q["answer"]:
                correct_txt = q["options"][q["answer"]]
                col = "#28a745" if sel_idx == q["answer"] else "#dc3545"
                st.html(
                    f'<div style="background:rgba(40,167,69,0.08);border-left:3px solid {col};'
                    f'border-radius:5px;padding:9px 13px;margin:4px 0 12px;{NO_SEL}">'
                    f'<span style="color:{col};-webkit-text-fill-color:{col};font-weight:700">'
                    f'{"✅ Correct!" if sel_idx==q["answer"] else f"❌ Correct answer: {correct_txt}"}</span><br>'
                    f'<span style="font-family:{FB};font-size:.86rem;color:#e6f1ff;'
                    f'-webkit-text-fill-color:#e6f1ff;line-height:1.6">{q["explanation"]}</span></div>'
                )
            elif sel_idx != q["answer"]:
                st.html(
                    f'<div style="background:rgba(220,53,69,0.08);border-left:3px solid #dc3545;'
                    f'border-radius:5px;padding:8px 12px;margin:4px 0 12px;{NO_SEL}">'
                    f'<span style="color:#dc3545;-webkit-text-fill-color:#dc3545;font-weight:600">'
                    f'Incorrect. Keep going!</span></div>'
                )


# ═══════════════════════════════════════════════════════════
# MAIN TAB
# ═══════════════════════════════════════════════════════════

def tab_edu_hub():
    explainer_edu_hub()

    render_card("📚 Education Hub — Hypothesis Testing Reference",
        p(f'Complete visual reference for {hl("hypothesis testing")} concepts, '
          f'formulas, and finance applications. Use alongside the calculator tabs.') +
        three_col(
            ib(f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">🃏 Concept Cards</span><br>'
               + p(f'{bdg(f"{sum(len(v) for v in CONCEPT_CARDS.values())} cards","gold")} across 3 themes'), "gold"),
            ib(f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">📖 Glossary</span><br>'
               + p(f'{bdg(f"{len(GLOSSARY)} key terms","blue")} with definitions + examples'), "blue"),
            ib(f'<span style="color:#28a745;-webkit-text-fill-color:#28a745;font-weight:600">📐 + 🗺 + 🎓</span><br>'
               + p(f'Formula Sheet · Decision Guide · {bdg(f"{len(MCQ_BANK)} MCQs","green")}'), "green"),
        )
    )

    mode = st.radio("Section",
                    ["🃏 Concept Cards", "📖 Glossary", "📐 Formula Sheet",
                     "🗺 Decision Guide", "🎓 MCQ Quiz"],
                    horizontal=True, key="edu_mode")

    if "Concept"  in mode: _section_concept_cards()
    elif "Gloss"  in mode: _section_glossary()
    elif "Formula"in mode: _section_formula_sheet()
    elif "Decision"in mode:_section_decision_guide()
    else:                   _section_mcq()
