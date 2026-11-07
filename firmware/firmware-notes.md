# Firmware notes — what is draft, what is tested

## Status

- `firmware_outline.py`: **draft only, Python syntax-checked** (py_compile) in this run.
- **Not** run on a board, **not** tested with KMK or QMK, **not** a working-firmware claim.
- Before any demo claim: load it on the chosen USB-C RP2040 board, test all 12 keys on both layers, test encoder clockwise / counter-clockwise / push, and log the results.

## Route choice, honestly stated

- KMK (CircuitPython) is the usual fast edit loop for RP2040 pads, but its standard keyboard class is matrix-based. Using it for a direct-wired pad needs a direct-pin approach that was not verified in this run, so no KMK keymap is faked here.
- QMK has a DIRECT_PINS feature that matches direct wiring, and it is a legitimate alternative route — but no QMK config is claimed here either, because it was not built or compiled in this run.
- The hand-rolled CircuitPython skeleton in `firmware_outline.py` is the starter that maps 1:1 to `pinout.csv` using only standard modules (digitalio, rotaryio, usb_hid, adafruit_hid). Pick KMK, QMK, or this skeleton after the board is named — do not present all three as done.

## Layers (locked)

- Layer 0 (default): media / editing — Copy, Paste, Cut, Undo, Save, Play/Pause, Prev, Next, Mute, Screenshot, Redo, hold-K12 for Layer 1.
- Layer 1 (held): volume / system — Vol Down/Up, Brightness Down/Up, Mute, Play/Pause, Prev, Next, Mute, Screenshot, Redo, hold-K12.
- Encoder: Layer 0 = volume, Layer 1 = track seek (scrub), push = mute on both layers.

## TODO before testing

1. Debounce timing for keys and encoder push.
2. Encoder detent-per-step count (varies by EC11 variant — do not assume 1 detent = 1 step).
3. Key-release handling for held modifier combos (Ctrl+C etc.).
4. OS check: shortcuts assume Windows; macOS/Linux need different keycodes.
5. Full test log: every key, both layers, encoder CW/CCW/push.
