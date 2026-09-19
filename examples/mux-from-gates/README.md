---
example: mux-from-gates
author: Steven Slaa
---

# Multiplexer

A **multiplexer**, or **mux**, is a switch controlled by a signal. It has several data inputs, one
output, and a **select** input that decides which data input gets through. It is how a computer
chooses: which register to read, which result to keep, which sensor to listen to. This sheet
builds a two-input mux from gates, then puts the Logic Lab's Multiplexer part next to it so you
can see they behave the same.

## What you will learn

- What a multiplexer does, and why "select" is a different kind of input from "data"
- How to build one from AND, OR and NOT
- The idea of *gating* a signal with AND

## Before you start

[The basic gates](../basic-gates) and [Majority vote](../majority-vote), whose sum-of-products
method this circuit uses.

## Try it

1. Set **A** to 1 and **B** to 0.
2. With **S** at 0, **Y** follows A. Click A a few times and watch Y copy it. Clicking B does
   nothing.
3. Click **S** to make it 1. Now Y follows B instead, and A is ignored.
4. **Y (part)**, from the Multiplexer part at the bottom, always matches Y.
5. Open the **Truth table** tab: eight rows, and the two Y columns are identical.

## The truth table

| S | A | B | Y |
|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

A shorter way to write it:

| S | Y |
|:-:|:-:|
| 0 | A |
| 1 | B |

## How it works

The trick is using an AND gate as a **gate** in the everyday sense: a door that is open or shut.
`X AND 1` is just X, so a 1 on one input lets the other input straight through. `X AND 0` is
always 0, so a 0 shuts the door no matter what X is.

- The top AND gets **A** and **NOT S**. When S is 0, NOT S is 1, the door is open, and A gets
  through. When S is 1, the door shuts and this gate outputs 0.
- The middle AND gets **B** and **S** itself, so it is open exactly when the other one is shut.
- The OR combines them. Only one of the two ANDs can be passing anything at a time, and the other
  outputs 0, so the OR simply passes on whichever one is open.

As an expression:

```
Y = (A AND NOT S) OR (B AND S)
```

The Multiplexer part does the same thing inside one box. Its select input is on the bottom edge,
to keep it apart from the data inputs on the left.

## Bigger multiplexers

With two select lines you can choose from four inputs, with three from eight, and so on: *n*
select bits choose from 2ⁿ inputs. Select the MUX part and set **Select bits** to 2 in the
Inspector to see the four-input version. The **Data bits** setting makes every input and the
output a bus, so the same part can choose between whole numbers instead of single bits.

## Where you meet this

- **Inside a CPU.** Which register feeds the adder, and whether the next instruction comes from
  the next address or from a jump, are both decided by multiplexers.
- **Microcontroller pins.** One physical pin on a chip can be a GPIO, a UART or an I2C line. A mux
  behind the pin picks which one is connected.
- **Analog muxes** do the same with voltages: one analog-to-digital converter reading eight
  sensors in turn.

## Things to try

- Build a four-input mux from three two-input MUX parts: two of them choose on S0, and the third
  chooses between their outputs on S1. Check it against a single MUX part with 2 select bits.
- A mux can compute any function. Wire a 2-input MUX with A on the select, 0 on input 0 and B on
  input 1. What gate have you made? (AND: when A is 0 the output is 0; when A is 1 it is B.)
- Set **Data bits** to 4 on the MUX part and give it two 4-bit input pins. Now it chooses between
  two numbers.

## Next

[Decoder](../decoder-leds): the opposite job, where a number picks one output out of several.
