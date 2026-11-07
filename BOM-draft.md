# BOM Draft — Week 5 Macro Pad (12 keys + knob)

**DRAFT ONLY. Not a Half Life BOM. Nothing ordered, nothing paid, no checkout.**

**LOCKED 2026-11-03 evening, on Sripad's "whatever you recommend":** the recommended lines below replace the earlier TBD board, encoder, switch, keycap, knob, and iron lines. Verified, snapshot, and TBD lines are still kept separate. **Do not sum them into a total.**

## A. Recommended / locked lines

| Qty | Part | Locked line | Status |
|---|---|---|---|
| 1 | Board — Pimoroni Pico LiPo 16MB, PIM560 | **$15.95, PiShop US live page, InStock (2026-11-03).** USB-C, Pico footprint, ~53 x 21 mm. Pin check from that page: user LED GP25, BOOT GP23, battery sense GP29 — nothing claims GP16, so the locked pinout GP2-GP16 is unchanged. LiPo charging circuit unused on desk USB. | Live-page verified, cart screenshot still needed. Headers/cables/batteries NOT included — a 2x20 header set is a new TBD line. |
| 1 | Board alternative (cheapest only) — WeAct RP2040 16MB, USB-C | **$5.62 + $3.23 shipping, snapshot (article updated Oct 2026).** User LED GP25, so GP16 is free. | Snapshot only, AliExpress wait, live cart not checked. Use only if AliExpress wait is accepted; otherwise Pico LiPo is the pick. |
| 1 | Encoder — Bourns PEC11R-4220F-S0024 | **$2.69, DigiKey PEC11R-4220F-S0024-ND, live cart 2026-11-07, 8,700 in stock.** 6mm flatted shaft, 20mm shaft length, 24 detents / 24 pulses, with push switch. Fits the Adafruit 5528 knob (6.00mm shaft). Cart total $15.02 in the capture is knob $2.95 + encoder $2.69 + $8.49 FedEx Ground + $0.89 tariff, tax not shown — do not quote $15.02 as the encoder total. | **EC11-compatible form, NOT an Alps EC11 part — do not label it EC11 in the BOM.** Footprint likely fits EC11, not proven by overlay — use PEC11R footprint in KiCad. Cart screenshot: cart-screenshots/digikey-encoder-cart-2026-11-07.pdf. |
| 2 packs | Switches — Gateron Yellow KS-9, linear, 50g, 3-pin, hot-swap | **$2.70 per 10-pack, Kono live page.** Two packs = $5.40 for 20 (arithmetic, not a cart total), 12 needed, 8 spare. | Live-page verified. Cart screenshot FAILED — kono.store add-to-cart fails site-wide ("200 parsererror"), cart verified empty. Needs Sripad takeover or a later retry. |
| 1 pack | Sockets — Kailh Hot-Swap PCB Socket, 25-pack, CPG151101S11 | **$3.49, Kono live page, InStock.** 12 needed, 13 spare. Sockets soldered to the PCB with the iron, switches then hot-swap in. | Live-page verified. Same Kono cart failure as switches — no Kono cart screenshot exists. Calculated only: $3.49 + 2 x $2.70 = $8.89, NOT a site total. |
| 12 | Keycaps — YMDK Cherry-profile 1u blank thick PBT, white, row R1 | **$0.20 each, YMDK live cart.** Line $2.40, cart subtotal shown $2.26 USD after a 6% daily discount (-$0.14). | Cart screenshot exists: cart-screenshots/ymdkey-keycaps-cart.pdf. Shipping/tax NOT shown ("calculated at checkout"). |
| 1 | Knob — Adafruit 5528, silver anodized aluminum machined knob | **$2.95, DigiKey live page, InStock.** 20mm dia, 6.00mm shaft, set screw, fits any 6mm shaft incl. D-shaft. Cart subtotal $2.95, shipping estimate $8.49 FedEx Ground, total estimate $11.44 (estimates, no tax line). | Cart screenshot exists: cart-screenshots/digikey-knob-cart.pdf. |
| 1 | Soldering iron kit, 60W | **LOCKED 2026-11-07 on Sripad's full-responsibility order: JAMCORAX 9-in-1, $11.29 on sale (was $12.59), Walmart live cart 2026-11-07, in stock, 60W, 110V, 200-450C, 5 tips, stand, solder wire and paste.** Hyper Tough 9-piece $19.97 was the fallback, live cart same day, voltage flag unresolved (110-120V features vs 100V specs table) — rejected for the flag, not just price. | Live cart screenshot: cart-screenshots/walmart-iron-cart-2026-11-07.pdf — cart $35.72 is frame $4.46 + both iron kits $31.26, free shipping, tax at checkout; do not quote $35.72 as the iron total. Iron only for Week 10 socket soldering. |
| 1 | Silver aluminum plate / case | **Custom plate from the plate drawing: 112 x 70 mm, 14 x 14 mm MX cutouts, 19.05 mm pitch, 4x3, 7 mm knob hole.** | Fab quote DONE 2026-11-07: SendCutSend $11.63, 5052 H32 aluminum 0.063in (1.6mm), $14.17 with deburring, shipping not shown. DXF parsed, no error, no order. Prebuilt aluminium macropads $70-$85 are full products, NOT BOM lines. |
| 1 | Custom PCB (key + encoder footprints, Kailh socket pads) | **Gerbers DO exist now in pcb/gerbers/, generated 2026-11-07, not KiCad-plotted, DRC not run.** Real KiCad file at pcb/macro-pad.kicad_pcb. | Fab quote DONE 2026-11-07: JLCPCB $7.80 board, $16.38 cheapest landed (Global Standard, not DDP), $34.40 UPS DDP. Gerbers parsed, no error, no order. The old $2 promo does NOT apply (112mm > 100mm limit). |
| 1 | USB-C cable (board to computer) | TBD — only if Sripad does not already own a usable one; do not assume. | Ownership never confirmed. |
| — | USB power bank ($8-15, earlier Week 5 plan) | **OUT of core BOM** — only add if Sripad later says portable; parts must be genuinely used. | — |

