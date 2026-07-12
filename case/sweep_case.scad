/* Sweep Bling MX — Enclosed Case, Left Half */

// ---- Render Control ----
PART    = "both";  // "bottom", "top", "both"
EXPLODE = 15;      // mm gap for exploded view (0 = assembled)

// ---- Global Parameters ----
wall      = 2.5;
wall_extra = 2.0;
pcb_clr   = 0.2;
pcb_thick = 1.6;
standoff  = 4.5;
eps       = 0.01;
$fn       = 48;

bot_h = wall + standoff + pcb_thick;  // 8.6
cav_h = 5.5;
plt_h = 7.7;
top_h = cav_h + plt_h;               // 13.2
pcb_w = 113.466;

boss_d  = 7.0;
thru_d  = 2.2;
csink_d = 4.0;
csink_z = 2.0;

lip_t     = 0.9;
lip_h     = 1.5;
groove_t  = 1.0;
groove_h  = 1.6;

mag_d  = 8.2;
mag_z  = 3.1;
foot_d = 10.5;
foot_z = 1.0;

thumb1_rot = -15;
thumb2_rot = -25;

chamfer_r = 1.0;
chamfer_n = 12;

nano_gap    = 6.0;
usb_z_local = nano_gap + pcb_thick + 1.5;  // 9.1

// ---- PCB Outline (205 points, from Gerber edge-cuts) ----
pcb_pts = [
    [113.454,61.998],[113.451,62.060],[113.444,62.122],[113.431,62.183],
    [113.413,62.242],[113.391,62.300],[113.364,62.355],[113.332,62.409],
    [113.296,62.459],[113.212,62.550],[113.114,62.626],[113.061,62.658],
    [113.005,62.685],[112.948,62.708],[112.888,62.726],[112.827,62.738],
    [112.766,62.746],[112.704,62.748],[96.000,62.746],[95.917,62.749],
    [95.835,62.759],[95.754,62.776],[95.675,62.800],[95.598,62.830],
    [95.524,62.866],[95.453,62.908],[95.386,62.956],[95.323,63.010],
    [95.264,63.068],[95.211,63.131],[95.163,63.199],[95.121,63.270],
    [95.084,63.344],[95.054,63.421],[95.031,63.500],[95.014,63.581],
    [95.003,63.663],[95.000,63.746],[95.005,85.141],[95.000,85.231],
    [94.984,85.319],[94.957,85.405],[94.921,85.487],[94.875,85.564],
    [94.820,85.635],[94.757,85.699],[94.687,85.755],[94.610,85.802],
    [92.334,86.657],[90.085,87.454],[87.822,88.214],[85.548,88.936],
    [83.261,89.621],[80.964,90.267],[78.656,90.876],[76.339,91.446],
    [74.012,91.978],[71.677,92.471],[69.334,92.925],[66.984,93.340],
    [64.627,93.717],[62.264,94.054],[59.897,94.352],[57.524,94.611],
    [55.148,94.830],[52.768,95.010],[50.385,95.151],[46.410,95.147],
    [43.830,95.098],[41.254,94.953],[38.685,94.711],[36.127,94.373],
    [33.584,93.939],[31.058,93.410],[28.555,92.787],[26.076,92.070],
    [23.626,91.261],[21.208,90.360],[18.826,89.369],[16.482,88.290],
    [14.181,87.123],[11.925,85.871],[9.717,84.534],[7.562,83.116],
    [5.461,81.618],[3.418,80.043],[1.435,78.391],[1.331,78.310],
    [1.229,78.226],[1.131,78.138],[1.035,78.047],[0.942,77.953],
    [0.853,77.856],[0.766,77.757],[0.683,77.654],[0.603,77.549],
    [0.527,77.441],[0.454,77.331],[0.385,77.219],[0.320,77.104],
    [0.258,76.987],[0.200,76.869],[0.146,76.748],[0.096,76.626],
    [0.050,76.502],[0.008,76.377],[0.000,22.072],[0.012,21.908],
    [0.038,21.747],[0.077,21.588],[0.129,21.433],[0.193,21.282],
    [0.269,21.138],[0.357,21.000],[0.455,20.869],[0.564,20.747],
    [0.683,20.635],[0.810,20.532],[0.946,20.440],[1.088,20.360],
    [1.237,20.291],[1.390,20.235],[1.548,20.192],[1.709,20.162],
    [1.871,20.144],[2.035,20.141],[2.310,20.140],[6.035,20.112],
    [9.760,20.034],[13.483,19.907],[17.204,19.731],[20.922,19.506],
    [24.637,19.232],[28.349,18.909],[32.055,18.536],[35.756,18.115],
    [39.452,17.645],[43.141,17.126],[46.822,16.558],[50.496,15.942],
    [54.162,15.277],[57.818,14.564],[61.465,13.803],[65.101,12.993],
    [68.726,12.136],[72.340,11.230],[73.742,10.859],[75.138,10.464],
    [76.527,10.047],[77.908,9.606],[79.283,9.142],[80.649,8.655],
    [82.007,8.146],[83.356,7.614],[84.697,7.059],[86.027,6.482],
    [87.349,5.883],[88.659,5.262],[89.960,4.620],[91.249,3.955],
    [92.527,3.270],[93.794,2.563],[95.048,1.835],[96.290,1.086],
    [97.520,0.317],[97.661,0.233],[97.808,0.162],[97.961,0.103],
    [98.118,0.057],[98.279,0.025],[98.441,0.006],[98.605,0.000],
    [98.768,0.008],[98.931,0.030],[99.091,0.065],[99.247,0.113],
    [99.399,0.174],[99.545,0.247],[99.685,0.333],[99.817,0.430],
    [99.941,0.537],[100.055,0.654],[100.159,0.781],[100.252,0.915],
    [111.704,21.001],[111.879,21.363],[112.045,21.729],[112.202,22.099],
    [112.351,22.473],[112.490,22.850],[112.621,23.230],[112.742,23.613],
    [112.854,23.999],[112.957,24.388],[113.050,24.779],[113.135,25.172],
    [113.209,25.567],[113.275,25.964],[113.331,26.362],[113.377,26.761],
    [113.413,27.162],[113.441,27.563],[113.458,27.965],[113.466,28.366],
    [113.454,30.886]
];

