# The 8 Universal Laws of Medical SCI Figures (医学 SCI 作图八大底层戒律)

These 8 axioms are cross-cutting invariants that apply to **every single figure** regardless of data type. Violating any of these laws results in immediate technical review rejection or reviewer revisions.

---

### Law 1: Zero-Internal-Text Law (图文严格分离律)
* **Axiom**: The graphical canvas is reserved purely for visual data marks and necessary coordinates.
* **Negative Constraints**:
  - NEVER call `ax.set_title()`, `plt.title()`, or `fig.suptitle()`.
  - NEVER embed narrative paragraphs or interpretive summaries inside text boxes on the canvas.
  - All conclusions, cohort definitions, and experimental contexts belong exclusively in the external Figure Legend (Caption).

### Law 2: Physical Scale Invariance Law (物理尺寸锁定律)
* **Axiom**: Figures must be created at their exact physical publication dimensions in inches/mm.
* **Standards**:
  - **Single Column**: `85 mm` (`3.35 in`), aspect ratio `1:0.75` ~ `1:0.85`
  - **1.5 Column**: `120 mm` (`4.72 in`)
  - **Double Column (Full Page Width)**: `175 mm` (`6.89 in`), max height $\le 225\text{ mm}$
* **Font Hierarchy**:
  - Panel labels: `8.5 ~ 9.0 pt` Bold
  - Axis titles: `7.5 ~ 8.0 pt` Bold
  - Tick labels & legends: `6.5 ~ 7.0 pt` Regular
  - **Absolute Floor**: Zero text elements below `5.0 pt`.

### Law 3: Anti-Collision & Outside Legend Law (空间防碰撞律)
* **Axiom**: Data marks must never be occluded by typography or legends.
* **Standards**:
  - Legends must be placed outside the bounding box (`bbox_to_anchor=(1.02, 1.0)`) or in a verified empty corner with `frameon=False`.
  - Dense text annotations (gene names, outlier tags) must use force-directed repulsion (`adjustText`).
  - If X-axis labels collide, rotate $30^\circ \sim 45^\circ$ with `ha='right'` or switch to horizontal bars.

### Law 4: Panel Co-Alignment Law (子图几何绝对对齐律)
* **Axiom**: Subplot letters must align to global physical grid lines regardless of Y-axis label widths.
* **Standards**:
  - Always anchor at `axes fraction (0, 1)` with fixed points offset:
    `ax.annotate('A', xy=(0, 1), xycoords='axes fraction', xytext=(-24, 8), textcoords='offset points', fontsize=9, fontweight='bold', va='bottom', ha='left')`

### Law 5: Data Transparency Law (数据诚实与反遮掩律)
* **Axiom**: Every individual biological replicate must be verifiable.
* **Standards**:
  - When $n < 10$, standalone bar charts (Dynamite plots) are forbidden. Overlay individual replicate scatter dots.
  - Bar chart baselines must start at 0. Never truncate Y-axis on bar plots to artificially inflate differences.

### Law 6: Statistical Semantic Completeness Law (统计语义完备律)
* **Axiom**: No ambiguous error bars or bare asterisks.
* **Standards**:
  - Figure captions must explicitly declare whether error bars represent Mean ± SD, Mean ± SEM, or Median (IQR).
  - Exact $p$-values must be given in brackets or clearly mapped to asterisk thresholds (`*** p < 0.001`).
  - Statistical tests must be named (e.g., Two-tailed unpaired Student's $t$-test, One-way ANOVA with Tukey's post-hoc).

### Law 7: Accessibility & Redundant Encoding Law (无障碍双重编码律)
* **Axiom**: Figures must remain 100% readable by color-blind reviewers and in grayscale print.
* **Standards**:
  - No red-green pairings. Use NEJM, Lancet, JAMA, or Okabe-Ito palettes.
  - Use dual encoding: differentiate groups by both color AND marker shape (`o`, `s`, `^`) or line style (solid, dashed).

### Law 8: Vector Asset & Embedded Font Law (矢量资产与字体内嵌律)
* **Axiom**: Typography must remain vector text streams in submitted PDF/EPS assets.
* **Standards**:
  - Hardcode `matplotlib.rcParams['pdf.fonttype'] = 42` and `ps.fonttype = 42` (TrueType embedded).
  - Hardcode `matplotlib.rcParams['axes.unicode_minus'] = False` (prevents broken minus glyphs).
  - Always output vector PDF as the primary submission asset.
