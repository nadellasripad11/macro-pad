pcb outline draft - not a fabrication order

this is a draft outline for the macro pad pcb. it matches pinout.csv and the plate drawing. gerbers DO exist now in pcb/gerbers/ (6 rs-274x files + 2 drill files, generated 2026-11-07, see pcb/BUILD-NOTE.md). they were NOT plotted in kicad and drc has NOT been run — open the pcb in real kicad and run drc before any fab order.

board outline
- overall pcb size, draft: 112 mm wide x 70 mm deep, to match the plate drawing. final size can shrink once the case is picked, but the key and encoder positions below must not move relative to each other.
- board thickness, copper weight, finish, solder mask colour: tbd by the fab quote. silver / white look is the goal, but that is a case and keycap look, not a pcb colour claim yet.
- usb-c: the pico footprint board sits on this pcb as a module, usb-c at the back edge. the pcb itself does not carry a second usb-c in this draft.

key and encoder positions, from the top left corner of the pcb, same grid as the plate
- pitch: 19.05 mm both ways.
- first key centre k1: x 12.7 mm, y 12.7 mm.
- row 1, back: k1 (12.7, 12.7), k2 (31.75, 12.7), k3 (50.8, 12.7), k4 (69.85, 12.7).
- row 2, middle: k5 (12.7, 31.75), k6 (31.75, 31.75), k7 (50.8, 31.75), k8 (69.85, 31.75).
- row 3, front: k9 (12.7, 50.8), k10 (31.75, 50.8), k11 (50.8, 50.8), k12 (69.85, 50.8).
- encoder centre: x 95 mm, y 31.75 mm, on the right of the grid, in line with the middle row.
- switch cutouts on the plate are 14 x 14 mm. the pcb needs the matching switch holes and socket pads at each key centre, not a 14 mm hole in the pcb itself.

kailh socket pads requirement
- 12 x kailh hot swap sockets, one per key, footprint cpg151101s11.
- each socket: two pads, one to the key gpio, one to the common ground bus.
- gpio mapping, from pinout.csv: k1 gp2, k2 gp3, k3 gp4, k4 gp5, k5 gp6, k6 gp7, k7 gp8, k8 gp9, k9 gp10, k10 gp11, k11 gp12, k12 gp13.
- encoder: a gp14, b gp15, push gp16, common to ground. encoder is 3.3v logic, active low inputs with internal pull ups.
- ground: one common ground bus for all 12 keys and the encoder. no matrix, no diodes.
- unused gpio on the pico footprint board: gp0, gp1, gp23, gp24, gp25 and the rest are left unconnected in this draft. gp25 is the pico lipo user led, gp23 is its boot button, gp29 is battery sense, so none of those are used as keys.

pico module area
- module footprint: pico footprint, approx 53 x 21 mm, placed underneath the key grid area, headers soldered to the pcb.
- note: the pimoroni pico lipo 16mb does not include headers, so a 2 x 20 header set is a separate bom line, still tbd, unless the board is soldered another way.
- keep the module clear of the switch sockets so sockets can be soldered and switches swapped from the top.

what is still missing before a fab order
- a real kicad .kicad_pcb file exists now at pcb/macro-pad.kicad_pcb, hand-authored in kicad 8 format, not opened in kicad yet. open it in real kicad and run drc.
- gerber files exist now in pcb/gerbers/, generated in python from the same coordinates as the kicad file, plus drill files, with a preview render checked by eye. they were NOT plotted by kicad.
- a fab quote for this exact outline exists now: jlcpcb $7.80 board, $16.38 cheapest landed, quote 2026-11-07, see BOM-draft.md. that is a quote, not an order.
- a final check that the chosen encoder body and the chosen knob shaft fit the 7 mm plate hole and the encoder position.
- case and mounting holes: tbd once the case is picked. do not drill mounting holes from this draft alone.
