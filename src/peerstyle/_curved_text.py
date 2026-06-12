"""Draw text along an arbitrary curve in a matplotlib Axes.

Adapted from https://github.com/thiebes/curved-text (MIT License).
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

import matplotlib.text as mtext
import numpy as np

if TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import ArrayLike

__all__ = ["CurvedText", "curved_text"]

_ANCHORS = ("start", "center", "end")


class CurvedText(mtext.Text):
    """A string drawn along an (x, y) curve, one character at a time.

    Parameters
    ----------
    x, y : array-like
        The curve in data coordinates: 1-D, equal length, at least two points.
    text : str
        The string to draw.
    axes : matplotlib.axes.Axes
        The axes to draw into.
    pos : float, default 0.5
        Arc-length fraction in [0, 1] for the anchor point.
    anchor : {"start", "center", "end"}, default "center"
        Which part of the label sits at ``pos``.
    offset : float, default 0.0
        Perpendicular offset off the curve, in points (positive = above a
        left-to-right curve).
    **kwargs
        Passed to each per-character :class:`~matplotlib.text.Text`
        (e.g. ``color``, ``fontsize``, ``alpha``, ``fontfamily``).
    """

    def __init__(self, x: ArrayLike, y: ArrayLike, text: str, axes: Axes, *,
                 pos: float = 0.5, anchor: str = "center", offset: float = 0.0,
                 **kwargs: Any) -> None:
        if anchor not in _ANCHORS:
            raise ValueError(f"anchor must be one of {_ANCHORS}, got {anchor!r}")
        x = np.asarray(x, dtype=float)
        y = np.asarray(y, dtype=float)
        if x.ndim != 1 or x.shape != y.shape or x.size < 2:
            raise ValueError("x and y must be 1-D arrays of equal length >= 2")
        if not (np.isfinite(x).all() and np.isfinite(y).all()):
            raise ValueError("x and y must contain only finite values")
        super().__init__(float(x[0]), float(y[0]), " ", **kwargs)
        self._cx = x
        self._cy = y
        self._pos = float(pos)
        self._anchor = anchor
        self._offset = float(offset)
        axes.add_artist(self)
        self._chars: list[mtext.Text] = []
        for ch in text:
            t = mtext.Text(0.0, 0.0, " " if ch == " " else ch, **kwargs)
            t.set_ha("center")
            t.set_va("center")
            axes.add_artist(t)
            self._chars.append(t)

    def set_zorder(self, zorder) -> None:
        super().set_zorder(zorder)
        for t in getattr(self, "_chars", ()):
            t.set_zorder(self.get_zorder() + 1)

    def remove(self) -> None:
        for t in self._chars:
            t.remove()
        self._chars = []
        super().remove()

    def draw(self, renderer, *args, **kwargs) -> None:
        if not self._chars:
            return
        axes = self.axes
        pts = axes.transData.transform(np.column_stack([self._cx, self._cy]))
        xf, yf = pts[:, 0], pts[:, 1]
        arc = np.insert(np.cumsum(np.hypot(np.diff(xf), np.diff(yf))), 0, 0.0)
        if not np.isfinite(arc[-1]) or arc[-1] <= 0.0:
            return
        rads = np.arctan2(np.diff(yf), np.diff(xf))
        inv = axes.transData.inverted()

        for t in self._chars:
            t.set_rotation(0)
        widths = [t.get_window_extent(renderer=renderer).width for t in self._chars]
        total = float(sum(widths))

        def _point(s):
            i = int(np.clip(np.searchsorted(arc, s) - 1, 0, len(arc) - 2))
            d = arc[i + 1] - arc[i]
            f = (s - arc[i]) / d if d else 0.0
            return i, xf[i] + f * (xf[i + 1] - xf[i]), yf[i] + f * (yf[i + 1] - yf[i])

        s0 = self._pos * arc[-1]
        if self._anchor == "center":
            cursor = s0 - total / 2.0
        elif self._anchor == "end":
            cursor = s0 - total
        else:
            cursor = s0

        _, x0, y0 = _point(cursor)
        _, x1, y1 = _point(cursor + total)
        dx, dy = x1 - x0, y1 - y0
        norm = float(np.hypot(dx, dy))
        nx, ny = (-dy / norm, dx / norm) if norm else (0.0, 1.0)
        scale = self._offset * renderer.points_to_pixels(1.0)
        ox, oy = nx * scale, ny * scale

        for t, w in zip(self._chars, widths):
            i, px, py = _point(cursor + w / 2.0)
            t.set_position(inv.transform((px + ox, py + oy)))
            t.set_rotation(np.degrees(rads[i]))
            t.set_visible(True)
            cursor += w


def curved_text(ax: Axes, x: ArrayLike, y: ArrayLike, text: str, *,
                pos: float = 0.5, anchor: str = "center", offset: float = 0.0,
                **kwargs: Any) -> CurvedText:
    """Draw ``text`` along the curve ``(x, y)`` on ``ax``.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
    x, y : array-like
        The curve in data coordinates.
    text : str
        The string to draw.
    pos : float, default 0.5
        Arc-length fraction (0 = start, 1 = end) for the anchor point.
    anchor : {"start", "center", "end"}, default "center"
        Which part of the label sits at ``pos``.
    offset : float, default 0.0
        Perpendicular offset in points (positive = above a left-to-right curve).
    **kwargs
        Forwarded to each character's :class:`~matplotlib.text.Text`
        (e.g. ``color``, ``fontsize``).

    Returns
    -------
    CurvedText
    """
    return CurvedText(x, y, text, ax, pos=pos, anchor=anchor, offset=offset,
                      **kwargs)
