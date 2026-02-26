"""
charts.py — SVG distribution charts for hypothesis testing visualizations
All charts rendered as inline SVG via st.markdown for pixel-perfect styling.
"""


def normal_curve_overview() -> str:
    return """
<svg width="100%" viewBox="0 0 680 160" style="max-width:680px;display:block;margin:16px auto">
  <defs>
    <linearGradient id="ng0" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   style="stop-color:#003366;stop-opacity:.2"/>
      <stop offset="50%"  style="stop-color:#004d80;stop-opacity:.8"/>
      <stop offset="100%" style="stop-color:#003366;stop-opacity:.2"/>
    </linearGradient>
  </defs>
  <path d="M25,140 Q70,140 100,132 Q145,114 180,80 Q215,44 248,22 Q278,8 340,8
           Q402,8 432,22 Q465,44 500,80 Q535,114 580,132 Q610,140 655,140Z"
        fill="url(#ng0)" stroke="#ADD8E6" stroke-width="2"/>
  <line x1="340" y1="14" x2="340" y2="128" stroke="#FFD700" stroke-width="1.5" stroke-dasharray="4"/>
  <text x="340" y="6"   fill="#FFD700"  font-size="11" text-anchor="middle" font-family="JetBrains Mono">μ (Mean)</text>
  <text x="340" y="152" fill="#ADD8E6"  font-size="10" text-anchor="middle" font-family="Source Sans Pro">Sampling Distribution of Test Statistic under H₀</text>
  <text x="248" y="152" fill="#8892b0"  font-size="9"  text-anchor="middle">−2σ</text>
  <text x="432" y="152" fill="#8892b0"  font-size="9"  text-anchor="middle">+2σ</text>
  <line x1="248" y1="128" x2="248" y2="136" stroke="#8892b0" stroke-width="1"/>
  <line x1="432" y1="128" x2="432" y2="136" stroke="#8892b0" stroke-width="1"/>
  <text x="148" y="152" fill="#8892b0" font-size="9" text-anchor="middle">−3σ</text>
  <text x="532" y="152" fill="#8892b0" font-size="9" text-anchor="middle">+3σ</text>
</svg>"""


def right_tailed_chart() -> str:
    return """
<svg width="100%" viewBox="0 0 310 175" style="max-width:310px;display:block;margin:8px auto">
  <defs>
    <linearGradient id="rg1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   style="stop-color:#003366;stop-opacity:.4"/>
      <stop offset="75%"  style="stop-color:#004d80;stop-opacity:.65"/>
      <stop offset="100%" style="stop-color:#dc3545;stop-opacity:.7"/>
    </linearGradient>
  </defs>
  <path d="M8,148 Q22,147 38,140 Q62,126 88,92 Q110,62 128,42
           Q140,28 155,28 Q170,28 182,36 Q198,50 215,74
           Q235,108 255,132 Q268,148 300,148Z"
        fill="url(#rg1)" stroke="#ADD8E6" stroke-width="1.5"/>
  <path d="M235,108 Q255,132 268,148 Q283,152 300,148 L300,148 L235,148Z"
        fill="rgba(220,53,69,.65)" stroke="#dc3545" stroke-width="2"/>
  <line x1="235" y1="108" x2="235" y2="152" stroke="#dc3545" stroke-width="2" stroke-dasharray="4"/>
  <text x="235" y="166" fill="#dc3545" font-size="10" text-anchor="middle" font-family="JetBrains Mono">z = +1.645</text>
  <text x="270"  y="138"  fill="#FFD700"  font-size="9"  font-family="Source Sans Pro">α=5%</text>
  <text x="130" y="165" fill="#8892b0" font-size="9" font-family="Source Sans Pro">Fail to Reject H₀</text>
  <text x="265" y="124" fill="#dc3545" font-size="15">✗</text>
  <text x="155" y="174" fill="#ADD8E6" font-size="9" text-anchor="middle" font-family="Source Sans Pro">H₁: μ &gt; μ₀ | Right-Tailed</text>
</svg>"""


