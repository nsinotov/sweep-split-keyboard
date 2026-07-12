#!/usr/bin/env bash
set -euo pipefail

BOARD="nice_nano//zmk"
FIRMWARE_DIR="firmware"
DOCKER_IMAGE="zmkfirmware/zmk-build-arm:stable"
DOCKER_CMD="docker run --rm -v $(pwd):/workdir -w /workdir ${DOCKER_IMAGE}"

mkdir -p "${FIRMWARE_DIR}"

build_side() {
    local shield="$1"
    local label="$2"
    echo "Building ${label}..."
    ${DOCKER_CMD} bash -c "\
        [ -d .west ] || west init -l config && \
        west update && \
        west zephyr-export && \
        west build -p -s zmk/app -b ${BOARD} -- \
            -DSHIELD=${shield} \
            -DZMK_CONFIG=/workdir/config && \
        cp build/zephyr/zmk.uf2 ${FIRMWARE_DIR}/${label}.uf2"
    echo "${label} done: ${FIRMWARE_DIR}/${label}.uf2"
}

case "${1:-all}" in
    left)   build_side "cradio_left"    "cradio_left"    ;;
    right)  build_side "cradio_right"   "cradio_right"   ;;
    reset)  build_side "settings_reset" "settings_reset"  ;;
    all)
        build_side "cradio_left"    "cradio_left"
        build_side "cradio_right"   "cradio_right"
        build_side "settings_reset" "settings_reset"
        ;;
    *)
        echo "Usage: $0 {left|right|reset|all}"
        exit 1
        ;;
esac
