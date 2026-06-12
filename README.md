# Plot Styling

A custom Matplotlib styling package for scientific plots.

## Installation

```bash
pip install .
```

## Usage

```python
import matplotlib.pyplot as plt
import plot_styling

# List available styles
print(plot_styling.list_styles())
# ['custom_style', 'ieee', 'nature', 'poster']

# Apply a specific style
plot_styling.use_style('nature')

# Or combine styles (e.g., use IEEE sizing with custom colors)
# plot_styling.use_style(['ieee', 'custom_style'])

# Create a plot
plt.plot([1, 2, 3], [4, 5, 6], label="Series 1")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Plot")
plt.legend()
plt.show()
```

## Visual Gallery

| `custom_style` | `ieee` |
|:---:|:---:|
| ![custom_style](docs/gallery/custom_style.png) | ![ieee](docs/gallery/ieee.png) |
| `nature` | `poster` |
| ![nature](docs/gallery/nature.png) | ![poster](docs/gallery/poster.png) |

## Available Styles

- `custom_style`: The default serif scientific style (high DPI, LaTeX enabled).
- `ieee`: Following IEEE journal guidelines (Times New Roman, specific sizing).
- `nature`: Following Nature journal guidelines (Sans-serif, compact).
- `poster`: High-visibility style with large fonts and thick lines for presentations.

## Features

- **Journal Presets**: Ready-to-use styles for IEEE, Nature, and more.
- **Modern Packaging**: Fully installable via `pip`.
- **High Quality**: Pre-configured for publication-quality PDF and PNG exports (300 DPI).
- **Flexible**: Combine multiple styles or use them alongside standard Matplotlib styles.
- **CI/CD**: Automated testing via GitHub Actions.