// ---- Switch Centres ----
sw_pos = [
    [ 9.542, 29.614], [ 9.542, 48.614], [ 9.542, 67.614],  // col 1 pinky
    [28.550, 41.490], [28.542, 60.540], [28.542, 79.614],   // col 2 ring
    [47.542, 47.718], [47.542, 66.736], [47.542, 85.754],   // col 3 middle
    [66.542, 43.146], [66.542, 62.164], [66.536, 81.182],   // col 4 index
    [85.522, 40.606], [85.522, 59.624], [85.542, 78.614],   // col 5 inner
    [75.814, 20.326], [95.492, 12.110]                       // thumbs
];
sw_rot = [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, thumb1_rot, thumb2_rot];

// ---- Mounting Holes ----
mount_pos = [
    [16.739, 78.320],
    [21.946, 31.076],
    [77.318, 88.226],
    [103.734, 19.392]
];

// ---- Magnet Pockets ----
magnet_pos = [
    [70, 33], [85, 33], [70, 55], [85, 55],
    [ 6, 35], [ 6, 64]
];

// ---- Rubber Foot Recesses ----
foot_pos = [
    [ 4, 24],
    [ 5, 74],
    [98,  6],
    [92, 83]
];

// ============================================================
// 2-D Profile Helpers
// ============================================================
module out2d() {
    offset(r=wall+wall_extra) polygon(pcb_pts);
}
module in2d()   { offset(r=pcb_clr) polygon(pcb_pts); }

module lip2d() {
    difference() {
        offset(r = pcb_clr + lip_t) polygon(pcb_pts);
        offset(r = pcb_clr)         polygon(pcb_pts);
    }
}
module groove2d() {
    difference() {
        offset(r = pcb_clr + groove_t) polygon(pcb_pts);
        offset(r = pcb_clr)            polygon(pcb_pts);
    }
}

// ============================================================
// Chamfered outer shell (stepped linear chamfer on top edge)
// ============================================================
module outer_chamfered() {
    linear_extrude(top_h - chamfer_r) out2d();
    dz = chamfer_r / chamfer_n;
    for (i = [0 : chamfer_n - 1]) {
        inset = chamfer_r * (i + 1) / chamfer_n;
        translate([0, 0, top_h - chamfer_r + i * dz])
            linear_extrude(dz + eps)
                offset(r=-inset) out2d();
    }
}

