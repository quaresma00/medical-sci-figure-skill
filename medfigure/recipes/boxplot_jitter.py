"""
Recipe: Small-sample Boxplot with overlaid individual sample jitter.
Enforces data transparency for n < 10 biological replicates.
"""
import matplotlib.pyplot as plt
import numpy as np
from medfigure.style import PALETTE_NEJM

def plot_jitter_boxplot(ax, groups_data, group_names, palette=None, ylabel="Expression Level (AU)"):
    """
    Plot transparent boxplot with visible biological replicates.
    """
    if palette is None:
        palette = PALETTE_NEJM

    positions = np.arange(len(groups_data))
    
    # Boxplot base (clean monochrome structure)
    bp = ax.boxplot(
        groups_data,
        positions=positions,
        widths=0.42,
        patch_artist=True,
        showfliers=False,
        boxprops=dict(facecolor='white', color='#333333', linewidth=0.7),
        medianprops=dict(color='#BC3C29', linewidth=1.2),
        whiskerprops=dict(color='#333333', linewidth=0.7),
        capprops=dict(color='#333333', linewidth=0.7)
    )

    # Overlaid individual sample jitter
    np.random.seed(42)
    for i, data in enumerate(groups_data):
        jitter = np.random.normal(0, 0.04, size=len(data))
        color = palette[i % len(palette)]
        ax.scatter(positions[i] + jitter, data, color=color, alpha=0.85, s=28, zorder=3, edgecolors='none')

    ax.set_xticks(positions)
    ax.set_xticklabels(group_names)
    ax.set_ylabel(ylabel)
