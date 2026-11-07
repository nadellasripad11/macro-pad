# Week 5 macro pad — PCB + plate build note

Built 2026-11-07 by `pcb/build_pcb.py` (single source of truth — rerun it to
regenerate everything). Sources: `pcb-outline-draft.md`, `pinout.csv`,
`netlist.csv`, `encoder-research-2026-11-07.md`.

## What was built

- `pcb/macro-pad.kicad_pcb` — KiCad 8 S-expression, 112 × 70 mm, 2-layer,
  1.6 mm. 14 footprints: 12 × Kailh CPG151101S11 sockets (K1–K12),
  1 × Bourns PEC11R-4220F-S0024 encoder (ENC1), 1 × Pico 2×20 module (U1,
  Pimoroni Pico LiPo, USB-C at the top/back edge). 59 tracks, 36 vias.
  Nets: GND common bus + GP2–GP16, direct wiring, no matrix, no diodes,
  matching `pinout.csv` (verified against the file by the build script).
- `pcb/gerbers/` — RS-274X: `macro-pad-F_Cu.gtl`, `macro-pad-B_Cu.gbl`,
  `macro-pad-F_Mask.gts`, `macro-pad-B_Mask.gbs`, `macro-pad-F_SilkS.gto`,
  `macro-pad-Edge_Cuts.gko`, plus Excellon `macro-pad-PTH.drl` (81 holes:
  40 Pico + 5 encoder + 36 vias, 0.4 / 1.0 mm) and `macro-pad-NPTH.drl`
  (60 holes: 12 × central 3.988 mm + 24 × alignment 1.702 mm + 24 ×
  retention/pin 3.0 mm).
- `plate/plate-112x70.dxf` — R2010 DXF, mm. Outline 112 × 70, 12 × 14 × 14 mm
  MX cutouts at the key centres (19.05 mm pitch, K1 at (12.7, 12.7) from
  top-left), one 7 mm knob hole at the encoder centre (95, 31.75).
  **Plate thickness noted in the DXF text: 1.5 mm nominal** (MX standard).
  See the caveat below — 1.5 mm is not locked.
- `pcb/preview-top-bottom.png`, `plate/preview-plate.png` — renders checked
  by eye (see below).

## What was verified (all by the build script, 2026-11-07)

- `pinout.csv` on disk matches the build: 12 keys, GP2–GP13.
- `.kicad_pcb` parses as S-expressions (recursive parse): root `kicad_pcb`,
  14 footprints, 59 segments, 36 vias, 17 nets declared, 4 Edge.Cuts lines.
  Parenthesis count balanced (2486).
- Net connectivity (graph check over pad centres + track segments + vias):
  every GP2–GP16 net is one connected component (key/encoder pad ↔ Pico
  pin); GND is one component across all 33 points (12 key pads, 2 encoder
  pads, 8 Pico GND pins, 3 row buses, vertical bus). Unused Pico pins
  (GP0, GP1, VBUS, VSYS, 3V3, 3V3_EN, ADC_VREF, GP17–GP28, RUN) are
  deliberately unconnected, per the draft.
- No same-layer track crossings between different nets (59 tracks checked).
  Layer scheme: horizontals on B.Cu, verticals on F.Cu, vias at bends.
- All 247 pad/track points inside the 112 × 70 outline.
- Gerber read-back: all 6 files parse, coordinates within 112 × 70.
  Drill files read back, both end M30.
- DXF read-back (ezdxf): 1 outline 112 × 70, 12 cutouts exactly 14 × 14
  at the key centres, 1 knob hole radius 3.5 at (95, 31.75).
- Preview renders checked by eye: top/bottom routing looks as designed
  (verticals on F.Cu, horizontals on B.Cu, GND bus at x = 80, Pico area
  on the right); plate render shows the 4 × 3 cutout grid and the knob
  hole in line with the middle row.
- Tightest clearances (measured from the build coordinates): GP6 B.Cu
  horizontal (y = 28.32) to row-2 GND bus (y = 29.21): ~0.44 mm edge to
  edge. GP13 F.Cu vertical (x = 78.64) to GND F.Cu bus (x = 80): ~0.76 mm
  edge to edge. Both are above the OSH Park 6 mil (0.152 mm) rule, but
  they are the tightest spots on the board.

## What is NOT verified — do not order from these files yet

- **KiCad is NOT installed in this sandbox** (apt install was killed as
  impractical), so the `.kicad_pcb` was authored by hand in KiCad 8
  format and the Gerbers were generated directly in Python (RS-274X) from
  the same coordinate tables. **The Gerbers are NOT KiCad-plotted and were
  NOT opened in KiCad / GerbView.** Validation was by the custom read-back
  and renders above; `gerber-tools` is not installable here either.
  Before any fab order, open the files in real KiCad and run DRC.
- **Encoder footprint is PROVISIONAL.** Pin layout used: A/C/B row at
  2.5 mm pitch, 7.5 mm below the shaft centre; switch row 5.0 mm behind
  that; all 5 pads 1.0 mm TH. This is from the garbled Bourns PEC11R
  datasheet text extraction (see `encoder-research-2026-11-07.md`) and
  was NOT proven by an overlay against the Bourns drawing. The file
  itself carries a "PEC11R PROVISIONAL - CHECK DATASHEET" silkscreen note.
  Overlay it against the Bourns PEC11R drawing before ordering a PCB.
  Also unresolved: terminal code 4 in PEC11R-4220F decodes as horizontal
  in one table, while DigiKey lists the part as vertical.
- **Pico / encoder Z-clearance is NOT verified.** The Pico module area
  (x 82.39–103.39, y 5.13–58.13, on the bottom side) overlaps the encoder
  pin pads in plan view (encoder pins at y 39.25 / 44.25, x 92.5–97.5).
  The plan is: encoder soldered first, Pico on tall headers so its body
  sits ~8–10 mm below the PCB while encoder pins protrude ~2–3 mm.
  That clearance was never measured on real parts. Check before ordering.
- **Pimoroni Pico LiPo length is ~53 mm, not the standard Pico 51 mm.**
  The module outline is drawn 53 × 21 mm; verify the real board before
  ordering headers/PCB.
- **Plate thickness 1.5 mm is NOT locked.** It is the MX standard and
  what the DXF notes, but `plate-pcb-fab-research-2026-11-07.md` found
  SendCutSend's closest listed stock is .063 in = 1.60 mm. Confirm the
  actual stock thickness at quote time; the DXF is a cut file, thickness
  is a material choice at the fab.
- **No mounting holes, no corner radius in either file.** Both were TBD
  in the draft and are still TBD. The DXF has square corners and no
  mounting holes; the PCB has no mounting holes either.
- **No physical fit test, no fab order, no quote.** No Gerbers have been
  uploaded anywhere. The OSH Park $60.75 (3 boards, rate arithmetic) and
  JLCPCB figures in the fab research are not quotes for this board.
- Solder mask: openings are pads + 0.1 mm; vias are tented (no mask
  opening). Silkscreen is outline + reference text only.
