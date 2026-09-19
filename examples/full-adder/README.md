---
example: full-adder
author: Steven Slaa
---

# Full adder

A [half adder](../half-adder) adds two bits, but in the middle of a long addition every column
has *three* things to add: a bit from each number, and the carry from the column to its right. A
full adder handles all three. Put one in every column, connect each carry out to the next carry
in, and you can add numbers of any size. This single circuit is the building block of computer
arithmetic.

## What you will learn

- Why every column after the first needs three inputs
- How to build a full adder from two half adders and an OR gate
- How full adders chain into a multi-bit adder

## Before you start

[Half adder](../half-adder). This circuit is two of them.

## Try it

1. Set **A**, **B** and **CIN** (carry in) with a click each.
2. Read **COUT** and **SUM** together as a 2-bit number: it is always A + B + CIN.
3. Try 1 + 1 + 1: the answer is 3, which is `11` in binary, so both outputs are 1.
4. Open the **Truth table** tab to see all eight cases.

## The truth table

| A | B | CIN | A + B + CIN | COUT | SUM |
|---|---|:---:|:-----------:|:----:|:---:|
| 0 | 0 |  0  |      0      |  0   |  0  |
| 0 | 0 |  1  |      1      |  0   |  1  |
| 0 | 1 |  0  |      1      |  0   |  1  |
| 0 | 1 |  1  |      2      |  1   |  0  |
| 1 | 0 |  0  |      1      |  0   |  1  |
| 1 | 0 |  1  |      2      |  1   |  0  |
| 1 | 1 |  0  |      2      |  1   |  0  |
| 1 | 1 |  1  |      3      |  1   |  1  |

## How it works

The circuit adds in two steps, the way you might add three numbers by hand.

**First half adder (left):** `A XOR B` and `A AND B`. The XOR output is the sum of A and B
without the carry; it goes on to the second step. The AND output is 1 if A and B on their own
already overflowed.

**Second half adder (right):** it adds CIN to that first sum. Its XOR is the final **SUM**. Its AND,
labelled *carry through*, is 1 if adding the carry in made the column overflow.

**The OR gate:** the column carries out if either step overflowed. They can never both overflow
at once (the most a column can hold is 1 + 1 + 1 = 3, which only overflows once), so an OR is
enough.

Written as expressions:

```
SUM  = A XOR B XOR CIN
COUT = (A AND B) OR (CIN AND (A XOR B))
```

The SUM is 1 when an odd number of inputs are 1. COUT is 1 when at least two of them are: it is
the same function as the [Majority vote](../majority-vote), built a different way.

## Chaining them

To add two 4-bit numbers, use four full adders, one per column. Wire each one's COUT to the next
one's CIN, from right to left, and tie the rightmost CIN to 0:

```
   A3 B3        A2 B2        A1 B1        A0 B0
    │ │          │ │          │ │          │ │
  ┌─┴─┴─┐      ┌─┴─┴─┐      ┌─┴─┴─┐      ┌─┴─┴─┐
◀─┤ FA  │◀─────┤ FA  │◀─────┤ FA  │◀─────┤ FA  │◀── 0
  └──┬──┘      └──┬──┘      └──┬──┘      └──┬──┘
     S3           S2           S1           S0
```

This is a **ripple-carry adder**, because the carry ripples from right to left. It is simple, but
the leftmost column cannot finish until every carry before it has arrived, so wider adders get
slower. Real processors use cleverer *carry-lookahead* designs that work out the carries in
parallel.

## Where you meet this

- **The ALU.** The arithmetic logic unit inside every CPU contains an adder built from this idea,
  and subtraction reuses it too (see the next example).
- **Old calculators and the Apollo Guidance Computer** added with exactly this kind of chain.

## Things to try

- Build a 2-bit ripple adder: copy the whole circuit (select it all, then Ctrl+C and Ctrl+V) and
  wire the first COUT to the second CIN. Check that 3 + 1 = 4 (`11 + 01 = 100`).
- Replace the OR gate with an XOR. The truth table still matches. Why? (Because both carries can
  never be 1 at once, and XOR and OR only differ in that case.)
- Rebuild COUT as `A·B + A·CIN + B·CIN`, the majority circuit, and check it agrees.

## Next

[Adding 4-bit numbers](../four-bit-adder): the Adder part, which is this chain packed into one
box.
