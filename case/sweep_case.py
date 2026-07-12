"""Sweep Bling MX — Enclosed Case, Left Half (CadQuery).

Usage:
    python3 sweep_case.py top | bottom | both
"""

import cadquery as cq
import sys
from pathlib import Path

# ============================================================
# Parameters
# ============================================================

WALL = 2.5
WALL_EXTRA = 2.0
PCB_CLR = 0.2
PCB_THICK = 1.6
STANDOFF = 4.5

BOT_H = WALL + STANDOFF + PCB_THICK  # 8.6
CAV_H = 5.5
PLT_H = 7.7
TOP_H = CAV_H + PLT_H  # 13.2
WELL_DEPTH = 6.0
PCB_W = 113.466

BOSS_D = 7.0
THRU_D = 2.2
CSINK_D = 4.0
CSINK_Z = 2.0

LIP_T = 0.9
LIP_H = 1.5
GROOVE_T = 1.0
GROOVE_H = 1.6

MAG_D = 8.2
MAG_Z = 3.1
FOOT_D = 10.5
FOOT_Z = 1.0

THUMB1_ROT = -15
THUMB2_ROT = -25

CHAMFER_R = 1.0
CHAMFER_STEPS = 12

NANO_GAP = 6.0
USB_Z_LOCAL = NANO_GAP + PCB_THICK + 1.5  # 9.1

MAIN_SW = 15
TOTAL_SW = 17

# ============================================================
# PCB Data (205-point outline from Gerber edge-cuts)
# ============================================================

