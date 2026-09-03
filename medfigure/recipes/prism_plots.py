"""
Authentic GraphPad Prism style plotting recipes for biomedical research papers (qPCR, Western Blot, ELISA).
Replicates the visual layout of CSdaw/ggprism.
"""
import matplotlib.pyplot as plt
import numpy as np
from medfigure.prism import PRISM_PALETTES

def plot_prism_bar_dots(
    ax,
    groups_data,
    group_names,
    palette_name="floral",
    fill_mode="outline",   # "outline" (white fill, bold border) or "tint" (soft fill + solid border)
    ylabel="Relative mRNA Expression",
    bar_width=0.55,
    dot_size=36,
    error="sem",           # "sem" (standard in qPCR/biomed) or "sd"
):
    """
    Render an authentic GraphPad Prism / ggprism style bar graph with superimposed dots.
    """
    colors = PRISM_PALETTES.get(palette_name, PRISM_PALETTES["floral"])
    positions = np.arange(len(groups_data))
    means = [np.mean(g) for g in groups_data]
    
    if error.lower() == "sem":
        err_values = [np.std(g, ddof=1) / np.sqrt(len(g)) for g in groups_data]
    else:
        err_values = [np.std(g, ddof=1) for g in groups_data]

    group_colors = [colors[i % len(colors)] for i in range(len(groups_data))]

    # 1. Bar fill and borders
    if fill_mode == "outline":
        facecolors = ['#FFFFFF'] * len(groups_data)
        edgecolors = group_colors
    else:
        facecolors = [c for c in group_colors]
        edgecolors = group_colors

    bars = ax.bar(
        positions,
        means,
        width=bar_width,
        color=facecolors,
        edgecolor=edgecolors,
        linewidth=1.2,
        alpha=0.35 if fill_mode != "outline" else 1.0,
        zorder=2
    )
    
    # If tint mode, redraw the border solid for clean edges
    if fill_mode != "outline":
        for i, pos in enumerate(positions):
            ax.bar(pos, means[i], width=bar_width, fill=False, edgecolor=edgecolors[i], linewidth=1.2, zorder=2.5)

    # 2. Classic GraphPad Prism upward error bars with wide caps
    for i in range(len(groups_data)):
        ax.errorbar(
            positions[i],
            means[i],
            yerr=[[0], [err_values[i]]],
            fmt='none',
            ecolor=edgecolors[i] if fill_mode == "outline" else '#000000',
            elinewidth=1.2,
            capsize=4.5,
            capthick=1.2,
            zorder=3
        )

    # 3. Superimposed Biological Replicate Dots (Open circles with thin black stroke)
    np.random.seed(42)
    for i, g in enumerate(groups_data):
        jitter = np.random.normal(0, 0.035, size=len(g))
        ax.scatter(
            positions[i] + jitter,
            g,
            s=dot_size,
            facecolors=group_colors[i],
            edgecolors='#111111',
            linewidths=0.7,
            alpha=0.9,
            zorder=4
        )

    # 4. Axes limits and ticks
    ax.set_xticks(positions)
    ax.set_xticklabels(group_names, fontweight='bold')
    ax.set_ylabel(ylabel, fontweight='bold')
    
    # Baseline strictly at 0
    max_val = max(np.max(g) for g in groups_data)
    ax.set_ylim(0, max_val * 1.35)

def add_prism_bracket(ax, x1, x2, y, text="***", tip_length=0.02, lw=1.0, fontsize=8):
    """
    Draw an authentic GraphPad Prism significance bracket.
    """
    y_range = ax.get_ylim()[1] - ax.get_ylim()[0]
    tip = y_range * tip_length

    # Draw the bracket line: _|-----|_
    ax.plot([x1, x1, x2, x2], [y - tip, y, y, y - tip], lw=lw, color='#000000', clip_on=False)
    
    # Text centered above bracket
    ax.text(
        (x1 + x2) * 0.5,
        y + y_range * 0.015,
        text,
        ha='center',
        va='bottom',
        fontsize=fontsize,
        fontweight='bold',
        color='#000000',
        clip_on=False
    )
