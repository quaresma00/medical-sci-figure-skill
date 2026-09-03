"""
Example 02: Kaplan-Meier Survival Curve with Synchronized Number at Risk Table.
Standard oncology and clinical trial presentation.
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from medfigure import set_medical_style
from medfigure.recipes import plot_km_with_risk_table

def main():
    set_medical_style(journal="lancet")
    
    np.random.seed(42)
    time_ctrl = np.array([2, 5, 8, 12, 15, 20, 24, 30, 36, 42])
    event_ctrl = np.array([1, 1, 0, 1, 1, 0, 1, 1, 0, 1])

    time_treat = np.array([4, 9, 14, 18, 22, 28, 34, 40, 48, 54])
    event_treat = np.array([1, 0, 1, 0, 1, 1, 0, 1, 0, 0])

    fig = plot_km_with_risk_table(
        groups=[
            {"name": "Control (Placebo)", "time": time_ctrl, "event": event_ctrl},
            {"name": "Investigational Agent", "time": time_treat, "event": event_treat}
        ],
        time_points=[0, 12, 24, 36, 48],
        hr_text="HR = 0.52 (95% CI: 0.31–0.84), p = 0.008",
        figsize=(4.72, 3.8)
    )
    
    out_pdf = "demo_02_km_survival.pdf"
    out_png = "demo_02_km_survival.png"
    fig.savefig(out_pdf, bbox_inches='tight')
    fig.savefig(out_png, dpi=300, bbox_inches='tight')
    print(f"Saved: {out_png} and {out_pdf}")

if __name__ == "__main__":
    main()
