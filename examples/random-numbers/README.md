---
example: random-numbers
author: Steven Slaa
---

# Random numbers from a shift register

Computers are machines that do exactly the same thing every time, so where do random numbers come
from? Very often from this circuit: a *linear-feedback shift register*, or LFSR. It is four
flip-flops and one gate, and it produces a sequence that looks thoroughly jumbled, visits every
4-bit number but one, and then starts again. It is not truly random, which is exactly why it is
useful: the same start always gives the same sequence.

## What you will learn

- How a shift register with feedback produces a long, jumbled sequence
- Why XNOR feedback can start from all zeros, and which state it must never reach
- What "pseudo-random" means
- Why the taps (which bits are fed back) matter

## Before you start

[D flip-flop](../d-flip-flop) and the [Shift register](../shift-register), which is the same
chain of flip-flops without the feedback.

## Try it

1. Press play (the stopwatch button in the toolbar). The clock ticks twice a second.
2. Watch the hex digit: 1, 3, 7, E, D, B, 6, C, 9, 2, 5, A, 4, 8, 0, and then 1 again.
3. Count them. That is 15 different numbers, every 4-bit value except F.
4. Watch the LEDs instead: each tick, every bit moves one place right, and a new bit appears at Q0.

## What happens over time

The register starts at all zeros, and on each rising clock edge every flip-flop copies its left
neighbour. Q0, which has no left neighbour, takes the feedback: `Q2 XNOR Q3`.

| Clock edge | Q3 Q2 Q1 Q0 | Digit | Feedback: Q2 XNOR Q3 |
|:----:|:-----------:|:-----:|:--------------------:|
| start | 0000 | 0 | 1 |
| 1  | 0001 | 1 | 1 |
| 2  | 0011 | 3 | 1 |
| 3  | 0111 | 7 | 0 |
| 4  | 1110 | E | 1 |
| 5  | 1101 | D | 1 |
| 6  | 1011 | B | 0 |
| 7  | 0110 | 6 | 0 |
| 8  | 1100 | C | 1 |
| 9  | 1001 | 9 | 0 |
| 10 | 0010 | 2 | 1 |
| 11 | 0101 | 5 | 0 |
| 12 | 1010 | A | 0 |
| 13 | 0100 | 4 | 0 |
| 14 | 1000 | 8 | 0 |
| 15 | 0000 | 0 | 1 |

Edge 15 is back to `0000`, the same as the start, so from here the 15 states repeat in the same
order forever. Each row's feedback bit is the Q0 of the row below it.

## How it works

### The shift register

The four **D flip-flops** are chained Q to D, exactly as in the [Shift register](../shift-register):
on every clock edge each one takes the value of the one before it. On its own that would just
move one bit along and push it off the end.

### The feedback

The trick is what goes into the first flip-flop. The **XNOR** gate at the top looks at the last
two bits, Q2 and Q3, and its answer becomes the next Q0. XNOR is "the two match": 1 when Q2 and Q3
are the same, 0 when they differ. So the bit that comes in depends on bits that are about to
leave, and the register keeps stirring itself.

### Why it never shows F

There is one state the circuit can never leave: `1111`. Q2 and Q3 are both 1, they match, the
feedback is 1, and the register shifts in a 1 and is `1111` again, forever. Every other state is
on one big loop of 15. Since `0000` is on the loop, the circuit can start from all zeros, which is
how flip-flops power up. (The classic version uses XOR instead; then `0000` is the stuck state,
and the register has to be seeded with something else first.)

### Why these taps

Feeding back Q2 and Q3 is a deliberate choice. Feedback from other pairs of bits gives shorter
loops; try it below. The taps that give the longest possible loop, 2ⁿ − 1 states for n bits, come
from the mathematics of polynomials over two values, and engineers simply look them up in a table.

## Where you meet this

- **Video games.** Many early consoles made their "random" enemy moves and noise sound effects
  with an LFSR; the Atari 2600 and the NES sound chip both had one.
- **Wi-Fi, Bluetooth, USB and Ethernet** scramble the bits they send with an LFSR, so long runs of
  identical bits do not confuse the receiver.
- **GPS satellites** each broadcast their own LFSR sequence, which is how a receiver tells them apart.
- **Chip testing.** A chip can test itself by feeding LFSR patterns through its own logic.

## Things to try

- Move the feedback tap: wire the XNOR's lower input to Q1 instead of Q2. How many numbers does it
  visit now before repeating?
- Replace the XNOR with an XOR. Now the circuit is stuck at 0 from the start. Why? (What does
  `0 XOR 0` give?)
- Make it 5 bits long with feedback from Q2 and Q4. A 5-bit maximal LFSR visits 31 states.
- Use only Q0 as your random bit, and watch it on its own LED. Does it look like coin flips?

## Next

[Edge detector](../edge-detector): a single flip-flop that remembers the past just long enough to
notice the moment a button goes down.
