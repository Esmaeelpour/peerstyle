# PeerStyle

**Publication-quality Matplotlib styling for peer-reviewed journals.**

[![CI](https://github.com/Esmaeelpour/peerstyle/actions/workflows/ci.yml/badge.svg)](https://github.com/Esmaeelpour/peerstyle/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/peerstyle)](https://pypi.org/project/peerstyle/)
[![Python](https://img.shields.io/pypi/pyversions/peerstyle)](https://pypi.org/project/peerstyle/)

PeerStyle gives you publication-ready Matplotlib figures in one line. Pick a journal preset, optionally stack modifier styles on top, and export — no manual rcParams tuning required.

---

## Install

```bash
pip install peerstyle
```

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

**Stack styles** — presets and modifiers compose freely:

```python
peerstyle.use_style(['ieee', 'bright', 'no-latex'])
```

**Safe in notebooks** — use the context manager to restore rcParams automatically:

```python
with peerstyle.style_context('nature'):
    fig, ax = plt.subplots()
    ax.plot(x, y)
# rcParams restored here
```

---

## Gallery

<div class="grid" markdown>

| `custom_style` | `ieee` |
|:-:|:-:|
| ![custom_style](gallery/custom_style.png) | ![ieee](gallery/ieee.png) |

| `nature` | `poster` |
|:-:|:-:|
| ![nature](gallery/nature.png) | ![poster](gallery/poster.png) |

| `bright` | `muted` |
|:-:|:-:|
| ![bright](gallery/bright.png) | ![muted](gallery/muted.png) |

| `grayscale` | `despine` |
|:-:|:-:|
| ![grayscale](gallery/grayscale.png) | ![despine](gallery/despine.png) |

</div>
