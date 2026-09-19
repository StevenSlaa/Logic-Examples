---
example: ripple-carry-adder
author: Steven Slaa
---

# Ripple-carry adder from gates

The [Adding 4-bit numbers](../four-bit-adder) example used the Adder part, a box that simply
works. This one opens the box. It adds two 4-bit numbers with nothing but XOR, AND and OR gates:
four [full adders](../full-adder), twenty gates in all, with the carry handed from one to the
next. On the way it introduces the two tools every larger circuit needs: **splitters**, to take a
bus apart and put it back together, and **tunnels**, to connect wires without drawing them.

## What you will learn

- How to split a bus into single bits, and join bits back into a bus
- How tunnels keep a large circuit readable
- How a multi-bit adder is built from identical one-bit slices
- Why a ripple-carry adder is simple but slow

## Before you start

[Full adder](../full-adder), which this circuit repeats four times, and
[Adding 4-bit numbers](../four-bit-adder) for buses and hex.

## Try it

The circuit opens with **A** = 9 and **B** = 5, so **SUM** shows 14 and the hex digit shows `E`.

1. Click **A** and **B** to count them up, or set them in the Inspector. SUM always matches A + B
   until the answer passes 15.
2. Set A = 15 and B = 1. The answer is 16, so SUM goes to 0 and **COUT** lights. Every carry wire,
   C1 to C4, is now bright: each column overflowed into the next.
3. Turn on **CIN** to add one more.
4. Compare it with the Adder part in [Adding 4-bit numbers](../four-bit-adder): same inputs,
   same outputs, and now you can see every gate that produces them.

## The layout, left to right

**Splitting the inputs.** A and B arrive as 4-bit buses (thick wires). Each goes into a
**Splitter**, which has the bus on one side and one wire per bit on the other. Branch 0 is the
least significant bit, worth 1; branch 3 is the most significant, worth 8. Each bit goes to a
tunnel named after it: `A0` to `A3` and `B0` to `B3`. CIN goes to a tunnel called `C0`.

**Tunnels.** Every tunnel with the same name is connected to every other one, as if a wire ran
between them. The `A0` tunnel on the left and the `A0` tunnel in the first adder are the same
signal. This keeps the drawing readable: without tunnels, eight wires would have to snake from the
inputs to four adders, crossing each other the whole way. Each tunnel shows its name above it.

**Four full adders.** The four blocks down the middle are the same circuit, one per bit. Block *i*
takes `Ai`, `Bi` and the carry in `Ci`, and produces the sum bit `Si` and the carry out
`C(i+1)`. It is exactly the [Full adder](../full-adder), gate for gate:

```
Si      = Ai XOR Bi XOR Ci
C(i+1)  = (Ai AND Bi) OR (Ci AND (Ai XOR Bi))
```

**Joining the result.** On the right, tunnels `S0` to `S3` feed a second splitter, drawn the other
way round. With its single wires driven, a splitter **joins** them into a bus, which goes to the
SUM pin and the hex display. The last carry, `C4`, is the COUT output.

## The carry chain

Follow the tunnels named `C`: CIN is `C0`, the first adder's carry out is `C1`, which is the
second adder's carry in, and so on to `C4`. That chain is what makes this a **ripple-carry**
adder.

It is also its weakness. Bit 3 cannot know its sum until bit 2 has worked out its carry, which
waits for bit 1, which waits for bit 0. In real hardware each gate takes a little time to switch,
so the delay grows with every bit: a 64-bit ripple adder waits for 64 carries in a row. (The Logic
Lab solves the whole circuit at once, so you see the settled answer rather than the wave.)

Real processors use **carry-lookahead** adders instead. They work out every carry straight from
the inputs, using the fact that a column *generates* a carry when `Ai AND Bi`, and *propagates*
one when `Ai XOR Bi`. More gates, far less waiting.

## Where you meet this

- **Early microprocessors** used ripple-carry adders because they are small. Today they still turn
  up where space matters more than speed.
- **Splitters and tunnels** are how every larger schematic is drawn. Real chip schematics use
  *net labels*, which are exactly tunnels: a name on a wire instead of the wire itself.

## Things to try

- Make it an 8-bit adder: copy the four blocks, rename their tunnels to bits 4 to 7 (`A4`, `C5`,
  and so on), widen the pins to 8 bits and use 8-branch splitters.
- Break it on purpose: rename one adder's carry-in tunnel from `C2` to `C9`, so nothing drives it.
  Try 3 + 1 and then 4 + 0: both come out wrong, in different ways. An input with nothing
  connected is treated as whatever leaves its gate unchanged, which is 0 for XOR but 1 for AND. So
  that adder's sum acts as if the carry were 0 while its carry acts as if it were 1, and the
  answers are off in both directions. That is why a missing wire can be so hard to spot.
- Turn it into a subtractor. A − B is A + (NOT B) + 1: put a NOT gate on each B bit and turn CIN on.
  Check that 9 − 5 gives 4.

## Next

[A 4-bit ALU](../alu): an adder, a subtractor and two logic operations, with a multiplexer to
choose between them.
