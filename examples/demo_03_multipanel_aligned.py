"""
Example 03: Multi-panel composite with pixel-perfect A, B label alignment.
Demonstrates automated QA and layout finalized spacing.
"""
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from medfigure import set_medical_style, add_panel_labels, PALETTE_NEJM, audit_medical_figure, create_outside_legend

def main():
    set_medical_style(journal="nejm")
    
    # Double column width: 175mm -> 6.89 in
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.89, 2.8), dpi=300)
    
    # Panel A: Time-course curve with outside legend
    time = np.linspace(0, 24, 25)
    ax1.plot(time, np.exp(-0.08 * time), label='Standard of Care', color=PALETTE_NEJM[1], lw=1.2)
    ax1.plot(time, np.exp(-0.04 * time), label='Combination Therapy', color=PALETTE_NEJM[0], lw=1.2, ls='--')
    ax1.set_xlabel('Follow-up Time (Weeks)')
    ax1.set_ylabel('Progression-Free Probability')
    ax1.legend(loc='lower left', frameon=False)
    
    # Panel B: Response rate comparison
    bars = ax2.bar([0, 1], [32.4, 68.9], color=[PALETTE_NEJM[1], PALETTE_NEJM[0]], width=0.45)
    ax2.set_xticks([0, 1])
    ax2.set_xticklabels(['SOC (n=50)', 'Combo (n=50)'])
    ax2.set_ylabel('Objective Response Rate (%)')
    ax2.set_ylim(0, 85)
    
    # Align A, B labels without drifting
    add_panel_labels(fig, [ax1, ax2], style="upper")
    
    plt.tight_layout()
    audit_medical_figure(fig)
    
    out_pdf = "demo_03_multipanel.pdf"
    out_png = "demo_03_multipanel.png"
    plt.savefig(out_pdf, bbox_inches='tight')
    plt.savefig(out_png, dpi=300, bbox_inches='tight')
    print(f"Saved: {out_png} and {out_pdf}")

if __name__ == "__main__":
    main()
