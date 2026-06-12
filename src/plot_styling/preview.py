import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import plot_styling

def create_sample_plot(style_name, output_path=None):
    """Generate a sample plot using a specific style."""
    plot_styling.use_style(style_name)
    
    x = np.linspace(0, 10, 100)
    
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), label='sin(x)')
    ax.plot(x, np.cos(x), label='cos(x)')
    ax.plot(x, np.sin(x) * np.cos(x), label='sin(x)cos(x)')
    
    ax.set_xlabel('X-axis Label')
    ax.set_ylabel('Y-axis Label')
    ax.set_title(f'Style: {style_name}')
    ax.legend()
    
    if output_path:
        fig.savefig(output_path)
        plt.close(fig)
        print(f"Saved preview for '{style_name}' to {output_path}")
    else:
        plt.show()

def generate_gallery(output_dir="docs/gallery"):
    """Generate preview images for all available styles."""
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    styles = plot_styling.list_styles()
    for style in styles:
        create_sample_plot(style, out_path / f"{style}.png")

if __name__ == "__main__":
    generate_gallery()
