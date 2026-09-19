---
example: nand-only
author: Steven Slaa
---

# Everything from NAND

Every gate on this sheet is the same one: NAND. Yet the three outputs are NOT, AND and OR. NAND
is called a **universal gate** because any circuit at all, a whole processor included, can be
built out of NAND gates and nothing else. This example shows how the three you need are made.

## What you will learn

- Why NAND (and NOR) are called universal gates
- How to build NOT, AND and OR from NAND gates alone
- How to check a rebuilt gate against the real one with a truth table

## Before you start

[The basic gates](../basic-gates) and [De Morgan's laws](../de-morgan). The OR section below
is De Morgan's first law put to work.

## Try it

1. Click **A** and **B** through all four combinations.
2. Compare the three outputs with what you would expect from real NOT, AND and OR gates.
3. Open the **Truth table** tab and check all four rows at once.

## The truth table

| A | B | NOT A | A AND B | A OR B |
|---|---|:-----:|:-------:|:------:|
| 0 | 0 |   1   |    0    |   0    |
| 0 | 1 |   1   |    0    |   1    |
| 1 | 0 |   0   |    0    |   1    |
| 1 | 1 |   0   |    1    |   1    |

## How it works

**NOT from one NAND (top).** Both inputs of the NAND are wired to A. A NAND outputs 0 only when
both of its inputs are 1, and here both inputs are always the same, so:

```
A = 0  →  NAND(0, 0) = 1
A = 1  →  NAND(1, 1) = 0
```

That is a NOT gate.

**AND from two NANDs (middle).** The first NAND gives `NOT (A AND B)`. The second one has both
inputs tied together, so it is the NOT gate from above, and it flips that back:

```
NOT (NOT (A AND B))  =  A AND B
```

**OR from three NANDs (bottom).** The first two NANDs each have their inputs tied together, so
they are NOT A and NOT B. The last NAND combines them:

```
NAND(NOT A, NOT B)  =  NOT ((NOT A) AND (NOT B))  =  A OR B
```

The last step is De Morgan's law. Say it in words: "it is not the case that A and B are both
off" means "A or B is on".

Since NOT, AND and OR together can describe any truth table (the
[Majority vote](../majority-vote) example shows how), and NAND can make all three, NAND can make
anything.

## Where you meet this

- **Chip manufacturing.** In CMOS, the transistor technology in almost every chip, a NAND gate
  takes four transistors while an AND takes six (it is a NAND plus a NOT). Chips are full of
  NANDs.
- **The 7400.** One of the first and best-known logic chips, the 7400, holds four NAND gates and
  nothing else. It is still made today.
- **Flash memory.** The "NAND" in NAND flash, the storage in USB sticks and SSDs, refers to how
  its memory cells are wired in series, the same way the transistors inside a NAND gate are.

## Things to try

- Build XOR from four NAND gates. Hint: call the first NAND `N = NAND(A, B)`; then
  `XOR = NAND(NAND(A, N), NAND(B, N))`. Check it against a real XOR gate on the same inputs.
- NOR is universal too. Build NOT, OR and AND from NOR gates only; it is this example with AND and
  OR swapped everywhere.
- Count the gates: how many NANDs does your XOR use, compared with how many AND, OR and NOT
  gates you would need?

## Next

[Majority vote](../majority-vote): given any truth table, how to find a circuit for it.
