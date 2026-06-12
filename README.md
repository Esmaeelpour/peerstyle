# PeerStyle

Publication-quality Matplotlib styling for peer-reviewed journals.

## Installation

```bash
pip install peerstyle
```

## Quick start

```python
import matplotlib.pyplot as plt
import peerstyle

peerstyle.use_style('nature')

fig, ax = plt.subplots(figsize=peerstyle.figsize('nature'))
ax.plot(x, y)
peerstyle.save(fig, 'figure.pdf')
```

## Styles

PeerStyle has two kinds of styles: **presets** (full looks for a specific journal or context) and **modifiers** (small tweaks you layer on top). Stack them freely:

```python
peerstyle.use_style(['ieee', 'bright', 'no-latex'])
```

### Presets

| Name | Description |
|------|-------------|
| `ieee` | IEEE journal — Times New Roman, 3.5 in column, ticks in |
| `nature` | Nature journal — Arial, 89 mm column, ticks out |
| `custom_style` | Default serif scientific style with LaTeX |
| `poster` | High-visibility for conference posters |

<div align="center">

| `custom_style` | `ieee` |
|:---:|:---:|
| <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/custom_style.png" width="380"> | <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/ieee.png" width="380"> |

| `nature` | `poster` |
|:---:|:---:|
| <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/nature.png" width="380"> | <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/poster.png" width="380"> |

</div>

### Modifiers

| Name | What it does |
|------|-------------|
| `no-latex` | Disables LaTeX, switches to STIX fonts (visually close to Computer Modern) |
| `despine` | Removes top and right spines — common in biology and statistics |
| `notebook` | Larger fonts and figure size for Jupyter notebooks |
| `bright` | [Paul Tol's](https://personal.sron.nl/~pault/) CVD-safe bright colour palette |
| `muted` | Paul Tol's CVD-safe muted colour palette (softer, good for many series) |
| `grayscale` | Black/grey with varied linestyles — for B&W print and monochrome checks |

<div align="center">

| `bright` | `muted` |
|:---:|:---:|
| <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/bright.png" width="380"> | <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/muted.png" width="380"> |

| `grayscale` | `despine` |
|:---:|:---:|
| <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/grayscale.png" width="380"> | <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/despine.png" width="380"> |

</div>

## API

### `use_style(name, **kwargs)`

Apply a style globally. Accepts a single name or a list for stacking.
Keyword overrides are applied on top: `figsize`, `fontsize`, `dpi`, `linewidth`, `colormap`.

```python
peerstyle.use_style('nature')
peerstyle.use_style(['ieee', 'bright'])
peerstyle.use_style('ieee', fontsize=9, figsize=(5, 3))
```

### `style_context(name, **kwargs)`

Context manager — restores rcParams automatically on exit. Safe to use in notebooks.

```python
with peerstyle.style_context('nature'):
    fig, ax = plt.subplots()
    ax.plot(x, y)
# rcParams restored here
```

### `figsize(style, *, ncols=1, nrows=1, double_col=False, aspect=0.75)`

Returns `(width, height)` in inches for a figure that fits the journal's column width.

```python
fig, ax   = plt.subplots(figsize=peerstyle.figsize('ieee'))
fig, axes = plt.subplots(1, 2, figsize=peerstyle.figsize('ieee', ncols=2))
fig, axes = plt.subplots(2, 1, figsize=peerstyle.figsize('nature', nrows=2))
fig, ax   = plt.subplots(figsize=peerstyle.figsize('nature', double_col=True))
```

### `save(fig, path, **kwargs)`

Save with publication defaults (`dpi=300`, `bbox_inches='tight'`). Any kwarg overrides.

```python
peerstyle.save(fig, 'figure.pdf')
peerstyle.save(fig, 'figure.png', dpi=600)
```

### `list_styles()`

```python
print(peerstyle.list_styles())
# ['bright', 'custom_style', 'despine', 'grayscale', 'ieee',
#  'muted', 'nature', 'no-latex', 'notebook', 'poster']
```

## Curved Text — Direct Line Labeling

Label curves along their own paths instead of in a legend, so the eye never
leaves the data to decode a colour key.

```python
x = np.linspace(0, 2 * np.pi, 400)

fig, ax = plt.subplots()
ax.plot(x, np.sin(x), color='C0')
ax.plot(x, np.cos(x), color='C1')

peerstyle.curved_text(ax, x, np.sin(x), 'sin(x)', pos=0.10, offset=9, color='C0')
peerstyle.curved_text(ax, x, np.cos(x), 'cos(x)', pos=0.88, offset=-9, color='C1')
```

<div align="center">
<img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/curved_text_demo.png" width="500">
</div>

| Parameter | Default | Description |
|-----------|---------|-------------|
| `pos` | `0.5` | Position along the curve as a fraction of arc length (0 = start, 1 = end) |
| `anchor` | `"center"` | Which part of the label lands at `pos`: `"start"`, `"center"`, or `"end"` |
| `offset` | `0.0` | Perpendicular offset in points — positive is above a left-to-right curve |

Extra kwargs (`color`, `fontsize`, `alpha`, …) pass through to each character's `Text`.

The object-oriented form is also available:

```python
from peerstyle import CurvedText
CurvedText(x, y, 'along the curve', ax, pos=0.2, anchor='start', offset=4.0)
```

> Curved text support is adapted from [thiebes/curved-text](https://github.com/thiebes/curved-text) (MIT License) — go give it a star.

## Registered style names

On import, PeerStyle registers all bundled styles with matplotlib under a `peerstyle.` prefix, so they work anywhere matplotlib accepts a style name:

```python
plt.style.use('peerstyle.nature')
plt.style.use(['peerstyle.ieee', 'peerstyle.bright'])
```
