# Examples

---

## Basic usage

Apply a preset and save a publication-ready figure:

```python
import numpy as np
import matplotlib.pyplot as plt
import peerstyle

peerstyle.use_style('nature')

x = np.linspace(0, 10, 200)
fig, ax = plt.subplots(figsize=peerstyle.figsize('nature'))
ax.plot(x, np.sin(x), label='sin(x)')
ax.plot(x, np.cos(x), label='cos(x)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
peerstyle.save(fig, 'figure.pdf')
```

---

## Stacking styles

Stack a preset with one or more modifiers. Each modifier overrides only what it touches:

```python
# IEEE style + CVD-safe colours + no LaTeX required
peerstyle.use_style(['ieee', 'bright', 'no-latex'])

# Nature style, open axes, Jupyter-friendly sizes
peerstyle.use_style(['nature', 'despine', 'notebook'])

# Black-and-white print check
peerstyle.use_style(['ieee', 'grayscale'])
```

---

## Context manager in notebooks

`style_context` restores all rcParams when the block exits, so it never leaks into subsequent cells:

```python
with peerstyle.style_context('ieee', fontsize=9):
    fig, ax = plt.subplots(figsize=peerstyle.figsize('ieee'))
    ax.plot(x, y)
    peerstyle.save(fig, 'ieee_figure.pdf')

# Back to default matplotlib settings here
```

---

## Multi-panel figures

`figsize` scales correctly for any grid layout:

```python
peerstyle.use_style('nature')

# 1×2 side-by-side panels
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=peerstyle.figsize('nature', ncols=2))

# 2×1 stacked panels
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=peerstyle.figsize('ieee', nrows=2))

# Full double-column width
fig, ax = plt.subplots(figsize=peerstyle.figsize('nature', double_col=True))
```

---

## Curved text — direct line labeling

Label lines along their own paths instead of in a legend:

```python
peerstyle.use_style(['nature', 'bright'])

x = np.linspace(0, 2 * np.pi, 400)

fig, ax = plt.subplots(figsize=peerstyle.figsize('nature'))
ax.plot(x, np.sin(x),      color='C0')
ax.plot(x, np.cos(x),      color='C1')
ax.plot(x, np.sin(2*x)/2,  color='C2')

peerstyle.curved_text(ax, x, np.sin(x),     'sin(x)',    pos=0.10, offset=9,  color='C0')
peerstyle.curved_text(ax, x, np.cos(x),     'cos(x)',    pos=0.88, offset=-9, color='C1')
peerstyle.curved_text(ax, x, np.sin(2*x)/2, '½ sin(2x)', pos=0.52, offset=9,  color='C2')

peerstyle.save(fig, 'labeled_lines.pdf')
```

![curved text demo](gallery/curved_text_demo.png)

Three placement controls:

- **`pos`** — where on the curve (0 = start, 1 = end, as a fraction of arc length)
- **`anchor`** — which part of the label lands at `pos`: `"start"`, `"center"`, or `"end"`
- **`offset`** — perpendicular distance off the curve in typographic points

---

## Inline rcParam overrides

Pass any common param directly to `use_style` or `style_context`:

```python
# Override figure size and font size on top of the preset
peerstyle.use_style('ieee', figsize=(5, 3), fontsize=9)

# Or in a context manager
with peerstyle.style_context('nature', dpi=150, linewidth=1.5):
    fig, ax = plt.subplots()
    ...
```

---

## Using with Seaborn or Pandas

PeerStyle needs a `matplotlib.axes.Axes`, which both libraries provide:

```python
import seaborn as sns

peerstyle.use_style(['nature', 'bright'])

ax = sns.lineplot(data=df, x='x', y='y', hue='group')
peerstyle.save(ax.figure, 'seaborn_figure.pdf')
```

```python
# Pandas
ax = df.plot(x='time', y=['a', 'b', 'c'])
peerstyle.save(ax.figure, 'pandas_figure.pdf')
```
