import matplotlib.pyplot as plt
from pathlib import Path
import os

__version__ = "0.1.0"

def get_style_path(name="custom_style"):
    """Return the absolute path to a included style file."""
    # Handle the case where the user might include the extension
    if name.endswith(".mplstyle"):
        name = name[:-9]
    return Path(__file__).parent / "styles" / f"{name}.mplstyle"

def list_styles():
    """List all available custom styles in this package."""
    styles_dir = Path(__file__).parent / "styles"
    if styles_dir.exists():
        return [f.stem for f in styles_dir.glob("*.mplstyle")]
    return []

def use_style(name="custom_style"):
    """
    Apply a custom Matplotlib style included in this package.
    
    Args:
        name (str or list): The name(s) of the style(s) to apply.
    """
    if isinstance(name, list):
        style_paths = []
        for n in name:
            path = get_style_path(n)
            style_paths.append(str(path) if path.exists() else n)
        plt.style.use(style_paths)
    else:
        style_path = get_style_path(name)
        if style_path.exists():
            plt.style.use(str(style_path))
        else:
            plt.style.use(name)
    
    # Check if LaTeX is requested but not available
    if plt.rcParams.get("text.usetex", False):
        import shutil
        if not shutil.which("latex"):
            print("Warning: LaTeX not found. Disabling 'text.usetex' for this session.")
            plt.rcParams["text.usetex"] = False

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