PCB_PTS = [
    (113.454, 61.998),
    (113.451, 62.060),
    (113.444, 62.122),
    (113.431, 62.183),
    (113.413, 62.242),
    (113.391, 62.300),
    (113.364, 62.355),
    (113.332, 62.409),
    (113.296, 62.459),
    (113.212, 62.550),
    (113.114, 62.626),
    (113.061, 62.658),
    (113.005, 62.685),
    (112.948, 62.708),
    (112.888, 62.726),
    (112.827, 62.738),
    (112.766, 62.746),
    (112.704, 62.748),
    (96.000, 62.746),
    (95.917, 62.749),
    (95.835, 62.759),
    (95.754, 62.776),
    (95.675, 62.800),
    (95.598, 62.830),
    (95.524, 62.866),
    (95.453, 62.908),
    (95.386, 62.956),
    (95.323, 63.010),
    (95.264, 63.068),
    (95.211, 63.131),
    (95.163, 63.199),
    (95.121, 63.270),
    (95.084, 63.344),
    (95.054, 63.421),
    (95.031, 63.500),
    (95.014, 63.581),
    (95.003, 63.663),
    (95.000, 63.746),
    (95.005, 85.141),
    (95.000, 85.231),
    (94.984, 85.319),
    (94.957, 85.405),
    (94.921, 85.487),
    (94.875, 85.564),
    (94.820, 85.635),
    (94.757, 85.699),
    (94.687, 85.755),
    (94.610, 85.802),
    (92.334, 86.657),
    (90.085, 87.454),
    (87.822, 88.214),
    (85.548, 88.936),
    (83.261, 89.621),
    (80.964, 90.267),
    (78.656, 90.876),
    (76.339, 91.446),
    (74.012, 91.978),
    (71.677, 92.471),
    (69.334, 92.925),
    (66.984, 93.340),
    (64.627, 93.717),
    (62.264, 94.054),
    (59.897, 94.352),
    (57.524, 94.611),
    (55.148, 94.830),
    (52.768, 95.010),
    (50.385, 95.151),
    (46.410, 95.147),
    (43.830, 95.098),
    (41.254, 94.953),
    (38.685, 94.711),
    (36.127, 94.373),
    (33.584, 93.939),
    (31.058, 93.410),
    (28.555, 92.787),
    (26.076, 92.070),
    (23.626, 91.261),
    (21.208, 90.360),
    (18.826, 89.369),
    (16.482, 88.290),
    (14.181, 87.123),
    (11.925, 85.871),
    (9.717, 84.534),
    (7.562, 83.116),
    (5.461, 81.618),
    (3.418, 80.043),
    (1.435, 78.391),
    (1.331, 78.310),
    (1.229, 78.226),
    (1.131, 78.138),
    (1.035, 78.047),
    (0.942, 77.953),
    (0.853, 77.856),
    (0.766, 77.757),
    (0.683, 77.654),
    (0.603, 77.549),
    (0.527, 77.441),
    (0.454, 77.331),
    (0.385, 77.219),
    (0.320, 77.104),
    (0.258, 76.987),
    (0.200, 76.869),
    (0.146, 76.748),
    (0.096, 76.626),
    (0.050, 76.502),
    (0.008, 76.377),
    (0.000, 22.072),
    (0.012, 21.908),
    (0.038, 21.747),
    (0.077, 21.588),
    (0.129, 21.433),
    (0.193, 21.282),
    (0.269, 21.138),
    (0.357, 21.000),
    (0.455, 20.869),
    (0.564, 20.747),
    (0.683, 20.635),
    (0.810, 20.532),
    (0.946, 20.440),
    (1.088, 20.360),
    (1.237, 20.291),
    (1.390, 20.235),
    (1.548, 20.192),
    (1.709, 20.162),
    (1.871, 20.144),
    (2.035, 20.141),
    (2.310, 20.140),
    (6.035, 20.112),
    (9.760, 20.034),
    (13.483, 19.907),
    (17.204, 19.731),
    (20.922, 19.506),
    (24.637, 19.232),
    (28.349, 18.909),
    (32.055, 18.536),
    (35.756, 18.115),
    (39.452, 17.645),
    (43.141, 17.126),
    (46.822, 16.558),
    (50.496, 15.942),
    (54.162, 15.277),
    (57.818, 14.564),
    (61.465, 13.803),
    (65.101, 12.993),
    (68.726, 12.136),
    (72.340, 11.230),
    (73.742, 10.859),
    (75.138, 10.464),
    (76.527, 10.047),
    (77.908, 9.606),
    (79.283, 9.142),
    (80.649, 8.655),
    (82.007, 8.146),
    (83.356, 7.614),
    (84.697, 7.059),
    (86.027, 6.482),
    (87.349, 5.883),
    (88.659, 5.262),
    (89.960, 4.620),
    (91.249, 3.955),
    (92.527, 3.270),
    (93.794, 2.563),
    (95.048, 1.835),
    (96.290, 1.086),
    (97.520, 0.317),
    (97.661, 0.233),
    (97.808, 0.162),
    (97.961, 0.103),
    (98.118, 0.057),
    (98.279, 0.025),
    (98.441, 0.006),
    (98.605, 0.000),
    (98.768, 0.008),
    (98.931, 0.030),
    (99.091, 0.065),
    (99.247, 0.113),
    (99.399, 0.174),
    (99.545, 0.247),
    (99.685, 0.333),
    (99.817, 0.430),
    (99.941, 0.537),
    (100.055, 0.654),
    (100.159, 0.781),
    (100.252, 0.915),
    (111.704, 21.001),
    (111.879, 21.363),
    (112.045, 21.729),
    (112.202, 22.099),
    (112.351, 22.473),
    (112.490, 22.850),
    (112.621, 23.230),
    (112.742, 23.613),
    (112.854, 23.999),
    (112.957, 24.388),
    (113.050, 24.779),
    (113.135, 25.172),
    (113.209, 25.567),
    (113.275, 25.964),
    (113.331, 26.362),
    (113.377, 26.761),
    (113.413, 27.162),
    (113.441, 27.563),
    (113.458, 27.965),
    (113.466, 28.366),
    (113.454, 30.886),
]

SW_POS = [
    (9.542, 29.614),
    (9.542, 48.614),
    (9.542, 67.614),
    (28.550, 41.490),
    (28.542, 60.540),
    (28.542, 79.614),
    (47.542, 47.718),
    (47.542, 66.736),
    (47.542, 85.754),
    (66.542, 43.146),
    (66.542, 62.164),
    (66.536, 81.182),
    (85.522, 40.606),
    (85.522, 59.624),
    (85.542, 78.614),
    (75.814, 20.326),
    (95.492, 12.110),
]

SW_ROT = [0] * MAIN_SW + [THUMB1_ROT, THUMB2_ROT]

MOUNT_POS = [
    (16.739, 78.320),
    (21.946, 31.076),
    (77.318, 88.226),
    (103.734, 19.392),
]

MAGNET_POS = [
    (70, 33),
    (85, 33),
    (70, 55),
    (85, 55),
    (6, 35),
    (6, 64),
]

FOOT_POS = [(4, 24), (5, 74), (98, 6), (92, 83)]


# ============================================================
# Geometry Helpers
# ============================================================


def _offset_wire(r: float) -> cq.Wire:
    pts = [cq.Vector(x, y, 0) for x, y in PCB_PTS]
    base = cq.Wire.makePolygon(pts, close=True)
    if abs(r) < 1e-9:
        return base
    return base.offset2D(r)[0]