def left_tailed_chart() -> str:
    return """
<svg width="100%" viewBox="0 0 310 175" style="max-width:310px;display:block;margin:8px auto">
  <defs>
    <linearGradient id="lg1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   style="stop-color:#dc3545;stop-opacity:.7"/>
      <stop offset="25%"  style="stop-color:#004d80;stop-opacity:.65"/>
      <stop offset="100%" style="stop-color:#003366;stop-opacity:.4"/>
    </linearGradient>
  </defs>
  <path d="M8,148 Q40,147 52,132 Q72,108 90,74 Q107,50 123,36
           Q135,28 150,28 Q165,28 177,36 Q192,48 210,74
           Q228,100 248,124 Q265,142 300,148Z"
        fill="url(#lg1)" stroke="#ADD8E6" stroke-width="1.5"/>
  <path d="M8,148 L68,148 L68,108 Q52,132 40,147 Q24,152 8,148Z"
        fill="rgba(220,53,69,.65)" stroke="#dc3545" stroke-width="2"/>
  <line x1="68" y1="108" x2="68" y2="152" stroke="#dc3545" stroke-width="2" stroke-dasharray="4"/>
  <text x="68" y="166" fill="#dc3545" font-size="10" text-anchor="middle" font-family="JetBrains Mono">z = −1.645</text>
  <text x="32" y="138" fill="#FFD700" font-size="9" font-family="Source Sans Pro">α=5%</text>
  <text x="185" y="165" fill="#8892b0" font-size="9" font-family="Source Sans Pro">Fail to Reject H₀</text>
  <text x="38"  y="124"  fill="#dc3545" font-size="15">✗</text>
  <text x="155" y="174" fill="#ADD8E6" font-size="9" text-anchor="middle" font-family="Source Sans Pro">H₁: μ &lt; μ₀ | Left-Tailed</text>
</svg>"""


def two_tailed_chart() -> str:
    return """
<svg width="100%" viewBox="0 0 660 190" style="max-width:660px;display:block;margin:16px auto">
  <defs>
    <linearGradient id="tg1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   style="stop-color:#dc3545;stop-opacity:.7"/>
      <stop offset="15%"  style="stop-color:#003366;stop-opacity:.5"/>
      <stop offset="50%"  style="stop-color:#004d80;stop-opacity:.8"/>
      <stop offset="85%"  style="stop-color:#003366;stop-opacity:.5"/>
      <stop offset="100%" style="stop-color:#dc3545;stop-opacity:.7"/>
    </linearGradient>
  </defs>
  <path d="M16,158 Q40,156 58,148 Q84,132 112,96 Q142,58 168,36
           Q192,20 330,20 Q468,20 492,36
           Q518,58 548,96 Q576,132 602,148 Q620,156 644,158Z"
        fill="url(#tg1)" stroke="#ADD8E6" stroke-width="2"/>
  <!-- Left rejection region -->
  <path d="M16,158 L82,158 L82,132 Q58,148 40,156 Q26,160 16,158Z"
        fill="rgba(220,53,69,.65)" stroke="#dc3545" stroke-width="2"/>
  <!-- Right rejection region -->
  <path d="M578,132 Q602,148 620,156 Q634,160 644,158 L644,158 L578,158Z"
        fill="rgba(220,53,69,.65)" stroke="#dc3545" stroke-width="2"/>
  <line x1="82"  y1="132" x2="82"  y2="162" stroke="#dc3545" stroke-width="2" stroke-dasharray="5"/>
  <line x1="578" y1="132" x2="578" y2="162" stroke="#dc3545" stroke-width="2" stroke-dasharray="5"/>
  <line x1="330" y1="26"  x2="330" y2="162" stroke="#FFD700" stroke-width="1.5" stroke-dasharray="4"/>
  <text x="46"  y="150" fill="#FFD700" font-size="9" font-family="Source Sans Pro">α/2=2.5%</text>
  <text x="614" y="150" fill="#FFD700" font-size="9" font-family="Source Sans Pro">α/2=2.5%</text>
  <text x="82"  y="178" fill="#dc3545" font-size="10" text-anchor="middle" font-family="JetBrains Mono">−1.960</text>
  <text x="578" y="178" fill="#dc3545" font-size="10" text-anchor="middle" font-family="JetBrains Mono">+1.960</text>
  <text x="330" y="13"  fill="#8892b0" font-size="10" text-anchor="middle" font-family="Source Sans Pro">H₀ Acceptance Region</text>
  <text x="330" y="186" fill="#ADD8E6" font-size="10" text-anchor="middle" font-family="Source Sans Pro">Two-Tailed Test (α=5%) — Rejection in BOTH Tails</text>
  <text x="46"  y="142" fill="#dc3545" font-size="14">✗</text>
  <text x="612" y="142" fill="#dc3545" font-size="14">✗</text>
  <text x="330" y="78"  fill="#28a745" font-size="10" text-anchor="middle" font-family="Source Sans Pro">Fail to Reject H₀</text>
</svg>"""


