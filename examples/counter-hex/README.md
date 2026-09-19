---
example: counter-hex
author: Steven Slaa
---

# Counter and hex display

Put a clock on a [D flip-flop](../d-flip-flop) and it takes one step per tick. Put a clock on a
**counter** and it counts the ticks. This example runs by itself: a clock ticks, a 4-bit counter
adds one on every tick, a hex display shows the count from 0 to F, and an LED marks the moment it
is about to wrap round. It is the heartbeat of timers, stopwatches and every processor's program
counter.

## What you will learn

- How the Logic Lab's clock and simulation speed work
- What a counter does on each rising edge, and what happens at the top
- Why a clear input is synchronous, and what that means

## Before you start

[D flip-flop](../d-flip-flop), for rising edges. [Adding 4-bit numbers](../four-bit-adder)
explains the hex display.

## Try it

This example starts with the clock running: the stopwatch button in the toolbar is on, and the
speed next to it is 2 Hz.

1. Watch the hex digit count 0, 1, 2 … 9, A, B … F, then back to 0.
2. When it reaches **F** (15), the red **carry** LED lights for one count.
3. Hold down **CLEAR**. On the next tick the counter goes back to 0 and stays there as long as you
   hold it. Let go and it carries on counting.
4. Change the speed to 16 Hz to make it race, or turn the stopwatch off and press the **Step**
   button next to it to advance one tick at a time.
5. Open the **Timing** tab to see the clock as a waveform.

## What happens over time

The clock's output goes high on odd ticks and low on even ones. Each **rising edge**, from 0 to 1,
moves the counter on by one, so the count goes up once every two ticks:

```
tick    0   1   2   3   4   5   6   7   8
CLK     0   1   0   1   0   1   0   1   0
count   0   1   1   2   2   3   3   4   4
```

After 15 comes 0: four bits can only hold 0 to 15, so the count wraps round, exactly like the
overflow in the 4-bit adder. The **carry** output is 1 while the count is 15, one step before the
wrap.

## How it works

The **Clock** part outputs a square wave in step with the simulation's tick counter. Its *Ticks per
phase* setting slows it down: at 2, it stays high for two ticks and low for two.

The **Counter** part is a 4-bit register with an adder feeding it: on each rising edge of its clock
input it loads its own value plus one. Its settings are the **Data bits** (how far it counts
before wrapping) and the **Radix** used to show its value.

**CLEAR** is a **Button** part: it outputs 1 only while you hold it down. It is wired to the
counter's R (reset) input. The reset is **synchronous**: it does not act the instant you press
it, but at the next rising edge, when the counter would otherwise have added one. Synchronous
reset keeps every change on the clock edge, for the reason the D flip-flop README gives.

The counter also has an **EN** (enable) input on its bottom edge. It is not connected here; an
enable that is not connected counts as on. Wire a 0 to it and the counter freezes.

## Where you meet this

- **Program counters.** A processor's program counter holds the address of the next instruction
  and counts up by one after each, unless a jump loads it with something else.
- **Timers.** A microcontroller's timer is a counter on its clock. When it wraps round, its carry
  raises an interrupt, which is how `sleep(1)` knows a second has passed.
- **Frequency dividers.** Bit 0 of the counter flips at half the clock rate, bit 1 at a quarter,
  and so on. A digital watch gets its one-second tick by counting a 32 768 Hz crystal: 2¹⁵ ticks is
  exactly one second.

## Things to try

- Wire an **Input pin** to the **EN** input and use it as a pause switch.
- Set the counter's **Data bits** to 3. It now counts 0 to 7. When does carry light up now?
- Make it count to 9 and wrap, like one digit of a clock: use a **Comparator** or an AND gate to
  spot 9, and feed that into CLEAR instead of the button. (Because the reset is synchronous, spot
  9, not 10.)
- Chain two counters: the first one's carry goes into the second one's EN, both on the same clock.
  Now you have an 8-bit counter shown on two hex digits.

## Next

[Traffic light](../traffic-light): a counter driving a decoder, to make a small state machine.
