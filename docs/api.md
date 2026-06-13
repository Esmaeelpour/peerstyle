# API Reference

Everything in PeerStyle is reachable from the top-level package:

```python
import peerstyle
```

The public API is small by design — a handful of functions for applying styles, sizing and saving figures, and labeling curves.

## Quick reference

**Styling**

| Function | Description |
|----------|-------------|
| [`use_style`](#use_style) | Apply a style globally |
| [`style_context`](#style_context) | Apply a style temporarily — restores rcParams on exit |

**Sizing & exporting**

| Function | Description |
|----------|-------------|
| [`figsize`](#figsize) | Figure dimensions that fit a journal column |
| [`save`](#save) | Save a figure with publication defaults |

**Introspection**

| Function | Description |
|----------|-------------|
| [`list_styles`](#list_styles) | Names of all bundled styles |
| [`get_style_path`](#get_style_path) | Path to a bundled `.mplstyle` file |

**Curve labeling**

| Function | Description |
|----------|-------------|
| [`curved_text`](#curved_text) | Draw text following a curve |
| [`CurvedText`](#curvedtext) | Object-oriented form of `curved_text` |

---

## `use_style`

```python
peerstyle.use_style(name='custom_style', **kwargs)
```

Apply a style globally. The change persists until the next `use_style` call, `matplotlib.rcdefaults()`, or the end of the session. If the chosen style requests LaTeX (`text.usetex: True`) but no LaTeX install is found, PeerStyle automatically falls back to STIX fonts and prints a warning.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| `name` | `str` or `list[str]` | A style name, or a list of names stacked left-to-right (later entries win). |
| `figsize` | `tuple` | Shortcut for `figure.figsize`, e.g. `(5, 3)`. |
| `fontsize` | `float` | Shortcut for `font.size`. |
| `dpi` | `float` | Shortcut for `figure.dpi`. |
| `linewidth` | `float` | Shortcut for `lines.linewidth`. |
| `colormap` | `str` | Shortcut for `image.cmap`. |
| any `rcParam` | any | Any `matplotlib.rcParams` key passes straight through, e.g. `**{'axes.grid': False}`. |

**Returns** `None` — modifies the global rcParams in place.

**Examples**

```python
peerstyle.use_style('nature')
peerstyle.use_style(['ieee', 'bright'])
peerstyle.use_style(['nature', 'despine', 'no-latex'])
peerstyle.use_style('ieee', fontsize=9, figsize=(5, 3))
```

!!! tip "Presets vs. modifiers"
    Stack a **preset** (`ieee`, `nature`, …) with one or more **modifiers** (`bright`, `despine`, `no-latex`, …). The preset sets the overall look; modifiers tweak one aspect each. See [Styles](styles.md) for the full list.

---

## `style_context`

```python
with peerstyle.style_context(name='custom_style', **kwargs):
    ...
```

Context-manager form of [`use_style`](#use_style). The previous rcParams are restored automatically when the block exits — the safe choice in Jupyter notebooks, where leaking global state between cells causes hard-to-trace surprises, and inside functions that shouldn't affect the caller's settings.

Accepts exactly the same arguments as `use_style`.

**Returns** A context manager. Nothing is yielded — use it as a bare `with` block.

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
peerstyle.figsize(style='ieee', *, ncols=1, nrows=1, double_col=False, aspect=0.75)
```

Return `(width, height)` in inches for a figure that fits the given journal's column width. Pass the result straight to `plt.subplots`.

**Parameters**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `style` | `str` | `"ieee"` | Preset name used to look up the column width. Unknown names fall back to `(3.5, 7.0)`. |
| `ncols` | `int` | `1` | Number of subplot columns. Width scales linearly. |
| `nrows` | `int` | `1` | Number of subplot rows. Height scales linearly. |
| `double_col` | `bool` | `False` | Use the full double-column (full-page) width. |
| `aspect` | `float` | `0.75` | Single-panel height/width ratio. `0.75` = 4:3, `0.618` = golden ratio. |

**Returns** `tuple[float, float]` — `(width, height)` in inches.

**Column widths by style**

| Style | Single column | Double column |
|-------|--------------|---------------|
| `ieee` | 3.5 in | 7.25 in |
| `nature` | 3.504 in (89 mm) | 7.205 in (183 mm) |
| `custom_style` | 3.5 in | 7.0 in |
| `poster` | 12.0 in | 12.0 in |

!!! note "How height is computed"
    Height is always `single_column_width × aspect × nrows` — it is **not** based on the double-column width. So `double_col=True` makes a figure wider but not taller; bump `aspect` (or `nrows`) if you also need more height.

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

# Golden-ratio aspect
fig, ax = plt.subplots(figsize=peerstyle.figsize('ieee', aspect=0.618))
```

---

## `save`

```python
peerstyle.save(fig, path, **kwargs)
```

Save a figure with publication-ready defaults — equivalent to `fig.savefig(path, dpi=300, bbox_inches='tight', pad_inches=0.05)`. Any keyword argument overrides the corresponding default.

**Returns** `None`.

**Examples**

```python
peerstyle.save(fig, 'figure.pdf')                  # PDF at 300 DPI
peerstyle.save(fig, 'figure.png', dpi=600)         # PNG at 600 DPI
peerstyle.save(fig, 'figure.svg')                  # SVG (vector, DPI ignored)
peerstyle.save(fig, 'figure.pdf', pad_inches=0.1)  # more whitespace
```

!!! tip "Choosing a format"
    - **PDF** — preferred for LaTeX documents; vector and fully editable.
    - **SVG** — for HTML/web; vector and editable in Illustrator/Inkscape. All bundled styles set `pdf.fonttype: 42` and `svg.fonttype: none`, so text stays as editable text rather than outlines.
    - **PNG** — for Word or submission systems that reject vector formats. Use `dpi=300` or higher.

---

## `list_styles`

```python
peerstyle.list_styles()
```

Return the names of all bundled styles — both presets and modifiers.

**Returns** `list[str]`. Order is not guaranteed; wrap in `sorted()` if you need it deterministic.

```python
>>> sorted(peerstyle.list_styles())
['bright', 'custom_style', 'despine', 'grayscale', 'ieee',
 'muted', 'nature', 'no-latex', 'notebook', 'poster']
```

---

## `get_style_path`

```python
peerstyle.get_style_path(name='custom_style')
```

Return a `pathlib.Path` to the bundled `.mplstyle` file for `name`. Useful for inspecting a style's exact settings or copying one as the basis for your own. A trailing `.mplstyle` in `name` is accepted and ignored.

**Returns** `pathlib.Path` — the path is returned even if the file does not exist, so check with `.exists()` if `name` may be invalid.

```python
path = peerstyle.get_style_path('ieee')
print(path)
# .../peerstyle/styles/ieee.mplstyle

print(path.read_text())  # inspect the raw settings
```

---

## `curved_text`

```python
peerstyle.curved_text(ax, x, y, text, *, pos=0.5, anchor='center', offset=0.0, **kwargs)
```

Draw `text` along the curve `(x, y)` on `ax`. Each character is individually rotated to match the curve's local tangent, and the layout is recomputed on every draw — so labels keep following the curve through figure resizing and interactive panning.

**Parameters**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `ax` | `Axes` | — | The axes to draw into. |
| `x` | array-like | — | x-coordinates of the curve. 1-D, ≥ 2 finite points. |
| `y` | array-like | — | y-coordinates of the curve. Same shape as `x`. |
| `text` | `str` | — | The string to draw. |
| `pos` | `float` | `0.5` | Anchor position as a fraction of arc length (0 = start, 1 = end). |
| `anchor` | `str` | `"center"` | Which part of the label lands at `pos`: `"start"`, `"center"`, or `"end"`. |
| `offset` | `float` | `0.0` | Perpendicular offset in typographic points. Positive = above a left-to-right curve. |
| `**kwargs` | | | Forwarded to each character's `matplotlib.text.Text` (`color`, `fontsize`, `alpha`, `fontfamily`, …). |

**Returns** [`CurvedText`](#curvedtext) — the artist, in case you want to update or remove it later.

**Example**

```python
x = np.linspace(0, 2 * np.pi, 400)

fig, ax = plt.subplots()
ax.plot(x, np.sin(x), color='C0')
ax.plot(x, np.cos(x), color='C1')

peerstyle.curved_text(ax, x, np.sin(x), 'sin(x)', pos=0.10, offset=9,  color='C0')
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

Object-oriented form of [`curved_text`](#curved_text), subclassing `matplotlib.text.Text`. Reach for this when you want to hold onto the artist and manipulate it directly; otherwise `curved_text` is more convenient.

!!! warning "Argument order differs"
    `CurvedText` takes `axes` **after** `x, y, text` (matching `matplotlib.text.Text`), whereas `curved_text` takes `ax` **first** (matching matplotlib's axes-first helper functions).

**Example**

```python
from peerstyle import CurvedText

ct = CurvedText(x, y, 'along the curve', ax,
                pos=0.2, anchor='start', offset=4.0, color='C0')

ct.remove()  # remove it later if needed
```
