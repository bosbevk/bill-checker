# Klopdit's brand guide

A reference: what Klopdit looks and sounds like, and what is fixed. Louis picked this direction on 2026-11-22, "A: the
meter's wheels", from three. Klopdit is a working name until the name is picked; if it changes, the wheels take the new
letters and everything else here holds.

## The idea

Klopdit checks a municipal bill, and most of a water bill comes from one object: the meter outside, with its row of
number wheels. The City of Cape Town's own page says "On all traditional water meters, black numbers represent
kilolitres and red numbers represent litres." The brand is those wheels. The name is set in them, four black and three
red, and the app's icon is one wheel that has rolled to a tick. No rival has a mark at all, and none uses the meter.

## The mark

The name in wheels is the wordmark (`marks/wordmark.svg`). The letters are outlines, so it needs no font. The first
four wheels are white with ink letters and the last three are red with white letters, always. On an ink ground the
frame disappears and the wheels stand alone, which is fine. It is never smaller than 120 pixels wide, since below that
the letters fill in; use the icon there. Leave one wheel's width of clear space around it.

The icon is one white wheel with an ink tick, on ink, with the edge of a red wheel beside it
(`marks/icon-square.svg` for the stores, which round the corners themselves, `marks/icon-rounded.svg` everywhere
else). It reads down to 16 pixels. `marks/icon-one-colour.svg` is for a stamp or a single-colour print.

Never stretch or tilt either, never change which wheels are red, never add a shadow or a glow, and never set the name
in wheels of any other colour.

## Colour

| Name | Value | Used for | Contrast |
|---|---|---|---|
| Ink | `#0f1b2d` | Text, the wheels' frame, dark grounds | 15.9 on Face |
| Face | `#f3f6f8` | The page, like a meter's face | |
| White | `#ffffff` | Cards and the black wheels | |
| Water blue | `#1463c9` | What you press, and "adds up" | 5.7 with white, 5.3 on Face |
| Wheel red | `#c2331f` | The red wheels, and the words "look here" | 5.6 with white, 5.1 on Face |
| Red tint | `#fbe6e2` | Behind a line to look at | red on it 4.6 |
| Blue tint | `#e3edf9` | Behind a note that isn't a problem | ink on it 14.6 |
| Grey | `#5a6676` | Small labels | 5.4 on Face |
| Line | `#d9e0e6` | Rules between rows | |

Every text pair passes WCAG 2.2 AA for normal text, 4.5 to 1, worked out from the values. Red is on the brand, so it
is never an alarm: a line to look at gets the red tint and the two words, never a red screen. A jump in use where the
sums are right is blue, because nothing is wrong. On a dark ground: ground `#0b1320`, card `#15233a`, text `#eef3f8`
(16.7), grey `#a3b1c2` (8.5), blue `#6aa8f5` (7.6), red `#f08a78` (7.6).

## Type

Schibsted Grotesk sets the words: weight 800 with tight spacing for headings, 400 for reading, 600 on buttons.
Martian Mono sets every number, reading and amount, and the two status words; it never sets a paragraph. A picture
holds at most three sizes of text. Both faces are on Google Fonts; read their licences before the app carries them.

## The wheels in the app

A meter reading is always shown on four wheels (`marks/reading-0038.svg`), so "billed 0038, your meter 0014" needs no
explaining. While a bill is checked the wheels may roll and settle; with reduced motion on, they don't move.

## How it talks

Like a neighbour who is good with numbers: calm, exact, on your side, never angry at the municipality. The one line
is "Klop jou munisipale rekening?" and "Does your municipal bill add up?". A line that matches says "adds up" or
"klop"; a line that doesn't says "look here" or "kyk hier". The sum comes before the opinion.

It always says: an example is an example; a draft letter is for you to check and send; this is information, not legal
advice; Klopdit is not a municipality or part of one. It never says: you'll get money back; your municipality is
overcharging you; anything like "AI lawyer"; "free", "best" or "new" on a store image.

## Files

`marks/` holds the wordmark, the three icons and two readings as SVG. `images/` holds the store icon at 1024 and 512,
the Play feature graphic, four phone screenshots, the Facebook card, the tester card and the A5 flyer. `source/`
holds the page and script that draw them (`node shoot.js`), the map's script, and the letters' outlines.

## Not confirmed

The three municipalities' logos could not be opened, so nobody has yet looked at them beside this. Swartland's site
sets a dark green, `#004d40`, as its colour, which is far from ours. The Afrikaans wording needs a first-language
reader. Apple's screenshot sizes and the fonts' licences were not read.
