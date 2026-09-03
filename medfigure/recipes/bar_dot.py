"""
Recipe: Standard Medical Superimposed Dot-Bar Plot (qPCR, Western Blot, ELISA).
Mean + SEM error bar with overlaid individual biological replicates.
The universal gold standard for small samples (n=3 to n=8).
"""
import matplotlib.pyplot as plt
import numpy as np
from medfigure.style import PALETTE_NEJM

def plot_superimposed_bar_dot(
    ax,
    groups_data,
    group_names,
    palette=None,
    ylabel="Relative Expression Level",
    bar_width=0.52,
    dot_size=32,
    error_metric="sem"
):
    """
    Plot academic standard bar graph with superimposed biological replicate dots.
    """
    if palette is None:
        palette = PALETTE_NEJM

    positions = np.arange(len(groups_data))
    means = [np.mean(g) for g in groups_data]
    
    if error_metric.lower() == "sem":
        errors = [np.std(g, ddof=1) / np.sqrt(len(g)) for g in groups_data]
    else:
        errors = [np.std(g, ddof=1) for g in groups_data]

    edge_colors = [palette[i % len(palette)] for i in range(len(groups_data))]

    # 1. Open bar with colored borders
    ax.bar(
        positions,
        means,
        width=bar_width,
        color='#FFFFFF',
        edgecolor=edge_colors,
        linewidth=1.2,
        zorder=2
    )

    # 2. Upward single-direction error bars (SEM)
    for i in range(len(groups_data)):
        ax.errorbar(
            positions[i],
            means[i],
            yerr=[[0], [errors[i]]],
            fmt='none',
            ecolor=edge_colors[i],
            elinewidth=1.2,
            capsize=3.5,
            capthick=1.2,
            zorder=3
        )

    # 3. Superimposed individual sample dots
    np.random.seed(42)
    for i, g in enumerate(groups_data):
        jitter = np.random.normal(0, 0.035, size=len(g))
        ax.scatter(
            positions[i] + jitter,
            g,
            s=dot_size,
            facecolors=edge_colors[i],
            edgecolors='#222222',
            linewidths=0.6,
            alpha=0.85,
            zorder=4
        )

    ax.set_xticks(positions)
    ax.set_xticklabels(group_names)
    ax.set_ylabel(ylabel)
