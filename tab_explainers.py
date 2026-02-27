"""
tab_explainers.py
Layman-friendly "How This Tab Works" explainer boxes for every tab.
Call render_explainer_XXX() at the top of each tab function.
"""
import streamlit as st
from components import FH, FB, FM, NO_SEL, ib, bdg, hl, gt, rt2, p, txt_s

# ── colour helpers ────────────────────────────────────────────────
def _gold(t):  return f'<span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:600">{t}</span>'
def _blue(t):  return f'<span style="color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;font-weight:600">{t}</span>'
def _green(t): return f'<span style="color:#28a745;-webkit-text-fill-color:#28a745;font-weight:600">{t}</span>'
def _red(t):   return f'<span style="color:#dc3545;-webkit-text-fill-color:#dc3545;font-weight:600">{t}</span>'
def _mono(t):  return f'<span style="font-family:{FM};color:#64ffda;-webkit-text-fill-color:#64ffda">{t}</span>'


def _explainer(steps, tip, variant="blue"):
    """
    Render a "How This Tab Works" box.
    steps = list of (emoji, bold_title, plain_description)
    tip   = Plain English one-liner shown in gold
    """
    rows = "".join(
        f'<div style="display:flex;align-items:flex-start;gap:10px;'
        f'margin-bottom:10px;{NO_SEL}">'
        f'<span style="font-size:1.05rem;min-width:24px">{icon}</span>'
        f'<div style="font-family:{FB};font-size:.88rem;color:#e6f1ff;'
        f'-webkit-text-fill-color:#e6f1ff;line-height:1.65">'
        f'<span style="font-weight:700;color:#ADD8E6;-webkit-text-fill-color:#ADD8E6">{title}:</span> {desc}'
        f'</div></div>'
        for icon, title, desc in steps
    )
    tip_box = (
        f'<div style="margin-top:12px;padding:9px 13px;'
        f'background:rgba(255,215,0,0.08);border-left:3px solid #FFD700;'
        f'border-radius:5px;font-family:{FB};font-size:.86rem;'
        f'color:#e6f1ff;-webkit-text-fill-color:#e6f1ff;line-height:1.6;{NO_SEL}">'
        f'💡 <span style="color:#FFD700;-webkit-text-fill-color:#FFD700;font-weight:700">'
        f'Plain English: </span>{tip}</div>'
    )
    header = (
        f'<div style="font-family:{FH};font-size:.92rem;font-weight:700;'
        f'color:#ADD8E6;-webkit-text-fill-color:#ADD8E6;'
        f'margin-bottom:11px;letter-spacing:.3px;{NO_SEL}">🗺 How This Tab Works</div>'
    )
    st.html(ib(header + rows + tip_box, variant))


# ═══════════════════════════════════════════════════════════
# TAB-SPECIFIC EXPLAINERS
# ═══════════════════════════════════════════════════════════

def explainer_overview():
    _explainer([
        ("🎯", "The Core Idea",
         f"Hypothesis testing is a formal way of asking: {_gold('Could this result have happened by chance?')} "
         f"You start with a baseline assumption (H₀ = nothing interesting happened) and use sample data "
         f"to decide whether to reject that assumption."),
        ("⚖", "H₀ vs H₁",
         f"Think of it like a courtroom. {_blue('H₀ is innocent until proven guilty.')} "
         f"H₁ is the prosecution's claim — that something has changed. "
         f"You need strong evidence (low p-value) to overturn the default assumption."),
        ("📏", "The Decision Rule",
         f"Calculate a {_gold('z-statistic')} — how many standard deviations your sample result is "
         f"from what H₀ predicted. If that number falls in the {_red('rejection zone')}, reject H₀. "
         f"If not, you simply lack enough evidence to reject it."),
        ("🔢", "Key Numbers to Remember",
         f"At {_gold('α = 5%')}, the magic numbers are {_mono('1.645')} (one-tailed) and "
         f"{_mono('1.960')} (two-tailed). These are your thresholds — exceed them and the result is "
         f"statistically significant."),
    ],
    tip="Hypothesis testing is asking: 'Is this result real, or just lucky sampling?' "
        "The p-value tells you the probability the result occurred by chance. Below 5%? Probably real.")


