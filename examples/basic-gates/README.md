---
example: basic-gates
author: Steven Slaa
---

# The basic gates

Every digital device you own, from a calculator to a phone, is built out of a handful of tiny
decisions: *are both of these on?*, *is either of these on?*, *are these different?* Each of
those decisions is a **gate**. There are only seven worth knowing, and this sheet has all of them
wired to the same two inputs, so you can compare their answers side by side.

## What you will learn

- What AND, OR, XOR, NAND, NOR, XNOR and NOT each decide
- How to read a truth table, and how to make the Logic Lab write one for you
- Why the "N" gates are simply the others turned upside down

## Before you start

Nothing. This is the first example.

## Try it

The circuit opens with both inputs, **A** and **B**, at 0. The simulation is already running.

1. Click **A**. It changes to 1, and every output that depends on it updates straight away.
2. Click **B** as well, then click **A** again to turn it off. Watch which outputs change each
   time.
3. Open the **Truth table** tab at the bottom of the screen. The Logic Lab has tried all four
   combinations of A and B for you and lists every output for each one.

Wires carrying a 1 are drawn bright; wires carrying a 0 are dark. You can follow a signal through
the circuit just by looking at it.

## The truth table

| A | B | AND | OR | XOR | NAND | NOR | XNOR | NOT A |
|---|---|:---:|:--:|:---:|:----:|:---:|:----:|:-----:|
| 0 | 0 |  0  | 0  |  0  |  1   |  1  |  1   |   1   |
| 0 | 1 |  0  | 1  |  1  |  1   |  0  |  0   |   1   |
| 1 | 0 |  0  | 1  |  1  |  1   |  0  |  0   |   0   |
| 1 | 1 |  1  | 1  |  0  |  0   |  0  |  1   |   0   |

## How it works

**AND** is 1 only when *every* input is 1. Think of two switches in a row on one wire: the lamp
only lights if both are closed.

**OR** is 1 when *at least one* input is 1. Two switches side by side: either one will do.

**XOR** (exclusive OR) is 1 when the inputs are *different*. It is OR with the "both" case taken
out. With more than two inputs it is 1 when an odd number of them are 1, which is why it turns up
in adders and in error checking.

**NOT** has a single input and flips it. It is drawn as a triangle with a small circle on the
tip; that circle, called a **bubble**, always means "inverted".

**NAND**, **NOR** and **XNOR** are AND, OR and XOR with a bubble on the output. Look at their
columns in the table: each one is the exact opposite of the gate it is named after. XNOR is 1
when the inputs are the *same*, which makes it a one-bit equality checker.

The wiring is worth a look too. A single wire leaves **A** and splits to seven gate inputs. A
split is just a place where one wire ends on another; the Logic Lab draws a dot there when three
or more wires meet. Where two wires only cross, with no dot and neither one ending on the other,
they are not connected.

## Where you meet this

- A car's interior light comes on when the driver's door **OR** the passenger's door is open.
- A washing machine only starts when the door is shut **AND** the start button is pressed.
- A light on a staircase with a switch at the top and the bottom is an **XOR**: flipping either
  switch changes the light.

## Things to try

- Select the AND gate and change **Inputs** to 3 in the Inspector. It grows a third input. What
  does it need now to output 1?
- Change the OR gate to 3 inputs as well, and wire the new input to **B**. Does the output ever
  change compared to before? (It should not: `B OR B` is just `B`.)
- Delete the NOT gate and rebuild it from a NAND with both inputs wired to A. Check the truth
  table still matches. The [Everything from NAND](../nand-only) example takes this idea all the
  way.

## Next

[De Morgan's laws](../de-morgan): two different circuits that always agree, and the trick for
swapping ANDs and ORs.