def _extrude_pcb(r: float, h: float) -> cq.Solid:
    return cq.Solid.extrudeLinear(_offset_wire(r), [], cq.Vector(0, 0, h))


def _out2d_solid(h: float, inset: float = 0) -> cq.Solid:
    return _extrude_pcb(WALL + WALL_EXTRA - inset, h)


def _out2d_chamfered() -> cq.Solid:
    dz = CHAMFER_R / CHAMFER_STEPS
    body = _out2d_solid(TOP_H - CHAMFER_R)
    for i in range(CHAMFER_STEPS):
        inset = CHAMFER_R * (i + 1) / CHAMFER_STEPS
        step = _out2d_solid(dz, inset=inset)
        step = step.translate(cq.Vector(0, 0, TOP_H - CHAMFER_R + i * dz))
        body = body.fuse(step)
    return body


def _ring_solid(inner_r: float, outer_r: float, h: float) -> cq.Solid:
    return _extrude_pcb(outer_r, h).cut(_extrude_pcb(inner_r, h))


def _box(x: float, y: float, z: float, w: float, d: float, h: float) -> cq.Solid:
    return cq.Solid.makeBox(w, d, h, pnt=cq.Vector(x, y, z))


def _cyl(x: float, y: float, z: float, d: float, h: float) -> cq.Solid:
    return cq.Solid.makeCylinder(d / 2, h, pnt=cq.Vector(x, y, z))


def _wp(shape: cq.Shape) -> cq.Workplane:
    return cq.Workplane("XY").newObject([shape])


def _fuse_all(solids: list) -> cq.Shape:
    result = solids[0]
    for s in solids[1:]:
        result = result.fuse(s)
    return result


# ============================================================
# Key Cutouts
# ============================================================


def _key_cutouts() -> cq.Shape:
    parts: list[cq.Shape] = []

    # 15 main keycap wells (20.5 mm), clipped to offset profile
    wells = [
        _box(
            SW_POS[i][0] - 10.25,
            SW_POS[i][1] - 10.25,
            TOP_H - WELL_DEPTH,
            20.5,
            20.5,
            WELL_DEPTH,
        )
        for i in range(MAIN_SW)
    ]
    clip = _extrude_pcb(2.5, TOP_H)
    parts.append(_fuse_all(wells).intersect(clip))

    # 17 clip holes (14x14)
    for i in range(TOTAL_SW):
        x, y = SW_POS[i]
        hole = _box(-7, -7, 0, 14, 14, TOP_H - WELL_DEPTH)
        if SW_ROT[i] != 0:
            hole = hole.rotate((0, 0, 0), (0, 0, 1), SW_ROT[i])
        parts.append(hole.translate(cq.Vector(x, y, 0)))

    # 2 thumb keycap wells (19.5 mm, rotated)
    for i in [15, 16]:
        x, y = SW_POS[i]
        well = _box(-9.75, -9.75, TOP_H - WELL_DEPTH, 19.5, 19.5, WELL_DEPTH)
        well = well.rotate((0, 0, 0), (0, 0, 1), SW_ROT[i])
        parts.append(well.translate(cq.Vector(x, y, 0)))

    return _fuse_all(parts)


# ============================================================
# Bottom Shell
# ============================================================


