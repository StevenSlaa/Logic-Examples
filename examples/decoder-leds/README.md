---
example: decoder-leds
author: Steven Slaa
---

# Decoder: binary to one-hot

A **decoder** takes a binary number and turns on exactly one of its outputs: the one with that
number. Give it 2 and output 2 lights up; every other output stays off. That pattern, where exactly
one line is on, is called **one-hot**. It is how a computer turns an address into "this memory
chip", or an instruction number into "do an addition".

## What you will learn

- What a decoder does, and what one-hot means
- How a 2-bit number can light one of four outputs
- How a decoder is built from AND and NOT gates

## Before you start

[The basic gates](../basic-gates). The [Multiplexer](../mux-from-gates) is a useful comparison.

## Try it

The circuit opens with **SEL** at 0, so the **Y0** LED is lit.

1. Click **SEL**. It is a 2-bit input, so it counts 0, 1, 2, 3 and back to 0. Its value is shown in
   decimal.
2. Each click moves the lit LED down one place. There is never more than one LED on, and never
   none.
3. Open the **Truth table** tab to see all four cases.

## The truth table

| SEL (decimal) | SEL (binary) | Y0 | Y1 | Y2 | Y3 |
|:-------------:|:------------:|:--:|:--:|:--:|:--:|
|       0       |      00      | 1  | 0  | 0  | 0  |
|       1       |      01      | 0  | 1  | 0  | 0  |
|       2       |      10      | 0  | 0  | 1  | 0  |
|       3       |      11      | 0  | 0  | 0  | 1  |

Read down the Y columns and you get a diagonal of 1s. That diagonal is what one-hot looks like.

## How it works

The wire from SEL is a 2-bit **bus**: two wires in one, carrying bit 1 (worth 2) and bit 0 (worth
1). It enters the decoder from the bottom, like the select line on a multiplexer.

Inside, each output is one AND gate that recognises one number, with a NOT on each bit that must
be 0:

```
Y0 = (NOT S1) AND (NOT S0)     SEL = 00
Y1 = (NOT S1) AND S0           SEL = 01
Y2 = S1 AND (NOT S0)           SEL = 10
Y3 = S1 AND S0                 SEL = 11
```

These are the "one AND per row" from the [Majority vote](../majority-vote) example. A decoder
is simply all of them at once, which is why it is often used as the first half of a sum-of-products
circuit: decode the input, then OR together the rows you want. The
[Traffic light](../traffic-light) example does exactly that.

## Decoders and multiplexers

A decoder and a multiplexer are close relatives. A mux uses its select lines to pick one *input*
to pass to a single output. A decoder uses them to pick one *output* to turn on. Put a decoder's
outputs into AND gates with your data inputs, OR the results together, and you have built a
multiplexer.

## Where you meet this

- **Memory addressing.** A computer's address bus goes into decoders that switch on exactly one
  memory chip, and then exactly one row inside it.
- **Instruction decoding.** A processor reads an instruction as a number, and a decoder turns that
  number into the one signal that starts the right operation.
- **Keyboards and LED matrices** scan rows one at a time; a decoder picks the row.

## Things to try

- Select the decoder and set **Select bits** to 3. It grows to eight outputs. Widen SEL to 3 bits
  and wire up four more LEDs.
- Build the 2-to-4 decoder from gates: split SEL with a **Splitter** into its two bits, add two NOT
  gates and four AND gates, and compare your outputs with the part's.
- Use the decoder to build a mux: four AND gates, each with one decoder output and one data input,
  into a 4-input OR.

## Next

On to **Memory and time**, starting with the [SR latch](../sr-latch): how a circuit can remember.
