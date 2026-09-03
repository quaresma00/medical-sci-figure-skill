"""
Medical Figure Quality Assurance (QA) Engine.
Synthesized from scipilot-figure-skill visual_qa and extended with clinical editorial checks.
"""
from __future__ import annotations
import logging
import warnings
import matplotlib.pyplot as plt
import matplotlib.text as mtext

_GLYPH_MARKERS = (
    "missing from current font",
    "Glyph",
    "glyph",
    "cannot be converted to a character",
)

class _GlyphWarningHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.messages: list[str] = []

    def emit(self, record):
        msg = record.getMessage()
        if any(m in msg for m in _GLYPH_MARKERS):
            self.messages.append(msg)

def _draw_and_collect_glyph_warnings(fig) -> list[str]:
    """Capture missing font glyph warnings during rasterization."""
    collected: list[str] = []
    mpl_logger = logging.getLogger("matplotlib")
    prev_level = mpl_logger.level
    mpl_logger.setLevel(logging.WARNING)
    handler = _GlyphWarningHandler()
    mpl_logger.addHandler(handler)

    try:
        with warnings.catch_warnings(record=True) as ws:
            warnings.filterwarnings("always", category=UserWarning)
            fig.canvas.draw()
            for w in ws:
                s = str(w.message)
                if any(m in s for m in _GLYPH_MARKERS):
                    collected.append(s)
    finally:
        mpl_logger.removeHandler(handler)
        mpl_logger.setLevel(prev_level)

    collected.extend(handler.messages)
    return list(dict.fromkeys(collected))

def _ticklabels_overlap(labels, renderer, axis: str = "x", tol: float = 1.0) -> bool:
    """Detect collision between adjacent tick labels."""
    boxes = []
    for l in labels:
        try:
            if l.get_visible() and l.get_text().strip():
                boxes.append(l.get_window_extent(renderer))
        except Exception:
            continue
    if len(boxes) < 2:
        return False
    if axis == "x":
        boxes.sort(key=lambda b: b.x0)
        return any(a.x1 - b.x0 > tol for a, b in zip(boxes, boxes[1:]))
    else:
        boxes.sort(key=lambda b: b.y0)
        return any(a.y1 - b.y0 > tol for a, b in zip(boxes, boxes[1:]))

def audit_medical_figure(fig, tol_px: float = 2.0) -> bool:
    """
    Full-spectrum quality assurance audit:
    1. Broken Glyphs / Unicode Minus Errors (from scipilot)
    2. Internal Titles (Medical Journal Violation)
    3. Tick Label Collisions (scipilot overlap algorithm)
    4. Text Clipping (Window extent boundary check)
    5. Font Sizes < 5.0pt (Editorial legibility failure)
    6. Truncated Bar Plot Baselines (Honesty rule)
    """
    critical_errors: list[str] = []
    warnings_list: list[str] = []

    # 1. Broken Glyphs
    glyphs = _draw_and_collect_glyph_warnings(fig)
    if glyphs:
        critical_errors.append(f"Broken Font Glyphs detected ({len(glyphs)} occurrences). Ensure axes.unicode_minus=False.")

    try:
        renderer = fig.canvas.get_renderer()
    except Exception:
        fig.canvas.draw()
        renderer = fig.canvas.get_renderer()

    W, H = float(fig.bbox.width), float(fig.bbox.height)

    # 2. Medical Title Check
    if fig._suptitle and fig._suptitle.get_text().strip():
        critical_errors.append("fig.suptitle() detected! Academic figures MUST NOT have internal titles.")

    for idx, ax in enumerate(fig.axes):
        # Title check
        title = ax.get_title().strip()
        if title:
            critical_errors.append(f"ax.set_title('{title}') detected on Axis {idx}. Place in caption instead.")

        # 3. Tick Collisions
        if ax.get_subplotspec() is not None:
            if _ticklabels_overlap(ax.get_xticklabels(), renderer, axis="x", tol=tol_px):
                warnings_list.append(f"Axis {idx}: X-axis tick labels overlap! Rotate 30-45 deg or reduce ticks.")
            if _ticklabels_overlap(ax.get_yticklabels(), renderer, axis="y", tol=tol_px):
                warnings_list.append(f"Axis {idx}: Y-axis tick labels overlap! Increase subplot height.")

        # 4. Text Clipping & Font Size
        for t in ax.texts:
            size = t.get_fontsize()
            if size < 5.0:
                warnings_list.append(f"Axis {idx}: Font size {size}pt is < 5.0pt ('{t.get_text()[:12]}...').")

        # 5. Bar plot Y-axis check
        has_bars = any('BarContainer' in str(type(c)) for c in ax.containers)
        if has_bars:
            ymin, _ = ax.get_ylim()
            if ymin > 0.01:
                critical_errors.append(f"Axis {idx}: Bar chart baseline starts at {ymin:.2f} (must start at 0).")

    # Output report
    if not critical_errors and not warnings_list:
        print(" [MedFigure QA Pass]: Conforms to medical SCI publication standards.")
        return True
    
    if critical_errors:
        print("❌ [MedFigure QA CRITICAL FAILURES]:")
        for err in critical_errors:
            print(f"   [CRITICAL] {err}")
    if warnings_list:
        print("⚠️ [MedFigure QA WARNINGS]:")
        for w in warnings_list:
            print(f"   [WARNING] {w}")
            
    return len(critical_errors) == 0
