# ready to push — week 5 macro pad repo staging

checked 2026-11-07, locally only. nothing has been created, pushed, or submitted.
creating the repo and pushing still needs sripad's tap.

## files present (36 files, 3.7 mb)

- README.md — 4,898 chars, 55 lines
- project-description.md — approved description, verbatim
- BOM-draft.md — locked prices, verified/snapshot/tbd kept separate, no summed total
- bom-verification-2026-11-03-pass5.md — recommendation-lock pass
- pinout.csv (16 lines: header + 12 keys + encoder) / netlist.csv (19 lines)
- pcb-outline-draft.md — updated 2026-11-07, gerbers exist, not kicad-plotted
- images/ — 4 pngs, all valid png image data: layout-diagram.png (2400x1400), schematic-finished.png (2800x1700), schematic-wiring-diagram.png (3179x1979), plate-drawing.png (1600x1250)
- firmware/ — firmware_outline.py (py_compile ok, syntax checked only, not run on a board), firmware-notes.md, test-plan.md
- pcb/ — macro-pad.kicad_pcb (112x70mm, 2-layer), BUILD-NOTE.md, gerbers/ (6 rs-274x + 2 drill files)
- plate/ — plate-112x70.dxf (112x70mm), README.md
- cart-screenshots/ — 10 pdfs: digikey encoder cart 2026-11-07, digikey knob cart, jlcpcb quote 2026-11-07, kono cart failed + kono cart empty, pishop board cart 2026-11-07, robotshop board cart (rejected waveshare alternative), sendcutsend plate quote 2026-11-07, walmart iron cart 2026-11-07, ymdk keycaps cart

## checks passed

- readme >=200 chars: yes, 4,898 chars, 55 lines
- readme >=2 images: yes, 4 images, all valid pngs
- readme what/why/how: yes — what (intro), why (## why), how (## how)
- readme bom table with real prices + purchase links: yes — all 9 locked lines, links added 2026-11-07 (pishop, digikey x2, kono x2, ymdk, walmart, jlcpcb quote, sendcutsend). bom table prices verified against BOM-draft.md:
  board $15.95, encoder $2.69, switches $2.70/10-pack, sockets $3.49, keycaps $2.26 cart, knob $2.95, iron $11.29 jamcorax, pcb $7.80 board / $16.38 cheapest landed, plate $11.63 ($14.17 with deburring)
- no fake total: readme and bom-draft both state no total is summed (shipping/tax not all known)
- forbidden content: none found — no ai look previews, no buddy / week 4 mention, no built/tested-on-hardware claim (readme says "nothing here is built or tested on hardware yet"), no real wallpaper, no stock tickers
- firmware: syntax checked only, honestly labelled draft, not a working-firmware claim
- gerbers: exist in pcb/gerbers/, 6 + 2 files, parsed by jlcpcb with no error 2026-11-07

## fixed in this check (2026-11-07)

- pcb-outline-draft.md (staging + source): "no gerber files exist yet" → gerbers DO exist in pcb/gerbers/, not kicad-plotted, drc not run. "what is still missing" section updated: kicad file exists, gerbers exist, fab quote exists (jlcpcb $7.80 / $16.38).
- BOM-draft.md (staging + source): plate line "fab quote tbd" → sendcutsend $11.63 done 2026-11-07; pcb line "gerbers do not exist yet / fab quote tbd" → gerbers exist, jlcpcb $7.80 / $16.38 done, old $2 promo does not apply (112mm > 100mm); "still to verify" items 4 and 7 updated to done, with drc + encoder footprint overlay still open.
- README.md bom table: purchase links were missing — added all 9, urls taken from the verified source files (no invented urls).
- repo-draft.md: stale "gerbers do not exist yet" note updated; verification-pass line updated to pass5, which was copied into staging.
- bom-verification-2026-11-03-pass5.md copied into staging (it was listed in repo-draft.md but missing from staging).

## checks still open — these block submission, not the push

- repo does NOT exist yet and is NOT linked on half life (project page says "no repo yet"). creating it + pushing + linking needs sripad's tap.
- half life bom is $0.00 / not entered — the bom must be entered on half life to match the repo bom after the repo is linked.
- kono cart screenshots do NOT exist: kono add-to-cart fails ("200 parsererror", cart empty, verified again 2026-11-07). the kono lines in the bom ($8.89 arithmetic only) have live-page prices but no cart total. switches/sockets sourcing decision still open: kono $8.89 (no proof) vs aliexpress $21.88 (live cart nov 3, arvin brand caveat).
- pishop board cart: live cart exists (pishop-board-cart-2026-11-07.pdf, $15.95), shipping/tax not shown.
- pcb: gerbers were NOT plotted in kicad and drc has NOT been run; encoder footprint is provisional (check vs bourns datasheet before any fab order); pico/encoder z-clearance unmeasured; no mounting holes, no corner radius; plate thickness 1.5mm in dxf vs sendcutsend 1.6mm stock.
- robotshop-board-cart.pdf in cart-screenshots/ is a REJECTED board alternative (waveshare rp2040-plus, backordered to 12/29/2026) — do not mistake it for a bom line.
- usb-c cable ownership still unconfirmed; headers are optional for direct wiring, specific 2x20 header set price not verified.
- 5h progress reel and submit are unlocked by the 10h entry 1 (posted 2026-11-07), but submit still needs sripad's explicit tap.

## how to push (do not run without sripad's tap)

1. create the repo on github as nadellasripad11, name to confirm with sripad first (suggested: macro-pad), public, no readme initialised by github (readme.md is in staging).
2. from ~/workspace/week5-macropad/repo-staging/:
   - `git init`
   - `git add .`
   - `git commit -m "week 5 freestyle: macro pad design, 12 keys + knob, direct wiring"`
   - `git branch -M main`
   - `git remote add origin https://github.com/nadellasripad11/macro-pad.git`
   - `git push -u origin main`
   note: github connector text-only route corrupts binaries — use the browser web-ui upload route for the png/pdf files, or git from a machine with the files, and verify the images render on github after push.
3. link the repo on the half life project page (https://halflife.hackclub.com/projects/t2xoz4fbf5fdnyzlrojov83c), verify the project page no longer says "no repo yet".
4. enter the bom on half life to match BOM-draft.md, with the cart screenshots above.
5. submit only on sripad's explicit "submit".
