# FAQ

---

## My figure looks different from the gallery — why?

The gallery images were generated with LaTeX rendering enabled. If `latex` is not installed on your machine, PeerStyle automatically falls back to STIX fonts, which are visually close but not identical. You will see a warning in the console:

```
Warning: LaTeX not found. Falling back to STIX fonts.
```

To get consistent output without installing LaTeX, explicitly add the `no-latex` modifier:

```python
peerstyle.use_style(['ieee', 'no-latex'])
```

---

## How do I reset to default Matplotlib settings?

```python
import matplotlib as mpl
mpl.rcdefaults()
```

Or use `style_context` so you never have to reset manually:

```python
with peerstyle.style_context('nature'):
    fig, ax = plt.subplots()
    ...
# defaults restored automatically
```

---

## My labels or tick marks are cut off when saving

This usually means `bbox_inches` was not set. Use `peerstyle.save` which sets `bbox_inches='tight'` by default:

```python
peerstyle.save(fig, 'figure.pdf')
```

If you use `fig.savefig` directly, add the argument yourself:

```python
fig.savefig('figure.pdf', bbox_inches='tight', pad_inches=0.05)
```

---

## Can I create my own custom style?

Yes. A `.mplstyle` file is plain text. Create one with only the settings you want to override:

```ini
# my_style.mplstyle
axes.prop_cycle: cycler('color', ['003f5c', '58508d', 'bc5090', 'ff6361', 'ffa600'])
lines.linewidth: 1.5
axes.linewidth: 0.8
```

Then load it by path:

```python
peerstyle.use_style('/path/to/my_style.mplstyle')

# or stack it with a preset
peerstyle.use_style(['ieee', '/path/to/my_style.mplstyle'])
```

---

## How do I use PeerStyle inside a function or class?

Use `style_context` so the style does not affect code outside the function:

```python
def make_figure(data):
    with peerstyle.style_context('nature'):
        fig, ax = plt.subplots(figsize=peerstyle.figsize('nature'))
        ax.plot(data)
        return fig
```

---

## Does PeerStyle work with Seaborn or Pandas?

Yes. Both render on Matplotlib axes, so `use_style` / `style_context` affect them as normal. For Seaborn, apply the style **before** calling Seaborn's theming functions — Seaborn's `set_theme()` will override rcParams set after it.

```python
peerstyle.use_style('nature')       # apply first
ax = sns.lineplot(x=x, y=y)        # then plot
```

---

## The `figsize` function doesn't have my journal's column width

Use the `aspect` parameter with a manual width instead:

```python
# ACS single column is 3.25 in
w = 3.25
fig, ax = plt.subplots(figsize=(w, w * 0.75))
```

Or open a GitHub issue to request a new preset.

---

## How do I make a style permanent (across sessions)?

Copy the `.mplstyle` file from the package:

```python
import shutil
import peerstyle

src = peerstyle.get_style_path('nature')
dst = Path.home() / '.config' / 'matplotlib' / 'stylelib' / 'nature.mplstyle'
dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copy(src, dst)
```

Then in any script, without importing peerstyle:

```python
import matplotlib.pyplot as plt
plt.style.use('nature')
```
