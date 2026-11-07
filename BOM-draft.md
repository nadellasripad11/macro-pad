# bom draft — week 5 macro pad (12 keys + knob)

**draft only. not a half life bom. nothing ordered, nothing paid, no checkout.**

**locked 2026-11-03 evening, on my "whatever you recommend":** the recommended lines below replace the earlier tbd board, encoder, switch, keycap, knob, and iron lines. verified, snapshot, and tbd lines are still kept separate. **do not sum them into a total.**

## a. recommended / locked lines

| qty | part | locked line | status |
|---|---|---|---|
| 1 | board — pimoroni pico lipo 16mb, PIM560 | **$15.95, pishop us live page, in stock (2026-11-03).** usb-c, pico footprint, ~53 x 21 mm. pin check from that page: user led GP25, boot GP23, battery sense GP29 — nothing claims GP16, so the locked pinout GP2-GP16 is unchanged. lipo charging circuit unused on desk usb. | live-page verified, cart screenshot still needed. headers/cables/batteries not included — a 2x20 header set is a new tbd line. |
| 1 | board alternative (cheapest only) — weact rp2040 16mb, usb-c | **$5.62 + $3.23 shipping, snapshot (article updated oct 2026).** user led GP25, so GP16 is free. | snapshot only, aliexpress wait, live cart not checked. use only if aliexpress wait is accepted; otherwise pico lipo is the pick. |
| 1 | encoder — bourns PEC11R-4220F-S0024 | **$2.69, digikey PEC11R-4220F-S0024-ND, live cart 2026-11-07, 8,700 in stock.** 6mm flatted shaft, 20mm shaft length, 24 detents / 24 pulses, with push switch. fits the adafruit 5528 knob (6.00mm shaft). cart total $15.02 in the capture is knob $2.95 + encoder $2.69 + $8.49 fedex ground + $0.89 tariff, tax not shown — do not quote $15.02 as the encoder total. | **ec11-compatible form, not an alps ec11 part — do not label it ec11 in the bom.** footprint likely fits ec11, not proven by overlay — use pec11r footprint in kicad. cart screenshot: cart-screenshots/digikey-encoder-cart-2026-11-07.pdf. |
| 2 packs | switches — gateron yellow KS-9, linear, 50g, 3-pin, hot-swap | **$2.70 per 10-pack, kono live page.** two packs = $5.40 for 20 (arithmetic, not a cart total), 12 needed, 8 spare. | live-page verified. cart screenshot failed — kono.store add-to-cart fails site-wide ("200 parsererror"), cart verified empty. needs me to take it over or a later retry. |
| 1 pack | sockets — kailh hot-swap pcb socket, 25-pack, CPG151101S11 | **$3.49, kono live page, in stock.** 12 needed, 13 spare. sockets soldered to the pcb with the iron, switches then hot-swap in. | live-page verified. same kono cart failure as switches — no kono cart screenshot exists. calculated only: $3.49 + 2 x $2.70 = $8.89, not a site total. |
| 12 | keycaps — ymdk cherry-profile 1u blank thick pbt, white, row r1 | **$0.20 each, ymdk live cart.** line $2.40, cart subtotal shown $2.26 usd after a 6% daily discount (-$0.14). | cart screenshot exists: cart-screenshots/ymdkey-keycaps-cart.pdf. shipping/tax not shown ("calculated at checkout"). |
| 1 | knob — adafruit 5528, silver anodized aluminum machined knob | **$2.95, digikey live page, in stock.** 20mm dia, 6.00mm shaft, set screw, fits any 6mm shaft incl. d-shaft. cart subtotal $2.95, shipping estimate $8.49 fedex ground, total estimate $11.44 (estimates, no tax line). | cart screenshot exists: cart-screenshots/digikey-knob-cart.pdf. |
| 1 | soldering iron kit, 60w | **locked 2026-11-07 : jamcorax 9-in-1, $11.29 on sale (was $12.59), walmart live cart 2026-11-07, in stock, 60w, 110v, 200-450c, 5 tips, stand, solder wire and paste.** hyper tough 9-piece $19.97 was the fallback, live cart same day, voltage flag unresolved (110-120v features vs 100v specs table) — rejected for the flag, not just price. | live cart screenshot: cart-screenshots/walmart-iron-cart-2026-11-07.pdf — cart $35.72 is frame $4.46 + both iron kits $31.26, free shipping, tax at checkout; do not quote $35.72 as the iron total. iron only for week 10 socket soldering. |
| 1 | silver aluminum plate / case | **custom plate from the plate drawing: 112 x 70 mm, 14 x 14 mm mx cutouts, 19.05 mm pitch, 4x3, 7 mm knob hole.** | fab quote done 2026-11-07: sendcutsend $11.63, 5052 H32 aluminum 0.063in (1.6mm), $14.17 with deburring, shipping not shown. dxf parsed, no error, no order. prebuilt aluminium macropads $70-$85 are full products, not bom lines. |
| 1 | custom pcb (key + encoder footprints, kailh socket pads) | **gerbers do exist now in pcb/gerbers/, generated 2026-11-07, not kicad-plotted, drc not run.** real kicad file at pcb/macro-pad.kicad_pcb. | fab quote done 2026-11-07: jlcpcb $7.80 board, $16.38 cheapest landed (global standard, not ddp), $34.40 ups ddp. gerbers parsed, no error, no order. the old $2 promo does not apply (112mm > 100mm limit). |
| 1 | usb-c cable (board to computer) | owned — i own one, will use my own. do not add to bom. | confirmed 2026-11-07. |
| — | usb power bank ($8-15, earlier week 5 plan) | **out of core bom** — only add if i later decide it is portable; parts must be genuinely used. | — |

