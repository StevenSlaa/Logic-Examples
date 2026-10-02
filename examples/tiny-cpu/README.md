---
example: tiny-cpu
author: Steven Slaa
---

# A tiny CPU from gates

Every computer, from a washing machine to a data centre, does the same thing over and over: fetch
an instruction, do what it says, move on to the next one. This example is a complete computer that
does exactly that, built from nothing but AND, OR, XOR and NOT gates and eleven D flip-flops.
There are no buses, no tunnels and no ready-made parts: every one of the 74 gates is on the sheet,
and every wire between them is drawn. It is big, but each block is a circuit you have already met.

## What you will learn

- What a program counter, an instruction and an opcode are
- How a ROM stores a program, built from a decoder and OR gates
- How one clock pulse runs one instruction
- How subtraction falls out of addition when numbers wrap around

## Before you start

This one uses almost everything in the course. Most of all: the [Full adder](../full-adder) and
[A 4-bit adder, wire by wire](../four-bit-adder-wired) for the adder, the
[Decoder](../decoder-leds) for the ROM, the [Multiplexer](../mux-from-gates) for choosing the next
value of each register, and the [D flip-flop](../d-flip-flop) for the registers themselves.

The sheet is large, so it opens zoomed out. Zoom in on one block at a time.

## Try it

Everything starts at 0. Press **STEP** to run one instruction, and keep pressing.

1. **Step 1** runs `LDI 9`: the **ACC** LEDs show `1001`, which is 9.
2. **Step 2** runs `OUT`: the **OUT** LEDs copy ACC and also show 9.
3. **Step 3** runs `ADD 15`: ACC becomes 8. See *Subtracting by adding* below.
4. **Step 4** runs `JMP 1`: the **PC** LEDs jump back to 1 instead of going on to 4.
5. Keep pressing. OUT counts down 9, 8, 7 … 0, then wraps round to 15 and carries on.

At every step the amber LEDs show the instruction being run: **OP1 OP0** is the opcode,
**D3 to D0** its number.

## What happens over time

Each press of STEP is one clock edge. All eleven flip-flops take their new value at that same
instant, so the whole machine moves exactly one instruction forward:

| Step | PC before | Instruction | ACC after | OUT after | PC after |
|:----:|:---------:|-------------|:---------:|:---------:|:--------:|
|  1   |     0     | `LDI 9`     |     9     |     0     |    1     |
|  2   |     1     | `OUT`       |     9     |     9     |    2     |
|  3   |     2     | `ADD 15`    |     8     |     9     |    3     |
|  4   |     3     | `JMP 1`     |     8     |     9     |    1     |
|  5   |     1     | `OUT`       |     8     |     8     |    2     |
|  6   |     2     | `ADD 15`    |     7     |     8     |    3     |

## The instructions

Each instruction is 6 bits: a 2-bit **opcode** that says what to do, and a 4-bit number **D**.

| Opcode | Name    | What it does                         |
|:------:|---------|--------------------------------------|
|  `00`  | `LDI d` | Load: ACC = d                        |
|  `01`  | `ADD d` | Add: ACC = ACC + d                   |
|  `10`  | `OUT`   | Show: OUT = ACC (D is ignored)       |
|  `11`  | `JMP d` | Jump: the next instruction is d      |

The program in the ROM:

| Address | Instruction | Bits (OP1 OP0 D3 D2 D1 D0) |
|:-------:|-------------|:--------------------------:|
|    0    | `LDI 9`     |        `00 1001`           |
|    1    | `OUT`       |        `10 0000`           |
|    2    | `ADD 15`    |        `01 1111`           |
|    3    | `JMP 1`     |        `11 0001`           |
|  4 – 7  | empty       |        `00 0000`           |

## How it works

The sheet reads left to right in six blocks, each with a heading.

**1. Program counter.** Three flip-flops, `PC0` to `PC2`, hold the address of the instruction
being run (0 to 7). Underneath, a small adder works out PC + 1: bit 0 is just NOT PC0, which the
flip-flop's NOT Q output gives for free, and bits 1 and 2 are a half adder chain. On the left, a
multiplexer made of two ANDs and an OR per bit chooses the next address: PC + 1 normally, or D
when the instruction is `JMP`.

**2. Program ROM.** A ROM (read-only memory) turns an address into a stored value. The eight
3-input ANDs are a decoder: exactly one of them, *word 0* to *word 7*, is 1 for each address.
Each instruction bit is then the OR of the words that have a 1 in that bit. Look at the ROM table
above: OP1 is 1 in words 1 and 3, so the OP1 gate ORs word 1 and word 3. D1 and D2 are 1 only in
word 2, so they need no gate at all; they are wired straight to word 2. Changing the program means
changing these wires, which is what *read-only* means.

**3. Opcode decoder.** Two NOT gates and four ANDs turn the two opcode bits into four lines,
`LDI`, `ADD`, `OUT` and `JMP`, exactly one of which is 1. This is the decoder again, this time on
the instruction.

**4. Adder.** A 4-bit ripple-carry adder, the same one as in
[A 4-bit adder, wire by wire](../four-bit-adder-wired), works out ACC + D all the time. Only
`ADD` uses the answer. The carry out of the top bit is dropped.

**5. Accumulator.** Four flip-flops hold ACC, the CPU's working number. In front of each, three
ANDs and an OR choose its next value: D for `LDI`, the adder's sum for `ADD`, and its own value,
kept, for `OUT` and `JMP`. Those last two are exactly the instructions whose OP1 is 1, so OP1 is
used directly as *keep*.

**6. Output register.** Four more flip-flops hold what the program wants to show. They copy ACC on
`OUT` and keep their value otherwise.

**The clock.** STEP is wired to the clock input of all eleven flip-flops. Between presses, the
gates settle: the ROM looks up the instruction, the decoders and adder work out every next value.
On the press, every flip-flop takes its next value at once. That split, *work out, then commit*,
is how every processor runs.

## Subtracting by adding

There is no subtract instruction, but `ADD 15` subtracts 1. With 4 bits, numbers wrap around at
16, like a clock face with 16 hours: 8 + 15 = 23, and 23 − 16 = 7. The extra 16 is the carry out
of the top bit, which the adder drops. Adding 16 − *n* is the same as subtracting *n*; this is the
idea behind **two's complement**, the way real computers store negative numbers.

## Where you meet this

- **Every processor** has a program counter, an instruction decoder, registers and an ALU, wired
  up just like this. Real ones have more of each and many more instructions.
- **Early computers** such as the Manchester Baby (1948) were about this simple: a handful of
  instructions, one accumulator, and a program you had to set up by hand.
- **Firmware ROMs** in early games consoles and calculators were built on the same principle:
  a decoder picks a word, and the wiring says which bits are 1.

## Things to try

- **Change a number.** Make the program count down from 5 instead: word 0 should be `LDI 5`,
  `00 0101`. D3 has to stop being 1 in word 0 (disconnect word 0 from the D3 OR), and D2 has to
  become 1 (add an OR gate for D2, fed from word 0 and word 2).
- **Count up.** Change `ADD 15` to `ADD 1`. Which ROM wires have to go?
- **Write your own program** in words 4 to 7, and change word 3 to `JMP 4` to run it. Words 4 to 7
  are already decoded; their outputs are waiting on the right of each AND gate.
- **Run it on its own:** replace STEP with a **Clock** and watch the countdown run by itself.

## Next

This is the last example in the course. From here, the next steps are the ones real CPUs took:
a RAM so that programs can store numbers, a conditional jump such as *jump if zero* so that
programs can make decisions, and a wider ALU.
