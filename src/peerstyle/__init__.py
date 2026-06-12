import matplotlib
import matplotlib.pyplot as plt
from contextlib import contextmanager
from pathlib import Path

from ._curved_text import CurvedText, curved_text

__version__ = "0.1.4"

__all__ = [
    "use_style",
    "style_context",
    "list_styles",
    "get_style_path",
    "figsize",
    "save",
    "curved_text",
    "CurvedText",
]

# Journal column widths in inches: (single-column, double-column)
_COLUMN_WIDTHS = {
    "ieee":         (3.5,   7.25),
    "nature":       (3.504, 7.205),
    "custom_style": (3.5,   7.0),
    "poster":       (12.0,  12.0),
}

# Register all bundled .mplstyle files with matplotlib so they are
# accessible via plt.style.use('peerstyle.nature') without any import.
_styles_dir = Path(__file__).parent / "styles"
for _f in _styles_dir.glob("*.mplstyle"):
    _key = f"peerstyle.{_f.stem}"
    if _key not in matplotlib.style.core.library:
        matplotlib.style.core.library[_key] = matplotlib.rc_params_from_file(
            str(_f), fail_on_error=False, use_default_template=False
        )
        if _key not in matplotlib.style.core.available:
            matplotlib.style.core.available.append(_key)


def get_style_path(name="custom_style"):
    """Return the absolute path to a bundled .mplstyle file."""
    if name.endswith(".mplstyle"):
        name = name[:-9]
    return _styles_dir / f"{name}.mplstyle"


def list_styles():
    """Return names of all bundled styles."""
    return [f.stem for f in _styles_dir.glob("*.mplstyle")]


def _resolve(name):
    """Resolve a style name to a path string or pass through for mpl built-ins."""
    p = get_style_path(name)
    return str(p) if p.exists() else name


def _fix_latex_fallback():
    """If usetex is on but latex is missing, fall back to STIX (visually close)."""
    if plt.rcParams.get("text.usetex", False):
        import shutil
        if not shutil.which("latex"):
            plt.rcParams["text.usetex"] = False
            plt.rcParams["mathtext.fontset"] = "stix"
            plt.rcParams["font.family"] = "serif"
            print("Warning: LaTeX not found. Falling back to STIX fonts.")


def _apply_kwargs(kwargs):
    """Map convenience kwargs to rcParams keys and apply them."""
    aliases = {
        "figsize":   "figure.figsize",
        "fontsize":  "font.size",
        "dpi":       "figure.dpi",
        "linewidth": "lines.linewidth",
        "colormap":  "image.cmap",
    }
    if kwargs:
        plt.rcParams.update({aliases.get(k, k): v for k, v in kwargs.items()})


def use_style(name="custom_style", **kwargs):
    """Apply a peerstyle preset globally.

    Parameters
    ----------
    name : str or list of str
        Preset name(s) to apply. Stacking is supported::

            peerstyle.use_style(['nature', 'despine', 'no-latex'])

    **kwargs
        Convenience overrides applied on top of the preset.
        Supported shortcuts: ``figsize``, ``fontsize``, ``dpi``,
        ``linewidth``, ``colormap``. Any other key is passed directly
        to ``plt.rcParams``.
    """
    names = [name] if isinstance(name, str) else name
    plt.style.use([_resolve(n) for n in names])
    _apply_kwargs(kwargs)
    _fix_latex_fallback()


@contextmanager
def style_context(name="custom_style", **kwargs):
    """Context manager that applies a style and restores rcParams on exit.

    Parameters
    ----------
    name : str or list of str
        Same stacking syntax as :func:`use_style`.
    **kwargs
        Same convenience overrides as :func:`use_style`.

    Example
    -------
    ::

        with peerstyle.style_context('nature'):
            fig, ax = plt.subplots()
            ...
        # rcParams are restored here automatically
    """
    names = [name] if isinstance(name, str) else name
    with plt.style.context([_resolve(n) for n in names]):
        _apply_kwargs(kwargs)
        _fix_latex_fallback()
        yield


def figsize(style="ieee", *, ncols=1, nrows=1, double_col=False, aspect=0.75):
    """Return ``(width, height)`` in inches for a figure that fits a journal column.

    Parameters
    ----------
    style : str
        Preset name to look up the column width.
    ncols : int
        Number of subplot columns — width scales linearly.
    nrows : int
        Number of subplot rows — height scales linearly.
    double_col : bool
        Use the double-column (full-page) width instead.
    aspect : float
        Height/width ratio for a single panel (default 0.75 = 4:3).

    Example
    -------
    ::

        fig, axes = plt.subplots(1, 2, figsize=peerstyle.figsize('ieee', ncols=2))
    """
    col_w, full_w = _COLUMN_WIDTHS.get(style, (3.5, 7.0))
    w = full_w if double_col else col_w * ncols
    h = col_w * aspect * nrows
    return (w, h)


def save(fig, path, **kwargs):
    """Save *fig* with publication-ready defaults.

    Equivalent to ``fig.savefig(path, dpi=300, bbox_inches='tight',
    pad_inches=0.05)``. Any keyword argument overrides the defaults.
    """
    defaults = dict(dpi=300, bbox_inches="tight", pad_inches=0.05)
    defaults.update(kwargs)
    fig.savefig(path, **defaults)
