# API Reference

## Quick reference

| Function | Description |
|----------|-------------|
| [`use_style`](#use_style) | Apply a style globally |
| [`style_context`](#style_context) | Context manager — restores rcParams on exit |
| [`figsize`](#figsize) | Return correct figure dimensions for a journal column |
| [`save`](#save) | Save a figure with publication defaults |
| [`list_styles`](#list_styles) | Return all available style names |
| [`get_style_path`](#get_style_path) | Return the path to a bundled `.mplstyle` file |
| [`curved_text`](#curved_text) | Draw text following a curve |
| [`CurvedText`](#curvedtext) | Object-oriented version of `curved_text` |

---

## `use_style`

```python
peerstyle.use_style(name, **kwargs)
```

Apply a style globally. Changes persist until the next `use_style` call or the end of the session.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| `name` | `str` or `list[str]` | Style name, or a list of names to stack in order. |
| `figsize` | `tuple` | Figure size override, e.g. `(5, 3)`. |
| `fontsize` | `float` | Base font size override. |
| `dpi` | `float` | Figure DPI override. |
| `linewidth` | `float` | Default line width override. |
| `colormap` | `str` | Default colormap override. |
| any `rcParam` key | any | Any key from `matplotlib.rcParams` is accepted directly, e.g. `**{'axes.grid': False}`. |

**Examples**

```python
peerstyle.use_style('nature')
peerstyle.use_style(['ieee', 'bright'])
peerstyle.use_style(['nature', 'despine', 'no-latex'])
peerstyle.use_style('ieee', fontsize=9, figsize=(5, 3))
```

---

## `style_context`

```python
with peerstyle.style_context(name, **kwargs):
    ...
```

Context manager version of [`use_style`](#use_style). The previous rcParams are restored automatically when the block exits — safe to use in Jupyter notebooks where leaking global state causes problems between cells.

Accepts exactly the same arguments as `use_style`.

**Example**

```python
with peerstyle.style_context('ieee', fontsize=9):
    fig, ax = plt.subplots(figsize=peerstyle.figsize('ieee'))
    ax.plot(x, y)
    peerstyle.save(fig, 'figure.pdf')
# default rcParams fully restored here
```

---

## `figsize`

```python
peerstyle.figsize(style, *, ncols=1, nrows=1, double_col=False, aspect=0.75)
```

Returns `(width, height)` in inches for a figure that fits the given journal's column width. Pass the result directly to `plt.subplots`.

**Parameters**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `style` | `str` | `"ieee"` | Preset name to look up the column width. |
| `ncols` | `int` | `1` | Number of subplot columns. Width scales linearly. |
| `nrows` | `int` | `1` | Number of subplot rows. Height scales linearly. |
| `double_col` | `bool` | `False` | Use the full double-column (full-page) width. |
| `aspect` | `float` | `0.75` | Height/width ratio for a single panel. `0.75` = 4:3, `0.618` = golden ratio. |

**Column widths by style**

| Style | Single column | Double column |
|-------|--------------|---------------|
| `ieee` | 3.5 in | 7.25 in |
| `nature` | 3.504 in (89 mm) | 7.205 in (183 mm) |
| `custom_style` | 3.5 in | 7.0 in |
| `poster` | 12.0 in | 12.0 in |

**Examples**

```python
# Single panel, single column
fig, ax = plt.subplots(figsize=peerstyle.figsize('ieee'))

# Two side-by-side panels
fig, axes = plt.subplots(1, 2, figsize=peerstyle.figsize('ieee', ncols=2))

# Two stacked panels
fig, axes = plt.subplots(2, 1, figsize=peerstyle.figsize('nature', nrows=2))

# Full double-column width
fig, ax = plt.subplots(figsize=peerstyle.figsize('nature', double_col=True))

# Golden ratio aspect
fig, ax = plt.subplots(figsize=peerstyle.figsize('ieee', aspect=0.618))
```

---

## `save`

```python
peerstyle.save(fig, path, **kwargs)
```

Save a figure with publication-ready defaults. Equivalent to calling `fig.savefig(path, dpi=300, bbox_inches='tight', pad_inches=0.05)`. Any keyword argument overrides the defaults.

**Examples**

```python
peerstyle.save(fig, 'figure.pdf')           # PDF at 300 DPI
peerstyle.save(fig, 'figure.png', dpi=600)  # PNG at 600 DPI
peerstyle.save(fig, 'figure.svg')           # SVG (vector, DPI ignored)
peerstyle.save(fig, 'figure.pdf', pad_inches=0.1)  # more padding
```

!!! tip "Format recommendations"
    - **PDF** — preferred for LaTeX documents; vector, fully editable.
    - **SVG** — for HTML/web use; vector, editable in Illustrator/Inkscape. All bundled styles set `pdf.fonttype: 42` and `svg.fonttype: none` so fonts remain editable.
    - **PNG** — for Word documents or online submission systems that don't accept vector formats. Use `dpi=300` minimum.

---

## `list_styles`

```python
peerstyle.list_styles()
```

Returns a list of all available style names (both presets and modifiers).

```python
>>> peerstyle.list_styles()
['bright', 'custom_style', 'despine', 'grayscale', 'ieee',
 'muted', 'nature', 'no-latex', 'notebook', 'poster']
```

---

## `get_style_path`

```python
peerstyle.get_style_path(name='custom_style')
```

Returns a `pathlib.Path` to the bundled `.mplstyle` file for `name`. Useful if you want to inspect or extend a style manually.

```python
path = peerstyle.get_style_path('ieee')
print(path)
# /path/to/peerstyle/styles/ieee.mplstyle

# Read the raw style settings
print(path.read_text())
```

---

## `curved_text`

```python
peerstyle.curved_text(ax, x, y, text, *, pos=0.5, anchor='center', offset=0.0, **kwargs)
```

Draw `text` along the curve `(x, y)` on `ax`. Each character is individually rotated to match the local tangent of the curve and recomputed on every draw, so the label follows the curve through figure resizing and interactive panning.

**Parameters**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `ax` | `Axes` | — | The axes to draw into. |
| `x` | array-like | — | x-coordinates of the curve. 1-D, at least 2 points, finite. |
| `y` | array-like | — | y-coordinates of the curve. Same shape as `x`. |
| `text` | `str` | — | The string to draw. |
| `pos` | `float` | `0.5` | Anchor position as a fraction of arc length (0 = start, 1 = end). |
| `anchor` | `str` | `"center"` | Which part of the label lands at `pos`: `"start"`, `"center"`, or `"end"`. |
| `offset` | `float` | `0.0` | Perpendicular offset in typographic points. Positive = above a left-to-right curve. |
| `**kwargs` | | | Forwarded to each character's `matplotlib.text.Text`, e.g. `color`, `fontsize`, `alpha`, `fontfamily`. |

**Returns** `CurvedText`

**Example**

```python
x = np.linspace(0, 2 * np.pi, 400)

fig, ax = plt.subplots()
ax.plot(x, np.sin(x), color='C0')
ax.plot(x, np.cos(x), color='C1')

peerstyle.curved_text(ax, x, np.sin(x), 'sin(x)', pos=0.10, offset=9, color='C0')
peerstyle.curved_text(ax, x, np.cos(x), 'cos(x)', pos=0.88, offset=-9, color='C1')
```

!!! tip "Placement tips"
    - Place labels on **flat portions** of the curve (near peaks or troughs) for the most readable result.
    - Spread `pos` values well apart so labels don't overlap — avoid clustering them in the `0.2–0.4` range.
    - Use positive `offset` to push a label above the curve, negative to push it below.

!!! note "Credit"
    Adapted from [thiebes/curved-text](https://github.com/thiebes/curved-text) (MIT License).

---

## `CurvedText`

```python
from peerstyle import CurvedText

CurvedText(x, y, text, axes, *, pos=0.5, anchor='center', offset=0.0, **kwargs)
```

Object-oriented form of [`curved_text`](#curved_text). Subclasses `matplotlib.text.Text`.

Note the argument order: `CurvedText` takes `axes` after `x, y, text` (matching `matplotlib.text.Text`), while `curved_text` takes `ax` first (matching matplotlib's axes-first helper functions).

**Example**

```python
from peerstyle import CurvedText

ct = CurvedText(x, y, 'along the curve', ax, pos=0.2, anchor='start', offset=4.0, color='C0')

# Remove later if needed
ct.remove()
```
