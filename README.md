# Logic Lab Examples

Worked, documented example circuits for the **Pulsar Logic Lab**, the digital logic simulator in
Pulsar IoT. Each one opens straight from the Logic Lab's library (the book icon in the Parts
panel), with its README next to it as a tab you can read while you click around the circuit.

They are written as a course. Start at **Basics 1** if logic gates are new to you; each example
says what it expects you to know already and where to go next.

See [examples/README.md](examples/README.md) for the full list.

```
examples/<example-id>/    example.json, README.md, <example-id>.logic.json
scripts/                  generate-manifest.py
manifest.json             generated catalog, do not edit by hand
```

## How the Logic Lab uses this repository

The Logic Lab reads `manifest.json` from the `main` branch. For every example it lists the title,
description and author, and it downloads the circuit and README from the URLs in the manifest.
Each download is checked against the SHA-256 hash in the manifest, so a file that changed without
the manifest being regenerated is refused rather than opened half-updated.

Opening an example gives you your own copy: you can change it freely, and it is saved in your
browser like any other project. Nothing is ever written back here.

## Add an example

1. Build the circuit in the Logic Lab. Keep it small enough to understand on one screen, and put a
   **Note** part on the sheet with a line or two about what to click first.
2. Open **Projects → Export current** and save the file as `<example-id>.logic.json`.
3. Create `examples/<example-id>/` (lowercase, hyphenated) and put the file in it with an
   `example.json` and a `README.md`.
4. Run `python3 scripts/generate-manifest.py` and commit everything it changed together with your
   example.

```json
{
  "id": "half-adder",
  "title": "1. Half adder",
  "description": "Adds two single bits. XOR makes the sum digit and AND makes the carry.",
  "author": "Your Name",
  "group": "Arithmetic",
  "order": 1,
  "tags": ["combinational", "arithmetic"],
  "entry": "half-adder.logic.json"
}
```

`group` is the heading the example is listed under; `order` only matters for a group meant to be
read in sequence. The rules for READMEs, and what a review looks for, are in
[CONTRIBUTING.md](CONTRIBUTING.md).

## Pointing the Logic Lab at a fork

The app reads the manifest URL from `SECRET_LOGIC_LIBRARY_MANIFEST_URL`. Set it to the raw URL of
`manifest.json` in your fork, and change `BASE` and `REPOSITORY` at the top of
`scripts/generate-manifest.py` to match, so the file URLs in the manifest point at your copy too.
