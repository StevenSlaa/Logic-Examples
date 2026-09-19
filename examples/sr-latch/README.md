---
example: sr-latch
author: Steven Slaa
---

# SR latch: a circuit that remembers

Every circuit so far has had no memory. Give it the same inputs and it gives the same outputs,
whatever happened a second ago. This one is different: press **S** and let go, and the output
stays on. Press **R** and let go, and it stays off. Two ordinary NOR gates, wired so that each
one's output feeds the other's input, can hold on to one bit. That loop is where all computer
memory begins.

## What you will learn

- What feedback is, and why it lets a circuit remember
- What Set, Reset and Hold do in an SR latch
- Why the "both on" case is called forbidden

## Before you start

[The basic gates](../basic-gates), especially NOR. [De Morgan's laws](../de-morgan) helps with
the "How it works" section but is not essential.

## Try it

The circuit opens with **R** (reset) held on, so it starts in a known state: **Q** is 0 and
**NOT Q** is 1.

1. Click **R** to turn it off. Q stays at 0. With both inputs off, the latch is *holding*.
2. Click **S** (set) to turn it on. Q goes to 1 and the red LED lights.
3. Click **S** again to turn it off. **Q stays at 1.** Nothing is telling it to be 1 any more; it
   remembers.
4. Click **R** on and off. Q goes to 0 and stays there.
5. Now turn S and R on together. Both Q and NOT Q go to 0, which is odd for two outputs whose
   names say one is the opposite of the other. See *The forbidden state* below.

## What happens over time

A latch has no truth table in the usual sense, because the output depends on its history. So we
write what each input combination *does*:

| S | R | Q next         | Name      |
|:-:|:-:|:---------------|:----------|
| 0 | 0 | same as before | Hold      |
| 1 | 0 | 1              | Set       |
| 0 | 1 | 0              | Reset     |
| 1 | 1 | 0 (and NOT Q 0) | Forbidden |

## How it works

Remember what a NOR gate does: it outputs 1 only when **both** inputs are 0. Any 1 on an input
forces its output to 0.

The top gate takes R and NOT Q, and its output is Q. The bottom gate takes Q and S, and its output
is NOT Q. Each one's output wraps round to the other's input.

- **Reset (R = 1).** The top gate has a 1 on an input, so Q is forced to 0. Now the bottom gate
  sees Q = 0 and S = 0, so NOT Q becomes 1.
- **Set (S = 1).** The same thing, mirrored: NOT Q is forced to 0, so the top gate sees R = 0 and
  NOT Q = 0, and Q becomes 1.
- **Hold (S = R = 0).** Now each gate's output depends only on the other gate. If Q is 1, the
  bottom gate outputs 0, which lets the top gate keep outputting 1. If Q is 0, the bottom gate
  outputs 1, which keeps the top gate at 0. Both situations are stable. The circuit stays in
  whichever one it was last pushed into. That is the memory.

The wires that carry Q down and NOT Q up are the **feedback** loop. Cut either one and the memory
is gone.

## The forbidden state

With S and R both on, both gates are forced to 0, so Q and NOT Q are both 0. That is not
dangerous, but it is not a meaningful state either. The real problem comes when both are released
at the same moment: each gate sees two 0s, both try to output 1, which forces both back to 0, and
so on. The circuit oscillates, or settles whichever way the faster gate wins, which you cannot
predict. That is why this example opens with R held on: with both inputs off and no history, the
Logic Lab would show you exactly that race.

Clicking one pin at a time, you cannot release both at once here. Real circuits avoid the problem
by never letting S and R be on together; the [D flip-flop](../d-flip-flop) does it by design.

## Where you meet this

- **Switch debouncing.** A mechanical switch bounces for a few milliseconds when pressed, making
  it look like many presses. An SR latch wired to a changeover switch catches the first contact
  and ignores the bounces.
- **Static RAM.** Every bit of a CPU's cache is a pair of inverters feeding each other, the same
  loop as this latch, plus two transistors for reading and writing it.
- **Alarm latches.** An alarm that must stay on after the sensor stops seeing anything, until
  someone presses reset, is an SR latch.

## Things to try

- Build the same latch from NAND gates. With NAND the inputs become *active low*: the latch sets
  when S goes to **0**. Label the pins `NOT S` and `NOT R` to keep that straight.
- Compare it with the **SR latch** part from the Memory section of the parts list, wired to its own
  pair of pins.
- Delete one of the feedback wires and try Set, then release. Q no longer holds.

## Next

[D flip-flop](../d-flip-flop): memory that only changes at the tick of a clock.
