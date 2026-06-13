# Styles

PeerStyle has two kinds of styles:

- **Presets** — complete looks for a specific journal or context.
- **Modifiers** — focused single-purpose tweaks that layer on top of a preset.

Stack them by passing a list:

```python
peerstyle.use_style(['ieee', 'bright', 'no-latex'])
```

All bundled styles are registered with Matplotlib on import under a `peerstyle.` prefix, so they work anywhere a style name is accepted:

```python
plt.style.use('peerstyle.nature')
plt.style.use(['peerstyle.ieee', 'peerstyle.muted'])
```

---

## Quick reference

| Name | Type | Font | Figure width | DPI |
|------|------|------|-------------|-----|
| `custom_style` | preset | LaTeX serif | 3.5 in | 300 |
| `ieee` | preset | Times New Roman | 3.5 in | 300 |
| `nature` | preset | Arial/Helvetica | 89 mm | 300 |
| `poster` | preset | sans-serif | 12 in | 150 |
| `no-latex` | modifier | STIX (serif) | — | — |
| `despine` | modifier | — | — | — |
| `notebook` | modifier | — | 6 in | 100 |
| `bright` | modifier | — | — | — |
| `muted` | modifier | — | — | — |
| `grayscale` | modifier | — | — | — |

---

## Presets

### `custom_style`

General-purpose serif scientific style. Enables LaTeX text rendering, 300 DPI, and grid lines. A good starting point for any journal that does not have a specific preset.

![custom_style](gallery/custom_style.png?v=3){ width="500" }

**Key settings:** `text.usetex: True` · `font.family: serif` · `figure.figsize: 3.5×2.625 in` · `figure.dpi: 300`

---

### `ieee`

Follows IEEE journal submission guidelines. Times New Roman, inward ticks on all four sides, minor ticks enabled, and a CVD-friendly color cycle.

![ieee](gallery/ieee.png?v=3){ width="500" }

**Key settings:** `font.serif: Times New Roman` · `figure.figsize: 3.5×2.625 in` · `xtick.direction: in` · `xtick.minor.visible: True`

---

### `nature`

Follows Nature journal submission guidelines. Arial/Helvetica, compact font sizes, outward ticks, 89 mm single-column width.

![nature](gallery/nature.png?v=3){ width="500" }

**Key settings:** `font.family: sans-serif` · `figure.figsize: 3.504×2.628 in` · `axes.labelsize: 7` · `xtick.labelsize: 5`

---

### `poster`

High-visibility style for conference posters. Large fonts, thick lines, vibrant colors, 150 DPI.

![poster](gallery/poster.png?v=3){ width="500" }

**Key settings:** `figure.figsize: 12×9 in` · `lines.linewidth: 4` · `axes.titlesize: 40`

---

## Modifiers

Modifiers are designed to be stacked on top of a preset. Applied alone they modify matplotlib's default style.

---

### `no-latex`

Disables LaTeX and switches to STIX fonts, which are visually close to Computer Modern. Use this on machines without a LaTeX install, or anywhere `text.usetex: True` would fail.

```python
peerstyle.use_style(['ieee', 'no-latex'])
peerstyle.use_style(['custom_style', 'no-latex'])
```

!!! note "Automatic fallback"
    PeerStyle applies this fallback automatically when LaTeX is enabled in the preset but `latex` is not found on your system.

**Key settings:** `text.usetex: False` · `mathtext.fontset: stix` · `font.family: serif`

---

### `despine`

Removes the top and right axis spines. Standard in biology, statistics, and data science.

![despine](gallery/despine.png?v=3){ width="500" }

```python
peerstyle.use_style(['nature', 'despine'])
```

**Key settings:** `axes.spines.top: False` · `axes.spines.right: False`

---

### `notebook`

Bumps fonts and figure size for Jupyter notebooks, where journal-sized figures are too small to read on screen. Also disables LaTeX.

![notebook](gallery/notebook.png?v=3){ width="500" }

```python
peerstyle.use_style(['nature', 'notebook'])
peerstyle.use_style(['ieee', 'notebook'])
```

**Key settings:** `figure.figsize: 6×4.5 in` · `figure.dpi: 100` · `font.size: 12` · `text.usetex: False`

---

### `bright`

[Paul Tol's](https://personal.sron.nl/~pault/) CVD-safe bright colour palette. Distinguishable by people with colour-vision deficiency and in greyscale print.

![bright](gallery/bright.png?v=3){ width="500" }

```python
peerstyle.use_style(['ieee', 'bright'])
```

**Colors:** `#4477AA` · `#EE6677` · `#228833` · `#CCBB44` · `#66CCEE` · `#AA3377` · `#BBBBBB`

---

### `muted`

Paul Tol's CVD-safe muted colour palette. Softer than `bright` and better when you have many series.

![muted](gallery/muted.png?v=3){ width="500" }

```python
peerstyle.use_style(['nature', 'muted'])
```

**Colors:** `#332288` · `#88CCEE` · `#44AA99` · `#117733` · `#999933` · `#DDCC77` · `#CC6677` · `#882255` · `#AA4499`

---

### `grayscale`

Black and grey tones with varied linestyles. Use this to verify monochrome readability or to meet journal requirements for B&W print.

![grayscale](gallery/grayscale.png?v=3){ width="500" }

```python
peerstyle.use_style(['ieee', 'grayscale'])
```

**Key settings:** varied `color` + `linestyle` cycle · `image.cmap: gray`
