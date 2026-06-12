import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import peerstyle

_GALLERY_DPI = 150

# Canvas sizes per style (overrides the default)
# poster: 40pt fonts need a large canvas to look proportional
# notebook: matches the 6x4.5 figsize that notebook modifier sets
_FIGSIZE = {
    'poster':   (10, 6.0),   # landscape canvas; legend placed outside to the right
    'notebook': (6.0, 4.5),  # matches the 6x4.5 figsize that notebook modifier sets
}
_DEFAULT_FIGSIZE = (5, 3.75)

# Modifier styles need a base preset to show what they actually change
_MODIFIER_BASE = 'ieee'
_MODIFIERS = frozenset({'bright', 'muted', 'grayscale', 'despine', 'no-latex', 'notebook'})


def _make_fig(style_key):
    figsize = _FIGSIZE.get(style_key, _DEFAULT_FIGSIZE)
    return plt.subplots(figsize=figsize, constrained_layout=True)


def create_sample_plot(style_name, output_path=None):
    matplotlib.rcdefaults()

    if style_name in _MODIFIERS:
        peerstyle.use_style([_MODIFIER_BASE, style_name])
    else:
        peerstyle.use_style(style_name)

    x = np.linspace(0, 10, 100)
    fig, ax = _make_fig(style_name)

    ax.plot(x, np.sin(x),           label='sin(x)')
    ax.plot(x, np.cos(x),           label='cos(x)')
    ax.plot(x, np.sin(x)*np.cos(x), label='sin(x)cos(x)')
    ax.set_xlabel('X-axis Label')
    ax.set_ylabel('Y-axis Label')
    ax.set_title(f'Style: {style_name}')
    # poster's thick lines fill every corner; put the legend outside to the right
    if style_name == 'poster':
        ax.legend(loc='center left', bbox_to_anchor=(1.02, 0.5))
    else:
        ax.legend()

    if output_path:
        fig.savefig(output_path, dpi=_GALLERY_DPI, bbox_inches='tight')
        plt.close(fig)
        print(f"  saved {style_name}")
    else:
        plt.show()


def create_curved_text_demo(style_name='nature', output_path=None):
    matplotlib.rcdefaults()
    peerstyle.use_style(style_name)

    x = np.linspace(0, 2 * np.pi, 400)
    fig, ax = _make_fig(style_name)

    curves = [
        (np.sin(x),     'sin(x)',    'C0', 0.10,  9),
        (np.cos(x),     'cos(x)',    'C1', 0.88, -9),
        (np.sin(2*x)/2, '½ sin(2x)', 'C2', 0.52,  9),
    ]
    for y, label, color, pos, offset in curves:
        ax.plot(x, y, color=color)
        peerstyle.curved_text(ax, x, y, label,
                              pos=pos, offset=offset, color=color, fontsize=9)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Curved Text — Direct Line Labeling')

    if output_path:
        fig.savefig(output_path, dpi=_GALLERY_DPI, bbox_inches='tight')
        plt.close(fig)
        print('  saved curved_text_demo')
    else:
        plt.show()


def generate_gallery(output_dir='docs/gallery'):
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    for style in peerstyle.list_styles():
        create_sample_plot(style, out_path / f'{style}.png')

    create_curved_text_demo('nature', out_path / 'curved_text_demo.png')


if __name__ == '__main__':
    generate_gallery()