def comparison_chart() -> str:
    return """
<svg width="100%" viewBox="0 0 680 202" style="max-width:680px;display:block;margin:12px auto">
  <!-- Left panel: One-tailed -->
  <rect x="4" y="4" width="318" height="188" rx="8" fill="rgba(0,51,102,.3)" stroke="#004d80" stroke-width="1.5"/>
  <text x="163" y="22" fill="#FFD700" font-size="12" text-anchor="middle" font-family="Playfair Display,serif">One-Tailed (Right) α=5%</text>
  <path d="M18,164 Q32,163 46,155 Q68,140 92,106 Q114,74 128,54
           Q140,38 158,38 Q176,38 188,46 Q206,60 222,88
           Q242,122 258,144 Q270,160 300,164Z"
        fill="rgba(0,77,128,.5)" stroke="#ADD8E6" stroke-width="1.5"/>
  <path d="M242,122 Q258,144 270,160 Q280,165 300,164 L300,164 L242,164Z"
        fill="rgba(220,53,69,.65)" stroke="#dc3545" stroke-width="1.5"/>
  <line x1="242" y1="122" x2="242" y2="168" stroke="#dc3545" stroke-width="2" stroke-dasharray="4"/>
  <text x="242" y="182" fill="#dc3545" font-size="9" text-anchor="middle" font-family="JetBrains Mono">+1.645</text>
  <text x="274" y="154" fill="#FFD700" font-size="8">5%</text>
  <text x="163" y="196" fill="#8892b0" font-size="9" text-anchor="middle" font-family="Source Sans Pro">All α in ONE tail → Higher Power</text>

  <!-- Right panel: Two-tailed -->
  <rect x="362" y="4" width="318" height="188" rx="8" fill="rgba(0,51,102,.3)" stroke="#004d80" stroke-width="1.5"/>
  <text x="521" y="22" fill="#FFD700" font-size="12" text-anchor="middle" font-family="Playfair Display,serif">Two-Tailed α=5%</text>
  <path d="M376,164 Q390,163 404,155 Q426,140 450,106 Q472,74 486,54
           Q498,38 516,38 Q534,38 546,46 Q564,60 580,88
           Q600,122 616,144 Q628,160 658,164Z"
        fill="rgba(0,77,128,.5)" stroke="#ADD8E6" stroke-width="1.5"/>
  <path d="M376,164 L424,164 L424,140 Q406,155 390,163 Q378,167 376,164Z"
        fill="rgba(220,53,69,.65)" stroke="#dc3545" stroke-width="1.5"/>
  <path d="M600,122 Q616,144 628,160 Q638,165 658,164 L658,164 L600,164Z"
        fill="rgba(220,53,69,.65)" stroke="#dc3545" stroke-width="1.5"/>
  <line x1="424" y1="140" x2="424" y2="168" stroke="#dc3545" stroke-width="2" stroke-dasharray="4"/>
  <line x1="600" y1="122" x2="600" y2="168" stroke="#dc3545" stroke-width="2" stroke-dasharray="4"/>
  <text x="424" y="182" fill="#dc3545" font-size="9" text-anchor="middle" font-family="JetBrains Mono">−1.96</text>
  <text x="600" y="182" fill="#dc3545" font-size="9" text-anchor="middle" font-family="JetBrains Mono">+1.96</text>
  <text x="521" y="196" fill="#8892b0" font-size="9" text-anchor="middle" font-family="Source Sans Pro">α split → More Conservative</text>
</svg>"""
