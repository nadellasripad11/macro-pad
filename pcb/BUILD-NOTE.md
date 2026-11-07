# week 5 macro pad — pcb + plate build note

built 2026-11-07 by `pcb/build_pcb.py` (single source of truth — rerun it to
regenerate everything). sources: `pcb-outline-draft.md`, `pinout.csv`,
`netlist.csv`, `encoder-research-2026-11-07.md`.

## what was built

- `pcb/macro-pad.kicad_pcb` — kicad 8 s-expression, 112 × 70 mm, 2-layer,
  1.6 mm. 14 footprints: 12 × kailh CPG151101S11 sockets (K1–K12),
  1 × bourns PEC11R-4220F-S0024 encoder (ENC1), 1 × pico 2×20 module (U1,
  pimoroni pico lipo, usb-c at the top/back edge). 59 tracks, 36 vias.
  nets: gnd common bus + GP2–GP16, direct wiring, no matrix, no diodes,
  matching `pinout.csv` (verified against the file by the build script).
- `pcb/gerbers/` — RS-274X: `macro-pad-F_Cu.gtl`, `macro-pad-B_Cu.gbl`,
  `macro-pad-F_Mask.gts`, `macro-pad-B_Mask.gbs`, `macro-pad-F_SilkS.gto`,
  `macro-pad-Edge_Cuts.gko`, plus excellon `macro-pad-PTH.drl` (81 holes:
  40 pico + 5 encoder + 36 vias, 0.4 / 1.0 mm) and `macro-pad-NPTH.drl`
  (60 holes: 12 × central 3.988 mm + 24 × alignment 1.702 mm + 24 ×
  retention/pin 3.0 mm).
- `plate/plate-112x70.dxf` — R2010 dxf, mm. outline 112 × 70, 12 × 14 × 14 mm
  mx cutouts at the key centres (19.05 mm pitch, k1 at (12.7, 12.7) from
  top-left), one 7 mm knob hole at the encoder centre (95, 31.75).
  **plate thickness noted in the dxf text: 1.5 mm nominal** (mx standard).
  see the caveat below — 1.5 mm is not locked.
- `pcb/preview-top-bottom.png`, `plate/preview-plate.png` — renders checked
  by eye (see below).

## what was verified (all by the build script, 2026-11-07)

- `pinout.csv` on disk matches the build: 12 keys, GP2–GP13.
- `.kicad_pcb` parses as s-expressions (recursive parse): root `kicad_pcb`,
  14 footprints, 59 segments, 36 vias, 17 nets declared, 4 Edge.Cuts lines.
  parenthesis count balanced (2486).
- net connectivity (graph check over pad centres + track segments + vias):
  every GP2–GP16 net is one connected component (key/encoder pad ↔ pico
  pin); gnd is one component across all 33 points (12 key pads, 2 encoder
  pads, 8 pico gnd pins, 3 row buses, vertical bus). unused pico pins
  (GP0, GP1, VBUS, VSYS, 3V3, 3V3_EN, ADC_VREF, GP17–GP28, RUN) are
  deliberately unconnected, per the draft.
- no same-layer track crossings between different nets (59 tracks checked).
  layer scheme: horizontals on B.Cu, verticals on F.Cu, vias at bends.
- all 247 pad/track points inside the 112 × 70 outline.
- gerber read-back: all 6 files parse, coordinates within 112 × 70.
  drill files read back, both end M30.
- dxf read-back (ezdxf): 1 outline 112 × 70, 12 cutouts exactly 14 × 14
  at the key centres, 1 knob hole radius 3.5 at (95, 31.75).
- preview renders checked by eye: top/bottom routing looks as designed
  (verticals on F.Cu, horizontals on B.Cu, gnd bus at x = 80, pico area
  on the right); plate render shows the 4 × 3 cutout grid and the knob
  hole in line with the middle row.
- tightest clearances (measured from the build coordinates): GP6 B.Cu
  horizontal (y = 28.32) to row-2 gnd bus (y = 29.21): ~0.44 mm edge to
  edge. GP13 F.Cu vertical (x = 78.64) to gnd F.Cu bus (x = 80): ~0.76 mm
  edge to edge. both are above the osh park 6 mil (0.152 mm) rule, but
  they are the tightest spots on the board.

## what is not verified — do not order from these files yet

- **kicad is not installed in this sandbox** (apt install was killed as
  impractical), so the `.kicad_pcb` was authored by hand in kicad 8
  format and the gerbers were generated directly in python (RS-274X) from
  the same coordinate tables. **the gerbers are not kicad-plotted and were
  not opened in kicad / gerbview.** validation was by the custom read-back
  and renders above; `gerber-tools` is not installable here either.
  before any fab order, open the files in real kicad and run drc.
- **encoder footprint is provisional.** pin layout used: a/c/b row at
  2.5 mm pitch, 7.5 mm below the shaft centre; switch row 5.0 mm behind
  that; all 5 pads 1.0 mm th. this is from the garbled bourns pec11r
  datasheet text extraction (see `encoder-research-2026-11-07.md`) and
  was not proven by an overlay against the bourns drawing. the file
  itself carries a "PEC11R PROVISIONAL - CHECK DATASHEET" silkscreen note.
  overlay it against the bourns pec11r drawing before ordering a pcb.
  also unresolved: terminal code 4 in PEC11R-4220F decodes as horizontal
  in one table, while digikey lists the part as vertical.
- **pico / encoder z-clearance is not verified.** the pico module area
  (x 82.39–103.39, y 5.13–58.13, on the bottom side) overlaps the encoder
  pin pads in plan view (encoder pins at y 39.25 / 44.25, x 92.5–97.5).
  the plan is: encoder soldered first, pico on tall headers so its body
  sits ~8–10 mm below the pcb while encoder pins protrude ~2–3 mm.
  that clearance was never measured on real parts. check before ordering.
- **pimoroni pico lipo length is ~53 mm, not the standard pico 51 mm.**
  the module outline is drawn 53 × 21 mm; verify the real board before
  ordering headers/pcb.
- **plate thickness 1.5 mm is not locked.** it is the mx standard and
  what the dxf notes, but `plate-pcb-fab-research-2026-11-07.md` found
  sendcutsend's closest listed stock is .063 in = 1.60 mm. confirm the
  actual stock thickness at quote time; the dxf is a cut file, thickness
  is a material choice at the fab.
- **no mounting holes, no corner radius in either file.** both were tbd
  in the draft and are still tbd. the dxf has square corners and no
  mounting holes; the pcb has no mounting holes either.
- **no physical fit test, no fab order, no quote.** no gerbers have been
  uploaded anywhere. the osh park $60.75 (3 boards, rate arithmetic) and
  jlcpcb figures in the fab research are not quotes for this board.
- solder mask: openings are pads + 0.1 mm; vias are tented (no mask
  opening). silkscreen is outline + reference text only.
