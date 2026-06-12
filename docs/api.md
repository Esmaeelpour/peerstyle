# API Reference

---

## `use_style`

```python
peerstyle.use_style(name, **kwargs)
```

Apply a style globally. Changes persist for the rest of the session (or until the next `use_style` call).

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| `name` | `str` or `list[str]` | Style name or list of names to stack. |
| `figsize` | `tuple` | Figure size in inches, e.g. `(5, 3)`. |
| `fontsize` | `float` | Base font size. |
| `dpi` | `float` | Figure DPI. |
| `linewidth` | `float` | Default line width. |
| `colormap` | `str` | Default colormap. |
| any `rcParam` key | any | Passed directly to `plt.rcParams`. |

**Examples**

```python
peerstyle.use_style('nature')
peerstyle.use_style(['ieee', 'bright'])
peerstyle.use_style('ieee', fontsize=9, figsize=(5, 3))
```

---

## `style_context`

```python
with peerstyle.style_context(name, **kwargs):
    ...
```

Context manager that applies a style and restores the previous rcParams on exit. Safe to use in Jupyter notebooks where polluting global state causes problems.

Accepts the same arguments as [`use_style`](#use_style).

**Example**

```python
with peerstyle.style_context('nature', fontsize=8):
    fig, ax = plt.subplots()
    ax.plot(x, y)
# rcParams fully restored here
```

---

## `figsize`

```python
peerstyle.figsize(style, *, ncols=1, nrows=1, double_col=False, aspect=0.75)
```

Returns `(width, height)` in inches sized to fit a journal's column width. Designed to be passed directly to `plt.subplots`.

**Parameters**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `style` | `str` | `"ieee"` | Preset name to look up the column width. |
| `ncols` | `int` | `1` | Number of subplot columns — width scales linearly. |
| `nrows` | `int` | `1` | Number of subplot rows — height scales linearly. |
| `double_col` | `bool` | `False` | Use the full double-column width instead of single. |
| `aspect` | `float` | `0.75` | Height/width ratio for a single panel (0.75 = 4:3). |

**Column widths**

| Style | Single column | Double column |
|-------|--------------|---------------|
| `ieee` | 3.5 in | 7.25 in |
| `nature` | 3.504 in (89 mm) | 7.205 in (183 mm) |
| `custom_style` | 3.5 in | 7.0 in |

**Examples**

```python
# Single panel
fig, ax = plt.subplots(figsize=peerstyle.figsize('ieee'))

# Two side-by-side panels, single-column width each
fig, axes = plt.subplots(1, 2, figsize=peerstyle.figsize('ieee', ncols=2))

# Two stacked panels
fig, axes = plt.subplots(2, 1, figsize=peerstyle.figsize('nature', nrows=2))

# Full double-column width
fig, ax = plt.subplots(figsize=peerstyle.figsize('nature', double_col=True))
```

---

## `save`

```python
peerstyle.save(fig, path, **kwargs)
```

Save a figure with publication-ready defaults: `dpi=300`, `bbox_inches='tight'`, `pad_inches=0.05`. Any keyword argument overrides the defaults.

**Examples**

```python
peerstyle.save(fig, 'figure.pdf')
peerstyle.save(fig, 'figure.png', dpi=600)
peerstyle.save(fig, 'figure.svg', dpi=150)
```

---

## `list_styles`

```python
peerstyle.list_styles()
```

Returns a sorted list of all available style names.

```python
>>> peerstyle.list_styles()
['bright', 'custom_style', 'despine', 'grayscale', 'ieee',
 'muted', 'nature', 'no-latex', 'notebook', 'poster']
```

---

## `curved_text`

```python
peerstyle.curved_text(ax, x, y, text, *, pos=0.5, anchor='center', offset=0.0, **kwargs)
```

Draw `text` along the curve `(x, y)` on `ax`. Each character is individually rotated to match the local tangent of the curve. The label recomputes its position on every draw, so it follows the curve through resizing and interactive panning.

**Parameters**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `ax` | `Axes` | — | The axes to draw into. |
| `x`, `y` | array-like | — | The curve in data coordinates. Must be 1-D, equal length, at least 2 points. |
| `text` | `str` | — | The string to draw. |
| `pos` | `float` | `0.5` | Anchor position as a fraction of arc length (0 = start, 1 = end). |
| `anchor` | `str` | `"center"` | Part of the label that lands at `pos`: `"start"`, `"center"`, or `"end"`. |
| `offset` | `float` | `0.0` | Perpendicular offset in typographic points. Positive is above a left-to-right curve. |
| `**kwargs` | | | Passed to each character's `matplotlib.text.Text` (e.g. `color`, `fontsize`, `alpha`). |

**Returns** `CurvedText`

**Examples**

```python
x = np.linspace(0, 2 * np.pi, 400)

fig, ax = plt.subplots()
ax.plot(x, np.sin(x), color='C0')
ax.plot(x, np.cos(x), color='C1')

peerstyle.curved_text(ax, x, np.sin(x), 'sin(x)', pos=0.10, offset=9, color='C0')
peerstyle.curved_text(ax, x, np.cos(x), 'cos(x)', pos=0.88, offset=-9, color='C1')
```

The object-oriented form is also available:

```python
from peerstyle import CurvedText

CurvedText(x, y, 'along the curve', ax, pos=0.2, anchor='start', offset=4.0)
```

!!! note "Credit"
    Curved text is adapted from [thiebes/curved-text](https://github.com/thiebes/curved-text) (MIT License).
