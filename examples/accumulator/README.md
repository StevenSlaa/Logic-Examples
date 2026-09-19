---
example: accumulator
author: Steven Slaa
---

# Accumulator: a register that adds

Early computers had one special register, the **accumulator**, and almost every instruction
worked on it: add a number to the accumulator, subtract from it, store it. This circuit is that
idea in its simplest form. An 8-bit register holds a running total, and every press of **ADD**
adds the input to it. The interesting part is the loop: the register's output goes into the adder,
and the adder's output goes back into the register.

## What you will learn

- How a register and an adder in a loop keep a running total
- Why the loop needs a clock to be safe
- How to combine two buttons into one clock, and what a synchronous clear is
- What happens when an 8-bit total overflows

## Before you start

[Adding 4-bit numbers](../four-bit-adder), [D flip-flop](../d-flip-flop) and
[Counter and hex display](../counter-hex).

## Try it

The circuit opens with **IN** = 5 and a total of 0.

1. Press **ADD**. **TOTAL** becomes 5.
2. Press ADD again: 10. Again: 15. Each press adds IN once.
3. Change IN to 100 and press ADD. The total jumps by 100.
4. Press **CLEAR**. The total goes back to 0.
5. Set IN to 250 and press ADD twice. The second time, the total wraps round past 255 and starts
   again from the bottom. See *Overflow* below.

The value display on the right shows the total in decimal; select it and change its **Radix** to
see the same number in hex or binary instead.

## How it works

**The loop.** The Adder has two inputs: IN on one, and on the other the register's own output,
which comes back round the bottom of the sheet. So the adder is always working out `total + IN`.
That answer sits waiting at the register's D input.

**The clock makes it safe.** Nothing changes until the register's clock rises. At that instant the
register copies `total + IN`, and that becomes the new total. The adder immediately starts working
out `new total + IN`, but the register is not listening any more, so the total only goes up once
per press.

Without the clock, if the register simply passed D through to Q, the loop would add IN, feed the
result back, add IN again, and keep going as fast as the gates could switch, forever. Clocked memory
is what makes a feedback loop like this behave.

**Two buttons, one clock.** ADD and CLEAR both need to make the register do something, but it has
one clock input. So they meet in an OR gate: pressing either one makes the clock rise. CLEAR is
also wired to the register's R (reset) input. The register's reset is **synchronous**: it only acts
on a clock edge. So pressing CLEAR does two things at once, R goes high and the clock rises, and on
that edge the register loads 0 instead of the sum.

## Overflow

The register and the adder are 8 bits wide, so the total can be 0 to 255. Past that it wraps:
250 + 250 = 500, and 500 − 256 = 244, so the total shows 244. The adder's carry out, which is not
connected here, is the ninth bit that got lost. A real processor keeps it in a **carry flag**, which
is how programs add numbers bigger than one register.

## Where you meet this

- **The first computers.** EDSAC (1949) and many machines after it did nearly all their arithmetic
  in an accumulator. The instruction "add the number at address 20" meant exactly this circuit,
  with IN coming from memory.
- **Microcontrollers.** The 6502 in the Commodore 64 and the NES, and the 8051 still found in
  cheap devices, are accumulator machines: their `A` register is this.
- **Digital signal processing.** A "multiply-accumulate" unit, the heart of audio filters and neural
  networks, is this loop with a multiplier in front of the adder.
- **Counters and timers.** Add 1 each tick and you have a counter; add a different number each tick
  and you have a frequency synthesiser.

## Things to try

- Replace ADD with a **Clock** part and start the clock. The total now climbs by IN on every tick.
  Set IN to 1 and you have built a counter from an adder and a register.
- Add a **SUB** button: put a Subtractor next to the adder, a 2-input Multiplexer choosing between
  them, and wire a MODE input pin to its select. You are halfway to the [ALU](../alu).
- Connect the adder's COUT to an LED that lights when the next ADD would overflow.
- Add a second register that copies the total when you press a STORE button: a memory for one
  answer, like the M+ key on a calculator.

## Next

[Electronic dice](../dice): a counter, a comparator and some decoding logic, put together into
something you can play with.
