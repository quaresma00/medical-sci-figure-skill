---
name: medical-sci-figure-skill
description: Universal medical SCI paper figure generation guidelines, complete figure atlas (17 chart archetypes), and automated QA engine for AI agents (NEJM, Lancet, JAMA, Nature Medicine standards).
---

# Complete Medical SCI Figure Atlas & Universal Rule System

An exhaustive, publication-grade specification and quality-assurance system for AI coding agents (Claude Code, Antigravity, Cursor, Codex). Synthesizes and standardizes the entire landscape of medical scientific publishing (**`SciencePlots`**, **`scipilot-figure-skill`**, **`ggsci`**, **`adjustText`**, and **`CSdaw/ggprism`**) across all high-impact clinical and biomedical journals (*NEJM*, *The Lancet*, *JAMA*, *Nature Medicine*, *Cell Press*).

---

## 1. Complete Medical SCI Figure Atlas (全图表类型全景图鉴与规范)

Every figure in a medical SCI manuscript belongs to one of the following 5 domains (17 archetypes). AI must strictly adhere to the archetype specifications:

### Domain 1: Continuous Data & Group Comparisons (组间实验与差异对比)

#### 1.1 Superimposed Dot-Bar Plot (小样本带散点柱状图)
* **Target Experiments**: RT-qPCR, Western Blot optical density, ELISA, small animal tumor burden ($n = 3 \sim 8$).
* **Standard Visuals**: 
  - Open bar (white fill + 1.2pt colored outline) OR tinted bar (0.35 alpha soft fill + solid border).
  - Single upward error bar representing **SEM** (Standard Error of Mean), with wide cap (`capsize=4.5pt`).
  - Individual biological replicate dots ($n=3 \sim 8$) overlaid near bar tops with thin black outline (`lw=0.7pt`).
* **Forbidden**: Standalone solid bars without points (Dynamite plot); Boxplots for $n \le 5$ (statistically meaningless quartiles).

#### 1.2 Boxplot with Jittered Scatter (中大样本箱线散点图)
* **Target Experiments**: Clinical cohort biomarkers, patient serum cytokines, cell culture assays ($n \ge 10$).
* **Standard Visuals**:
  - Clean box showing Median (center thick line) and Interquartile Range (IQR, 25th-75th percentiles).
  - Whiskers extending to 1.5× IQR (Tukey style) or Min-to-Max.
  - Overlaid individual jittered scatter points (`alpha=0.7`, `size=20~30`).
* **Forbidden**: Hiding median; omitting individual points when $n < 30$.

#### 1.3 Violin & Raincloud Plot (小提琴云雨图)
* **Target Experiments**: Flow cytometry Mean Fluorescence Intensity (MFI), single-cell expression distribution ($n \ge 30$).
* **Standard Visuals**: Half-violin kernel density estimation (KDE) + interior mini-boxplot + bottom jitter scatter (raindrops).

#### 1.4 Paired Dot-Line Plot (配对前后连线散点图)
* **Target Experiments**: Before vs. After treatment in the same patient (Paired $t$-test / Wilcoxon signed-rank).
* **Standard Visuals**: Paired dots connected by thin directional lines (`lw=0.8pt, alpha=0.6`), visually highlighting trajectory.

---

### Domain 2: Survival & Longitudinal Trajectories (生存分析与时间追踪)

#### 2.1 Kaplan-Meier Curve with Synchronized Risk Table (带风险表的 KM 曲线)
* **Target Experiments**: Clinical trials, oncology survival analysis (OS, PFS, RFS, DFS).
* **Mandatory Elements**:
  - Step curves with vertical tick marks for censored patients.
  - **Synchronized "Number at Risk" Table** perfectly aligned below the time axis.
  - Median survival times with 95% CI.
  - Hazard Ratio (HR) with 95% CI and Log-rank test $p$-value.
* **Forbidden**: KM curve without a Number at Risk table; omitting censoring marks.

#### 2.2 Longitudinal Tumor Growth / Trajectory Plot (纵向病程/肿瘤生长曲线)
* **Target Experiments**: Preclinical in vivo drug efficacy, animal weight tracking.
* **Standard Visuals**: Time points on X-axis; connected points with SEM error bars; treatment initiation marked with a downward arrow ($\downarrow$).

---

### Domain 3: Clinical Trials & Evidence-Based Medicine (临床试验与循证医学)

#### 3.1 CONSORT / PRISMA Flowchart (入组与筛选流程图)
* **Target Experiments**: Randomized controlled trials (RCTs), Meta-analyses, cohort studies.
* **Standard Visuals**: Rectangular boxes with crisp connectors; precise accounting of screened, excluded (with explicit reasons), randomized, lost to follow-up, and final analyzed (ITT vs. PP).

#### 3.2 Forest Plot for Subgroup & Meta-Analysis (亚组与 Meta 森林图)
* **Target Experiments**: Hazard ratios/Odds ratios across patient strata (age, sex, biomarker status).
* **Standard Visuals**:
  - Vertical null-effect line at 1.0 (for HR/RR/OR) or 0.0 (for difference metrics).
  - Square point estimates with area proportional to study weight; horizontal error bars for 95% CI.
  - Overall summary diamond at the bottom.
  - Explicit direction labels: "$\leftarrow$ Favors Treatment" vs "Favors Control $\rightarrow$".

#### 3.3 Receiver Operating Characteristic (ROC) & Precision-Recall Curve (诊断模型 ROC)
* **Target Experiments**: Diagnostic biomarker validation, machine learning clinical risk prediction.
* **Standard Visuals**: True Positive Rate vs. False Positive Rate; diagonal dashed reference line ($45^\circ$); legend displaying `AUC = 0.XX (95% CI: 0.XX–0.XX), p < 0.001`.

