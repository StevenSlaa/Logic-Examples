---
example: sequence-detector
author: Steven Slaa
---

# Sequence detector: a finite-state machine

Bits arrive one at a time, and the circuit should light up whenever the last three were **1, 0,
1**. No gate can do this on its own, because the answer depends on what came *before*. The
circuit has to remember how much of the pattern it has seen so far. That memory is its **state**,
and a circuit built this way is a **finite-state machine**. This example shows the method for
designing one from scratch, step by step, and then the circuit it produces.

## What you will learn

- How to describe a problem as states and transitions
- How to turn a state diagram into a state table, and a state table into gates
- How flip-flops hold the state and gates compute the next one
- What "overlapping" detection means, and why it matters

## Before you start

[D flip-flop](../d-flip-flop), [Majority vote](../majority-vote) (sum of products) and
[Traffic light](../traffic-light), which is a simpler state machine with no inputs.

## Try it

The machine starts with nothing seen. **BIT** is the next input bit and **STEP** is the clock:
set BIT, then press STEP to feed it in.

1. Feed in 1, 0, 1: set BIT to 1 and press STEP, set it to 0 and press STEP, set it to 1 and press
   STEP. **FOUND** lights.
2. Feed in 0 and then 1. FOUND lights again: the `1` that ended the first match also started the
   second, `1 0 1 0 1`. That is **overlapping** detection.
3. Feed in 1, 1, 0, 1. FOUND lights only at the end: the first 1 was not part of it.
4. Select either flip-flop, or watch the `Q0` and `Q1` tunnels, to see the state after each step.

## Step 1: the states

What does the machine need to remember? Only how much of `1 0 1` it has matched so far:

| State | Meaning               | Q1 Q0 |
|:-----:|-----------------------|:-----:|
| S0    | nothing useful yet    |  00   |
| S1    | just saw `1`          |  01   |
| S2    | just saw `1 0`        |  10   |
| S3    | just saw `1 0 1`      |  11   |

Four states fit in two bits, so the state lives in two D flip-flops, **Q1** and **Q0**. FOUND is on
exactly in S3.

## Step 2: the transitions

For each state and each input, where do we go next? Think about what the last few bits now are:

```
          BIT = 0          BIT = 1
S0 (00)   S0  "…0"         S1  "1"
S1 (01)   S2  "1 0"        S1  "1"      a second 1 is still the start of a new match
S2 (10)   S0  "1 0 0"      S3  "1 0 1"  found it
S3 (11)   S2  "1 0"        S1  "1"      the last 1 can start the next match
```

The last row is the overlapping part. After `1 0 1`, a `0` gives `…1 0`, which is already two
thirds of the next match, so we go to S2, not back to S0.

## Step 3: the next-state equations

Write the table with the bits spelled out, and read off each flip-flop's D input:

| Q1 Q0 | BIT | next Q1 | next Q0 |
|:-----:|:---:|:-------:|:-------:|
|  00   |  0  |    0    |    0    |
|  00   |  1  |    0    |    1    |
|  01   |  0  |    1    |    0    |
|  01   |  1  |    0    |    1    |
|  10   |  0  |    0    |    0    |
|  10   |  1  |    1    |    1    |
|  11   |  0  |    1    |    0    |
|  11   |  1  |    0    |    1    |

**next Q0** is the easy one: it equals BIT in every row. So `D0 = BIT`, a plain wire.

**next Q1** is 1 in three rows. Using sum of products:

```
row 01,0:  Q0 AND (NOT BIT)                  (Q1 does not matter here …
row 11,0:  Q0 AND (NOT BIT)                   … so these two rows merge)
row 10,1:  Q1 AND (NOT Q0) AND BIT

D1 = (NOT BIT AND Q0)  OR  (BIT AND Q1 AND NOT Q0)
```

And the output: `FOUND = Q1 AND Q0`.

## Step 4: the circuit

That is exactly what is on the sheet:

- **BIT** goes straight to flip-flop Q0's D input.
- A NOT gate makes NOT BIT.
- The 3-input AND gate, labelled *saw 10, now 1*, is `BIT AND Q1 AND NOT Q0`.
- The 2-input AND gate, labelled *saw 1, now 0*, is `NOT BIT AND Q0`.
- An OR combines them into flip-flop Q1's D input.
- The AND gate on the right is `Q1 AND Q0`, driving FOUND and its LED.
- **STEP** clocks both flip-flops, so they move to the next state together.

The state comes back round through **tunnels**: `Q0`, `Q1`, and `NQ0` (the flip-flop's own NOT Q
output, which saves an inverter). Every tunnel with the same name is the same wire.

## Where you meet this

- **Serial receivers.** A UART or USB chip is a state machine that watches incoming bits for a start
  pattern, then counts bits into a byte.
- **Text search.** Searching for a word in a file uses the same idea in software: a state for "how
  much of the word I have matched so far" (look up the KMP algorithm).
- **Combination locks and keypads.** Enter the right digits in the right order and the state reaches
  "open"; a wrong digit sends it back towards the start.
- **Network and protocol parsers**, vending machines and lift controllers are all state machines
  designed exactly this way.

## Things to try

- Change the pattern to `1 1 0`. Work through steps 1 to 3 on paper first: the states are "nothing",
  "1", "1 1" and "1 1 0". Then change the gates to match.
- Make it non-overlapping: after a match, go back to S0 whatever the next bit is. Which rows of the
  table change, and what does that do to D1 and D0?
- Add a **Counter** clocked by FOUND to count how many times the pattern has appeared.
- Replace STEP with a **Clock** and BIT with the output of the [Shift register](../shift-register),
  so it watches a pattern going round.

## Next

[Accumulator](../accumulator): a register and an adder in a loop, the core of the earliest
computers.
