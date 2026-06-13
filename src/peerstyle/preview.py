import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import peerstyle

_GALLERY_DPI = 150

# Every gallery image is rendered at the SAME figure size and font scale
# so the thumbnails compare apples-to-apples (this is what matplotlib's own
# style gallery does). Each style still shows its real identity — colour
# cycle, serif/sans family, tick config, grid, spines, linestyles — only
# the preview's size and font sizes are normalised. Without this, nature's
# tiny 5-7pt fonts look microscopic next to poster's 40pt fonts when both
# are forced to the same display width.
_GALLERY_FIGSIZE = (5.0, 3.6)
_GALLERY_RC = {
    'figure.figsize':  _GALLERY_FIGSIZE,
    'figure.dpi':      _GALLERY_DPI,
    'font.size':       11,
    'axes.titlesize':  12,
    'axes.labelsize':  11,
    'legend.fontsize': 9,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'lines.linewidth': 1.6,
    'savefig.bbox':    'tight',
    'savefig.pad_inches': 0.05,
}

# Modifiers have no standalone look; stack them on a base preset so the
# thumbnail shows what the modifier actually changes.
_MODIFIER_BASES = {
    'bright':    'ieee',
    'muted':     'ieee',
    'grayscale': 'ieee',
    'despine':   'nature',
    'no-latex':  'ieee',
    'notebook':  'nature',
}


def _apply_style(style_name):
    matplotlib.rcdefaults()
    base = _MODIFIER_BASES.get(style_name)
    if base:
        peerstyle.use_style([base, style_name])
    else:
        peerstyle.use_style(style_name)
    # Normalise size/fonts last so they win over whatever the style set.
    plt.rcParams.update(_GALLERY_RC)


def create_sample_plot(style_name, output_path=None):
    _apply_style(style_name)

    x = np.linspace(0, 10, 100)
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x),           label='sin(x)')
    ax.plot(x, np.cos(x),           label='cos(x)')
    ax.plot(x, np.sin(x)*np.cos(x), label='sin(x)cos(x)')
    ax.set_xlabel('X-axis Label')
    ax.set_ylabel('Y-axis Label')
    ax.set_title(f'Style: {style_name}')
    ax.legend()

    if output_path:
        fig.savefig(output_path, dpi=_GALLERY_DPI)
        plt.close(fig)
        print(f"  saved {style_name}")
    else:
        plt.show()


def create_curved_text_demo(style_name='nature', output_path=None):
    _apply_style(style_name)

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
                              pos=pos, offset=offset, color=color, fontsize=10)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Curved Text — Direct Line Labeling')

    if output_path:
        fig.savefig(output_path, dpi=_GALLERY_DPI)
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
