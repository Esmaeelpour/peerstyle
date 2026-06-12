# PeerStyle

Publication-quality Matplotlib styling for peer-reviewed journals.

## Installation

```bash
pip install peerstyle
```

## Usage

```python
import matplotlib.pyplot as plt
import peerstyle

# List available styles
print(peerstyle.list_styles())
# ['custom_style', 'ieee', 'nature', 'poster']

# Apply a specific style
peerstyle.use_style('nature')
```

## Visual Gallery

<div align="center">

| Default (`custom_style`) | IEEE Journal (`ieee`) |
|:---:|:---:|
| <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/custom_style.png" width="400"> | <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/ieee.png" width="400"> |

| Nature Journal (`nature`) | Presentation Poster (`poster`) |
|:---:|:---:|
| <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/nature.png" width="400"> | <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/poster.png" width="400"> |

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
