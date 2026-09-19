---
example: dice
author: Steven Slaa
---

# Electronic dice

Hold the button and the die spins; let go and it lands on a number from 1 to 6, with the right
dots lit on a die face. There is no random number generator in it. The randomness comes from you:
a counter steps round 0 to 5 sixteen times a second, far too fast to stop on purpose, and you
decide the moment it stops. This example puts together a counter, a comparator, an adder, a
splitter and some decoding logic into one small machine.

## What you will learn

- How to make a counter count to a number other than a power of two
- How human timing can stand in for randomness
- How to design decoding logic from a picture: which dots light for which number
- How to lay out a bigger circuit so it stays readable

## Before you start

[Counter and hex display](../counter-hex), [Decoder](../decoder-leds), and
[Majority vote](../majority-vote) for turning a truth table into gates.

## Try it

The clock is already running at 32 Hz; check the stopwatch button in the toolbar is on.

1. Hold down **ROLL**. The hex digit and the die face flicker through 1 to 6.
2. Let go. The die stops on whatever it was showing.
3. Roll a few more times. Each face should come up about as often as any other.
4. To see it count, turn the speed down to 2 Hz, hold ROLL, and watch each face in turn.

## How it works

The sheet has three parts: counting on the left, the number in the middle, and the dots on the
right.

### Counting 0 to 5

The **Counter** is 4 bits wide, so on its own it would count 0 to 15. To make it wrap after 5, a
**Comparator** checks its output against a **Constant** of 5. When the count is 5, the comparator's
`=` output goes high and travels through the `WRAP` tunnel to the counter's R (reset) input. The
reset is synchronous, so on the next clock edge the counter goes to 0 instead of 6. That gives the
sequence 0, 1, 2, 3, 4, 5, 0, 1, …, six states in all.

**ROLL** is wired to the counter's EN (enable) input. While you hold it, the counter counts; let go
and EN goes low, and the counter holds its value no matter how many clock edges arrive.

### The number

A die shows 1 to 6, not 0 to 5, so an **Adder** adds a Constant of 1 before the **Hex digit**.

### The dots

This is the interesting part. A die face has seven dot positions, but they only ever light in four
groups:

```
 TL  .  TR        P2 lights TL and BR   (every face except 1)
 ML  C  MR        P4 lights TR and BL   (faces 4, 5 and 6)
 BL  .  BR        P6 lights ML and MR   (face 6 only)
                  P1 lights C           (odd faces: 1, 3 and 5)
```

So the circuit only needs four signals. Write them down against the count `c` (the face minus one)
in binary, `C2 C1 C0`:

| Face | c | C2 C1 C0 | P1 (centre) | P2 | P4 | P6 |
|:----:|:-:|:--------:|:-----------:|:--:|:--:|:--:|
|  1   | 0 |   000    |      1      | 0  | 0  | 0  |
|  2   | 1 |   001    |      0      | 1  | 0  | 0  |
|  3   | 2 |   010    |      1      | 1  | 0  | 0  |
|  4   | 3 |   011    |      0      | 1  | 1  | 0  |
|  5   | 4 |   100    |      1      | 1  | 1  | 0  |
|  6   | 5 |   101    |      0      | 1  | 1  | 1  |

Now read off each column:

- **P1 = NOT C0.** Odd faces are even counts, and an even number ends in 0.
- **P2 = C0 OR C1 OR C2.** It is on for every count except 0, and 0 is the only count with no bits
  set.
- **P4 = C2 OR (C1 AND C0).** Counts 3, 4 and 5: either C2 is set (4 and 5), or the count is `011`.
- **P6 = C2 AND C0.** Only count 5, `101`. Count 7 would match too, but the counter never gets there,
  and a designer is allowed to use that.

A **Splitter** takes the count apart into `C0`, `C1` and `C2`, tunnels carry them to the four little
gate circuits, and four more tunnels, `P1` to `P6`, carry the results to the LEDs of the die face.

## How random is it?

As random as your thumb. The counter goes through all six faces in 0.375 seconds, and nobody can
time a button press to a sixteenth of a second, so in practice every face is equally likely. That
is the same trick early video games used: they counted frames while the title screen waited for you
to press start, and used that count as their random seed.

## Where you meet this

- **Handheld electronic dice and board-game timers** are this circuit on one small chip.
- **Random seeds in software.** Many programs still seed their random numbers from a fast clock
  sampled when something unpredictable happens, like a key press or a network packet arriving.
- **Display decoding.** Turning a number into the right pattern of lights is the same job as a
  seven-segment decoder or a character generator.

## Things to try

- Speed it up or slow it down with the toolbar's speed selector. At what speed can you start to
  aim for a particular face?
- Make a coin: change the Constant 5 to 1 so it counts 0 to 1, and show heads or tails on two LEDs.
- Build a second die next to the first, on the same ROLL button, and add the two faces with an
  Adder to roll 2 to 12.
- Replace the four gate circuits with a **Decoder** on the count and OR gates, like the
  [Traffic light](../traffic-light). Which way uses fewer gates?

## Next

This is the last example in the course. You now have everything you need to design your own:
a reaction timer, a stopwatch with hex digits, or a 4-bit computer with a program counter, the
ALU and a RAM.
