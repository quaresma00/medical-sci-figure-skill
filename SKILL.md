---
name: medical-sci-figure-skill
description: Universal medical SCI paper figure generation guidelines, decision grammar, and automated QA engine for AI agents, synthesized from SciencePlots, scipilot-figure-skill, ggsci, and adjustText.
---

# Medical SCI Figure Skill: Universal Rules & QA Grammar

An authoritative, synthesis-driven figure generation specification and quality-assurance engine for AI agents (Claude Code, Antigravity, Cursor, Codex). Engineered by synthesizing best-in-class open-source projects (**`SciencePlots`**, **`scipilot-figure-skill`**, **`ggsci`**, **`adjustText`**), adapted specifically for medical top tiers (*NEJM*, *The Lancet*, *JAMA*, *Nature Medicine*, *Cell Press*).

---

## 1. Universal Chart Selection Decision Tree (选型决策语法)

Before writing any plotting code, determine chart type strictly by **data topology + clinical argument**:

| Data Shape | Clinical / Biological Intent | Mandatory Chart Type | STRICTLY FORBIDDEN |
| :--- | :--- | :--- | :--- |
| **1 Continuous + 1 Categorical ($n < 10$)** (qPCR, WB, ELISA, small mice cohorts) | Compare biomarker/mRNA expression in small replicates | **Superimposed Dot-Bar (Open/Tint Bar + SEM + Individual Dots)** or **Dot Plot with Mean line** | **Pure Dynamite Bar (no dots) OR Boxplot for $n \le 5$ (meaningless quartiles)** |
| **1 Continuous + 1 Categorical ($n \ge 10$)** (Clinical cohorts, single-cell) | Compare distribution across clinical groups | **Boxplot / Violin with quartile whiskers** | Standalone bar chart |
| **Time-to-event (Survival)** | Compare survival trajectories (PFS / OS) | **Step curve + synchronized Risk Table** | Line chart without risk numbers |
| **Odds / Hazard Ratios across Subgroups** | Clinical trial subgroup or Meta-analysis | **Forest plot (log scale, vertical null line)** | Grouped bar chart |
| **2 Continuous variables** | Correlation / Biomarker titration curve | **Scatter plot + regression fit + exact $r/p$** | Connected line plot (unless time series) |
| **High-dimensional Gene / Feature Matrix** | Expression clustering / Immune profiling | **Heatmap (z-score, viridis/cividis, colorbar)** | Rainbow/Jet colormaps |
| **Proportions / Compositions** | Patient cohort baseline demographics | **Stacked horizontal bar or Treemap** | **Pie charts / 3D charts** |

---

## 2. The 8 Universal Medical Figure Laws (八大底层戒律)

### Law 1: Zero-Internal-Text Law (图文严格分离)
* **Axiom**: Figure canvases are reserved solely for data and structural coordinates.
* **Negative Constraints**:
  - NEVER call `ax.set_title()`, `plt.title()`, or `fig.suptitle()`.
  - NEVER insert interpretive commentary or explanatory text boxes inside subplots.
  - Deliver all titles and descriptions as external text in the Figure Legend (`Figure 1. [Title]. (A) ... (B) ...`).

### Law 2: Physical Scale Invariance Law (印刷尺寸锁定)
* **Axiom**: Plots must be initialized at their true print dimensions, never resized after rendering.
* **Standard Dimensions**:
  - **Single Column**: `85 mm` (`3.35 in`), aspect ratio `1:0.75` ~ `1:0.85`
  - **1.5 Column**: `120 mm` (`4.72 in`)
  - **Double Column**: `175 mm` (`6.89 in`), max height `225 mm` (`8.8 in`)
* **Strict Point Hierarchy**:
  - Panel labels (A, B, C): `8 ~ 9 pt` Bold
  - Axis titles: `7 ~ 8 pt` Bold
  - Tick labels & Legends: `6 ~ 7 pt` Regular
  - **Absolute Floor**: NEVER allow any text below `5.0 pt`.

### Law 3: Anti-Collision & Outside Legend Law (空间防重叠与外挂图例)
* **Axiom**: Visual data ink must never be occluded by typography.
* **Requirements**:
  - Place legends outside plot boundaries (`bbox_to_anchor=(1.02, 1.0), loc='upper left'`) with `frameon=False`.
  - Dense text annotations (gene names, outlier tags) MUST use force-directed repulsion (`adjustText`).
  - If X-axis categorical labels collide, rotate $30^\circ \sim 45^\circ$ with `ha='right'` or switch to horizontal bars.