def explainer_one_tailed():
    _explainer([
        ("➡", "When to Use One-Tailed",
         f"Use a one-tailed test when you already have a {_gold('prior belief about direction')} — "
         f"for example, you believe a fund OUTPERFORMS (not just 'differs'). "
         f"You only care about evidence in one direction."),
        ("⚡", "The Power Advantage",
         f"Because all the rejection probability (α) is concentrated in {_gold('ONE tail')}, "
         f"the critical value is SMALLER (1.645 instead of 1.960 at α=5%). "
         f"This makes it {_green('easier to reject H₀')} when the true effect is in your predicted direction."),
        ("🔢", "The Formula",
         f"Compute {_mono('z = (x̄ − μ₀) / (σ/√n)')}. This is just: "
         f"how far is my sample mean from the hypothesised mean, measured in standard errors? "
         f"A larger z means stronger evidence against H₀."),
        ("⚠", "The Risk",
         f"If you guess the wrong direction, you {_red('cannot detect')} the true effect. "
         f"The direction MUST be committed to before seeing the data — otherwise results are invalid."),
    ],
    tip="Right-tailed = 'I think it went UP.' Left-tailed = 'I think it went DOWN.' "
        "Choose based on theory, not data. The smaller critical value gives you more power to detect real effects.")


def explainer_two_tailed():
    _explainer([
        ("↔", "When to Use Two-Tailed",
         f"Use two-tailed when you only know {_gold('something changed')} but not which direction. "
         f"Example: 'Did the new trading system change our VaR?' — it could go up or down."),
        ("✂", "Splitting Alpha",
         f"Two-tailed tests divide α equally across {_gold('both tails')} (α/2 = 2.5% each at α=5%). "
         f"This shifts the critical value from 1.645 to {_red('1.960')} — "
         f"a higher bar to clear, making the test more conservative."),
        ("📊", "p-value Calculation",
         f"The two-tailed p-value is {_mono('2 × P(Z > |z|)')} — you double it because "
         f"an extreme result in either direction counts as evidence against H₀. "
         f"This is why the same z-statistic gives a larger p-value in a two-tailed test."),
        ("🏦", "Finance Context",
         f"Two-tailed tests suit {_blue('neutrality checks')}: "
         f"'Is this portfolio beta still 1.0?' or 'Has bond duration drifted from target?' "
         f"You do not predict direction — you check for any drift."),
    ],
    tip="Two-tailed = 'I don't care which way it moved, I just want to know IF it moved.' "
        "More conservative (harder to reject), but safer — you won't miss an unexpected reversal.")


def explainer_comparison():
    _explainer([
        ("⚖", "The Core Trade-off",
         f"One-tailed tests have {_green('more power')} (easier to detect real effects) "
         f"but only work if you are sure about direction. "
         f"Two-tailed tests are {_blue('safer and more defensible')} but need stronger evidence to reject H₀."),
        ("📌", "Type I vs Type II Errors",
         f"{_red('Type I Error (α)')} = False Alarm — you reject H₀ when it is actually true. "
         f"Controlled by your significance level. "
         f"{_gold('Type II Error (β)')} = Missed Signal — you fail to reject a false H₀. "
         f"Power = 1 − β is the probability of correctly detecting a real effect."),
        ("🔭", "Critical Value Explorer",
         f"The interactive explorer at the bottom lets you change α and see how the "
         f"{_gold('rejection region')} shifts. Smaller α → more extreme critical values → "
         f"harder to reject H₀ → lower Type I Error but higher Type II Error."),
        ("💡", "Decision Rule",
         f"When in doubt: {_gold('use two-tailed')}. It is the default in academic research. "
         f"Use one-tailed only when strong theoretical reasons justify the directional prediction."),
    ],
    tip="Think of it like car safety: one-tailed = airbag that only deploys in head-on crashes (more effective but misses side impacts). "
        "Two-tailed = airbag that deploys in any crash (safer, catches everything).")


def explainer_finance():
    _explainer([
        ("💹", "Finance Hypothesis Tests",
         f"Every row in the table is a real question a portfolio manager or risk officer asks. "
         f"The math is identical each time — only the {_gold('context, H₀, and variable')} change. "
         f"Mastering the framework means you can test any claim with data."),
        ("🏦", "The Solved Example — Bond Duration",
         f"A bond portfolio manager set a {_gold('target modified duration of 7 years')}. "
         f"After restructuring 49 bonds, the average came out at 7.84 years. "
         f"Is that drift statistically significant, or just normal sampling variation? "
         f"The t-test answers this question formally."),
        ("📋", "Why t-test here?",
         f"We use a {_blue('t-test (not z-test)')} because σ (population std dev) is unknown — "
         f"we only have sample standard deviation s. "
         f"The t-distribution has heavier tails than normal, making it harder to reject H₀, "
         f"which is appropriate when we have less certainty."),
        ("🎯", "Reading the Output",
         f"The {_gold('t-statistic')} shows how many standard errors the sample mean is from H₀. "
         f"Compare it to the {_gold('critical value')} for your chosen α. "
         f"The {_gold('p-value')} gives the exact probability — below 1%? Very strong evidence of drift."),
    ],
    tip="Each finance example follows the same 5-step script: state H₀ and H₁, compute the test statistic, "
        "find the critical value, compare them, and draw a conclusion. "
        "The only thing that changes is what you are testing.")


