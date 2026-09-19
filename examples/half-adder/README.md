---
example: half-adder
author: Steven Slaa
---

# Half adder

A computer adds numbers the way you learned to at school: one column at a time, carrying into the
next column when a column overflows. In binary each column holds just 0 or 1, so adding one
column is a tiny problem with only four cases, and two gates solve it. This is the first step
from logic gates to arithmetic.

## What you will learn

- How binary addition works, one column at a time
- Why XOR is the sum and AND is the carry
- What "half" means here, and what is missing

## Before you start

[The basic gates](../basic-gates). If binary is new, the section below covers what you need.

## Try it

The circuit opens with **A** = 1 and **B** = 0.

1. Look at the outputs: **SUM** is 1 and **CARRY** is 0, because 1 + 0 = 1.
2. Click **B** to make it 1. Now SUM goes to 0 and CARRY to 1: 1 + 1 = 2, which is written `10` in
   binary.
3. The green LED shows SUM and the amber LED shows CARRY. Open the **Truth table** tab to see all
   four cases.

## Binary in one paragraph

In decimal each column is worth ten times the one to its right: ones, tens, hundreds. In binary
each column is worth *two* times the one to its right: ones, twos, fours, eights. So `10` in
binary is one two and no ones, which is 2, and `11` is one two and one one, which is 3. When a
column adds up to 2 it overflows, exactly as a decimal column overflows at 10: you write 0 and
carry 1.

## The truth table

| A | B | A + B | CARRY | SUM |
|---|---|:-----:|:-----:|:---:|
| 0 | 0 |   0   |   0   |  0  |
| 0 | 1 |   1   |   0   |  1  |
| 1 | 0 |   1   |   0   |  1  |
| 1 | 1 |   2   |   1   |  0  |

Read CARRY and SUM together as a two-digit binary number and you get A + B.

## How it works

Look at the SUM column: it is 1 when A and B are *different*. That is exactly **XOR**.

Look at the CARRY column: it is 1 only when *both* A and B are 1. That is exactly **AND**.

That is the whole circuit. A and B each split and go to both gates; XOR produces the sum digit
and AND produces the carry.

It is called a *half* adder because it only has two inputs. Any column except the rightmost one
also has to add the carry coming in from the column before, which makes three inputs. A circuit
that handles that third input is a [full adder](../full-adder).

## Where you meet this

- **Every processor.** The arithmetic unit at the heart of a CPU starts from this idea. The
  rightmost bit of an addition can use a half adder, since nothing carries into it.
- **Counters.** Adding 1 to a binary number is a chain of half adders: each column adds the carry
  from the one before to its own bit.

## Things to try

- Select the XOR gate and change **Inputs** to 3, then wire a third input pin to it. What does the
  sum column do now with three inputs? (It is 1 when an odd number are 1: exactly the sum digit of
  adding three bits.)
- Build a half *subtractor*: the difference is still XOR, and the borrow is `(NOT A) AND B`. Check
  it with the truth table: A − B for each row.
- Put two half adders in a chain to add 1 to a 2-bit number. The first adds the 1 to bit 0; the
  second adds its carry to bit 1.

## Next

[Full adder](../full-adder): the version with three inputs, which can be chained to add numbers
of any length.
