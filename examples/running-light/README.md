---
example: running-light
author: Steven Slaa
---

# Running light

A row of lights where one dot runs along and wraps round is the classic "this machine is busy"
display, from 1980s TV cars to the progress bars in installers. You could build it from a counter
and a [Decoder](../decoder-leds). This example does it a stranger and cleverer way: a ring of four
flip-flops that runs through eight states, and eight AND gates that each need to look at only two
wires to know which state it is in.

## What you will learn

- What a Johnson counter (or "twisted ring" counter) is, and why it has twice as many states as
  flip-flops
- How to decode a state from just two neighbouring bits
- Why every flip-flop's inverted output `~Q` is useful
- How to read a pattern from a table of states

## Before you start

The [Shift register](../shift-register), which this circuit closes into a ring, and the
[Decoder](../decoder-leds) for the idea of lighting one output per number.

## Try it

1. Press play (the stopwatch button in the toolbar).
2. Watch the column of red LEDs on the right: one light runs from 0 down to 7, then jumps back to 0.
3. Now watch the four flip-flops at the top. Ones fill up from the left, then zeros follow them.
4. Pause, and step one tick at a time with the step button to match each light with the flip-flops.

## What happens over time

| Clock edge | Q0 Q1 Q2 Q3 | Light | Picked out by |
|:----------:|:-----------:|:-----:|:-------------:|
| start | 0 0 0 0 | 0 | ¬Q0 and ¬Q3 |
| 1     | 1 0 0 0 | 1 | Q0 and ¬Q1 |
| 2     | 1 1 0 0 | 2 | Q1 and ¬Q2 |
| 3     | 1 1 1 0 | 3 | Q2 and ¬Q3 |
| 4     | 1 1 1 1 | 4 | Q3 and Q0 |
| 5     | 0 1 1 1 | 5 | ¬Q0 and Q1 |
| 6     | 0 0 1 1 | 6 | ¬Q1 and Q2 |
| 7     | 0 0 0 1 | 7 | ¬Q2 and Q3 |
| 8     | 0 0 0 0 | 0 | back to the start |

`¬Q0` means "not Q0", which is the flip-flop's `~Q` output.

## How it works

### The twisted ring

The four **D flip-flops** are a [Shift register](../shift-register): on each clock edge every bit
moves one place right. If the last bit went straight back to the first, whatever pattern was in
the ring would just go round and round. Instead the wire along the top takes the last flip-flop's
**inverted** output, `~Q3`, back to the first D input. That twist is the whole trick.

Starting from all zeros, `~Q3` is 1, so ones shift in from the left until the ring is full. Now
`~Q3` is 0, so zeros shift in and chase the ones out. After eight edges the ring is empty again.
Four flip-flops, eight states: a Johnson counter always has twice as many states as it has stages.

### Decoding with two wires

A normal 3-bit counter would need gates looking at all three bits to pick out one state. A Johnson
counter's patterns are much friendlier: every state is a block of ones and a block of zeros, so
each state is completely identified by the one place where the pattern changes. Look at state 2,
`1 1 0 0`: it is the only state where Q1 is 1 and Q2 is 0. State 4, `1 1 1 1`, is the only one with
both ends set.

So each of the eight **AND gates** on the right looks at just two neighbouring wires, as labelled
above it, and drives one LED. The eight long wires running down the sheet carry each flip-flop's
`Q` and `~Q` to the gates that need them.

## Where you meet this

- **Clock dividers and multi-phase clocks.** A Johnson counter's outputs are evenly spaced copies
  of a slower clock, which is useful for driving motors and in radio receivers.
- **Stepper motors** step through a short fixed pattern of coil currents, which is a counter like
  this one.
- **Glitch-free decoding.** Only one flip-flop changes per tick, so the two-input decoders never
  briefly show a wrong state while bits are changing; with an ordinary binary counter they can.
- **LED chasers and "Knight Rider" lights** are this circuit, or a cousin of it.

## Things to try

- Remove the twist: connect Q3 (not `~Q3`) to the first D input. What happens from all zeros?
- Add a fifth flip-flop to the ring. How many states are there now, and which pairs of wires would
  you need to decode them?
- Make the light bounce instead of wrapping: you need only the first five lights, then the same
  five in reverse. Which gates' outputs would you OR together?
- Turn the four flip-flops' Q outputs into a [Hex digit](../counter-hex) with a joining Splitter.
  The numbers come out as 0, 1, 3, 7, F, E, C, 8: can you see the pattern?

## Next

That is the end of the core course. The **Projects** group puts it all together, starting with
the [Ripple-carry adder](../ripple-carry-adder): a 4-bit adder built from nothing but gates.