def case_bottom() -> cq.Workplane:
    shell = _wp(_out2d_solid(BOT_H))

    # Alignment lip
    lip = _ring_solid(PCB_CLR, PCB_CLR + LIP_T, LIP_H)
    shell = shell.union(_wp(lip.translate(cq.Vector(0, 0, BOT_H))))

    # Inner cavity
    cavity = _extrude_pcb(PCB_CLR, BOT_H - WALL)
    shell = shell.cut(_wp(cavity.translate(cq.Vector(0, 0, WALL))))

    # Controller clearance
    shell = shell.cut(_wp(_box(PCB_W, 29, WALL, 1.2, 33, BOT_H - WALL + 1.5)))

    # Screw through-holes and countersinks
    for mx, my in MOUNT_POS:
        shell = shell.cut(_wp(_cyl(mx, my, 0, THRU_D, BOT_H + LIP_H)))
        shell = shell.cut(_wp(_cyl(mx, my, 0, CSINK_D, CSINK_Z)))

    # Battery pocket
    shell = shell.cut(_wp(_box(93, 30.5, WALL, 20, 30, STANDOFF)))

    # Power switch slot
    shell = shell.cut(_wp(_box(95, 69.3, 5.7, 2, 8, BOT_H - 4.2)))

    # Power switch finger recess
    inner_w = cq.Wire.makePolygon([
        cq.Vector(96.9, 69.3, 5.7),
        cq.Vector(96.9, 77.3, 5.7),
        cq.Vector(96.9, 77.3, BOT_H),
        cq.Vector(96.9, 69.3, BOT_H),
    ], close=True)
    outer_w = cq.Wire.makePolygon([
        cq.Vector(99.6, 67.3, 4),
        cq.Vector(99.6, 80.3, 4),
        cq.Vector(99.6, 80.3, BOT_H),
        cq.Vector(99.6, 67.3, BOT_H),
    ], close=True)
    shell = shell.cut(_wp(cq.Solid.makeLoft([inner_w, outer_w])))

    # Magnet pockets
    for mx, my in MAGNET_POS:
        shell = shell.cut(_wp(_cyl(mx, my, 0, MAG_D, MAG_Z)))

    # Rubber foot recesses
    for fx, fy in FOOT_POS:
        shell = shell.cut(_wp(_cyl(fx, fy, 0, FOOT_D, FOOT_Z)))

    # Bottom-wall openings
    shell = shell.cut(_wp(_box(25, 12, (BOT_H - 2.5) / 2, 4.0, 10, 2.5)))
    shell = shell.cut(_wp(_box(38, 10, (BOT_H - 3.0) / 2, 6.0, 10, 3.0)))
    shell = shell.cut(_wp(_box(53, 8, (BOT_H - 2.0) / 2, 6.0, 10, 2.0)))

    # Screw bosses
    bosses = _fuse_all([_cyl(mx, my, WALL, BOSS_D, STANDOFF) for mx, my in MOUNT_POS])
    for mx, my in MOUNT_POS:
        bosses = bosses.cut(_cyl(mx, my, 0, THRU_D, BOT_H))
    shell = shell.union(_wp(bosses))

    return shell


# ============================================================
# Top Shell
# ============================================================


def case_top() -> cq.Workplane:
    shell = _wp(_out2d_chamfered())

    # Switch-body cavity
    shell = shell.cut(_wp(_extrude_pcb(PCB_CLR, CAV_H)))

    # Controller tab recess
    recess_h = TOP_H - CAV_H + 4
    part1 = _extrude_pcb(PCB_CLR, recess_h).intersect(_box(96.3, 25, 0, 20, 38, recess_h))
    part2 = _extrude_pcb(PCB_CLR + 2.2, recess_h).intersect(
        _box(112, 25, 0, 5, 38, recess_h)
    )
    ctrl_recess = part1.fuse(part2).translate(cq.Vector(0, 0, CAV_H - 5.5))
    shell = shell.cut(_wp(ctrl_recess))

    # Key cutouts
    cutouts = _key_cutouts()
    shell = shell.cut(_wp(cutouts))

    # USB-C through-hole
    shell = shell.cut(_wp(_box(99.6, 62.0, USB_Z_LOCAL - 2.5, 10.5, 7, 5)))

    # USB-C plug clearance
    shell = shell.cut(_wp(_box(98.1, 65.0, USB_Z_LOCAL - 4.0, 13.5, 24, 8.2)))

    # Alignment groove
    shell = shell.cut(_wp(_ring_solid(PCB_CLR, PCB_CLR + GROOVE_T, GROOVE_H)))

    # Screw columns (square for strong FDM infill)
    columns = _fuse_all([
        _box(mx - BOSS_D / 2, my - BOSS_D / 2, 0, BOSS_D, BOSS_D, TOP_H)
        for mx, my in MOUNT_POS
    ])
    columns = columns.cut(cutouts)
    shell = shell.union(_wp(columns))

    return shell


# ============================================================
# CQ-Editor
# ============================================================

if "show_object" in dir():
    show_object(case_top(), name="top", options={"color": "steelblue"})
    show_object(
        case_bottom().translate((0, 0, -(BOT_H + 15))),
        name="bottom",
        options={"color": "slategray"},
    )

# ============================================================
# CLI Export
# ============================================================

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else "both"
    if part not in ("top", "bottom", "both"):
        print(f"Usage: {sys.argv[0]} [top|bottom|both]")
        sys.exit(1)

    out_dir = Path(__file__).parent

    if part in ("bottom", "both"):
        print("Building bottom shell...")
        bottom = case_bottom()
        path = out_dir / "sweep_case_bottom.stl"
        cq.exporters.export(bottom, str(path))
        print(f"  -> {path}")

    if part in ("top", "both"):
        print("Building top shell...")
        top = case_top()
        path = out_dir / "sweep_case_top.stl"
        cq.exporters.export(top, str(path))
        print(f"  -> {path}")

    print("Done.")
