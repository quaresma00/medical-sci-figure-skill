"""
Example 04: Clinical Cohort Boxplot with Overlaid Jitter Scatter.
Standard data presentation for cohort biomarkers (n >= 10).
"""
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from medfigure import set_medical_style, add_significance_bracket
from medfigure.recipes import plot_jitter_boxplot

def main():
    set_medical_style(journal="nejm")
    
    fig, ax = plt.subplots(figsize=(3.35, 2.75), dpi=300)
    
    # Continuous biomarker data with n=12 per group
    np.random.seed(42)
    ctrl = np.random.normal(loc=12.0, scale=1.8, size=12)
    treat = np.random.normal(loc=17.5, scale=2.1, size=12)
    
    plot_jitter_boxplot(ax, [ctrl, treat], group_names=['Healthy', 'Patient Cohort'], ylabel='Serum Biomarker (ng/mL)')
    add_significance_bracket(ax, 0, 1, y=21.5, p_value=0.002, test_name="Mann-Whitney U")
    
    plt.tight_layout()
    out_pdf = "demo_04_clinical_boxplot.pdf"
    out_png = "demo_04_clinical_boxplot.png"
    plt.savefig(out_pdf, bbox_inches='tight')
    plt.savefig(out_png, dpi=300, bbox_inches='tight')
    print(f"Saved: {out_png} and {out_pdf}")

if __name__ == "__main__":
    main()
