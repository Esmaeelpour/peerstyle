# SciStyle

A custom Matplotlib styling package for scientific plots.

## Installation

```bash
pip install scistyle
```

## Usage

```python
import matplotlib.pyplot as plt
import scistyle

# List available styles
print(scistyle.list_styles())
# ['custom_style', 'ieee', 'nature', 'poster']

# Apply a specific style
scistyle.use_style('nature')

# Or combine styles (e.g., use IEEE sizing with custom colors)
# scistyle.use_style(['ieee', 'custom_style'])

# Create a plot
plt.plot([1, 2, 3], [4, 5, 6], label="Series 1")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Plot")
plt.legend()
plt.show()
```

## Visual Gallery

<div align="center">

| Default (`custom_style`) | IEEE Journal (`ieee`) |
|:---:|:---:|
| <img src="https://raw.githubusercontent.com/Esmaeelpour/scistyle/main/docs/gallery/custom_style.png" width="400"> | <img src="https://raw.githubusercontent.com/Esmaeelpour/scistyle/main/docs/gallery/ieee.png" width="400"> |

| Nature Journal (`nature`) | Presentation Poster (`poster`) |
|:---:|:---:|
| <img src="https://raw.githubusercontent.com/Esmaeelpour/scistyle/main/docs/gallery/nature.png" width="400"> | <img src="https://raw.githubusercontent.com/Esmaeelpour/scistyle/main/docs/gallery/poster.png" width="400"> |

</div>

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
