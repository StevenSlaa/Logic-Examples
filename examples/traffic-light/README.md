---
example: traffic-light
author: Steven Slaa
---

# Traffic light: a state machine

A traffic light is always in one of a few **states**, red, red and amber, green, amber, and it
moves from one to the next on a timer. That makes it a **state machine**, and it is a perfect
first one to build, because every piece is something you have already met: a clock to keep time,
a counter to remember the state, a decoder to tell the states apart, and a few OR gates to decide
which lamps each state lights.

## What you will learn

- What a state machine is: states, transitions and outputs
- How a counter can hold the state and a decoder can recognise it
- How to turn "lamp X is on in these states" into gates

## Before you start

[Decoder](../decoder-leds) and [Counter and hex display](../counter-hex). This circuit is the
two of them joined together.

## Try it

The clock starts running when the example opens. Watch the lamps cycle:

```
phase 0   red
phase 1   red + amber
phase 2   green
phase 3   amber
          … and back to phase 0
```

That is the UK and Dutch sequence for traffic. Turn off the stopwatch in the toolbar and use the
**Step** button to move one tick at a time; the phase changes every four ticks. Select the counter
to see its value (the phase) in the Inspector, and open the **Signals** tab to see each lamp.

## The states

| Phase | Counter (binary) | Decoder output on | RED | AMBER | GREEN |
|:-----:|:----------------:|:-----------------:|:---:|:-----:|:-----:|
|   0   |        00        |       out 0       |  1  |   0   |   0   |
|   1   |        01        |       out 1       |  1  |   1   |   0   |
|   2   |        10        |       out 2       |  0  |   0   |   1   |
|   3   |        11        |       out 3       |  0  |   1   |   0   |

## How it works

There are three layers, from left to right.

**1. Time: the clock.** Its *Ticks per phase* is set to 2, so it rises once every four ticks. At the
2 Hz simulation speed that is one rising edge every two seconds.

**2. State: the counter.** A 2-bit counter holds which phase we are in, 0 to 3. Each rising edge
moves it on by one, and after 3 it wraps to 0. That wrap is what makes the sequence repeat, for
free. The counter is the machine's **memory**: the only thing that knows where we are.

**3. Outputs: the decoder and the OR gates.** The decoder turns the 2-bit phase into four wires,
exactly one of them on. Then each lamp is the OR of the phases it is lit in. Read the table down
each lamp's column:

```
RED   = phase 0 OR phase 1
AMBER = phase 1 OR phase 3
GREEN = phase 2
```

That is sum of products, from the [Majority vote](../majority-vote) example, with the decoder
doing the AND half. Phase 1 feeds two OR gates, because two lamps are lit in it; the wire splits
to reach both.

This split into *state*, held in flip-flops, and *output logic*, made of gates that only look at
the state, is the shape of every state machine, however large.

## Where you meet this

- **Real traffic controllers** are state machines, with more states (pedestrian crossings, a
  flashing amber night mode) and with inputs from sensors in the road deciding some of the
  transitions.
- **Washing machines, lifts and vending machines** are state machines: fill, wash, rinse, spin.
- **Communication protocols.** A USB or network chip follows a state machine to know which part of
  a message it is receiving.
- **Processors.** Fetch, decode, execute is a state machine at the core of every CPU.

## Things to try

- Make it a Dutch pedestrian light: two states, red and green, with a 1-bit counter.
- Real lights stay red and green much longer than amber. Use a **3-bit** counter and a decoder with
  3 select bits, which gives eight phases, and spend several phases on red and several on green.
  Only the OR gates need to change.
- Add an input pin called **NIGHT** that, when on, makes the amber lamp flash and the others stay
  dark. Hint: AND the normal lamp outputs with NOT NIGHT, and OR the amber lamp with NIGHT AND
  the clock.
- Add a **Hex digit** display on the counter's output to see the phase number while it runs.

## Next

That is the end of the core course. The **Projects** group puts it all together, starting with
the [Ripple-carry adder](../ripple-carry-adder): a 4-bit adder built from nothing but gates.
