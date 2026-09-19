---
example: d-flip-flop
author: Steven Slaa
---

# D flip-flop: remembering on a clock edge

The [SR latch](../sr-latch) remembers, but it reacts the instant its inputs change. In a big
circuit, signals arrive at slightly different times, and a latch that listens all the time will
catch some of them half-way. The fix is to listen only at one precise moment: when a clock signal
rises from 0 to 1. A **D flip-flop** does exactly that. It is the most common memory element in
digital electronics; a processor contains millions of them.

## What you will learn

- The difference between level-triggered and edge-triggered memory
- What a rising clock edge is
- Why almost every digital system is built around a clock

## Before you start

[SR latch](../sr-latch), for the idea of a circuit holding one bit.

## Try it

Everything starts at 0. **D** is the data you want to store and **CLK** is the clock, which here
you drive by hand.

1. Click **D** to set it to 1. **Q** does not change. The flip-flop is not listening.
2. Click **CLK** to take it from 0 to 1. That is a **rising edge**, and at that moment Q copies D:
   Q is now 1 and the green LED lights.
3. Click **D** back to 0. Q stays 1. The clock is high, but it is not *rising*, so the flip-flop
   still is not listening.
4. Click **CLK** back to 0. That is a falling edge, which this flip-flop ignores. Q stays 1.
5. Click **CLK** to 1 again. Rising edge: Q copies D, which is now 0.

The **Signals** tab at the bottom lists D, CLK and Q with their current values, if you would rather
read them than follow the wires.

## What happens over time

| CLK                | D | Q next         |
|:-------------------|:-:|:---------------|
| rising (0 → 1)     | 0 | 0              |
| rising (0 → 1)     | 1 | 1              |
| anything else      | x | same as before |

The `x` means it does not matter what D is. Only the value of D at the rising edge counts.

## How it works

Think of the flip-flop as a camera, with the clock as the shutter button. D is whatever is in
front of the camera, and it can change as often as it likes. Q is the last photo taken. It only
changes when you press the button, and then it shows what was in front of the lens *at that
instant*.

Inside, a D flip-flop is usually two latches in a row, with the clock inverted between them. While
the clock is low, the first latch follows D and the second one holds. When the clock rises, the
first latch freezes and the second one copies it. At no moment are both open at once, so D can
never run straight through. That arrangement is called **master–slave**.

**NOT Q** is simply the opposite of Q, provided because it is often needed and saves an inverter.

## Why clocks

With every flip-flop in a system updating on the same clock edge, the whole circuit moves in steps.
Between edges, signals ripple through the gates and settle; at the edge, every flip-flop captures
the settled result at once. As long as the clock is slow enough for everything to settle, it does
not matter which signal arrived first. That is what the "3 GHz" of a processor means: its
flip-flops take a step three billion times a second.

## Where you meet this

- **Registers.** An 8-bit register is eight D flip-flops sharing one clock. The Logic Lab's
  **Register** part is exactly that.
- **Pipelines.** A processor passes each instruction through stages with a row of flip-flops
  between them, so each stage can work on a different instruction at the same time.
- **Synchronisers.** A button press arriving at any moment is fed through a flip-flop or two so
  that the rest of the circuit only ever sees it change on a clock edge.

## Things to try

- Replace the **CLK** input pin with a **Clock** part and start the clock with the stopwatch button
  in the toolbar. Now Q copies D once per clock period; toggle D and watch Q follow a little late.
- Wire **NOT Q** back to **D** (delete the D pin first). Every rising edge now flips Q. You have made
  a circuit that divides the clock frequency by two. Chain four of them, each one's NOT Q clocking
  the next, and the four Q outputs count up in binary: a 4-bit ripple counter.
- Put four flip-flops side by side on one clock to make a 4-bit register, and compare it with the
  **Register** part.

## Next

[Counter and hex display](../counter-hex): a clock that runs by itself, and a counter that counts
its ticks.
