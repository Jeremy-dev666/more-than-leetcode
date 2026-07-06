# -*- coding: utf-8 -*-
"""Generate 2D prefix-sum schematic diagrams in the same pastel style as
prefix_sum_inclusion_exclusion.png (convention: x = row, y = col)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

BLUE   = dict(fc="#dce9f7", ec="#2b6cb0")
RED    = dict(fc="#fbe9e7", ec="#a94434")
GREEN  = dict(fc="#ddf0e8", ec="#1f8a5f")
ORANGE = dict(fc="#f9ecd2", ec="#9c7c1c")
VIOLET = dict(fc="#eae4f6", ec="#6b4fa3")
GRAY_EDGE = "#b3b3b3"
GRAY_DASH = "#a6a6a6"
INK = "#3a3a3a"

GAP = 0.46          # horizontal space between panels (operator lives here)
ROUND = 0.035


def rounded(x0, y0, w, h, fc, ec, lw):
    return FancyBboxPatch(
        (x0, y0), w, h,
        boxstyle=f"round,pad=0,rounding_size={ROUND}",
        fc=fc, ec=ec, lw=lw, mutation_aspect=1,
    )


def draw_panel(ax, ox, title, caption, regions, vlines, hlines, dots=()):
    """One unit square at x-offset `ox`.

    regions: list of (x0, y0, x1, y1, colors) in [0,1]^2, y measured upward
    vlines/hlines: dashed guide positions
    dots: (x, y, edgecolor) anchor markers
    """
    ax.add_patch(rounded(ox, 0, 1, 1, "white", GRAY_EDGE, 1.4))
    for vx in vlines:
        ax.plot([ox + vx, ox + vx], [0.015, 0.985],
                ls=(0, (4, 3)), lw=1.1, color=GRAY_DASH, zorder=2)
    for hy in hlines:
        ax.plot([ox + 0.015, ox + 0.985], [hy, hy],
                ls=(0, (4, 3)), lw=1.1, color=GRAY_DASH, zorder=2)
    for x0, y0, x1, y1, c in regions:
        ax.add_patch(rounded(ox + x0, y0, x1 - x0, y1 - y0,
                             c["fc"], c["ec"], 2.4))
    for dx, dy, ec in dots:
        ax.plot(ox + dx, dy, "o", ms=9, mfc=ec, mec="white", mew=1.6, zorder=6)
    ax.text(ox + 0.5, 1.22, title, ha="center", va="center",
            fontsize=15, color=INK)
    ax.text(ox + 0.5, -0.22, caption, ha="center", va="center",
            fontsize=15, color=INK)


def draw_figure(path, panels, ops):
    n = len(panels)
    total_w = n + (n - 1) * GAP
    fig, ax = plt.subplots(figsize=(3.1 * n, 3.1 * 2.0 / (total_w / n)))
    for i, p in enumerate(panels):
        draw_panel(ax, i * (1 + GAP), **p)
    for i, op in enumerate(ops):
        ax.text((i + 1) * (1 + GAP) - GAP / 2, 0.5, op,
                ha="center", va="center", fontsize=24, color=INK)
    ax.set_xlim(-0.15, total_w + 0.15)
    ax.set_ylim(-0.5, 1.5)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(path, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", path)


# ---------------------------------------------------------------- build ----
# S(x, y) = S(x-1, y) + S(x, y-1) - S(x-1, y-1) + a(x, y)
FX, FY = 0.72, 0.30   # vertical split at col FX; last row occupies y in [0, FY]
build = [
    dict(title=r"$S(x-1,\ y)$", caption="少最后一行",
         regions=[(0, FY, 1, 1, BLUE)], vlines=[FX], hlines=[FY]),
    dict(title=r"$S(x,\ y-1)$", caption="少最后一列",
         regions=[(0, 0, FX, 1, GREEN)], vlines=[FX], hlines=[FY]),
    dict(title=r"$S(x-1,\ y-1)$", caption="重叠算了两次,减掉",
         regions=[(0, FY, FX, 1, RED)], vlines=[FX], hlines=[FY]),
    dict(title=r"$a(x,\ y)$", caption="补上当前格",
         regions=[(FX, 0, 1, FY, VIOLET)], vlines=[FX], hlines=[FY]),
    dict(title=r"$S(x,\ y)$", caption="完整前缀和",
         regions=[(0, 0, 1, 1, ORANGE)], vlines=[FX], hlines=[FY]),
]
draw_figure("notes/assets/prefix-sum-2d-build.png", build, ["+", "−", "+", "="])

# ----------------------------------------------------------- difference ----
# Four point-updates on d; after prefix-summing, region (r1,c1)-(r2,c2) gains v.
# Visually: rows grow downward, cols rightward; an update at a point spreads
# to everything below-right of it.
C1, C2 = 0.32, 0.74   # col boundaries (x-axis)
R1, R2 = 0.72, 0.28   # row boundaries as y-up coords: r1 top edge, r2+1 bottom
VL, HL = [C1, C2], [R2, R1]
diff = [
    dict(title=r"$d(r_1,\ c_1)$  +$v$", caption="影响右下整片",
         regions=[(C1, 0, 1, R1, BLUE)], vlines=VL, hlines=HL,
         dots=[(C1, R1, BLUE["ec"])]),
    dict(title=r"$d(r_1,\ c_2{+}1)$  −$v$", caption="消掉右侧多余",
         regions=[(C2, 0, 1, R1, RED)], vlines=VL, hlines=HL,
         dots=[(C2, R1, RED["ec"])]),
    dict(title=r"$d(r_2{+}1,\ c_1)$  −$v$", caption="消掉下方多余",
         regions=[(C1, 0, 1, R2, RED)], vlines=VL, hlines=HL,
         dots=[(C1, R2, RED["ec"])]),
    dict(title=r"$d(r_2{+}1,\ c_2{+}1)$  +$v$", caption="补回多消的角",
         regions=[(C2, 0, 1, R2, GREEN)], vlines=VL, hlines=HL,
         dots=[(C2, R2, GREEN["ec"])]),
    dict(title="求前缀和之后", caption="目标区域整体 +v",
         regions=[(C1, R2, C2, R1, ORANGE)], vlines=VL, hlines=HL),
]
draw_figure("notes/assets/prefix-sum-2d-diff.png", diff, ["−", "−", "+", "="])
