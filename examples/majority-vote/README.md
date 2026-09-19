---
example: majority-vote
author: Steven Slaa
---

# Majority vote: from truth table to circuit

Three judges each press yes or no, and the light comes on if at least two of them said yes. That
is easy to say in words, but how do you get from the words to gates? This example shows a method
that always works: write down the truth table, pick out the rows where the answer is 1, and build
one AND gate per row. It is called **sum of products**.

## What you will learn

- How to write a truth table from a description in words
- The sum-of-products method for turning any truth table into AND and OR gates
- How to spot a simplification, and why it matters

## Before you start

[The basic gates](../basic-gates). The other Basics examples help but are not required.

## Try it

1. Click **A**, **B** and **C** to set the three votes.
2. The **MAJORITY** output and the green LED come on when two or three votes are 1.
3. Open the **Truth table** tab: eight rows, since three inputs have 2 × 2 × 2 = 8 combinations.

## The truth table

| A | B | C | MAJORITY |
|---|---|---|:--------:|
| 0 | 0 | 0 |    0     |
| 0 | 0 | 1 |    0     |
| 0 | 1 | 0 |    0     |
| 0 | 1 | 1 |    1     |
| 1 | 0 | 0 |    0     |
| 1 | 0 | 1 |    1     |
| 1 | 1 | 0 |    1     |
| 1 | 1 | 1 |    1     |

## How it works

### Step 1: one AND per row that says yes

There are four rows with a 1 in the output. For each one, write an AND that is true for exactly
that row, with a NOT on each input that is 0 in that row:

```
row 011:  (NOT A) AND B AND C
row 101:  A AND (NOT B) AND C
row 110:  A AND B AND (NOT C)
row 111:  A AND B AND C
```

### Step 2: OR them together

The output is 1 if we are in any of those rows:

```
MAJORITY = (NOT A)·B·C + A·(NOT B)·C + A·B·(NOT C) + A·B·C
```

Here `·` means AND and `+` means OR, which is how you will see it written in most books. That
already works: four 3-input ANDs, three NOTs and one 4-input OR. It is correct, but it is bigger
than it needs to be.

### Step 3: simplify

Look at it in words instead. "At least two of three" means some *pair* agrees on yes. There are
only three pairs:

```
MAJORITY = A·B + A·C + B·C
```

That is the circuit on the sheet: one AND for each pair and a 3-input OR to collect them. Three
2-input ANDs and one OR, and no NOTs at all. You can check it gives the same truth table: the
row 111 is covered three times over, which does no harm, since an OR does not mind how many of its
inputs are 1.

Finding the smallest circuit for a truth table is a skill of its own; the tools for it are
Boolean algebra and **Karnaugh maps**, both worth looking up once this makes sense.

## Where you meet this

- **Fault-tolerant computers.** Spacecraft and aircraft often run three computers side by side
  and vote on the result. If one fails, the other two outvote it. This exact circuit, on every
  bit, is the voter.
- **Adders.** The carry out of a full adder is 1 when at least two of A, B and the carry in are 1.
  It is a majority vote; compare this sheet with the [Full adder](../full-adder).

## Things to try

- Build the unsimplified four-AND version from step 2 on the same inputs and compare the two
  outputs in the truth table. They should match on every row.
- Change the rule to "exactly two of three". Which row do you have to remove, and what does that
  do to the circuit?
- Add a fourth voter, D, with the rule "at least three of four". Now each AND looks at a group
  of three voters instead of a pair. How many groups of three are there? (Four: ABC, ABD, ACD
  and BCD.)

## Next

On to the **Arithmetic** group, starting with the [Half adder](../half-adder): the same method,
used to add numbers.
