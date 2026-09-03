"""
Publication-ready qPCR / Western Blot standard plot:
Bar graph with overlaid individual biological replicate dots (GraphPad Prism & Nature standard).
"""
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from medfigure import (
    set_medical_style,
    add_panel_labels,
    add_significance_bracket,
    PALETTE_NEJM,
)

def plot_classic_qpcr(output_png="qpcr_classic_paper_style.png", output_pdf="qpcr_classic_paper_style.pdf"):
    # 1. Apply journal styling
    palette = set_medical_style(journal="nejm", base_size=7.5)

    # 2. Dimensions: 85 mm single column -> 3.35 in, height 2.8 in
    fig, ax = plt.subplots(figsize=(3.35, 2.8), dpi=300)

    # 3. Simulated qPCR data (n=5 biological replicates, 2^-ddCt relative to GAPDH)
    np.random.seed(42)
    control = np.array([0.92, 1.05, 0.98, 1.12, 0.93])
    model = np.array([4.10, 4.65, 3.85, 4.30, 4.50])
    treatment = np.array([2.05, 2.35, 1.85, 2.20, 2.15])

    groups = [control, model, treatment]
    group_names = ['Control', 'LPS', 'LPS +\nInhibitor']
    positions = np.arange(len(groups))

    # Calculate Mean & SEM (Standard Error of the Mean, standard in qPCR papers)
    means = [np.mean(g) for g in groups]
    sems = [np.std(g, ddof=1) / np.sqrt(len(g)) for g in groups]

    # Colors: Control (Neutral Gray/Blue), Model (NEJM Brick Red), Treatment (NEJM Blue/Green)
    bar_colors = ['#FFFFFF', '#FFFFFF', '#FFFFFF']
    edge_colors = [palette[1], palette[0], palette[3]]  # Navy, Red, Green

    # 4. Standard Academic Bar Graph: Open bar (white face, thick colored border)
    bar_width = 0.52
    bars = ax.bar(
        positions,
        means,
        width=bar_width,
        color=bar_colors,
        edgecolor=edge_colors,
        linewidth=1.2,
        zorder=2
    )

    # 5. Upward-only SEM Error Bars (Classic GraphPad Prism / Nature standard)
    for i in range(len(groups)):
        ax.errorbar(
            positions[i],
            means[i],
            yerr=[[0], [sems[i]]],  # Upward error bar only
            fmt='none',
            ecolor=edge_colors[i],
            elinewidth=1.2,
            capsize=3.5,
            capthick=1.2,
            zorder=3
        )

    # 6. Overlaid Individual Data Points (Open circles, standard biological replicates)
    for i, g in enumerate(groups):
        # Center points slightly jittered or aligned
        jitter = np.random.normal(0, 0.04, size=len(g))
        ax.scatter(
            positions[i] + jitter,
            g,
            s=32,
            facecolors=edge_colors[i],
            edgecolors='#222222',
            linewidths=0.6,
            alpha=0.85,
            zorder=4
        )

    # 7. Axes and baseline
    ax.set_xticks(positions)
    ax.set_xticklabels(group_names)
    ax.set_ylabel('Relative mRNA Expression\n(Fold change to GAPDH)')
    ax.set_ylim(0, 6.0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # 8. Standard Academic Significance Brackets (Stars + exact caption definitions)
    # Bracket 1: Control vs Model (*** p < 0.001)
    ax.plot([0, 0, 1, 1], [4.9, 5.05, 5.05, 4.9], lw=0.8, c='#333333')
    ax.text(0.5, 5.12, "***", ha='center', va='bottom', fontsize=8, fontweight='bold', c='#333333')

    # Bracket 2: Model vs Treatment (** p < 0.01)
    ax.plot([1, 1, 2, 2], [5.4, 5.55, 5.55, 5.4], lw=0.8, c='#333333')
    ax.text(1.5, 5.62, "**", ha='center', va='bottom', fontsize=8, fontweight='bold', c='#333333')

    # Panel Label A
    add_panel_labels(fig, [ax], labels=['A'], style="upper", x_offset_pt=-24, y_offset_pt=8)

    plt.tight_layout()
    fig.savefig(output_pdf, bbox_inches='tight')
    fig.savefig(output_png, dpi=300, bbox_inches='tight')
    print(f"Generated classic qPCR figure: {output_png}")

if __name__ == "__main__":
    plot_classic_qpcr()
