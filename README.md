# Medical SCI Figure Toolkit & Skill (`medfigure`)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-brightgreen.svg)](https://python.org)
[![Based on](https://img.shields.io/badge/synthesized%20from-SciencePlots%20%7C%20scipilot%20%7C%20ggsci-blueviolet.svg)](https://github.com/quaresma00/medical-sci-figure-skill)

A universal figure generation constraint system, Python toolkit, and automated QA engine engineered to eliminate figure-related rejections in high-impact medical journals (*NEJM*, *The Lancet*, *JAMA*, *Nature Medicine*, *BMJ*, *Cell Press*).

---

## 🔬 Proven Foundations: Standing on the Shoulders of Giants

Rather than inventing rules in isolation, `medfigure` is synthesized from and extends several established, high-star open-source standards:

1. **`garrettj403/SciencePlots` (4.5k+ ⭐)**: Adopted core publication-grade spine ratios, outward tick geometry, and sans-serif mathematical text settings (`mathtext.fontset = 'stixsans'`).
2. **`Haojae/scipilot-figure-skill` (SciPilot)**: Re-engineered the post-render Visual QA pipeline (`_draw_and_collect_glyph_warnings`, collision detection, and window extent clipping audits) and the reading-order panel alignment algorithm.
3. **`nanxstats/ggsci` (1.8k+ ⭐)**: Integrated reverse-engineered, authentic color palettes from *NEJM*, *The Lancet*, *JAMA*, and *JCO*.
4. **`Phlya/adjustText` (2.5k+ ⭐)**: Integrated force-directed repulsion algorithms to automatically eliminate overlapping text labels.

---

## 📐 The 8 Universal Laws for Medical SCI Figures

| Universal Law | The Rejection Hazard It Solves | The Absolute Constraint |
| :--- | :--- | :--- |
| **1. Zero-Internal-Text** | AI dashboard titles & narrative essays | `ax.set_title()` and canvas textboxes are STRICTLY BANNED. Captions go outside. |
| **2. Physical Scale Invariance** | Microscopic fonts when figures are scaled in Word/LaTeX | Lock `figsize` to exact column widths (85mm single / 175mm double). All text 5–9 pt. |
| **3. Anti-Collision & Outside Legend** | Legend/labels occluding data curves and points | Legends placed outside (`bbox_to_anchor`). Overlapping text repelled via `adjustText`. |
| **4. Panel Co-Alignment** | Drifting panel labels (A/B/C/D) due to variable Y-tick widths | Subplot anchors at `axes fraction (0, 1)` + fixed points offset. |
| **5. Data Transparency** | Hiding distributions with dynamite bars ($n < 10$) | Mandatory individual replicate overlay (jitter/stripplot) + boxplots. Y-axis starts at 0. |
| **6. Statistical Completeness** | Ambiguous error bars & bare asterisks (`*`) | Must declare SD/SEM/CI, exact $p$-values ($p = 0.024$), and test names. |
| **7. Accessibility & Redundancy** | Reviewers with color vision deficiency (CVD) | No red-green pairs. Dual encoding (color + marker/linestyle). |
| **8. Vector & Embedded Fonts** | Editorial PDF compilation failures & missing glyphs | `pdf.fonttype = 42` (TrueType), `axes.unicode_minus = False`, vector PDF export. |

---

## 💻 Quick Start

### Installation

```bash
git clone https://github.com/quaresma00/medical-sci-figure-skill.git
cd medical-sci-figure-skill
pip install -e .
```

### Publication-Grade Script with Built-in Medical QA Audit

```python
import matplotlib.pyplot as plt
import numpy as np
from medfigure import set_medical_style, add_panel_labels, create_outside_legend, audit_medical_figure, PALETTE_NEJM

# 1. Apply NEJM publication preset
set_medical_style(journal="nejm")

# 2. Set exact double-column physical dimensions: 175mm -> 6.89 in
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.89, 2.8), dpi=300)

# Panel A: Progression trajectory
t = np.linspace(0, 12, 13)
ax1.plot(t, np.exp(-0.15 * t), label="Control", color=PALETTE_NEJM[1], lw=1.2)
ax1.plot(t, np.exp(-0.06 * t), label="Targeted Inhibitor", color=PALETTE_NEJM[0], lw=1.2, ls="--")
ax1.set_xlabel("Time (Months)")
ax1.set_ylabel("Progression-Free Probability")
create_outside_legend(ax1)

# Panel B: Biomarker comparison (n=8 per group, transparent box + individual scatter)
np.random.seed(42)
ctrl_data = np.random.normal(10, 1.5, 8)
treat_data = np.random.normal(15, 2.0, 8)
ax2.boxplot([ctrl_data, treat_data], positions=[0, 1], widths=0.4,
            boxprops=dict(color='#333333'), medianprops=dict(color='#BC3C29', lw=1.2))
ax2.scatter([0]*8 + np.random.normal(0, 0.03, 8), ctrl_data, color=PALETTE_NEJM[1], s=25, alpha=0.8)
ax2.scatter([1]*8 + np.random.normal(0, 0.03, 8), treat_data, color=PALETTE_NEJM[0], s=25, alpha=0.8)
ax2.set_xticks([0, 1])
ax2.set_xticklabels(["Vehicle", "Inhibitor"])
ax2.set_ylabel("Serum Cytokine Level (pg/mL)")

# 3. Automatically align Panel letters (A, B) across axes
add_panel_labels(fig, [ax1, ax2], style="upper")

# 4. Run automated Medical Quality Audit
audit_passed = audit_medical_figure(fig)

fig.savefig("publication_figure.pdf", bbox_inches='tight')
```

---

## 🤖 Direct Agent Integration

To force any AI assistant (Claude Code, Antigravity, Cursor, Codex) to plot under these zero-revision rules, provide [`SKILL.md`](SKILL.md) as its system skill.

---

## 📜 License & Acknowledgements

MIT License.
Special thanks to the authors and maintainers of `SciencePlots`, `scipilot-figure-skill`, `ggsci`, and `adjustText`.
