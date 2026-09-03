"""
Smart annotation, force-directed repulsion, and statistical significance brackets.
Integrates adjustText collision elimination.
"""
import matplotlib.pyplot as plt

def smart_repel_text(ax, x, y, labels, fontsize=6.5, arrow_color='#888888', **kwargs):
    """
    Repel overlapping text annotations using adjustText.
    """
    try:
        from adjustText import adjust_text
    except ImportError:
        raise ImportError("adjustText is required for smart_repel_text. Install it with: pip install adjustText")

    texts = [
        ax.text(xi, yi, str(lbl), fontsize=fontsize, va='center', ha='center')
        for xi, yi, lbl in zip(x, y, labels)
    ]
    
    arrowprops = kwargs.pop('arrowprops', dict(arrowstyle='->', color=arrow_color, lw=0.5))
    adjust_text(texts, ax=ax, arrowprops=arrowprops, **kwargs)
    return texts

def add_significance_bracket(ax, x1, x2, y, p_value, test_name=None, h_ratio=0.03, lw=0.75, fontsize=6.5):
    """
    Draw an academic significance bracket with exact p-value and optional test name.
    Strictly avoids vague asterisks (*).
    """
    y_range = ax.get_ylim()[1] - ax.get_ylim()[0]
    h = y_range * h_ratio
    
    # Draw bracket lines
    ax.plot([x1, x1, x2, x2], [y, y + h, y + h, y], lw=lw, c='#333333', clip_on=False)
    
    # Format p-value string
    if isinstance(p_value, (int, float)):
        if p_value < 0.001:
            p_str = "p < 0.001"
        else:
            p_str = f"p = {p_value:.3f}"
    else:
        p_str = str(p_value)
        
    if test_name:
        label_text = f"{p_str}\n({test_name})"
    else:
        label_text = p_str

    ax.text((x1 + x2) * 0.5, y + h * 1.1, label_text,
            ha='center', va='bottom', fontsize=fontsize, color='#333333', clip_on=False)
