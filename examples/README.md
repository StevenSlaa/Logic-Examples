# Examples

Every example is a folder with a circuit you can open in the Pulsar Logic Lab and a README that
walks through it. They are grouped into short courses; within a group, the numbers are the order
to read them in.

New to logic? Start with **The basic gates** and work down. Each README ends by pointing at the
next one.

<!-- generated:start -->
### Basics

Four short circuits, in order. Start here if you have never met a logic gate.

| Example | What it shows |
| --- | --- |
| [1. The basic gates](basic-gates) | Seven gates side by side, all fed from the same two inputs. |
| [2. De Morgan's laws](de-morgan) | Two circuits built from different gates that always give the same answer. |
| [3. Everything from NAND](nand-only) | NOT, AND and OR built out of nothing but NAND gates, which is why a chip factory only really needs one gate. |
| [4. Majority vote: from truth table to circuit](majority-vote) | Three inputs, and the output agrees with the majority. |

### Arithmetic

Adding numbers with gates, one binary column at a time.

| Example | What it shows |
| --- | --- |
| [1. Half adder](half-adder) | Adds two single bits. |
| [2. Full adder](full-adder) | Adds two bits plus a carry from the column before. |
| [3. A 4-bit adder, wire by wire](four-bit-adder-wired) | Four full adders on one sheet, every bit its own pin and every carry a wire you can follow. |
| [4. Adding 4-bit numbers](four-bit-adder) | The Adder part on 4-bit buses, with a hex display and the carry out. |
| [5. Multiplying two numbers](two-bit-multiplier) | Multiplies two 2-bit numbers with AND gates and two half adders: long multiplication from school, done in binary. |

### Choosing and routing

Circuits that pick one signal out of several, or point at one output.

| Example | What it shows |
| --- | --- |
| [1. Multiplexer](mux-from-gates) | A select line chooses which of two inputs reaches the output, built from gates and then again with the Multiplexer part. |
| [2. Decoder: binary to one-hot](decoder-leds) | A 2-bit number lights exactly one of four LEDs. |

### Memory and time

Circuits that remember, and circuits that move on with a clock.

| Example | What it shows |
| --- | --- |
| [1. SR latch: a circuit that remembers](sr-latch) | Two NOR gates feeding each other hold a bit after the input goes away. |
| [2. D flip-flop: remembering on a clock edge](d-flip-flop) | Copies its input only at the instant the clock rises. |
| [3. Counter and hex display](counter-hex) | A clock drives a 4-bit counter, shown on a hex digit, with a clear button and a carry LED. |
| [4. Traffic light: a state machine](traffic-light) | A counter walks through four phases and a decoder with two OR gates turns each phase into lamps. |
| [5. Random numbers from a shift register](random-numbers) | Four flip-flops and one XNOR gate produce a jumbled sequence of 15 numbers: a linear-feedback shift register, the classic hardware random number source. |
| [6. Edge detector](edge-detector) | A flip-flop remembers what the button was one tick ago, so one gate can turn a long press into a single one-tick pulse. |
| [7. Running light](running-light) | A Johnson counter feeds its last bit back upside down, and eight AND gates turn its states into one light running down a column. |

### Projects

Bigger circuits that combine everything before them. Each is a small machine: take it one part at a time.

| Example | What it shows |
| --- | --- |
| [1. Ripple-carry adder from gates](ripple-carry-adder) | Four full adders, twenty gates, one 4-bit adder. |
| [2. A 4-bit ALU](alu) | Add, subtract, AND and OR on two 4-bit numbers, picked by an opcode, with zero, carry and borrow flags. |
| [3. Shift register: serial in, parallel out](shift-register) | Four D flip-flops in a chain move every bit one place along on each clock. |
| [4. Sequence detector: a finite-state machine](sequence-detector) | Watches a stream of bits and lights up when it has just seen 1, 0, 1. |
| [5. Accumulator: a register that adds](accumulator) | An 8-bit register feeding its own adder keeps a running total. |
| [6. Electronic dice](dice) | A fast counter stopped by a button picks a number from 1 to 6, and gate logic lights the right dots on a die face. |
| [7. A tiny CPU from gates](tiny-cpu) | A working 4-bit computer, 74 gates and 11 flip-flops, every wire drawn. |
<!-- generated:end -->

## Words used throughout

- **Bit**: a single 0 or 1. On a wire, 0 is low (off) and 1 is high (on).
- **Gate**: a part whose output depends only on its inputs right now, like AND or OR.
- **Truth table**: every combination of inputs, and the output each one gives.
- **Combinational**: a circuit with no memory. The same inputs always give the same outputs.
- **Sequential**: a circuit with memory. What it outputs also depends on what happened before.
- **Bus**: several wires carrying one number, drawn as a single thicker line.
- **Clock**: a signal that switches between 0 and 1 at a steady rate, to keep time.
