"""
Demonstration of Authentic GraphPad Prism / ggprism figures in Python.
Replicating the look-and-feel of real biomedical publications.
"""
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from medfigure import (
    set_prism_style,
    plot_prism_bar_dots,
    add_prism_bracket,
    add_panel_labels,
    audit_medical_figure,
)

def main():
    # 1. Authentic GraphPad Prism style (Solid black 1.0pt spines, outward ticks, Arial bold)
    set_prism_style(palette="floral", base_size=8.0, spine_width=1.0)

    # 2. Double-column width: 175 mm -> 6.89 in
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.89, 2.9), dpi=300)

    # Simulated qPCR data (n=5 biological replicates)
    np.random.seed(2026)
    ctrl = np.array([0.95, 1.05, 0.90, 1.10, 1.00])
    model = np.array([4.20, 4.60, 3.80, 4.40, 4.50])
    treat = np.array([2.10, 2.40, 1.90, 2.25, 2.15])
    data = [ctrl, model, treat]
    groups = ['Control', 'LPS', 'LPS +\nInhibitor']

    # Subplot 1: Mode "outline" (White fill, bold outline - iconic Nature/Cell biochemistry style)
    plot_prism_bar_dots(ax1, data, groups, fill_mode="outline", ylabel="Relative mRNA Expression\n(Fold change to GAPDH)")
    add_prism_bracket(ax1, 0, 1, y=4.9, text="***", fontsize=8.5)
    add_prism_bracket(ax1, 1, 2, y=5.4, text="**", fontsize=8.5)

    # Subplot 2: Mode "tint" (Soft tinted fill + solid border - classic GraphPad Prism default in medical journals)
    plot_prism_bar_dots(ax2, data, groups, fill_mode="tint", ylabel="Relative Protein Level\n(Fold change to Total)")
    add_prism_bracket(ax2, 0, 1, y=4.9, text="p < 0.001", fontsize=7.0)
    add_prism_bracket(ax2, 1, 2, y=5.4, text="p = 0.003", fontsize=7.0)

    # Panel Labels A, B
    add_panel_labels(fig, [ax1, ax2], labels=['A', 'B'], style="upper", x_offset_pt=-24, y_offset_pt=8)

    plt.tight_layout()
    audit_medical_figure(fig)
    
    out_png = "prism_authentic_qpcr_demo.png"
    out_pdf = "prism_authentic_qpcr_demo.pdf"
    fig.savefig(out_png, dpi=300, bbox_inches='tight')
    fig.savefig(out_pdf, bbox_inches='tight')
    print(f"Generated authentic Prism figure: {out_png}")

if __name__ == "__main__":
    main()
