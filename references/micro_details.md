# Publication Figure Reverse Engineering: The Micro-Detail Blueprint (顶刊论文图片像素级复刻细节手册)

This document provides the exact mathematical proportions, geometric tolerances, and typography weights required to 1:1 recreate the visual aesthetic of figures published in *Nature*, *Cell*, *NEJM*, and *The Lancet* (and as produced by GraphPad Prism).

---

## 1. Spine & Tick Anatomy (坐标轴与刻度微观几何)

| Visual Element | Top-Tier Publication Standard | Implementation Parameter |
| :--- | :--- | :--- |
| **Spine Stroke Width** | Solid **`1.0 pt`** black (`#000000`). Never 0.5–0.8pt (looks flimsy). | `ax.spines['left'].set_linewidth(1.0)` |
| **Active Spines** | **L-Frame Only**: Left (Y) and Bottom (X). Top and Right permanently OFF. | `sns.despine(ax=ax, top=True, right=True)` |
| **Tick Direction** | Strictly **Outward** (`direction='out'`). Inward ticks obscure near-axis points. | `ax.tick_params(direction='out')` |
| **Tick Stroke Width** | Strictly **`1.0 pt`** (must equal spine width, 1:1:1 rule). | `ax.tick_params(width=1.0)` |
| **Major Tick Length** | Exactly **`3.5 ~ 4.5 pt`**. Shorter looks stubby; longer looks like grid lines. | `ax.tick_params(length=4.0)` |
| **Tick Label Padding** | Exactly **`3.0 ~ 4.0 pt`**. Breathing space between tick tip and numeral. | `ax.tick_params(pad=3.5)` |
| **Floating Origin Gap** | Y-axis minimum is offset by **1–2 pt** from X-axis to avoid pinching data points. | `ax.set_ylim(bottom=0)` with slight margins |

---

## 2. Bar, Error Bar & Scatter Anatomy (柱体、误差棒与散点微观几何)

| Visual Element | Top-Tier Publication Standard | Implementation Parameter |
| :--- | :--- | :--- |
| **Bar Width Ratio** | Occupies **55% ~ 62%** of categorical slot width. | `width = 0.58` (in categorical step of 1.0) |
| **Bar Border Stroke** | Exactly **`1.2 pt`** (must equal or slightly exceed spine width). | `ax.bar(..., edgecolor=color, linewidth=1.2)` |
| **Bar Fill Modes** | **Mode A (Open/Outline)**: 100% white fill + bold border (*Cell/Nature* style).<br>**Mode B (Tinted)**: 30%–35% alpha fill + 100% solid border (*NEJM/Prism* style). | Mode A: `color='#FFFFFF', edgecolor=c`<br>Mode B: `color=c, alpha=0.35, edgecolor=c` |
| **Error Bar Direction** | **Upward-Only** for zero-baseline bar graphs. Prevents cluttering bar interior. | `yerr=[[0]*n, sem_values]` |
| **Error Bar Stroke** | Exactly **`1.2 pt`** (strictly matching bar border thickness). | `elinewidth=1.2, capthick=1.2` |
| **Error Bar Cap Width** | Exactly **30% ~ 40%** of bar width (`4.0 ~ 5.0 pt`). | `capsize=4.5` |
| **Replicate Dot Size** | **`30 ~ 40 pt²`** (diameter ~5.5–6.5 pt). Visible without swallowing neighboring points. | `s=36` |
| **Replicate Dot Halo** | **The Halo Detail**: Outer stroke **`0.7 pt`** dark border (`#111111`), inner fill `alpha=0.85`. Allows overlapping replicates to show distinct crescent boundaries. | `edgecolors='#111111', linewidths=0.7, alpha=0.85` |
| **Jitter Constraint** | Horizontal dispersion strictly clamped to **$\pm 8\%$** of bar width. Never spills over bar edges. | `np.random.normal(0, 0.035)` |

---

## 3. Significance Bracket Anatomy (显著性桥架微观几何)

| Visual Element | Top-Tier Publication Standard | Implementation Parameter |
| :--- | :--- | :--- |
| **Hook Drop (Tip)** | Vertical down-hooks extend downward by exactly **1.8% ~ 2.2%** of total Y-span. | `tip = y_span * 0.02` |
| **Bracket Stroke Width** | Exactly **`0.8 ~ 1.0 pt`** solid black. | `lw=0.9, color='#000000'` |
| **Data Clearance Gap** | Horizontal beam hovers **3.0% ~ 5.0%** of Y-span above highest replicate/error bar. | `y_beam = max(data) + y_span * 0.035` |
| **Asterisk Position** | Centered **1.5 ~ 2.0 pt** above beam. Never floating high; never intersecting beam. | `y_text = y_beam + y_span * 0.015` |
| **Asterisk Typography** | Bold, tight tracking: `***` in **Arial Bold `8.0 ~ 8.5 pt`**. | `fontsize=8.5, fontweight='bold'` |
| **Multi-Tier Stepping** | When stacking brackets (A vs B, B vs C, A vs C), vertical step is **6.0% ~ 8.0%** of Y-span. | `y_tier2 = y_tier1 + y_span * 0.07` |

---

## 4. Typography & Spacing Hierarchy (字体层级与间距)

| Hierarchy Level | Font Family | Size (pt) | Weight | Case / Style |
| :--- | :--- | :--- | :--- | :--- |
| **Panel Labels (A, B, C)** | Arial / Helvetica | **`8.5 ~ 9.0 pt`** | **Bold** | Uppercase, anchored at `xycoords='axes fraction' (0, 1)`, offset `(-24, 8)` pt |
| **Axis Titles** | Arial / Helvetica | **`7.5 ~ 8.0 pt`** | **Bold** | Title Case (e.g., `Relative mRNA Expression`) |
| **Category Tick Labels** | Arial / Helvetica | **`7.0 ~ 7.5 pt`** | **Bold** / Medium | Plain text, no italics unless gene symbol (`*p53*`) |
| **Numeric Ticks & Units** | Arial / Helvetica | **`6.5 ~ 7.0 pt`** | Regular | Standard numerals |
| **Significance Notations** | Arial / Helvetica | **`7.5 ~ 8.5 pt`** | **Bold** | `*`, `**`, `***`, or `ns` |
| **Absolute Minimum** | Any element | **$\ge 5.0\text{ pt}$** | — | **Zero tolerance** for text below 5.0 pt |

---

## 5. Multi-Panel Composite Gutters (多子图拼版间距)

* **Horizontal Gutter**: Exactly **`0.45 ~ 0.55 in`** between subplots. Guarantees that multi-line rotated Y-axis labels of the right subplot never collide with the right edge of the left subplot.
* **Vertical Gutter**: Exactly **`0.40 ~ 0.50 in`** between rows. Leaves ample room for row 2 panel letters without intersecting row 1 X-axis category labels.
