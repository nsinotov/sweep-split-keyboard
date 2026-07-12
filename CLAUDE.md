# Sweep Split Keyboard

Wireless 34-key split keyboard project: Sweep Bling MX PCB + nice!nano v2 + ZMK firmware.

## Project Structure

- `config/` — ZMK firmware configuration (cradio shield, nice_nano//zmk board)
- `case/` — 3D-printable case (OpenSCAD + CadQuery sources, STL exports)
- `gallery/` — build photos
- `firmware/` — local build output (.uf2 files, gitignored)
- `build.yaml` — ZMK GitHub Actions build matrix
- `build.sh` — local Docker-based build script

## ZMK Configuration

- Shield: `cradio` (built into ZMK, no external module needed)
- Board: `nice_nano//zmk` (nice!nano v2, Zephyr HWMv2 format)
- Config files follow ZMK naming convention: `config/cradio.keymap`, `config/cradio.conf`
- Physical layout file: `config/cradio.json` (for keymap editors)

## Keymap

7 layers: BASE (QWERTY + home row mods), SYM, NAV, NUM, MOUSE, SCROLL, FUN.
FUN is a conditional layer activated by holding NAV + MOUSE simultaneously.
Home row mods use bilateral trigger (left-hand mods only trigger on right-hand key presses and vice versa).

## Hardware Notes

- Battery: 402030 Li-Po 200 mAh per half
- Battery indicator: 4-LED board with push button (press to check level)
- Case has a side hole for reset button access
- Direct-pin wiring (no matrix, no diodes)

## Build

Push to GitHub for CI builds, or run `./build.sh` locally with Docker.
