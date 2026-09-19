---
example: de-morgan
author: Steven Slaa
---

# De Morgan's laws

Here are two circuits built from completely different gates. The top one is a single NAND. The
bottom one inverts each input and then ORs them. Try every combination of inputs and they give
the same answer every time. That is not a coincidence; it is one of the two most useful rules in
digital logic, and once you know it you can rearrange any circuit to use the gates you have.

## What you will learn

- De Morgan's two laws, and how to say them in words
- How to prove two circuits are the same by comparing their truth tables
- The "push the bubble through" trick for swapping AND and OR

## Before you start

[The basic gates](../basic-gates), so that AND, OR, NOT and NAND are familiar.

## Try it

1. Click **A** and **B** through all four combinations: 00, 01, 10, 11.
2. Watch **X** (from the NAND) and **Y** (from the NOTs and the OR). They are always equal.
3. Open the **Truth table** tab to see all four rows at once and check it properly.

## The truth table

| A | B | X = NOT (A AND B) | NOT A | NOT B | Y = (NOT A) OR (NOT B) |
|---|---|:-----------------:|:-----:|:-----:|:----------------------:|
| 0 | 0 |         1         |   1   |   1   |           1            |
| 0 | 1 |         1         |   1   |   0   |           1            |
| 1 | 0 |         1         |   0   |   1   |           1            |
| 1 | 1 |         0         |   0   |   0   |           0            |

The X column and the Y column are identical. Two circuits with the same truth table *are* the same
circuit, as far as anything outside them can tell.

## How it works

The law in this circuit says:

```
NOT (A AND B)  =  (NOT A) OR (NOT B)
```

In words: *"not both"* is the same as *"at least one of them is not"*. If it is not true that you
have both a ticket and a passport, then you are missing your ticket or you are missing your
passport (or both).

The second law is the same thing with AND and OR swapped:

```
NOT (A OR B)  =  (NOT A) AND (NOT B)
```

*"Neither"* is the same as *"not this, and not that"*.

There is a mechanical way to remember both. To move a NOT across a gate, **flip the gate** (AND
becomes OR, OR becomes AND) and **put a NOT on every input** instead. Engineers call this pushing
the bubble through the gate. Try it on the drawing in your head: the bubble on the NAND's output
slides back to the two inputs, and the AND shape turns into an OR shape. That is exactly the
bottom circuit.

## Where you meet this

- **Chip design.** Some gates are cheaper or faster to make than others; in CMOS, the technology
  inside almost every chip, NAND and NOR are the cheapest. De Morgan's laws let a designer write
  the logic however is clearest and then convert it.
- **Programming.** `!(a && b)` is the same as `!a || !b`. The same laws tidy up conditions in
  code, and explain why `if (!(x > 0 && x < 10))` means "x is outside the range".
- **Search filters.** "Not (red and large)" returns everything that is not red plus everything
  that is not large.

## Things to try

- Build the second law below this one: a NOR on A and B into a pin called **P**, and two NOT gates
  into an AND into a pin called **Q**. Check the truth table: P and Q should always match.
- Replace the whole top circuit with an OR gate that has a NOT on each input. Is it still equal to
  X? (It should be: that is the first law read backwards.)
- Use the law to build an AND gate out of one OR gate and three NOT gates.

## Next

[Everything from NAND](../nand-only): if you can invert and you have one kind of gate, you can
build all the others.
