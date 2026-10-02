---
example: four-bit-adder-wired
author: Steven Slaa
---

# A 4-bit adder, wire by wire

One [full adder](../full-adder) adds a single column. To add real numbers you need one per column,
with each column's carry handed to the next. This example builds exactly that for 4-bit numbers
(0 to 15), with nothing hidden: every bit has its own input pin, every gate is on the sheet, and
every carry is a wire you can follow with your finger. It is the chain that the Adder part packs
into one box.

## What you will learn

- How four full adders become one 4-bit adder
- How a binary number is spread over separate wires, one per bit
- How the carry ripples from the lowest bit to the highest

## Before you start

[Full adder](../full-adder). Each of the four rows here is that circuit, drawn a little tighter.

## Try it

The circuit opens on 9 + 5. A is `1001` (A3 A2 A1 A0) and B is `0101`, so the outputs read
`1110` (S3 S2 S1 S0), which is 14.

1. Find **A0** and **B0**, at the top. Both are 1, so bit 0 overflows: **C1** goes to 1 and
   carries into the bit 1 row.
2. Click **A1** to make A = 11. Now 11 + 5 = 16, which is `10000`: every carry lights in turn,
   S0 to S3 all go to 0 and **COUT** turns on.
3. Turn on **CIN** at the top to add one more.
4. Pick two numbers, set their bits, and check the answer by hand.

## Reading the numbers

Each number is four wires, one per bit. The rows are labelled with what their bit is worth:

| Bit | Worth | Pins |
|:---:|:-----:|------|
|  0  |   1   | A0, B0, S0 |
|  1  |   2   | A1, B1, S1 |
|  2  |   4   | A2, B2, S2 |
|  3  |   8   | A3, B3, S3 |

To read a number, add up what the bits that are 1 are worth. `1001` is 8 + 1 = 9. COUT is worth 16.

Bit 0 is at the top of the sheet but on the right when you write the number down. That is just the
way the sheet is drawn: the carry has to go somewhere, and here it runs downwards.

## How it works

Each row is one full adder, laid out like the [Full adder](../full-adder) example:

- **Left:** half adder 1 adds `Ai` and `Bi` (XOR on top, AND below).
- **Middle:** half adder 2 adds the carry in to that sum. Its XOR is the sum bit `Si`.
- **Right:** the OR, labelled `C1` to `C4`, is the row's carry out.

The carry out of each row runs down the sheet and becomes the carry in of the row below. CIN goes
into bit 0, and bit 3's carry out is COUT:

```
CIN ─▶ bit 0 ─C1─▶ bit 1 ─C2─▶ bit 2 ─C3─▶ bit 3 ─C4─▶ COUT
```

This is a **ripple-carry adder**. Bit 3 cannot know its answer until bit 2's carry has arrived,
which waits for bit 1, which waits for bit 0. In real hardware every gate takes a moment to switch,
so wider adders get slower. (The Logic Lab works out the whole circuit at once, so you only see
the settled answer.)

Where the carry wire runs down into a row it crosses the `Ai XOR Bi` wire. They do not connect:
wires only join where one ends on the other.

## Where you meet this

- **Every CPU** adds with a chain of full adders, though fast ones work out the carries in
  parallel instead of waiting for them to ripple (*carry-lookahead*).
- **Early microprocessors** used exactly this ripple chain, because it is small.

## Things to try

- Try 15 + 1. Every row carries, the most any addition can ripple, and the answer is `10000`.
- Delete the C2 wire between bit 1 and bit 2. Which sums now go wrong, and which still work?
- Make it a 5-bit adder: copy the bit 3 row, put it underneath, and move COUT to the new row.
  The largest answer is now 31 + 31 + 1 = 63.

## Next

[Adding 4-bit numbers](../four-bit-adder): the same adder as one Adder part, working on buses.
