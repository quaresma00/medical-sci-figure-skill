"""
Recipe: Clinical trial Subgroup & Meta-analysis Forest Plot.
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_forest(subgroups, estimates, ci_lows, ci_highs, metric="Hazard Ratio", figsize=(5.5, 3.5)):
    """
    Publication standard forest plot with vertical null effect line.
    """
    fig, ax = plt.subplots(figsize=figsize, dpi=300)
    y_pos = np.arange(len(subgroups))[::-1]
    
    # Null effect vertical line (1.0 for ratios)
    ax.axvline(1.0, color='#666666', linestyle='--', lw=0.8, zorder=1)
    
    for i, y in enumerate(y_pos):
        est = estimates[i]
        low = ci_lows[i]
        high = ci_highs[i]
        
        # CI Whisker
        ax.plot([low, high], [y, y], color='#00468B', lw=1.2, zorder=2)
        # Point Estimate Square
        ax.scatter(est, y, color='#00468B', marker='s', s=35, zorder=3)
        
        # Text annotation on the right
        ci_str = f"{est:.2f} ({low:.2f}–{high:.2f})"
        ax.text(2.6, y, ci_str, va='center', ha='left', fontsize=6.5)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(subgroups, fontweight='bold')
    ax.set_xlabel(f"{metric} (95% CI)")
    
    # Bottom direction labels
    ax.text(0.5, -1.2, "← Favors Treatment", ha='center', va='center', fontsize=6.0, color='#333333')
    ax.text(1.5, -1.2, "Favors Control →", ha='center', va='center', fontsize=6.0, color='#333333')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    return fig, ax