def explainer_non_finance():
    _explainer([
        ("🌍", "Why Non-Finance Examples?",
         f"Hypothesis testing is a {_gold('universal framework')} — the same z-test and t-test "
         f"that tests fund alpha also tests whether a new drug works, whether exam scores improved, "
         f"or whether a factory's output quality changed. Same math, different data."),
        ("🔬", "How Each Example Works",
         f"Each case study follows the same structure: {_gold('real-world scenario')} → "
         f"{_blue('null and alternative hypotheses')} → test statistic calculation → "
         f"decision at chosen significance level. The interactive sliders let you change "
         f"the inputs and see how the conclusion shifts."),
        ("📊", "Reading the Results",
         f"The {_gold('z or t statistic')} tells you: in units of standard errors, "
         f"how far is my sample result from what H₀ predicted? "
         f"The {_gold('p-value')} is the probability this happened by chance. "
         f"Below α? The result is {_green('statistically significant')}."),
        ("🎓", "Learning Transfer",
         f"Once you understand the mechanics here, {_blue('every finance test becomes intuitive')}. "
         f"CAPM beta test, Sharpe ratio test, VaR backtest — they are all just "
         f"instances of the same framework with domain-specific variables."),
    ],
    tip="Think of these as 'hypothesis testing in everyday life.' "
        "Did the new fertiliser increase crop yield? Did the teaching method improve scores? "
        "The logic is identical to testing whether a fund manager has genuine skill.")


def explainer_edu_hub():
    _explainer([
        ("🃏", "Concept Cards",
         f"Visual badge-style reference cards grouped by topic: "
         f"{_gold('Core Concepts')}, {_gold('Test Selection')}, {_gold('Error Types')}, "
         f"{_gold('Finance Applications')}. Each card shows the key idea, formula, and context side-by-side. "
         f"Great for quick review before exams."),
        ("📖", "Glossary",
         f"Searchable definitions for every key term — from {_gold('p-value')} to "
         f"{_gold('Type II Error')} to {_gold('Statistical Power')}. "
         f"Each entry has: plain-English definition, formula, worked example, and finance application."),
        ("📐", "Formula Sheet",
         f"All critical formulas in one compact reference: z-test, t-test, p-value formulas, "
         f"critical values table. Designed for quick lookup during problem-solving or revision."),
        ("🗺", "Decision Guide",
         f"Answers the most common exam questions: {_gold('Which test?')} "
         f"{_gold('One-tailed or two-tailed?')} {_gold('z or t?')} "
         f"Structured as decision trees and comparison tables — practical, not theoretical."),
        ("🎓", "MCQ Quiz",
         f"Test your understanding with questions from Foundation to Advanced level, "
         f"covering concepts, calculations, and interpretation. "
         f"Immediate feedback with full explanations."),
    ],
    tip="Start with Concept Cards for a visual overview. Use the Glossary when you hit an unfamiliar term. "
        "Run the MCQ Quiz to confirm you can apply the concepts under pressure.")


def explainer_python():
    _explainer([
        ("📦", "What the Code Does",
         f"Four ready-to-run Python snippets covering the {_gold('complete z-test and t-test workflow')}: "
         f"computing the test statistic, finding critical values, calculating p-values, "
         f"and printing a clear decision. Copy-paste into any Jupyter notebook."),
        ("🔢", "The z_test Function",
         f"The main function takes: sample mean, population mean, std dev, n, α, and tail direction. "
         f"It handles {_gold('all three tail types')} (right, left, two-tailed) automatically. "
         f"Returns the z-statistic, p-value, and a True/False reject decision."),
        ("🤖", "Live Code Runner",
         f"The interactive section at the bottom lets you {_gold('run a live z-test')} with "
         f"your own numbers and instantly see the result plotted on a distribution chart. "
         f"This is exactly the computation that happens inside the other tabs' calculators."),
        ("📋", "Critical Values Table",
         f"The reference table at the bottom shows {_gold('z and t critical values')} for "
         f"α = 10%, 5%, 2.5%, 1%, 0.5% — both one-tailed and two-tailed. "
         f"The memory anchor {_mono('1.645 → 1.96 → 2.33 → 2.576')} covers 90% of all finance tests."),
    ],
    tip="Start with the z_test function — it handles everything in one call. "
        "Change the 'tail' argument to 'right', 'left', or 'two' to match your hypothesis. "
        "The Live Code Runner lets you verify any calculation from the other tabs instantly.")
