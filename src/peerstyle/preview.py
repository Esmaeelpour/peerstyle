import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import peerstyle

_GALLERY_DPI = 150

# All modifiers need a base so the canvas size, font scale, and line
# weight are consistent with the other gallery images.
# Using ieee as base gives the 3.5×2.625 journal canvas that all
# preset images share, making everything proportional at display size.
_MODIFIER_BASES = {
    'bright':   'ieee',
    'muted':    'ieee',
    'grayscale': 'ieee',
    'despine':  'nature',
    'no-latex': 'ieee',
    'notebook': 'nature',
}


def create_sample_plot(style_name, output_path=None):
    matplotlib.rcdefaults()

    base = _MODIFIER_BASES.get(style_name)
    if base:
        peerstyle.use_style([base, style_name])
    else:
        peerstyle.use_style(style_name)

    # Let every style use its own figsize from rcParams — no overrides.
    # poster at 12×9 is correct: its thick border and fonts are
    # proportional to that canvas, and scale normally at display size.
    fig, ax = plt.subplots()

    x = np.linspace(0, 10, 100)
    ax.plot(x, np.sin(x),           label='sin(x)')
    ax.plot(x, np.cos(x),           label='cos(x)')
    ax.plot(x, np.sin(x)*np.cos(x), label='sin(x)cos(x)')
    ax.set_xlabel('X-axis Label')
    ax.set_ylabel('Y-axis Label')
    ax.set_title(f'Style: {style_name}')
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
    fig, ax = plt.subplots()

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
