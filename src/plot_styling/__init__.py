import matplotlib.pyplot as plt
from pathlib import Path
import os

def get_style_path(name="custom_style"):
    """Return the absolute path to a included style file."""
    return Path(__file__).parent / "styles" / f"{name}.mplstyle"

def use_style(name="custom_style"):
    """
    Apply a custom Matplotlib style included in this package.
    
    Args:
        name (str): The name of the style to apply (without .mplstyle extension).
    """
    style_path = get_style_path(name)
    if style_path.exists():
        plt.style.use(str(style_path))
    else:
        # Fallback to standard matplotlib styles if not found in our package
        plt.style.use(name)

def register_styles():
    """Register all styles in this package with Matplotlib."""
    styles_dir = Path(__file__).parent / "styles"
    if styles_dir.exists():
        for style_file in styles_dir.glob("*.mplstyle"):
            # This is one way to make it available as a name
            # However, plt.style.use(path) is often more reliable
            pass

# For backward compatibility or immediate effect if imported
# (Optional: decide if we want to auto-apply)
