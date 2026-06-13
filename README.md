# PeerStyle

Publication-quality Matplotlib styling for peer-reviewed journals.

Yeah, you can prompt an LLM to spit out an rcParams block. I did that for a while too. But you still end up tweaking it every time, it drifts between projects, and half the time the font sizes are just vibes. So I packaged mine up properly.

[![CI](https://github.com/Esmaeelpour/peerstyle/actions/workflows/ci.yml/badge.svg)](https://github.com/Esmaeelpour/peerstyle/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/peerstyle)](https://pypi.org/project/peerstyle/)
[![Python](https://img.shields.io/pypi/pyversions/peerstyle)](https://pypi.org/project/peerstyle/)

---

## Gallery

<div align="center">

| `custom_style` | `ieee` |
|:---:|:---:|
| <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/custom_style.png?v=5" width="380"> | <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/ieee.png?v=5" width="380"> |

| `nature` | `poster` |
|:---:|:---:|
| <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/nature.png?v=5" width="380"> | <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/poster.png?v=5" width="380"> |

| `bright` | `muted` |
|:---:|:---:|
| <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/bright.png?v=5" width="380"> | <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/muted.png?v=5" width="380"> |

| `grayscale` | `despine` |
|:---:|:---:|
| <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/grayscale.png?v=5" width="380"> | <img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/despine.png?v=5" width="380"> |

</div>

---

## Installation

```bash
pip install peerstyle
```

---

## Usage

**Apply a style globally:**

```python
import peerstyle

peerstyle.use_style('nature')
```

**Stack styles** — presets and modifiers compose freely:

```python
peerstyle.use_style(['ieee', 'bright', 'no-latex'])
```

**Use as a context manager** — rcParams restore automatically on exit, safe in notebooks:

```python
with peerstyle.style_context('nature'):
    fig, ax = plt.subplots()
    ax.plot(x, y)
```

**Get the right figure size for a journal column:**

```python
fig, ax = plt.subplots(figsize=peerstyle.figsize('ieee'))
fig, axes = plt.subplots(1, 2, figsize=peerstyle.figsize('ieee', ncols=2))
fig, ax = plt.subplots(figsize=peerstyle.figsize('nature', double_col=True))
```

**Save with publication defaults** (`dpi=300`, `bbox_inches='tight'`):

```python
peerstyle.save(fig, 'figure.pdf')
```

---

## Styles

### Presets

Full looks for a specific journal or context.

| Name | Description |
|------|-------------|
| `custom_style` | Default serif scientific style with LaTeX |
| `ieee` | IEEE journal — Times New Roman, 3.5 in column, ticks in |
| `nature` | Nature journal — Arial, 89 mm column, ticks out |
| `poster` | High-visibility for conference posters |

### Modifiers

Small, focused tweaks designed to be layered on top of a preset.

| Name | What it does |
|------|-------------|
| `no-latex` | Disables LaTeX, uses STIX fonts (visually close to Computer Modern) |
| `despine` | Removes top and right spines — common in biology and statistics |
| `notebook` | Larger fonts and figure size for Jupyter notebooks |
| `bright` | [Paul Tol's](https://personal.sron.nl/~pault/) CVD-safe bright colour palette |
| `muted` | Paul Tol's CVD-safe muted palette — softer, good for many series |
| `grayscale` | Black/grey with varied linestyles for B&W print |

All bundled styles are also registered with matplotlib on import, so they work anywhere a style name is accepted:

```python
plt.style.use('peerstyle.nature')
plt.style.use(['peerstyle.ieee', 'peerstyle.muted', 'peerstyle.no-latex'])
```

---

## Curved Text

Label lines along their own paths — no legend needed.

```python
peerstyle.curved_text(ax, x, np.sin(x), 'sin(x)', pos=0.10, offset=9, color='C0')
peerstyle.curved_text(ax, x, np.cos(x), 'cos(x)', pos=0.88, offset=-9, color='C1')
```

<div align="center">
<img src="https://raw.githubusercontent.com/Esmaeelpour/peerstyle/main/docs/gallery/curved_text_demo.png?v=5" width="500">
</div>

| Parameter | Default | Description |
|-----------|---------|-------------|
| `pos` | `0.5` | Anchor position as a fraction of arc length (0 = start, 1 = end) |
| `anchor` | `"center"` | Part of the label that lands at `pos`: `"start"`, `"center"`, or `"end"` |
| `offset` | `0.0` | Perpendicular offset in points — positive is above a left-to-right curve |

Extra kwargs (`color`, `fontsize`, `alpha`, …) pass through to each character's `Text`. An object-oriented `CurvedText` class is also available for those who prefer it.

> Curved text adapted from [thiebes/curved-text](https://github.com/thiebes/curved-text) (MIT) — go give it a star.

---

## API Reference

| Function | Description |
|----------|-------------|
| `use_style(name, **kwargs)` | Apply a style globally. Accepts a name or list. Kwargs: `figsize`, `fontsize`, `dpi`, `linewidth`, `colormap`. |
| `style_context(name, **kwargs)` | Context manager version of `use_style` — restores rcParams on exit. |
| `figsize(style, *, ncols, nrows, double_col, aspect)` | Returns `(w, h)` in inches for the journal's column width. |
| `save(fig, path, **kwargs)` | Saves with `dpi=300`, `bbox_inches='tight'` by default. |
| `list_styles()` | Returns a list of all available style names. |
| `curved_text(ax, x, y, text, *, pos, anchor, offset, **kwargs)` | Draws text following a curve. |
