import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import peerstyle

_GALLERY_DPI = 150

# Modifier styles are shown stacked on a preset so the visitor can see
# what each modifier changes. Bases match the canonical usage examples
# in the docs and are varied so modifier images look distinct from each other.
_MODIFIER_BASES = {
    'bright':   'nature',   # nature base so the color shift is obvious
    'muted':    'nature',
    'grayscale': 'ieee',
    'despine':  'nature',
    'no-latex': 'ieee',
    'notebook': 'nature',
}

# poster uses a smaller canvas so the 40pt fonts look dramatic at display size
_FIGSIZE = {'poster': (6, 4.5)}


def create_sample_plot(style_name, output_path=None):
    matplotlib.rcdefaults()

    base = _MODIFIER_BASES.get(style_name)
    if base:
        peerstyle.use_style([base, style_name])
    else:
        peerstyle.use_style(style_name)

    figsize = _FIGSIZE.get(style_name)
    x = np.linspace(0, 10, 100)
    fig, ax = plt.subplots(figsize=figsize)  # None → style controls its own size

    # poster uses only 2 curves; 3 oscillating curves leave no room for the
    # large legend box that the 40pt font produces on a small canvas
    if style_name == 'poster':
        ax.plot(x, np.sin(x), label='sin(x)')
        ax.plot(x, np.cos(x), label='cos(x)')
    else:
        ax.plot(x, np.sin(x),           label='sin(x)')
        ax.plot(x, np.cos(x),           label='cos(x)')
        ax.plot(x, np.sin(x)*np.cos(x), label='sin(x)cos(x)')
    ax.set_xlabel('X-axis Label')
    ax.set_ylabel('Y-axis Label')
    ax.set_title(f'Style: {style_name}')
    # poster's thick lines fill the axes; horizontal legend below is a common poster layout
    if style_name == 'poster':
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.22), ncol=2)
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
