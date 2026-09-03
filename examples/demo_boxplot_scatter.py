"""
Demo: Small-sample Boxplot with Individual Replicate Scatter.
"""
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from medfigure import set_medical_style, add_significance_bracket
from medfigure.recipes import plot_jitter_boxplot

def main():
    set_medical_style(journal="nejm")
    
    fig, ax = plt.subplots(figsize=(3.35, 2.75), dpi=300)
    
    # Continuous data with n=8 per group
    np.random.seed(42)
    ctrl = np.random.normal(loc=12.0, scale=1.8, size=8)
    treat = np.random.normal(loc=17.5, scale=2.1, size=8)
    
    plot_jitter_boxplot(ax, [ctrl, treat], group_names=['Vehicle', 'Targeted Drug'], ylabel='Biomarker Level (ng/mL)')
    add_significance_bracket(ax, 0, 1, y=21.0, p_value=0.004, test_name="Unpaired t-test")
    
    plt.tight_layout()
    plt.savefig("boxplot_scatter_demo.pdf", bbox_inches='tight')
    print("Saved boxplot_scatter_demo.pdf")

if __name__ == "__main__":
    main()
