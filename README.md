# Medical SCI Figure Skill & Toolkit (`medfigure`)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-brightgreen.svg)](https://python.org)
[![Aesthetic Standard](https://img.shields.io/badge/standard-GraphPad%20Prism%20%7C%20NEJM%20%7C%20Lancet-blueviolet.svg)](https://github.com/quaresma00/medical-sci-figure-skill)

An exhaustive, publication-grade figure generation constraint system, Python toolkit, and automated QA engine engineered to **eliminate figure-related rejections and achieve 1:1 publication-grade reverse engineering** in high-impact medical journals (*NEJM*, *The Lancet*, *JAMA*, *Nature Medicine*, *Cell Press*).

---

## 🏛️ Comprehensive Repository Structure (仓库全局架构)

```text
medical-sci-figure-skill/
├── SKILL.md                          # 供 AI Agent 直接读取的规范总纲 (包含决策语法与 17 种图元定义)
├── README.md                         # 本说明文件
├── pyproject.toml                    # 构建与打包规范 (medfigure v2.1.0)
├── .gitignore                        # 干净的 Git 过滤配置
├── LICENSE                           # MIT 开源许可证
│
├── references/                       # 核心规范与逆向细节库
│   ├── figure_atlas.md               # 5 大医学领域、17 种标准图元全景图鉴与规范
│   ├── micro_details.md              # 顶刊图片像素级复刻细节手册 (线宽1:1:1、刻度、同心圆散点、挂钩)
│   └── universal_laws.md             # 跨图表通用的八大底层戒律与防退修红线
│
├── medfigure/                        # Python 核心工具库
│   ├── __init__.py                   # 模块顶层快捷导出
│   ├── prism.py                      # 逆向 GraphPad Prism / ggprism 的视觉主题与官方调色板
│   ├── style.py                      # NEJM, Lancet, JAMA 临床顶刊出版级预设与调色板
│   ├── layout.py                     # 子图拓扑排序、像素级 A/B/C/D 对齐、外挂图例
│   ├── annotation.py                 # 基于 adjustText 的防重叠文字避让与显著性连线
│   ├── qa.py                         # 自动化医学视觉与学术质检引擎 (审计标题、截断、字号、字形)
│   └── recipes/                      # 真实科研最高频图表标准生成器
│       ├── __init__.py
│       ├── prism_plots.py            # GraphPad Prism 经典柱状散点图与阶梯显著性横折线
│       ├── bar_dot.py                # 标准 Superimposed Dot-Bar (qPCR, WB, ELISA)
│       ├── km_survival.py            # 自带 Number at Risk 表格的 Kaplan-Meier 生存曲线
│       ├── boxplot_jitter.py         # 临床队列箱线图 + 样本抖动散点
│       └── forest_plot.py            # 亚组分析与 Meta 分析森林图
│
└── examples/                         # 4 个涵盖核心场景的实测可运行示例
    ├── demo_01_prism_qpcr_wb.py      # 纯正 Prism 风格的 qPCR/WB 图 (Open Outline 与 Soft Tint 两种模式)
    ├── demo_02_km_survival_risk_table.py # 临床/肿瘤学标准 KM 曲线与对齐风险人数表
    ├── demo_03_multipanel_aligned.py # 多子图拼排 + 像素级 A/B/C/D 绝对对齐 + 自动化 QA
    └── demo_04_clinical_boxplot.py   # 中大样本临床队列箱线图与显著性标注
```

---

## 🔬 Proven Foundations (开源渊源与致敬)

本项目不是闭门造车，而是深度吸收、合成并扩展了以下顶级开源项目：

1. **`CSdaw/ggprism` & GraphPad Prism**: 逆向移植了生物医学界最经典的 1.0pt 粗边框坐标轴、向外刻度、Open/Tint 柱体、单向 SEM 误差棒与阶梯显著性横折线。
2. **`garrettj403/SciencePlots` (4.5k+ ⭐)**: 继承了严谨的出版级脊线比例、外向刻度几何参数及 sans-serif 数学字体 (`mathtext.fontset = 'stixsans'`)。
3. **`Haojae/scipilot-figure-skill`**: 吸收了基于渲染器包围盒的文本裁剪越界检测、刻度重叠碰撞检测与视觉阅读拓扑排序算法，并二次开发升级为医学特异性质检器 `medfigure.qa`。
4. **`nanxstats/ggsci` (1.8k+ ⭐)**: 集成了逆向还原的 *NEJM*, *The Lancet*, *JAMA*, *JCO* 权威医学色盘。
5. **`Phlya/adjustText` (2.5k+ ⭐)**: 集成了力导向斥力算法，自动推开密集标签并画引线。

---

## 🗺️ The Complete Medical SCI Figure Atlas (全图表 17 种标准图元全集)

详见 [`references/figure_atlas.md`](references/figure_atlas.md)：

| 领域分类 | 图元名称 (Archetype) | 适用实验 / 场景 | 核心视觉特征 |
| :--- | :--- | :--- | :--- |
| **1. 组间连续变量** | **1.1 Superimposed Dot-Bar** | qPCR, WB 定量, ELISA ($n=3\sim8$) | Open/Tint 柱 + 向上 SEM + 独立样本散点 |
| | **1.2 Boxplot + Jitter** | 临床患者队列生化标志物 ($n\ge10$) | 中位数粗线 + IQR 箱体 + 散点微扰 |
| | **1.3 Violin / Raincloud** | 流式 MFI, 单细胞表达分布 ($n\ge30$) | 半边小提琴核密度 + 内部微型箱线 + 雨滴散点 |
| | **1.4 Paired Dot-Line** | 同一患者治疗前 vs 治疗后配对 | 点对点细线相连，直观展示个体轨迹 |
| **2. 生存随访** | **2.1 KM + Risk Table** | 肿瘤临床试验 OS/PFS 随访 | 阶梯曲线 + 截尾竖线 + 绝对对齐风险人数表 |
| | **2.2 Longitudinal Growth** | 动物荷瘤体积与体重追踪 | 均值折线 + SEM 须线 + 给药时间箭头 ($\downarrow$) |
| **3. 临床循证** | **3.1 CONSORT/PRISMA** | RCT 入组筛选流程、Meta 流程 | 直角框图 + 筛查/排除/随机/失访/分析全记录 |
| | **3.2 Forest Plot** | 亚组疗效、Meta 分析 | 对数坐标轴 + 垂直 1.0 无效线 + 权重方块与菱形 |
| | **3.3 ROC / PR Curve** | 疾病诊断模型、生物标志物验证 | 对角参考虚线 + 阶梯曲线 + AUC (95% CI) |
| | **3.4 Nomogram / Calibration** | 预后评分系统与校准验证 | 点数映射尺 + 45° 理想线与 Bootstrap 校准线 |
| **4. 高通量组学** | **4.1 Volcano Plot** | 转录组/蛋白组差异表达 | 双截断虚线 + 红蓝显著散点 + adjustText 引线 |
| | **4.2 Clustered Heatmap** | 差异基因聚类模式 | 行列聚类树 + z-score + 临床注释条 + 均匀色标 |
| | **4.3 PCA / UMAP / t-SNE** | 单细胞聚类降维 | 等比例坐标系 + 色盲安全亚型着色 + 透明散点 |
| | **4.4 GO/KEGG Bubble** | 通路功能富集分析 | Gene Ratio 横轴 + 气泡面积 (Count) + 气泡颜色 (-log10 P) |
| | **4.5 GWAS Manhattan** | 基因突变位点全基因组扫描 | 染色体交替双色 + 全基因组红虚线 ($P=5\times10^{-8}$) |
| **5. 分子病理** | **5.1 Cropped Blot Panel** | Western Blot 灰度条带 | 矩形裁切条带 + 左侧分子量 (kDa) + 内参对齐 |
| | **5.2 IHC / IF Microscopy** | 病理免疫组化/荧光摄影 | **右下角必须物理标注 Scale Bar** + 通道颜色标明 |

---

## 🔍 The Micro-Detail Blueprint (像素级复刻细节)

详见 [`references/micro_details.md`](references/micro_details.md)：

* **线宽绝对 1:1:1 律**：坐标轴线宽、柱体边框线宽、误差棒线宽**严格统一为 1.0 pt 或 1.2 pt**，绝不粗细混杂；
* **刻度外挂**：主刻度必须朝外（`direction='out'`），长度固定为 `4.0 pt`，线宽与轴线严格同宽；
* **散点同心圆（Halo Dot）**：散点采用 `0.7 pt` 黑色外框 + `85%` 透明度填充，两个样本数值重合时依然能看清半月牙重叠轮廓；
* **显著性横折线（2% 挂钩下垂）**：两端折角向下延伸整个 Y 轴跨度的 `2.0%`，横梁距离最高数据点留白 `3.5%`，星号紧贴横梁上方 `1.5 pt`；
* **多子图呼吸槽**：两子图水平间隙保留 `0.45 ~ 0.55 in`，保证右图 Y 轴标题文字绝不侵入左图区域。

---

## 🚀 快速上手 (Python 示例)

### 安装

```bash
git clone https://github.com/quaresma00/medical-sci-figure-skill.git
cd medical-sci-figure-skill
pip install -e .
```

### 1. 绘制纯正 GraphPad Prism 风格的 qPCR / WB 柱状散点图

```python
import matplotlib.pyplot as plt
import numpy as np
from medfigure import set_prism_style, plot_prism_bar_dots, add_prism_bracket

# 一键注入纯正 GraphPad Prism / ggprism 参数
set_prism_style(palette="floral", base_size=8.0, spine_width=1.0)

fig, ax = plt.subplots(figsize=(3.35, 2.8), dpi=300)

data = [
    np.array([0.95, 1.05, 0.90, 1.10, 1.00]),
    np.array([4.20, 4.60, 3.80, 4.40, 4.50]),
    np.array([2.10, 2.40, 1.90, 2.25, 2.15])
]

# 绘制 Open Outline 模式 (白底空心彩色粗边框柱 + 向上 SEM + 独立样本散点)
plot_prism_bar_dots(ax, data, group_names=['Control', 'LPS', 'LPS + Drug'], fill_mode="outline")

# 添加经典 Prism 阶梯显著性横折线
add_prism_bracket(ax, 0, 1, y=4.9, text="***")
add_prism_bracket(ax, 1, 2, y=5.4, text="**")

fig.savefig("qpcr_figure.pdf", bbox_inches='tight')
```

### 2. 运行内置全套示例

```bash
python examples/demo_01_prism_qpcr_wb.py
python examples/demo_02_km_survival_risk_table.py
python examples/demo_03_multipanel_aligned.py
python examples/demo_04_clinical_boxplot.py
```

---

## 🤖 AI Agent 技能载入

直接将 [`SKILL.md`](SKILL.md) 挂载进 Claude Code、Antigravity、Cursor 或任何 AI Coding Agent，AI 即可根据 17 种标准图元决策树和微观细节法则自动生成符合顶刊审稿规范的代码。
