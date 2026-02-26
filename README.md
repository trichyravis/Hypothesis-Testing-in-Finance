# Hypothesis Testing in Finance — Streamlit App
### The Mountain Path – World of Finance | Prof. V. Ravichandran

## Overview
Interactive Streamlit application covering One-Tailed and Two-Tailed Hypothesis Tests
with real-world finance and risk management examples.

## Features
- **6 Interactive Tabs**: Overview, One-Tailed, Two-Tailed, Comparison, Finance Examples, Python Code
- **Live calculators** with adjustable parameters (α, sample mean, std dev, n)
- **Interactive matplotlib plots** with rejection regions rendered in Mountain Path dark theme
- **Critical value explorer** with dynamic chart updates
- **Live Python code runner** for instant z-test computation
- **Comprehensive critical values reference table**

## Project Structure
```
hypothesis_testing_app/
├── app.py           # Main entry point
├── styles.py        # CSS injection (Mountain Path design theme)
├── tabs.py          # All 6 tab content functions + shared plot helper
├── charts.py        # SVG distribution diagrams (inline, no image files)
├── components.py    # Reusable HTML helper functions
└── requirements.txt
```

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Design System
| Color | Hex | Usage |
|---|---|---|
| Dark Blue | `#003366` | Primary brand, tab active state |
| Mid Blue | `#004d80` | Hover states, chart fills |
| Gold | `#FFD700` | Headings, highlights, key values |
| Card BG | `#112240` | Card backgrounds |
| App BG | `#0a1628` | Base dark background |
| Light Blue | `#ADD8E6` | Secondary headings, curve strokes |
| Green | `#28a745` | Fail to reject, success states |
| Red | `#dc3545` | Reject, rejection regions |

**Fonts**: Playfair Display (headings) + Source Sans Pro (body) + JetBrains Mono (code/formulas)

## Author
**Prof. V. Ravichandran**
28+ Years Corporate Finance & Banking Experience | 10+ Years Academic Excellence

- [LinkedIn](https://www.linkedin.com/in/trichyravis)
- [GitHub](https://github.com/trichyravis)
