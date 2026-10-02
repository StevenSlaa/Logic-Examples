---
example: two-bit-multiplier
author: Steven Slaa
---

# Multiplying two numbers

Adding needed a carry; multiplying sounds much harder. But a multiplier is built from parts you have
already met: AND gates and half adders. This example multiplies two 2-bit numbers, so 0 to 3
times 0 to 3, using the same long multiplication you learned at school. In binary the times table
is so small that one AND gate does all of it.

## What you will learn

- Why multiplying one binary digit by another is just AND
- How long multiplication works in binary: partial products, shifted, then added
- How half adders add up the columns
- How many output bits a product needs

## Before you start

[Half adder](../half-adder), because this circuit contains two of them, and
[Adding 4-bit numbers](../four-bit-adder) for reading binary numbers.

## Try it

The circuit opens on A = 3 (`A1 A0` = `11`) and B = 2 (`B1 B0` = `10`), so the outputs show
`P3 P2 P1 P0` = `0110`, which is 6.

1. Click **B0** to make B = 3. The product becomes `1001`, 9: the largest it can ever be.
2. Click **A1** to make A = 1. Now it is 1 × 3 = `0011`.
3. Click **A0** to make A = 0. Anything times zero: `0000`.
4. Open the **Truth table** tab at the bottom to see all 16 sums at once.

## The truth table

Every combination, with A and B as numbers:

| A | B | A1 A0 | B1 B0 | P3 P2 P1 P0 | Product |
|:-:|:-:|:-----:|:-----:|:-----------:|:-------:|
| 0 | any | 00 | any | 0000 | 0 |
| 1 | 1 | 01 | 01 | 0001 | 1 |
| 1 | 2 | 01 | 10 | 0010 | 2 |
| 1 | 3 | 01 | 11 | 0011 | 3 |
| 2 | 1 | 10 | 01 | 0010 | 2 |
| 2 | 2 | 10 | 10 | 0100 | 4 |
| 2 | 3 | 10 | 11 | 0110 | 6 |
| 3 | 1 | 11 | 01 | 0011 | 3 |
| 3 | 2 | 11 | 10 | 0110 | 6 |
| 3 | 3 | 11 | 11 | 1001 | 9 |

(and anything times 0 is 0, which fills in the other six rows.)

## How it works

### One-bit times tables

The whole binary times table has four entries: 0 × 0 = 0, 0 × 1 = 0, 1 × 0 = 0 and 1 × 1 = 1. That
is exactly the truth table of an AND gate. So multiplying one bit of A by one bit of B is one AND
gate, and with two bits each there are four of them, the four gates on the left. Each one is
labelled with the two bits it multiplies.

### Long multiplication

Multiply `A1 A0` by `B1 B0` the way you would on paper: first by B0, then by B1 shifted one
column left, then add.

```
            A1    A0
      ×     B1    B0
      ----------------
          A1·B0  A0·B0      ← A times B0
   A1·B1  A0·B1             ← A times B1, moved one column left
   -----------------------
   P3  P2    P1     P0
```

Each column is added on its own, just like in the [Ripple-carry adder](../ripple-carry-adder):

- **P0** is alone in its column: `A0·B0`, straight from the top gate to the output.
- **P1** adds `A1·B0` and `A0·B1`. Adding two bits is a half adder: the XOR labelled **P1** makes
  the sum digit, and the AND labelled **carry** makes the carry into the next column.
- **P2** adds `A1·B1` and that carry. Another half adder: the XOR labelled **P2** for the sum,
  the AND labelled **P3** for the carry.
- **P3** is the carry out of column 2. Nothing else lands there, so it is the last digit.

### Why four output bits

The biggest product is 3 × 3 = 9, which needs four bits (`1001`). In general an n-bit number times
an m-bit number needs n + m bits, which is why a 32-bit computer multiplying two 32-bit numbers
gets a 64-bit answer.

## Where you meet this

- **Every processor has a multiplier**, and the simplest kind, the *array multiplier*, is this
  circuit made bigger: one AND gate per pair of bits, and rows of adders to add the columns.
- **Faster multipliers** (Wallace trees, Booth encoding) are clever ways of adding those same
  partial products in fewer steps.
- **Tiny microcontrollers** with no multiplier do the same long multiplication in software, one
  shift and add at a time.

## Things to try

- Find the two rows of the truth table where the product is 6. Why does multiplying in either
  order give the same gates' outputs, just from different AND gates?
- Delete the **carry** gate and watch which products go wrong. They are exactly the ones where
  both `A1·B0` and `A0·B1` are 1.
- Add a **Splitter** set to 4 bits, mirrored, joining P0 to P3 into a bus, and show the product on
  a **Hex digit**.
- Squaring: wire B1 to A1 and B0 to A0 instead of using pins (delete B's pins first). Which
  squares can a 2-bit number have?

## Next

On to **Choosing and routing**, starting with the [Multiplexer](../mux-from-gates).
