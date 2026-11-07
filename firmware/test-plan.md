firmware test plan - draft only, not run

status: firmware_outline.py is draft only, python syntax checked only. not run on a board, not a kmk or qmk compile test, not a working firmware claim.

before any claim that it works, run these in order and log each result:
1. load the outline on the exact named usb-c rp2040 board, with the board datasheet open.
2. press each key once on layer one, check the right shortcut or media action fires, then release, check it stops.
3. hold k12, press each key once on layer two, check the right volume or system action fires, then release k12, check it goes back to layer one.
4. turn the knob clockwise and counter clockwise on layer one, check volume up and down, one step at a time.
5. hold k12, turn the knob both ways, check scrub or seek, one step at a time.
6. push the knob on both layers, check mute fires, then release, check it does not stick.
7. check debounce: fast presses, held keys, and knob detents, note any double fires or missed steps, and the detent count per step for the exact ec11 used.
8. check os: shortcuts in the outline assume windows. if the computer is macos or linux, remap and retest before claiming anything.

do not claim a board test, a demo, or working firmware until this log exists, with the board name, the ec11 variant, and the os in it.
