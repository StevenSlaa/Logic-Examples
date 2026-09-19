---
example: shift-register
author: Steven Slaa
---

# Shift register: serial in, parallel out

Some connections only have one wire to spare: a USB data line, a network cable, a pin between two
chips. To send a whole number down it, you send the bits one after another, one per clock tick.
That is **serial** communication. At the receiving end, a **shift register** catches each bit as
it arrives and moves the earlier ones along, so after a few ticks the whole number is sitting
there side by side, **in parallel**. This one is four D flip-flops in a row.

## What you will learn

- How a chain of flip-flops moves bits along on each clock edge
- What serial and parallel mean, and how a shift register converts between them
- Why every flip-flop must share one clock

## Before you start

[D flip-flop](../d-flip-flop): this circuit is four of them.

## Try it

Everything starts at 0. **DATA** is the next bit to send and **SHIFT** is the clock: a button,
so each press is exactly one rising edge.

1. Set **DATA** to 1 and press **SHIFT**. **Q0** lights.
2. Set DATA to 0 and press SHIFT. The 1 moves to **Q1**, and Q0 takes the new 0.
3. Send 1 and then 1 again. After four presses in total, the four LEDs show the last four bits you
   sent, newest at Q0 and oldest at Q3.
4. Keep going: every press pushes one bit in on the left and drops the oldest one off the right.

Sending 1, 0, 1, 1 looks like this:

| Press | DATA | Q0 | Q1 | Q2 | Q3 |
|:-----:|:----:|:--:|:--:|:--:|:--:|
|   1   |  1   | 1  | 0  | 0  | 0  |
|   2   |  0   | 0  | 1  | 0  | 0  |
|   3   |  1   | 1  | 0  | 1  | 0  |
|   4   |  1   | 1  | 1  | 0  | 1  |

## How it works

The four flip-flops are chained: DATA goes into the first one's D, the first one's Q goes into the
second one's D, and so on. The SHIFT button is wired to all four clock inputs at once.

When SHIFT rises, **every flip-flop copies its D at the same instant**. The first one takes DATA.
The second one takes what the first one held *just before* the edge, and so on down the line. So
every bit moves exactly one place, and none is lost or skipped.

That "just before" is the whole trick, and it is why this has to be built from edge-triggered
flip-flops. Try to build it from level-triggered latches that are open while the clock is high,
and the new bit would race straight through all four in one go, the way water runs through a row
of open doors.

## Where you meet this

- **Serial ports and SPI.** A microcontroller talking to a sensor over SPI shifts bits out one per
  clock, and the sensor shifts them into a register like this one.
- **The 74HC595**, one of the most used chips in hobby electronics, is an 8-bit version of this
  circuit with an extra latch on the outputs. It turns three microcontroller pins into eight
  outputs, and chains to make more.
- **LED matrices and long LED strips** are driven by shifting data through a chain of registers.
- **Multiplying by two.** Shifting a binary number one place towards the high end doubles it, the
  way appending a 0 in decimal multiplies by ten.

## Things to try

- Send a single 1 (DATA on, press SHIFT, DATA off). Then delete the DATA pin and wire the last
  flip-flop's Q back to the first one's D. Press SHIFT: the single 1 now circles round forever, a
  **ring counter**, the circuit behind a chasing LED light.
- Wire NOT Q3 back to DATA instead. From all zeros, the pattern fills with ones and then empties
  again over eight presses: a **Johnson counter**.
- Join Q0 to Q3 into a 4-bit bus with a Splitter (drawn the other way round, so its single wires
  feed the bus) and show it on a **Hex digit**. Send the bits of a number, starting with the
  highest bit, and read it off the display.
- Replace the SHIFT button with a **Clock** part and start the clock in the toolbar.

## Next

[Sequence detector](../sequence-detector): flip-flops that do not just store bits but decide what
happens next.
