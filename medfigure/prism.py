"""
GraphPad Prism & ggprism reproduction theme for Matplotlib.
Faithfully recreates the iconic biomedical research visual standard from CSdaw/ggprism & GraphPad Prism.
"""
import matplotlib.pyplot as plt

PRISM_PALETTES = {
    # The most popular palette in biomedical papers (ggprism floral)
    "floral": ["#4878D0", "#EE854A", "#6ACC65", "#D65F5F", "#956CB4", "#8C613C", "#DC7EC0", "#797979", "#D5BB67", "#82C6E2"],
    # High-contrast clinical candy palette
    "candy": ["#5B8FF9", "#5AD8A6", "#5D7092", "#F6BD16", "#E8684A", "#6DC8EC", "#9270CA", "#FF9D4D", "#269A99", "#FF99C3"],
    # Classic Prism default
    "default": ["#333333", "#0072B2", "#D55E00", "#009E73", "#CC79A7", "#F0E442"],
    # Colorblind safe
    "colorblind": ["#0072B2", "#D55E00", "#009E73", "#E69F00", "#56B4E9", "#CC79A7", "#000000"]
}

def set_prism_style(palette="floral", base_size=8.0, spine_width=1.0):
    """
    Apply authentic GraphPad Prism / ggprism aesthetic parameters.
    - Solid 1.0pt L-shaped spines
    - Outward 4.0pt ticks with 1.0pt thickness
    - Crisp Arial typography
    - TrueType font embedding (pdf.fonttype=42)
    """
    colors = PRISM_PALETTES.get(palette, PRISM_PALETTES["floral"])
    
    plt.rcParams.update({
        # Typography: Arial is the universal Prism standard
        'font.family': 'sans-serif',
        'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
        'mathtext.fontset': 'stixsans',
        'pdf.fonttype': 42,
        'ps.fonttype': 42,
        'axes.unicode_minus': False,

        # Classic Prism Spines: Only Left and Bottom, 1.0pt solid black
        'axes.linewidth': spine_width,
        'axes.edgecolor': '#000000',
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.spines.left': True,
        'axes.spines.bottom': True,

        # Classic Prism Ticks: Outward, 1.0pt thick, 4.0pt long
        'xtick.direction': 'out',
        'ytick.direction': 'out',
        'xtick.major.width': spine_width,
        'ytick.major.width': spine_width,
        'xtick.major.size': 4.0,
        'ytick.major.size': 4.0,
        'xtick.color': '#000000',
        'ytick.color': '#000000',

        # Font Hierarchy (Prism bold style)
        'axes.labelsize': base_size,
        'axes.labelweight': 'bold',
        'axes.labelcolor': '#000000',
        'xtick.labelsize': base_size - 0.5,
        'ytick.labelsize': base_size - 0.5,
        'legend.fontsize': base_size - 1.0,
        'legend.frameon': False,

        # No background grid
        'axes.grid': False,
        'axes.prop_cycle': plt.cycler(color=colors),
    })
    return colors
