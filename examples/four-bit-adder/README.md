---
example: four-bit-adder
author: Steven Slaa
---

# Adding 4-bit numbers

Wiring four [full adders](../full-adder) by hand is worth doing once, and then never again. The
Logic Lab's **Adder** part is that chain in one box, and it works on **buses**: groups of wires
that carry a whole number at once. This example adds two numbers from 0 to 15 and shows what
happens when the answer does not fit.

## What you will learn

- What a bus is and how the Logic Lab draws one
- How to read and set multi-bit values
- What overflow is, and how the carry out reports it

## Before you start

[Full adder](../full-adder), so you know what is inside the Adder part.

## Try it

The circuit opens with **A** = 5 and **B** = 3, so **SUM** shows 8 and the hex digit shows `8`.

1. Click **A**. A 4-bit input pin counts up by one each time you click it, wrapping from 15 back to
   0. You can also select it and type a value in the Inspector.
2. Set A to 12 and B to 7. The true answer is 19, but SUM shows **3** and **COUT** turns on. See
   *Overflow* below.
3. Turn on **CIN**. The sum goes up by one: carry in is the "+1" from a column to the right.
4. Open the **Signals** tab to watch every value at once. The **Truth table** tab works too, but
   with 9 input bits it has 512 rows.

## Buses

Look at the wires from A and B: they are drawn thicker than the one from CIN. A thick wire is a
**bus**, here four wires side by side carrying bits 3, 2, 1 and 0 of a number. The Adder takes two
4-bit buses in and gives a 4-bit bus out. The pins on A, B and SUM show their values in decimal
because their **Radix** is set to Decimal in the Inspector; switch it to Binary to see the four
bits.

The **Hex digit** display on the right shows the same SUM bus as one hexadecimal digit, 0 to 9
then A to F for 10 to 15. Four bits are exactly one hex digit, which is why programmers write
binary in hex.

## Overflow

Four bits can hold 0 to 15. When the answer is bigger, the fifth bit of the answer comes out of
**COUT** and the four bits in SUM are what is left over:

| A  | B | A + B | COUT | SUM | read as COUT·16 + SUM |
|---:|--:|------:|:----:|----:|:---------------------:|
|  5 | 3 |     8 |  0   |   8 |           8           |
| 12 | 7 |    19 |  1   |   3 |          19           |
| 15 | 1 |    16 |  1   |   0 |          16           |
| 15 | 15 |   30 |  1   |  14 |          30           |

Nothing is lost: COUT is worth 16. A bigger adder would feed it into the next adder's CIN, which
is how an 8-bit adder is two 4-bit adders in a row.

## How it works

Inside the Adder is a ripple-carry chain of four full adders: bit 0 of A and B go into the first,
its carry goes into the second along with bit 1 of each, and so on. CIN feeds the first one and
COUT comes out of the last. The picture in the [Full adder](../full-adder) README is exactly this
part with its lid off.

## Where you meet this

- **Every CPU register is a bus.** A 64-bit processor adds two 64-bit buses at once, and the carry
  out becomes the processor's carry flag, which programs check for overflow.
- **Wrap-around bugs.** When a counter stored in too few bits overflows, it wraps to zero. The
  year 2038 problem, when 32-bit clocks run out, is this table's last row happening to a real
  clock.

## Things to try

- Add a second Adder and chain them into an 8-bit adder: widen the pins to 8 bits, use a
  **Splitter** to split each 8-bit bus into two halves, and feed the first adder's COUT into the
  second adder's CIN.
- Swap the Adder for a **Subtractor**. What happens when B is bigger than A? (The answer wraps
  around from the top, and the borrow out turns on.)
- Put a **Comparator** on A and B next to the adder, with LEDs on its outputs, to show which of the
  two numbers is bigger.

## Next

On to **Choosing and routing**, starting with the [Multiplexer](../mux-from-gates).
