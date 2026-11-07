# macro pad

so for week 5 freestyle i made a macro pad. its got twelve keys in a 3 by 4 grid plus one big knob on the side, no screen cause i wanted it clean.

white keycaps, silver case, silver metal knob. linear switches so its smooth and quiet and theyre hot swap, so the switches just pop in after the sockets are done.

its running on a rp2040 board wired direct, one wire per key, no matrix stuff and no diodes to mess with. layer one is editing and media like copy paste cut save play, hold the bottom right key and you get layer two for volume and system stuff. the knob does volume or scrub depending on the layer and pushing it mutes.

## why

i wanted something small that i would actually use every day, and something that looks clean on a desk, not a big keyboard project. the look is minimal white and silver, and the pad is only for the stuff i do all the time, editing and media first, volume and system second.

## how

twelve keys, four across and three deep, 19.05mm pitch, plus one encoder on the right in line with the middle row. direct wiring, one gpio per key, no matrix, no diodes. the keys are active low with internal pull ups. the encoder is a bourns pec11r, a and b on gp14 and gp15, push on gp16. the board is a pimoroni pico lipo 16mb, pico footprint, usb-c at the back. the sockets are kailh hot swap, soldered to the pcb, then the switches pop in. the firmware is a circuitpython outline, not run on a board yet.

the pcb is 112 by 70mm, 2 layer, in `pcb/macro-pad.kicad_pcb`, with gerbers in `pcb/gerbers/`. the plate is 112 by 70mm, dxf in `plate/plate-112x70.dxf`, 12x 14x14mm cutouts and a 7mm knob hole.

this is design only. nothing here is built or tested on hardware yet.

## what is not finished

- the gerbers were not plotted in kicad, they were generated in python from the same coordinates. open the pcb in real kicad and run drc before any fab order. see `pcb/BUILD-NOTE.md`.
- the encoder footprint is provisional, check it against the bourns datasheet before ordering a pcb.
- the plate thickness is 1.5mm in the dxf notes, sendcutsend closest stock is 0.063in, 1.6mm.
- no mounting holes, no corner radius yet.
- the switches and sockets seller is still open. kono cart failed with a 200 parsererror on november 7, cart empty, no cart total. aliexpress is the other option at 21.88 for the same two lines, see `BOM-draft.md`.

## bom

verified, snapshot, and to be decided lines are kept separate in `BOM-draft.md`. no total is summed here because shipping, tax, and the plate shipping are not all known yet.

| part | price | where | status |
|---|---|---|---|
| pimoroni pico lipo 16mb | $15.95 | [pishop us](https://www.pishop.us/product/pimoroni-pico-lipo-16mb/), live cart nov 7 | in stock, headers not included |
| bourns pec11r-4220f-s0024 encoder | $2.69 | [digikey](http://www.digikey.com/en/products/detail/PEC11R-4220F-S0024/PEC11R-4220F-S0024-ND/4499660), live cart nov 7 | 8,700 in stock |
| gateron yellow ks-9 switches, 2x 10 pack | $2.70 each | [kono](https://kono.store/collections/switches/products/gateron-switches), live page nov 7 | available, cart failed, no cart total |
| kailh hot swap sockets, 25 pack | $3.49 | [kono](https://kono.store/collections/mechanical-keyswitches/products/kailh-hot-swap-pcb-socket), live page nov 7 | in stock, cart failed, no cart total |
| ymdk white 1u keycaps, 12 | $2.26 cart | [ymdk](https://ymdkey.com/products/cherry-profile-1u-r1-r2-r3-r4-blank-thick-pbt-alphanumeric-custom-keycaps-for-keycap-diy) | cart shown |
| adafruit 5528 silver knob | $2.95 | [digikey](https://www.digikey.com:443/en/products/detail/adafruit-industries-llc/5528/16653404), live cart nov 3 | in stock, shipping $8.49 est |
| jamcorax 9-in-1 soldering iron kit, 60w | $11.29 | [walmart](https://www.walmart.com/ip/Soldering-Iron-Kit-60-W-110-V-Fast-Heat-Up-Soldering-Iron-9-In-1-Adjustable-Temperature-200-450-Soldering-Welding-Iron-Kit-for-Electronics-Hobby-Diy/19903153286), live cart nov 7 | in stock, 110v |
| pcb, jlcpcb, 5 boards | $7.80 board, $16.38 cheapest landed | [jlcpcb quote](https://jlcpcb.com/quote), nov 7 | gerbers parsed, no order |
| plate, sendcutsend, 5052 aluminum 0.063in | $11.63, $14.17 with deburring | [sendcutsend](https://sendcutsend.com/), quote nov 7 | dxf parsed, shipping not shown, no order |

## files

- `images/layout-diagram.png` — top view, 12 keys, knob on the right
- `images/schematic-finished.png` — schematic, gp2 to gp16, common ground
- `images/schematic-wiring-diagram.png` — wiring diagram
- `images/plate-drawing.png` — plate drawing for a quote, not to scale for cutting
- `pinout.csv` / `netlist.csv` — gp2 to gp16 mapping
- `firmware/firmware_outline.py` — circuitpython outline, syntax checked only, not run on a board
- `cart-screenshots/` — cart and quote captures, totals as shown on the page

half life week 5, freestyle, weeks 5 and 10.