// ============================================================
// Key Cutouts
// ============================================================
module all_key_cutouts() {
    // 15 main keycap wells (20.5 mm), clipped to offset profile
    intersection() {
        union() {
            for (i = [0 : 14])
                translate([sw_pos[i][0] - 10.25, sw_pos[i][1] - 10.25, top_h - 6])
                    cube([20.5, 20.5, 6 + eps]);
        }
        translate([0, 0, top_h - 6 - eps])
            linear_extrude(6 + 2*eps) offset(r=2.5) polygon(pcb_pts);
    }
    // 17 clip holes (14x14)
    for (i = [0 : 16])
        translate([sw_pos[i][0], sw_pos[i][1], 0])
            rotate([0, 0, sw_rot[i]])
                translate([-7, -7, -eps])
                    cube([14, 14, top_h - 6 + 2*eps]);
    // 2 thumb keycap wells (19.5 mm, rotated)
    for (i = [15 : 16])
        translate([sw_pos[i][0], sw_pos[i][1], 0])
            rotate([0, 0, sw_rot[i]])
                translate([-9.75, -9.75, top_h - 6])
                    cube([19.5, 19.5, 6 + eps]);
}

// ============================================================
// Bottom Shell
// ============================================================
module case_bottom() {
    difference() {
        union() {
            linear_extrude(bot_h) out2d();
            translate([0, 0, bot_h])
                linear_extrude(lip_h) lip2d();
        }

        // inner cavity
        translate([0, 0, wall])
            linear_extrude(bot_h - wall + eps) in2d();

        // controller clearance
        translate([pcb_w, 29, wall - eps])
            cube([1.2, 33, bot_h - wall + 2*eps + 1.5]);

        // screw through-holes & countersinks
        for (m = mount_pos) {
            translate([m[0], m[1], -eps])
                cylinder(d=thru_d, h=bot_h + lip_h + 2*eps);
            translate([m[0], m[1], -eps])
                cylinder(d=csink_d, h=csink_z + eps);
        }

        // battery pocket
        translate([93, 30.5, wall - eps])
            cube([20, 30, standoff + 2*eps]);

        // power switch slot
        translate([95, 69.3, 5.7])
            cube([2, 8, bot_h - 4.2 + eps]);

        // power switch finger recess
        hull() {
            translate([96.9, 69.3, 5.7])
                cube([eps, 8, bot_h - 5.7 + eps]);
            translate([99.6, 67.3, 4])
                cube([eps, 13, bot_h - 4 + eps]);
        }

        // magnet pockets
        for (m = magnet_pos)
            translate([m[0], m[1], -eps])
                cylinder(d=mag_d, h=mag_z + eps);

        // rubber foot recesses
        for (f = foot_pos)
            translate([f[0], f[1], -eps])
                cylinder(d=foot_d, h=foot_z + eps);

        // bottom-wall openings
        translate([25, 12, (bot_h - 2.5) / 2])
            cube([4.0, 10, 2.5]);
        translate([38, 10, (bot_h - 3.0) / 2])
            cube([6.0, 10, 3.0]);
        translate([53, 8, (bot_h - 2.0) / 2])
            cube([6.0, 10, 2.0]);
    }

    // screw bosses
    difference() {
        for (m = mount_pos)
            translate([m[0], m[1], wall])
                cylinder(d=boss_d, h=standoff);
        for (m = mount_pos)
            translate([m[0], m[1], -eps])
                cylinder(d=thru_d, h=bot_h + 2*eps);
    }
}

// ============================================================
// Top Shell
// ============================================================
module case_top() {
    difference() {
        outer_chamfered();

        // switch-body cavity
        translate([0, 0, -eps])
            linear_extrude(cav_h + eps) in2d();

        // controller tab recess
        translate([0, 0, cav_h - 5.5])
            linear_extrude(top_h - cav_h + 4)
                union() {
                    intersection() {
                        in2d();
                        translate([96.3, 25]) square([20, 38]);
                    }
                    intersection() {
                        offset(r=pcb_clr+2.2) polygon(pcb_pts);
                        translate([112, 25]) square([5, 38]);
                    }
                }

        // key cutouts
        all_key_cutouts();

        // USB-C through-hole
        translate([99.6, 62.0, usb_z_local - 2.5])
            cube([10.5, 7, 5]);

        // USB-C plug clearance
        translate([98.1, 65.0, usb_z_local - 4.0])
            cube([13.5, 24, 8.2]);

        // alignment groove
        translate([0, 0, -eps])
            linear_extrude(groove_h + eps) groove2d();
    }

    // screw columns (square for strong FDM infill)
    difference() {
        for (m = mount_pos)
            translate([m[0] - boss_d/2, m[1] - boss_d/2, 0])
                cube([boss_d, boss_d, top_h]);
        all_key_cutouts();
    }
}

// ============================================================
// Assembly / Render
// ============================================================
if (PART == "bottom")
    case_bottom();

if (PART == "top")
    case_top();

if (PART == "both") {
    case_bottom();
    translate([0, 0, bot_h + EXPLODE])
        case_top();
}
