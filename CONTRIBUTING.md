# Contributing

Thanks for adding to the examples. They are read by people who are learning, often on their own,
so a review cares much more about the README than about the circuit.

## The circuit

- **One idea per example.** If you find yourself explaining two things, it is two examples.
- **Fits on one screen** at the zoom the Logic Lab opens at. Use tunnels rather than a long wire
  that runs off the edge.
- **Labels on everything the reader touches.** Input pins, output pins and LEDs get names that
  match the README (`A`, `B`, `CIN`, `SUM`), so "click CIN" means something.
- **A Note part on the sheet** that says what to do first. The README is not always open.
- **Opens in a sensible state.** It should not start oscillating or show `x` on an output unless
  that is the lesson. Set the input pins before you export.
- **No crossings that look like joins.** Two wires only connect where one ends on the other; if a
  crossing could be misread, move one of them.

## The README

Every README follows the same outline, so a reader always knows where to look:

1. A title and one paragraph on *why* this circuit matters, before *what* it is.
2. **What you will learn**: three or four bullets.
3. **Before you start**: which examples it builds on, if any.
4. **Try it**: what to click in the Logic Lab, and what should happen.
5. **The truth table** (for circuits without memory) or **what happens over time** (for circuits
   with it).
6. **How it works**: the circuit explained part by part.
7. **Where you meet this**: the same idea in real hardware.
8. **Things to try**: two to four small changes to make, with what they should show.
9. **Next**: the example to go to after this one.

Write in plain sentences. Explain a term the first time you use it. Assume the reader is clever
but has never seen this before.

Relative links to other examples (`[half adder](../half-adder)`) work on GitHub; keep them, but
make sure the sentence still makes sense to someone reading it in the Logic Lab, where they are
not clickable.

## Before you open a pull request

Run `python3 scripts/generate-manifest.py` and commit what it changed. CI runs it again and fails
if anything differs, which almost always means the manifest was not regenerated after an edit.
