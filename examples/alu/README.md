---
example: alu
author: Steven Slaa
---

# A 4-bit ALU

Every processor has an **arithmetic logic unit**: the part that actually computes. It takes two
numbers and an **opcode**, a small number that says what to do with them, and produces a result
and a few **flags** that describe that result. This one works on 4-bit numbers and knows four
operations. It is tiny, but it has the same shape as the ALU in the computer you are reading this
on.

## What you will learn

- What an ALU, an opcode and a flag are
- Why an ALU computes every answer at once and then chooses one
- How a multiplexer turns an opcode into a choice
- How flags such as ZERO and CARRY are made

## Before you start

[Adding 4-bit numbers](../four-bit-adder) for buses, and the [Multiplexer](../mux-from-gates).
[Ripple-carry adder](../ripple-carry-adder) shows what the Adder part is made of.

## Try it

The circuit opens with **A** = 6, **B** = 3 and **OP** = 0, so **RESULT** shows 9 (6 + 3).

1. Click **OP** to step through the four operations. With A = 6 and B = 3:

   | OP | Operation | RESULT | Why |
   |:--:|-----------|:------:|-----|
   | 0  | A + B     |   9    | 6 + 3 |
   | 1  | A − B     |   3    | 6 − 3 |
   | 2  | A AND B   |   2    | `0110 AND 0011 = 0010` |
   | 3  | A OR B    |   7    | `0110 OR 0011 = 0111` |

2. Set OP to 1 and make A and B equal. RESULT is 0 and the green **ZERO** flag lights.
3. Set A = 3 and B = 6 with OP = 1. 3 − 6 does not fit in an unsigned number: RESULT wraps round to
   13, and the **BORROW** flag lights to say so.
4. Set A = 12, B = 7 and OP = 0. The answer, 19, is too big for 4 bits: RESULT shows 3 and **CARRY**
   lights.

The **Truth table** tab works here too, with 1024 rows: every A, every B, every opcode.

## How it works

**Four units, all working all the time.** A and B each fan out to four parts at once: an Adder, a
Subtractor, and AND and OR gates. The two gates have their **Data bits** set to 4, so each one works
on all four bits side by side: bit 0 of A with bit 0 of B, bit 1 with bit 1, and so on. That is
called a **bitwise** operation.

**A multiplexer chooses.** All four answers arrive at a 4-input Multiplexer, set to 4 data bits. OP
is a 2-bit number, wired to the multiplexer's select input, so it picks one of the four:

```
OP = 0  →  input 0  →  adder
OP = 1  →  input 1  →  subtractor
OP = 2  →  input 2  →  AND
OP = 3  →  input 3  →  OR
```

This looks wasteful, since three of the four answers are thrown away every time, but it is how
real hardware works. Gates cost almost nothing to leave running, and computing everything at once
means the right answer is ready the moment the opcode arrives, instead of waiting for the right
unit to start.

**Flags.** The flags describe the result so the next instruction can make a decision:

- **ZERO** comes from a Comparator that checks RESULT against a Constant of 0. Processors use this
  flag for "if equal": subtract two numbers, and if the result is zero they were the same.
- **CARRY** is the adder's carry out: the true sum did not fit in 4 bits.
- **BORROW** is the subtractor's borrow out: B was bigger than A, so the result wrapped round.

CARRY and BORROW here always come from their own units, whichever operation is selected. A real
ALU usually routes them through the same multiplexer so the flag always matches the result.

## Where you meet this

- **Every CPU.** An instruction such as `ADD R1, R2` or `AND R1, R2` becomes an opcode on an ALU
  just like this one, only 32 or 64 bits wide and with a dozen or more operations.
- **Conditional jumps.** `if (a == b)` compiles to a subtraction followed by a jump that looks at
  the ZERO flag. `if (a < b)` looks at the borrow.
- **The 74181**, a famous 1970s chip, was a 4-bit ALU with 32 operations. Minicomputers built their
  processors from several of them side by side.

## Things to try

- Add a fifth operation, XOR: a 4-bit XOR gate on A and B. The multiplexer only has four inputs, so
  set its **Select bits** to 3 and widen OP to 3 bits. That gives eight slots; fill the new ones.
- Make the CARRY flag follow the operation: a second multiplexer with 2 select bits and 1 data bit,
  wired to OP, with the adder's carry on input 0, the subtractor's borrow on input 1, and a
  Constant 0 on inputs 2 and 3.
- Add a **NEGATIVE** flag: in signed numbers the top bit is the sign. Use a Splitter on RESULT and
  take bit 3.
- Build the subtractor from the adder instead: A − B = A + (NOT B) + 1. That is how real ALUs
  avoid having two separate units.

## Next

[Shift register](../shift-register): moving bits in time rather than combining them.
