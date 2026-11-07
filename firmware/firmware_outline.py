# Week 5 Macro Pad — firmware outline / starter skeleton
#
# STATUS: DRAFT ONLY.
# - Python syntax-checked with py_compile in this run (syntax only).
# - NOT run on a board, NOT tested with a real RP2040 board, NOT a compile-tested KMK/QMK build.
# - Do not claim this as working firmware until it has been loaded on the chosen board and every key + the encoder have been tested.
#
# Why this is hand-rolled CircuitPython, not a KMK keymap:
# KMK's standard keyboard class is matrix-based (row/column pins). This pad is DIRECT-wired
# (one GPIO per key), so a KMK matrix keymap would not match the wiring without an extra
# direct-pin layer that is not verified here. QMK does have a DIRECT_PINS feature, and that
# is the alternative route if Sripad prefers QMK — it is named in firmware-notes.md, not
# faked here. The skeleton below uses only standard CircuitPython modules (digitalio,
# rotaryio, usb_hid, adafruit_hid), so every pin in it maps 1:1 to pinout.csv.
#
# OS assumption: Windows-style shortcuts (Ctrl+C/V/X/Z/S, Win+Shift+S screenshot).
# Change the keycodes if Sripad uses macOS/Linux.

import board
import digitalio
import rotaryio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# --- Pin map: MUST match pinout.csv ---
KEY_PINS = [
    board.GP2,   # K1  Copy
    board.GP3,   # K2  Paste
    board.GP4,   # K3  Cut
    board.GP5,   # K4  Undo
    board.GP6,   # K5  Save
    board.GP7,   # K6  Play / Pause
    board.GP8,   # K7  Previous track
    board.GP9,   # K8  Next track
    board.GP10,  # K9  Mute
    board.GP11,  # K10 Screenshot
    board.GP12,  # K11 Redo
    board.GP13,  # K12 Hold = Layer 1 (index 11, handled specially below)
]
LAYER_KEY_INDEX = 11
ENCODER_A = board.GP14
ENCODER_B = board.GP15
ENCODER_PUSH = board.GP16

# --- Layer 0: media / editing ---
# Each entry is a tuple of Keycode values sent together, or a consumer-control action
# marked with ("CC", code). None = no action on that layer.
LAYER0 = [
    (Keycode.CONTROL, Keycode.C),            # K1 Copy
    (Keycode.CONTROL, Keycode.V),            # K2 Paste
    (Keycode.CONTROL, Keycode.X),            # K3 Cut
    (Keycode.CONTROL, Keycode.Z),            # K4 Undo
    (Keycode.CONTROL, Keycode.S),            # K5 Save
    ("CC", ConsumerControlCode.PLAY_PAUSE),  # K6
    ("CC", ConsumerControlCode.SCAN_PREVIOUS_TRACK),  # K7
    ("CC", ConsumerControlCode.SCAN_NEXT_TRACK),      # K8
    ("CC", ConsumerControlCode.MUTE),        # K9
    (Keycode.GUI, Keycode.SHIFT, Keycode.S), # K10 Screenshot (Windows)
    (Keycode.CONTROL, Keycode.Y),            # K11 Redo
    None,                                    # K12 = layer hold, not a key
]

# --- Layer 1: volume / system (held via K12) ---
LAYER1 = [
    ("CC", ConsumerControlCode.VOLUME_DECREMENT),  # K1
    ("CC", ConsumerControlCode.VOLUME_INCREMENT),  # K2
    ("CC", ConsumerControlCode.BRIGHTNESS_DECREMENT),  # K3
    ("CC", ConsumerControlCode.BRIGHTNESS_INCREMENT),  # K4
    ("CC", ConsumerControlCode.MUTE),        # K5
    ("CC", ConsumerControlCode.PLAY_PAUSE),  # K6 (kept from Layer 0)
    ("CC", ConsumerControlCode.SCAN_PREVIOUS_TRACK),  # K7
    ("CC", ConsumerControlCode.SCAN_NEXT_TRACK),      # K8
    ("CC", ConsumerControlCode.MUTE),        # K9
    (Keycode.GUI, Keycode.SHIFT, Keycode.S), # K10 Screenshot (kept)
    (Keycode.CONTROL, Keycode.Y),            # K11 Redo (kept)
    None,                                    # K12 = layer hold
]

# --- Encoder ---
# Layer 0: volume up/down. Layer 1: track seek (scrub) via fast-forward/rewind.
# Push (either layer): mute. Debounce / detent handling is TODO in the test pass —
# do not claim detent counts until tested on the real encoder.
ENCODER_LAYER0_CW = ("CC", ConsumerControlCode.VOLUME_INCREMENT)
ENCODER_LAYER0_CCW = ("CC", ConsumerControlCode.VOLUME_DECREMENT)
ENCODER_LAYER1_CW = ("CC", ConsumerControlCode.FAST_FORWARD)
ENCODER_LAYER1_CCW = ("CC", ConsumerControlCode.REWIND)
ENCODER_PUSH_ACTION = ("CC", ConsumerControlCode.MUTE)


def setup_inputs():
    """Return (keys, layer_key, encoder, encoder_push) — all active LOW."""
    keys = []
    for pin in KEY_PINS:
        d = digitalio.DigitalInOut(pin)
        d.direction = digitalio.Direction.INPUT
        d.pull = digitalio.Pull.UP
        keys.append(d)
    push = digitalio.DigitalInOut(ENCODER_PUSH)
    push.direction = digitalio.Direction.INPUT
    push.pull = digitalio.Pull.UP
    encoder = rotaryio.IncrementalEncoder(ENCODER_A, ENCODER_B)
    return keys, keys[LAYER_KEY_INDEX], encoder, push


def send_action(kbd, cc, action):
    if action is None:
        return
    if action[0] == "CC":
        cc.send(action[1])
    else:
        kbd.press(*action)
        kbd.release_all()


# Main loop is intentionally left as structure, not a tested loop:
# - poll keys each cycle, track pressed/released edges (debounce TODO)
# - layer = LAYER1 if layer_key is LOW else LAYER0
# - encoder: compare encoder.position to last_position; CW = +1 step, CCW = -1 step
# - encoder push edge: send MUTE
# TODO before any demo claim: debounce timing, encoder detent-per-step count,
#   key-release handling for held combos, and a full 12-key + encoder test log.