### Law 4: Panel Co-Alignment Law (子图几何绝对对齐)
* **Axiom**: Subplot letters must align on universal grid lines regardless of Y-axis tick label widths.
* **Mathematical Anchor**:
  Anchor panel labels at `axes fraction (0, 1)` with fixed offset points:
  ```python
  ax.annotate('A', xy=(0, 1), xycoords='axes fraction',
              xytext=(-24, 8), textcoords='offset points',
              fontsize=9, fontweight='bold', va='bottom', ha='left',
              annotation_clip=False)
  ```

### Law 5: Data Transparency Law (数据诚实与反遮掩)
* **Axiom**: Every individual biological replicate must be verifiable.
* **Requirements**:
  - Always show individual data points when $n < 10$.
  - Bar chart baselines must start at 0. Never truncate Y-axis to artificially inflate differences.

### Law 6: Statistical Semantic Completeness Law (统计表达完备)
* **Axiom**: No ambiguous error bars or bare asterisks.
* **Requirements**:
  - Always declare in caption whether error bars represent Mean ± SD, Mean ± SEM, or Median (IQR).
  - Report exact $p$-values (e.g. $p = 0.024$, or $p < 0.001$), never bare asterisks.
  - State the exact test (e.g., Two-tailed Mann-Whitney U test, One-way ANOVA with Tukey's post-hoc test).

### Law 7: Accessibility & Redundant Encoding Law (色盲友好与双重编码)
* **Axiom**: Figures must remain 100% decipherable under grayscale printing and by color-blind reviewers.
* **Requirements**:
  - NEVER use red vs. green pairings. Use official NEJM, Lancet, JAMA, or Okabe-Ito palettes.
  - Apply **redundant encoding**: differentiate groups by both color AND marker shape (`o`, `s`, `^`) or line style (solid, dashed).

### Law 8: Vector Asset & Embedded Font Law (矢量资产与字体内嵌)
* **Axiom**: Typography must remain editable text streams in vector PDF/EPS outputs.
* **Requirements**:
  - Hardcode `matplotlib.rcParams['pdf.fonttype'] = 42` and `ps.fonttype = 42` (TrueType embedded).
  - Hardcode `matplotlib.rcParams['axes.unicode_minus'] = False` (avoids broken minus glyphs).
  - Export vector PDF as primary submission asset.

---

## 3. Official Journal Palette Standards (from `ggsci`)

```python
# NEJM (New England Journal of Medicine)
PALETTE_NEJM = ["#BC3C29", "#0072B5", "#E18727", "#20854E", "#7876B1", "#6F99AD", "#FFDC91", "#EE4C97"]

# The Lancet
PALETTE_LANCET = ["#00468B", "#ED0000", "#42B540", "#0099B4", "#925E9F", "#FDAF91", "#AD002A", "#ADB6B6"]

# JAMA (Journal of the American Medical Association)
PALETTE_JAMA = ["#374E55", "#DF8F44", "#00A1D5", "#B24745", "#79AF97", "#6A6599", "#80796B"]

# JCO (Journal of Clinical Oncology)
PALETTE_JCO = ["#002855", "#B8860B", "#8B0000", "#2E8B57", "#4682B4", "#4B0082"]
```

---

## 4. Automated Figure QA Loop (质检闭环)

Every AI plotting workflow must execute the layout audit before saving final figures:

```python
from medfigure import set_medical_style, add_panel_labels, audit_medical_figure
import matplotlib.pyplot as plt

# 1. Setup style
set_medical_style(journal="nejm")

# 2. Render plot at exact physical dimensions
fig, axes = plt.subplots(1, 2, figsize=(6.89, 2.8), dpi=300)

# ... [Perform plotting] ...

# 3. Align panel labels
add_panel_labels(fig, axes, style="upper")

# 4. Automated Medical QA Audit (intercepts internal titles, overlaps, clipping, and tiny fonts)
passed = audit_medical_figure(fig)
if passed:
    fig.savefig("final_figure.pdf", bbox_inches='tight')
```
