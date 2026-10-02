---
example: edge-detector
author: Steven Slaa
---

# Edge detector

A button tells a circuit whether it is held down *right now*. Very often that is the wrong
question. A lift should count one press of the call button, not one press per millisecond you hold
it; a game should fire once when you press the trigger. What you want is the *moment* the button
goes down: the rising edge. This example finds it with one flip-flop and one gate, and two counters
side by side show the difference.

## What you will learn

- The difference between a level (is it high?) and an edge (did it just go high?)
- How a flip-flop can remember what a signal was one tick ago
- How to turn a press of any length into a pulse exactly one clock tick long
- Why almost every digital input goes through something like this

## Before you start

[D flip-flop](../d-flip-flop), and [Counter and hex display](../counter-hex) for the counter's
enable input.

## Try it

1. Press play (the stopwatch button in the toolbar). The clock rises 4 times a second.
2. Hold **PRESS** with the mouse, or hold the **space bar** if your Logic Lab supports keyboard keys
   on buttons. Keep holding for a couple of seconds.
3. The top digit, **held**, counts up on every tick while you hold. The bottom one, **presses**,
   goes up by exactly one, and the amber **PULSE** LED blinks once.
4. Let go, and press again quickly. Now both counters go up by about one each.

## What happens over time

Holding PRESS for three clock ticks, from just before tick 1:

| Clock edge | PRESS | last tick (Q) | new press (PULSE) | held | presses |
|:----------:|:-----:|:-------------:|:-----------------:|:----:|:-------:|
| before     | 0 | 0 | 0 | 0 | 0 |
| you press  | 1 | 0 | **1** | 0 | 0 |
| 1          | 1 | 1 | 0 | 1 | 1 |
| 2          | 1 | 1 | 0 | 2 | 1 |
| 3          | 1 | 1 | 0 | 3 | 1 |
| you let go | 0 | 1 | 0 | 3 | 1 |
| 4          | 0 | 0 | 0 | 3 | 1 |

PULSE is high only between the moment you press and the next clock edge, and that edge is exactly
when the counters look at it. So **presses** sees it once, and **held** sees PRESS every time.

## How it works

### Remembering one tick ago

The **D flip-flop** labelled *last tick* has PRESS on its D input. On every clock edge it copies
PRESS, so between edges its output Q says what PRESS was at the last tick. It is a memory one tick
long.

### Spotting the change

A new press is "PRESS is down now, but was up at the last tick". The flip-flop's inverted output
`~Q` already means "was up at the last tick", so one **AND** gate does the rest:

```
new press = PRESS AND NOT (PRESS one tick ago)
```

The moment you press, PRESS goes high while the flip-flop still holds the old 0, so the AND gate
fires. At the next clock edge the flip-flop catches up, `~Q` goes low, and the pulse ends, however
long you keep holding.

### The two counters

Both **Counters** are on the same clock. *ticks held* has PRESS on its EN (enable) input, so it
counts every tick you hold. *presses* has the pulse on its EN, so it counts once per press.

## Where you meet this

- **Keyboards and buttons.** A key press is turned into one "key down" event like this, which is
  also why holding a key does not type the letter thousands of times.
- **Microcontrollers** have "interrupt on rising edge" settings on their input pins, which is this
  circuit built into the chip.
- **Counters for real-world events**, like the cars passing a sensor or the turns of a wheel,
  count edges, not levels.
- **Button debouncing.** Real buttons bounce, flickering on and off for a few milliseconds when
  pressed. Sampling them on a slow clock, as this flip-flop does, is half of the cure.

## Things to try

- Make it a *falling* edge detector, which fires when you let go: feed the AND gate PRESS's
  opposite and the flip-flop's Q instead.
- Connect the AND gate to Q instead of `~Q`. What do you have now?
- Slow the clock right down with the speed selector, and tap PRESS quickly between two rising edges.
  Sometimes the counters miss it entirely. Why?
- Use the pulse to clock the [Shift register](../shift-register) instead of a button, so every
  press shifts exactly once.

## Next

[Running light](../running-light): four flip-flops in a ring, and a light that runs down a column.