## b. rejected / superseded lines (do not use)

- waveshare rp2040-plus 16mb $8.39 — robotshop cart page now says "re-stocking soon", due 12/29/2026, cart will backorder. not in stock now.
- snapklik rp2040-plus-m 4mb $39.98 — search in stock only, live page not opened, far more expensive.
- alps EC11E18244AU $5.09, digikey — out of stock, 1,131 expected 20-jan-2027.
- vxb ec11 5-pack $39.99 — confirmed in-stock 6mm route, but $39.99 for one needed encoder is rejected on value now that pec11r is recommended.
- arduiner ec11 encoder only, €2.24 ex vat, back-order — superseded by pec11r.
- dangkeebs gateron yellow $2.00/10-pack — page "sold out" vs metadata "available", and 5-pin, not the locked 3-pin KS-9. do not substitute silently.
- keyboard.io white kailh sockets x25 $2.00 — text "sold out" vs metadata "in stock". do not substitute silently.
- sparkfun 60w iron only $28.82 — rejected, see iron line above.
- adafruit macropad enclosure pack $4.95 — fails: pcb not aluminum, out of stock, made for adafruit's own board.

## c. what is not in this bom (and why)

- diodes: none — direct wiring, not matrix.
- oled/screen: none — locked out.
- leds / rgb: none — locked minimal white + silver design; rgb was only in a rejected look preview.
- resistors for keys/encoder: none — internal pull-ups.
- battery/charger circuit: none — desk usb only.

## totals — deliberately not summed

adding verified + snapshot + tbd prices together would produce a fake total. a half life bom total can only be claimed after us vendor cart screenshots exist for every line, with shipping/tax shown.

## still to verify (in order)

1. pico lipo cart screenshot + header set price (or weact live cart, if the aliexpress route is chosen). board live page re-verified 2026-11-07: $15.95 in stock, headers not included, header sets $1.45-$2.95 generic, specific set not verified; headers optional for direct wiring.
2. pec11r live cart done 2026-11-07, $2.69 digikey, footprint likely fits ec11, use pec11r footprint in kicad.
3. kono cart failed again 2026-11-07 (200 parsererror, cart empty) — switches/sockets decided 2026-11-07: kono, i will take cart screenshots and enter bom in half life myself. kono $8.89 arithmetic only until my screenshot lands. aliexpress $21.77 live cart nov 7 rejected by that decision.
4. plate fab quote done 2026-11-07: sendcutsend $11.63, dxf parsed, no error. pcb gerbers done 2026-11-07 in pcb/gerbers/, not kicad-plotted, drc not run.
5. iron kit locked 2026-11-07: jamcorax $11.29, walmart live cart.
6. usb-c cable: owned, i own one, do not add to bom.
7. real kicad pcb + gerbers done 2026-11-07, fab quote done 2026-11-07 (jlcpcb $7.80 / $16.38 landed). still open: open in real kicad and run drc, overlay encoder footprint vs bourns datasheet.
8. week 5 tier amounts on the live dashboard (do not assume tier 1/2/3 from earlier weeks).

## fab quotes — live, 2026-11-07, no order
- pcb, jlcpcb, gerbers uploaded and parsed, no error: 2-layer, 112x70mm, FR-4, 1.6mm, 5 boards, HASL lead-free, green, 1oz. board price $7.80 ($4.00 engineering + $3.80 board). cheapest landed $16.38 via global standard direct line ($7.80 + $8.58, 8-10 days, not ddp, duties not shown). default ups express saver ddp $34.40 ($7.80 + $26.60, 2-4 days). quote pdf: cart-screenshots/jlcpcb-quote-2026-11-07.pdf.
- plate, sendcutsend, dxf uploaded and parsed, no error: 112x70mm, 12x 14x14 cutouts + 7mm hole confirmed in preview. 5052 H32 aluminum, 0.063in (1.6mm, no exact 1.5mm gauge), no finish: $11.63, arrives wed nov 11. deburring pre-selected adds $2.54, $14.17, arrives thu nov 12. shipping not shown in guest quote, calculated at cart/checkout. quote pdf: cart-screenshots/sendcutsend-plate-quote-2026-11-07.pdf.
- note: gerbers were not kicad-plotted, encoder footprint provisional, open in real kicad and run drc before any fab order. see pcb/BUILD-NOTE.md.
