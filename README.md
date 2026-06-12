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
- **Curved Text**: Label lines directly along their paths — no legend needed.
- **CI/CD**: Automated testing via GitHub Actions.

## Curved Text — Direct Line Labeling

Label curves along their own paths instead of in a legend, so the eye never
leaves the data to decode a colour key.

```python
import numpy as np
import matplotlib.pyplot as plt
import peerstyle

peerstyle.use_style('nature')

x = np.linspace(0, 2 * np.pi, 400)

fig, ax = plt.subplots()
ax.plot(x, np.sin(x), color='C0')
ax.plot(x, np.cos(x), color='C1')

peerstyle.curved_text(ax, x, np.sin(x), 'sin(x)', pos=0.25, offset=6, color='C0')
peerstyle.curved_text(ax, x, np.cos(x), 'cos(x)', pos=0.30, offset=6, color='C1')

plt.show()
```

<div align="center">
<img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/curved_text_demo.png" width="500">
</div>

Placement is controlled by three parameters:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `pos` | `0.5` | Where the label is anchored along the curve, as a fraction of arc length (0 = start, 1 = end). |
| `anchor` | `"center"` | Which part of the label lands at `pos`: `"start"`, `"center"`, or `"end"`. |
| `offset` | `0.0` | Perpendicular shift off the curve in typographic points. Positive is above a left-to-right curve. |

Extra keyword arguments (`color`, `fontsize`, `alpha`, `fontfamily`, …) are
passed through to each character's `matplotlib.text.Text`.

The object-oriented form is also available:

```python
from peerstyle import CurvedText

CurvedText(x, y, 'along the curve', ax, pos=0.2, anchor='start', offset=4.0)
```

The label recomputes its position on every draw, so it keeps following the
curve through figure resizing and interactive panning or zooming.

> Curved text support is adapted from [thiebes/curved-text](https://github.com/thiebes/curved-text) (MIT License) — go give it a star.
