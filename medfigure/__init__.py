"""
medfigure: Publication-ready medical SCI figure generation library & skill.
Synthesized from SciencePlots, scipilot-figure-skill, ggsci, and adjustText.
"""

from medfigure.style import (
    set_medical_style,
    PALETTE_NEJM,
    PALETTE_LANCET,
    PALETTE_JAMA,
    PALETTE_JCO,
    PALETTE_NATURE,
    PALETTE_OKABE_ITO,
)
from medfigure.layout import (
    add_panel_labels,
    create_outside_legend,
    get_journal_figsize,
    finalize_figure,
)
from medfigure.annotation import (
    smart_repel_text,
    add_significance_bracket,
)
from medfigure.qa import (
    audit_medical_figure,
)

__version__ = "2.0.0"
__all__ = [
    "set_medical_style",
    "PALETTE_NEJM",
    "PALETTE_LANCET",
    "PALETTE_JAMA",
    "PALETTE_JCO",
    "PALETTE_NATURE",
    "PALETTE_OKABE_ITO",
    "add_panel_labels",
    "create_outside_legend",
    "get_journal_figsize",
    "finalize_figure",
    "smart_repel_text",
    "add_significance_bracket",
    "audit_medical_figure",
]
