# firmware notes — what is draft, what is tested

## status

- `firmware_outline.py`: **draft only, python syntax-checked** (py_compile) in this run.
- **not** run on a board, **not** tested with kmk or qmk, **not** a working-firmware claim.
- before any demo claim: load it on the chosen usb-c rp2040 board, test all 12 keys on both layers, test encoder clockwise / counter-clockwise / push, and log the results.

## route choice, honestly stated

- kmk (circuitpython) is the usual fast edit loop for rp2040 pads, but its standard keyboard class is matrix-based. using it for a direct-wired pad needs a direct-pin approach that was not verified in this run, so no kmk keymap is faked here.
- qmk has a DIRECT_PINS feature that matches direct wiring, and it is a legitimate alternative route — but no qmk config is claimed here either, because it was not built or compiled in this run.
- the hand-rolled circuitpython skeleton in `firmware_outline.py` is the starter that maps 1:1 to `pinout.csv` using only standard modules (digitalio, rotaryio, usb_hid, adafruit_hid). pick kmk, qmk, or this skeleton after the board is named — do not present all three as done.

## layers (locked)

- layer 0 (default): media / editing — copy, paste, cut, undo, save, play/pause, prev, next, mute, screenshot, redo, hold-k12 for layer 1.
- layer 1 (held): volume / system — vol down/up, brightness down/up, mute, play/pause, prev, next, mute, screenshot, redo, hold-k12.
- encoder: layer 0 = volume, layer 1 = track seek (scrub), push = mute on both layers.

## todo before testing

1. debounce timing for keys and encoder push.
2. encoder detent-per-step count (varies by ec11 variant — do not assume 1 detent = 1 step).
3. key-release handling for held modifier combos (ctrl+c etc.).
4. os check: shortcuts assume windows; macos/linux need different keycodes.
5. full test log: every key, both layers, encoder cw/ccw/push.