## B. Rejected / superseded lines (do not use)

- Waveshare RP2040-Plus 16MB $8.39 — RobotShop cart page now says "Re-stocking soon", due 12/29/2026, cart will backorder. Not in stock now.
- Snapklik RP2040-Plus-M 4MB $39.98 — search InStock only, live page not opened, far more expensive.
- Alps EC11E18244AU $5.09, DigiKey — out of stock, 1,131 expected 20-Jan-2027.
- VXB EC11 5-pack $39.99 — confirmed in-stock 6mm route, but $39.99 for one needed encoder is rejected on value now that PEC11R is recommended.
- Arduiner EC11 encoder only, €2.24 ex VAT, back-order — superseded by PEC11R.
- Dangkeebs Gateron Yellow $2.00/10-pack — page "sold out" vs metadata "available", and 5-pin, not the locked 3-pin KS-9. Do not substitute silently.
- Keyboard.io white Kailh sockets x25 $2.00 — text "sold out" vs metadata "in stock". Do not substitute silently.
- SparkFun 60W iron only $28.82 — rejected, see iron line above.
- Adafruit MacroPad enclosure pack $4.95 — fails: PCB not aluminum, out of stock, made for Adafruit's own board.

## C. What is NOT in this BOM (and why)

- Diodes: none — direct wiring, not matrix.
- OLED/screen: none — locked out.
- LEDs / RGB: none — locked minimal white + silver design; RGB was only in a rejected look preview.
- Resistors for keys/encoder: none — internal pull-ups.
- Battery/charger circuit: none — desk USB only.

## Totals — deliberately NOT summed

Adding verified + snapshot + TBD prices together would produce a fake total. A Half Life BOM total can only be claimed after US vendor cart screenshots exist for every line, with shipping/tax shown.

## Still to verify (in order)

1. Pico LiPo cart screenshot + header set price (or WeAct live cart, if the AliExpress route is chosen). Board live page re-verified 2026-11-07: $15.95 InStock, headers NOT included, header sets $1.45-$2.95 generic, specific set not verified; headers optional for direct wiring.
2. PEC11R live cart DONE 2026-11-07, $2.69 DigiKey, footprint likely fits EC11, use PEC11R footprint in KiCad.
3. Kono cart FAILED again 2026-11-07 (200 parsererror, cart empty) — switches/sockets sourcing decision still open: Kono $8.89 arithmetic only, no cart proof, vs AliExpress $21.88 live cart Nov 3.
4. Plate fab quote DONE 2026-11-07: SendCutSend $11.63, DXF parsed, no error. PCB Gerbers DONE 2026-11-07 in pcb/gerbers/, not KiCad-plotted, DRC not run.
5. Iron kit LOCKED 2026-11-07: JAMCORAX $11.29, Walmart live cart.
6. USB-C cable: owned or buy.
7. Real KiCad PCB + Gerbers DONE 2026-11-07, fab quote DONE 2026-11-07 (JLCPCB $7.80 / $16.38 landed). Still open: open in real KiCad and run DRC, overlay encoder footprint vs Bourns datasheet.
8. Week 5 tier amounts on the live dashboard (do not assume Tier 1/2/3 from earlier weeks).

## fab quotes — live, 2026-11-07, no order
- pcb, jlcpcb, gerbers uploaded and parsed, no error: 2-layer, 112x70mm, fr-4, 1.6mm, 5 boards, hasl lead-free, green, 1oz. board price $7.80 ($4.00 engineering + $3.80 board). cheapest landed $16.38 via global standard direct line ($7.80 + $8.58, 8-10 days, not ddp, duties not shown). default ups express saver ddp $34.40 ($7.80 + $26.60, 2-4 days). quote pdf: cart-screenshots/jlcpcb-quote-2026-11-07.pdf.
- plate, sendcutsend, dxf uploaded and parsed, no error: 112x70mm, 12x 14x14 cutouts + 7mm hole confirmed in preview. 5052 h32 aluminum, 0.063in (1.6mm, no exact 1.5mm gauge), no finish: $11.63, arrives wed nov 11. deburring pre-selected adds $2.54, $14.17, arrives thu nov 12. shipping not shown in guest quote, calculated at cart/checkout. quote pdf: cart-screenshots/sendcutsend-plate-quote-2026-11-07.pdf.
- note: gerbers were not kicad-plotted, encoder footprint provisional, open in real kicad and run drc before any fab order. see pcb/BUILD-NOTE.md.
