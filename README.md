# Plot Styling

A custom Matplotlib styling package for scientific plots.

## Installation

```bash
pip install .
```

## Usage

```python
import matplotlib.pyplot as plt
import plot_styling

# Apply the custom style
plot_styling.use_style()

# Create a plot
plt.plot([1, 2, 3], [4, 5, 6])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Plot")
plt.show()
```

## Features

- High-quality serif fonts for scientific publications.
- Clean and consistent axes and grid settings.
- Preset color palettes.
- Easy to use and distribute.
