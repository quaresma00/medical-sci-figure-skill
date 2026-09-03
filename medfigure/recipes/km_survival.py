"""
Recipe: Kaplan-Meier survival curves with mandatory Number at Risk table.
"""
import matplotlib.pyplot as plt
import numpy as np
from medfigure.style import PALETTE_NEJM

def plot_km_with_risk_table(groups, time_points, hr_text=None, figsize=(4.72, 3.8), palette=None):
    """
    Draw publication-standard KM survival plot with synchronized Number at Risk table.
    """
    if palette is None:
        palette = PALETTE_NEJM

    # Grid: Main plot (80% height), Risk table (20% height)
    fig = plt.figure(figsize=figsize, dpi=300)
    gs = fig.add_gridspec(2, 1, height_ratios=[4, 1.2], hspace=0.35)
    ax_km = fig.add_subplot(gs[0])
    ax_table = fig.add_subplot(gs[1], sharex=ax_km)

    for i, grp in enumerate(groups):
        color = palette[i % len(palette)]
        times = np.sort(grp["time"])
        events = grp["event"][np.argsort(grp["time"])]
        
        # Step curve calculation
        n = len(times)
        surv = [1.0]
        t_axis = [0.0]
        cur_surv = 1.0
        
        for t, e in zip(times, events):
            t_axis.extend([t, t])
            surv.append(cur_surv)
            if e == 1:
                cur_surv *= (1.0 - 1.0 / n)
            surv.append(cur_surv)
            n -= 1
            
        ax_km.step(t_axis, surv, where='post', label=grp["name"], color=color, lw=1.3)

    ax_km.set_ylabel("Overall Survival Probability")
    ax_km.set_ylim(-0.02, 1.02)
    ax_km.legend(loc='lower left', frameon=False)
    
    if hr_text:
        ax_km.text(0.98, 0.95, hr_text, transform=ax_km.transAxes,
                   ha='right', va='top', fontsize=6.5, color='#333333')

    # Draw Risk Table
    ax_table.axis('off')
    y_pos = np.linspace(0.8, 0.2, len(groups))
    
    for i, grp in enumerate(groups):
        color = palette[i % len(palette)]
        ax_table.text(-0.05, y_pos[i], grp["name"], transform=ax_table.transAxes,
                      ha='right', va='center', fontsize=6.5, fontweight='bold', color=color)
        for tp in time_points:
            n_risk = np.sum(grp["time"] >= tp)
            ax_table.text(tp, y_pos[i], str(n_risk),
                          ha='center', va='center', fontsize=6.5, color='#333333')

    ax_km.set_xticks(time_points)
    ax_table.set_xlim(ax_km.get_xlim())
    ax_km.set_xlabel("Time (Months)")
    return fig
