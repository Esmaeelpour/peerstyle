import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import peerstyle

_GALLERY_DPI = 150
# Poster fonts are 32-40pt so it needs a much bigger canvas than other styles
_FIGSIZE = {
    'poster': (10, 7.5),
}
_DEFAULT_FIGSIZE = (5, 3.75)


def _gallery_fig(style_name):
    """Return a figure sized correctly for the given style's font scale."""
    figsize = _FIGSIZE.get(style_name, _DEFAULT_FIGSIZE)
    return plt.subplots(figsize=figsize, constrained_layout=True)


def create_sample_plot(style_name, output_path=None):
    """Generate a sample plot using a specific style."""
    peerstyle.use_style(style_name)

    x = np.linspace(0, 10, 100)
    fig, ax = _gallery_fig(style_name)

    ax.plot(x, np.sin(x), label='sin(x)')
    ax.plot(x, np.cos(x), label='cos(x)')
    ax.plot(x, np.sin(x) * np.cos(x), label='sin(x)cos(x)')
    ax.set_xlabel('X-axis Label')
    ax.set_ylabel('Y-axis Label')
    ax.set_title(f'Style: {style_name}')
    ax.legend()

    if output_path:
        fig.savefig(output_path, dpi=_GALLERY_DPI, bbox_inches='tight')
        plt.close(fig)
        print(f"Saved preview for '{style_name}' to {output_path}")
    else:
        plt.show()


def create_curved_text_demo(style_name="nature", output_path=None):
    """Generate a demo plot showing curved text labeling with a given style."""
    peerstyle.use_style(style_name)

    x = np.linspace(0, 2 * np.pi, 400)
    fig, ax = _gallery_fig(style_name)

    curves = [
        (np.sin(x),      "sin(x)",    "C0", 0.10,  9),
        (np.cos(x),      "cos(x)",    "C1", 0.88, -9),
        (np.sin(2*x)/2,  "½ sin(2x)", "C2", 0.52,  9),
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
        print(f"Saved curved text demo to {output_path}")
    else:
        plt.show()


def generate_gallery(output_dir="docs/gallery"):
    """Generate preview images for all available styles plus the curved text demo."""
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    for style in peerstyle.list_styles():
        create_sample_plot(style, out_path / f"{style}.png")

    create_curved_text_demo("nature", out_path / "curved_text_demo.png")


if __name__ == "__main__":
    generate_gallery()
