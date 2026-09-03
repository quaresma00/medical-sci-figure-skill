"""
Style presets and palettes for medical scientific publications.
Synthesized from SciencePlots and ggsci.
"""
import matplotlib.pyplot as plt

# Official Color Palettes (Colorblind Safe, from ggsci)
PALETTE_NEJM = ["#BC3C29", "#0072B5", "#E18727", "#20854E", "#7876B1", "#6F99AD", "#FFDC91", "#EE4C97"]
PALETTE_LANCET = ["#00468B", "#ED0000", "#42B540", "#0099B4", "#925E9F", "#FDAF91", "#AD002A", "#ADB6B6"]
PALETTE_JAMA = ["#374E55", "#DF8F44", "#00A1D5", "#B24745", "#79AF97", "#6A6599", "#80796B"]
PALETTE_JCO = ["#002855", "#B8860B", "#8B0000", "#2E8B57", "#4682B4", "#4B0082"]
PALETTE_NATURE = ["#E64B35", "#4DBBD5", "#00A087", "#3C5488", "#F39B7F", "#8491B4", "#91D1C2", "#DC0000"]
PALETTE_OKABE_ITO = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"]

JOURNAL_PALETTES = {
    "nejm": PALETTE_NEJM,
    "lancet": PALETTE_LANCET,
    "jama": PALETTE_JAMA,
    "jco": PALETTE_JCO,
    "nature": PALETTE_NATURE,
    "okabe_ito": PALETTE_OKABE_ITO,
}

def set_medical_style(journal="nejm", font_family="sans-serif", base_size=7.5):
    """
    Apply publication-grade parameters for medical journals.
    Synthesizes SciencePlots tick/math parameters and ggsci authentic color palettes.
    """
    journal_key = journal.lower()
    palette = JOURNAL_PALETTES.get(journal_key, PALETTE_NEJM)

    plt.rcParams.update({
        # Font & Vector Export Guard (SciencePlots & scipilot consensus)
        'font.family': font_family,
        'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
        'mathtext.fontset': 'stixsans', # Match sans-serif body text
        'pdf.fonttype': 42,             # Embedded TrueType
        'ps.fonttype': 42,
        'axes.unicode_minus': False,     # Prevent hyphen minus breakage

        # Clean Lineage & Spines (Despine top/right)
        'axes.linewidth': 0.6,
        'axes.edgecolor': '#333333',
        'axes.spines.top': False,
        'axes.spines.right': False,
        
        # Typography Hierarchy (Exact publication points)
        'axes.labelsize': base_size,
        'axes.labelweight': 'bold',
        'axes.titlesize': base_size,
        'axes.titleweight': 'bold',
        'xtick.labelsize': max(5.5, base_size - 1.0),
        'ytick.labelsize': max(5.5, base_size - 1.0),
        'legend.fontsize': max(5.5, base_size - 1.0),
        'legend.title_fontsize': base_size,

        # Ticks & Geometry (SciencePlots standard)
        'xtick.major.width': 0.6,
        'ytick.major.width': 0.6,
        'xtick.major.size': 3.0,
        'ytick.major.size': 3.0,
        'xtick.direction': 'out',
        'ytick.direction': 'out',
        'axes.grid': False,

        # Color Cycle
        'axes.prop_cycle': plt.cycler(color=palette),
        
        # Legend Defaults
        'legend.frameon': False,
    })
    return palette
