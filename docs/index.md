# PeerStyle

**Publication-quality Matplotlib styling for peer-reviewed journals.**

[![CI](https://github.com/Esmaeelpour/peerstyle/actions/workflows/ci.yml/badge.svg)](https://github.com/Esmaeelpour/peerstyle/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/peerstyle)](https://pypi.org/project/peerstyle/)
[![Python](https://img.shields.io/pypi/pyversions/peerstyle)](https://pypi.org/project/peerstyle/)

PeerStyle gives you publication-ready Matplotlib figures in one line. Pick a journal preset, layer modifier styles on top, and export — no manual rcParams tuning required.

---

## Install

```bash
pip install peerstyle
```

Requires Python ≥ 3.8 and Matplotlib ≥ 3.5. No other dependencies.

---

## Quick start

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

Stack a preset with modifiers to compose exactly what you need:

```python
# IEEE style, CVD-safe colors, no LaTeX required
peerstyle.use_style(['ieee', 'bright', 'no-latex'])

# Nature style, open axes, Jupyter-friendly
peerstyle.use_style(['nature', 'despine', 'notebook'])
```

Use the context manager in notebooks — rcParams restore automatically on exit:

```python
with peerstyle.style_context('ieee'):
    fig, ax = plt.subplots(figsize=peerstyle.figsize('ieee'))
    ax.plot(x, y)
    peerstyle.save(fig, 'figure.pdf')
# default rcParams restored here
```

---

## Gallery

### Presets

| `custom_style` | `ieee` |
|:-:|:-:|
| ![custom_style](gallery/custom_style.png?v=5) | ![ieee](gallery/ieee.png?v=5) |

| `nature` | `poster` |
|:-:|:-:|
| ![nature](gallery/nature.png?v=5) | ![poster](gallery/poster.png?v=5) |

### Color modifiers

| `bright` | `muted` |
|:-:|:-:|
| ![bright](gallery/bright.png?v=5) | ![muted](gallery/muted.png?v=5) |

### Layout modifiers

| `grayscale` | `despine` |
|:-:|:-:|
| ![grayscale](gallery/grayscale.png?v=5) | ![despine](gallery/despine.png?v=5) |

### Curved text

Label lines directly along their paths — no legend needed.

![curved text demo](gallery/curved_text_demo.png?v=5)