#### 3.4 Nomogram & Calibration Curve (列线图与校准曲线)
* **Target Experiments**: Clinical prognostic scoring systems.
* **Standard Visuals**: Point assignment axis (0–100) for clinical covariates; total score mapped to survival probability. Calibration curves must include the $45^\circ$ ideal line and bootstrap-corrected curve.

---

### Domain 4: High-Throughput Omics & Bioinformatics (高通量组学与生信图)

#### 4.1 Volcano Plot for Differential Expression (差异表达火山图)
* **Target Experiments**: RNA-seq, proteomics, single-cell differential analysis.
* **Standard Visuals**:
  - X-axis: $\log_2(\text{Fold Change})$; Y-axis: $-\log_{10}(P\text{-value})$.
  - Dashed cutoff thresholds (e.g., $|\log_2\text{FC}| > 1$, $P\text{-adj} < 0.05$).
  - Statistically significant upregulated (Red/NEJM Brick) and downregulated (Blue/NEJM Navy) points.
  - Key hub genes annotated using force-directed repulsion (`adjustText`).

#### 4.2 Clustered Heatmap (层次聚类热图)
* **Target Experiments**: Multi-gene expression profiling, patient clustering.
* **Standard Visuals**: Row and column hierarchical dendrograms; z-score standardized values; perceptually uniform colormap (`viridis`, `magma`, or zero-centered `RdBu_r`); top clinical metadata annotation bars; independent colorbar.

#### 4.3 Dimension Reduction Scatter (PCA, UMAP, t-SNE 降维散点图)
* **Target Experiments**: Single-cell transcriptomics (scRNA-seq), CyTOF, bulk PCA.
* **Standard Visuals**: Equal aspect ratio; categorical clusters encoded by colorblind-safe palettes; point size adjusted to avoid occlusion (`s=5~15, alpha=0.6~0.8`).

#### 4.4 Functional Enrichment Bubble Plot (GO / KEGG 富集气泡图)
* **Target Experiments**: Pathway enrichment (Gene Ontology, KEGG, Reactome).
* **Standard Visuals**: Y-axis: Pathway description; X-axis: Gene Ratio or Enrichment Factor; Bubble size: Gene Count; Bubble color: $-\log_{10}(P\text{-adj})$ or FDR.

#### 4.5 GWAS Manhattan Plot (全基因组关联分析曼哈顿图)
* **Target Experiments**: Single nucleotide polymorphism (SNP) disease association.
* **Standard Visuals**: Chromosomes ordered 1–22 along X-axis with alternating contrasting colors; horizontal red dashed genome-wide significance line at $P = 5 \times 10^{-8}$.

---

### Domain 5: Molecular Blots & Histopathology (分子条带与切片图)

#### 5.1 Cropped Western Blot Panel (Western Blot 条带图)
* **Standard Visuals**: Uniformly cropped rectangles; molecular weight ladder markers indicated in kDa on the left; internal control (e.g. $\beta$-actin, GAPDH) placed directly below target protein bands; linear contrast without saturating background.

#### 5.2 Histopathology & Immunofluorescence (IHC / IF 显微摄影切片图)
* **Mandatory Requirements**:
  - Physical scale bar (e.g., $50\,\mu\text{m}$, $100\,\mu\text{m}$) MUST be physically overlaid in the lower-right corner.
  - STRICTLY FORBIDDEN to simply write "400×" in the caption.
  - Staining channels, dyes, and target antibodies explicitly labeled (e.g. DAPI: blue; CD8: green).
  - Insets/enlargements must be outlined with a colored rectangle in the main overview image.

---

## 2. Universal Publishing Rules (跨所有图表的通用戒律)

### 2.1 The 8 Universal Laws
1. **Zero-Internal-Text Law**: Absolutely NO titles (`ax.set_title` BANNED) and NO narrative textboxes inside any figure. Captions belong exclusively in the external Figure Legend.
2. **Physical Scale Invariance Law**: Initialize plots at true publication width: Single column `85 mm` (`3.35 in`), Double column `175 mm` (`6.89 in`). Text MUST strictly adhere to 5.0–9.0 pt.
3. **Anti-Collision & Outside Legend Law**: Legends outside the plot canvas (`bbox_to_anchor=(1.02, 1.0)`). Labels repelled via `adjustText`.
4. **Panel Co-Alignment Law**: Panel letters (A, B, C, D) anchored at `xy=(0, 1), xycoords='axes fraction'` with fixed offset points.
5. **Data Transparency Law**: Show individual data points when $n < 10$. Bar baselines must start at 0.
6. **Statistical Completeness Law**: Declare SD vs. SEM vs. 95% CI. Display exact $p$-values and test names.
7. **Accessibility & Redundant Encoding Law**: NO red-green pairings. Dual-encode via color + marker/line style.
8. **Vector Asset & Embedded Font Law**: Hardcode `pdf.fonttype = 42` (TrueType embedded) and `axes.unicode_minus = False`. Export vector PDF.

---

## 3. Aesthetic Presets: GraphPad Prism & Medical Top Tiers

```python
from medfigure import set_prism_style, set_medical_style

# 1. GraphPad Prism / ggprism Style (for wet-lab biology: qPCR, WB, ELISA, animal studies)
set_prism_style(palette="floral", base_size=8.0, spine_width=1.0)

# 2. NEJM / Lancet Top-Tier Clinical Style (for clinical cohorts, survival, trials)
set_medical_style(journal="nejm", base_size=7.5)
```
