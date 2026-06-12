# Changelog

---

## 0.1.4

**New modifier styles**

- `no-latex` — disables LaTeX and switches to STIX fonts as a close substitute
- `despine` — removes top and right spines
- `notebook` — larger fonts and figure size for Jupyter notebooks
- `bright` — Paul Tol's CVD-safe bright colour palette
- `muted` — Paul Tol's CVD-safe muted colour palette
- `grayscale` — black/grey tones with varied linestyles for B&W print

**New API**

- `style_context()` — context manager that restores rcParams on exit
- `figsize()` — returns exact figure dimensions for a journal's column width
- `save()` — one-line publication-ready `fig.savefig` wrapper
- `use_style()` now accepts inline kwarg overrides (`fontsize`, `figsize`, `dpi`, …)
- All bundled styles registered as `peerstyle.<name>` in matplotlib's style library on import

**Fixes**

- LaTeX fallback now switches to STIX fonts instead of silently degrading appearance
- `pdf.fonttype: 42` and `svg.fonttype: none` added to all styles (Illustrator-editable exports)
- `savefig.bbox: tight` added to all styles
- Minor ticks enabled in the `ieee` preset

---

## 0.1.3

**New feature**

- `curved_text()` and `CurvedText` class — draw text along an arbitrary curve, with each character rotated to match the local tangent. Adapted from [thiebes/curved-text](https://github.com/thiebes/curved-text) (MIT).

---

## 0.1.2

- Package renamed to **PeerStyle** (previously SciStyle).
- Repository moved to [Esmaeelpour/peerstyle](https://github.com/Esmaeelpour/peerstyle).

---

## 0.1.1

- Fixed README gallery images after repository rename.

---

## 0.1.0

Initial release.

- Four bundled styles: `custom_style`, `ieee`, `nature`, `poster`.
- `use_style()`, `list_styles()`, `get_style_path()`.
