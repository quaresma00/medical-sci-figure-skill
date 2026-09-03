"""
Layout tools, reading-order subplot sorting, and panel alignment.
Adapted and extended from scipilot-figure-skill layout_tools.
"""
from __future__ import annotations
import string
import matplotlib.pyplot as plt

PANEL_STYLES = {
    "nature": lambda s: s,                    # a, b, c
    "science": lambda s: s,                   # a, b, c
    "ieee": lambda s: f"({s})",               # (a), (b), (c)
    "upper": lambda s: s.upper(),             # A, B, C
    "upper_paren": lambda s: f"({s.upper()})",# (A), (B), (C)
}

def get_journal_figsize(columns=1, height_ratio=0.75):
    """
    Get exact publication dimensions in inches.
    columns: 1 (85mm / 3.35 in), 1.5 (120mm / 4.72 in), 2 (175mm / 6.89 in)
    """
    widths = {1: 3.35, 1.5: 4.72, 2: 6.89}
    width = widths.get(columns, 3.35)
    height = width * height_ratio
    return (width, min(height, 8.8))

def _data_axes(fig) -> list:
    """Filter to subplots with subplotspec, excluding standalone colorbars or insets."""
    return [ax for ax in fig.axes if ax.get_subplotspec() is not None]

def add_panel_labels(
    fig,
    axes=None,
    labels=None,
    style: str = "upper",
    fontsize=None,
    fontweight: str = "bold",
    x_offset_pt: float = -24.0,
    y_offset_pt: float = 8.0,
    ha: str = "left",
    va: str = "bottom",
    color: str = "black",
):
    """
    Add pixel-aligned panel labels (A, B, C, D) to subplots.
    Sorted in natural reading order (top-to-bottom, left-to-right).
    Anchored to axes fraction (0, 1) with an absolute points offset.
    """
    if axes is None:
        axes = _data_axes(fig)
        axes = sorted(
            axes,
            key=lambda ax: (-round(ax.get_position().y1, 3), round(ax.get_position().x0, 3)),
        )
    elif hasattr(axes, 'flat'):
        axes = list(axes.flat)
    else:
        axes = list(axes)

    n = len(axes)
    if n == 0:
        return []

    if labels is None:
        fmt = PANEL_STYLES.get(style, lambda s: s.upper())
        letters = string.ascii_lowercase
        labels = [fmt(letters[i] if i < 26 else letters[i // 26 - 1] + letters[i % 26]) for i in range(n)]

    if fontsize is None:
        fontsize = plt.rcParams.get("axes.labelsize", 8.5)

    placed = []
    for ax, lab in zip(axes, labels):
        t = ax.annotate(
            lab,
            xy=(0, 1), xycoords="axes fraction",
            xytext=(x_offset_pt, y_offset_pt), textcoords="offset points",
            fontsize=fontsize, fontweight=fontweight, color=color,
            ha=ha, va=va,
            annotation_clip=False
        )
        placed.append(t)
    return placed

def finalize_figure(fig, prefer: str = "constrained") -> str:
    """Safely apply layout engine to prevent margin clipping."""
    used = "none"
    if prefer == "constrained":
        try:
            fig.set_layout_engine("constrained")
            fig.canvas.draw()
            used = "constrained"
        except Exception:
            used = "none"
    if used == "none":
        try:
            fig.tight_layout()
            used = "tight"
        except Exception:
            used = "none"
    return used

def create_outside_legend(ax, loc='upper left', bbox_to_anchor=(1.02, 1.0), **kwargs):
    """Place legend safely outside the plot axes to prevent data occlusion."""
    return ax.legend(loc=loc, bbox_to_anchor=bbox_to_anchor, frameon=False, **kwargs)
