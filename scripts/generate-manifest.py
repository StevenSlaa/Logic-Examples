#!/usr/bin/env python3
"""Validate the examples and generate the Pulsar Logic Lab catalog (manifest.json)."""
from pathlib import Path
import hashlib, json, os

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"
VERSION = os.environ.get("CATALOG_VERSION", "1.0.0")
REPOSITORY = "https://github.com/StevenSlaa/Logic-Examples"
BASE = "https://raw.githubusercontent.com/StevenSlaa/Logic-Examples/refs/heads/main"
# The Logic Lab reads exactly this project format; anything else would fail to open.
PROJECT_SCHEMA_VERSION = 2

# Examples are listed in this order, in the manifest and so in the Logic Lab's library, where
# each group is a heading with this line under it. A group that is not on this list still works:
# it goes at the end, in alphabetical order, without a description.
GROUPS = (
    ("Basics", "Four short circuits, in order. Start here if you have never met a logic gate."),
    ("Arithmetic", "Adding numbers with gates, one binary column at a time."),
    ("Choosing and routing", "Circuits that pick one signal out of several, or point at one output."),
    ("Memory and time", "Circuits that remember, and circuits that move on with a clock."),
    ("Projects", "Bigger circuits that combine everything before them. Each is a small machine: take it one part at a time."),
)
GROUP_ORDER = [name for name, _ in GROUPS]
GROUP_DESCRIPTIONS = dict(GROUPS)


def fail(folder: Path, message: str):
    raise ValueError(f"examples/{folder.name}: {message}")


def entry(path: Path, folder: Path, mime: str):
    data = path.read_bytes()
    relative = path.relative_to(ROOT).as_posix().replace(" ", "%20")
    return {"path": path.relative_to(folder).as_posix(), "url": f"{BASE}/{relative}",
            "sha256": hashlib.sha256(data).hexdigest(), "mime": mime}


def write_front_matter(readme: Path, fields: dict):
    """Puts the example id and author at the top of a README, as YAML front matter.

    Written from example.json rather than by hand, so the two always agree. GitHub renders it
    as a small table; the Logic Lab hides it and shows the author on the card instead.
    """
    text = readme.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        _, _, text = text[4:].partition("---\n")
        text = text.lstrip("\n")
    lines = "\n".join(f"{key}: {value}" for key, value in fields.items() if value)
    readme.write_text(f"---\n{lines}\n---\n\n{text}", encoding="utf-8", newline="\n")


def check_circuit(folder: Path, path: Path):
    """The same checks the Logic Lab makes when it opens a file, so a broken one fails here."""
    try:
        project = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        fail(folder, f"{path.name} is not valid JSON ({error})")
    if project.get("schemaVersion") != PROJECT_SCHEMA_VERSION:
        fail(folder, f"{path.name} must be a version {PROJECT_SCHEMA_VERSION} Logic Lab project")
    circuits = project.get("circuits") or []
    if not project.get("id") or not project.get("name") or not circuits:
        fail(folder, f"{path.name} is missing its id, name or circuits")
    ids = [circuit.get("id") for circuit in circuits]
    if len(set(ids)) != len(ids) or not all(ids):
        fail(folder, f"{path.name} has an empty or duplicated circuit id")
    if project.get("activeCircuitId") not in ids:
        fail(folder, f"{path.name} opens on a circuit that does not exist")
    for circuit in circuits:
        for component in circuit.get("components", []):
            if not component.get("id") or not component.get("type") or "position" not in component:
                fail(folder, f"{path.name}: a component in {circuit.get('name')} is incomplete")
        for wire in circuit.get("wires", []):
            a, b = wire.get("a", {}), wire.get("b", {})
            if a.get("x") != b.get("x") and a.get("y") != b.get("y"):
                fail(folder, f"{path.name}: wire {wire.get('id')} is diagonal")


examples, ids = [], set()
for folder in sorted(p for p in EXAMPLES.iterdir() if p.is_dir()):
    path = folder / "example.json"
    if not path.exists(): fail(folder, "missing example.json")
    if not (folder / "README.md").exists(): fail(folder, "missing README.md")
    metadata = json.loads(path.read_text(encoding="utf-8"))
    required = ("id", "title", "description", "entry")
    if any(not metadata.get(key) for key in required): fail(folder, f"example.json must contain {required}")
    if metadata["id"] != folder.name: fail(folder, "id must match the directory name")
    if metadata["id"] in ids: fail(folder, f"duplicate id {metadata['id']}")
    ids.add(metadata["id"])
    circuit = folder / metadata["entry"]
    if not circuit.is_file() or not circuit.name.endswith(".logic.json"):
        fail(folder, "entry must point to a .logic.json file")
    check_circuit(folder, circuit)
    order = metadata.get("order", 0)
    if not isinstance(order, int): fail(folder, "order must be a whole number")
    tags = metadata.get("tags", [])
    if not isinstance(tags, list) or not all(isinstance(tag, str) and tag for tag in tags):
        fail(folder, "tags must be a list of words")
    write_front_matter(folder / "README.md", {"example": metadata["id"], "author": metadata.get("author")})
    examples.append({"id": metadata["id"], "title": metadata["title"],
                     "description": metadata["description"], "author": metadata.get("author", ""),
                     "group": metadata.get("group", "Other"), "order": order, "tags": tags,
                     "source": f"{REPOSITORY}/tree/main/examples/{metadata['id']}",
                     "circuit": entry(circuit, folder, "application/json"),
                     "readme": entry(folder / "README.md", folder, "text/markdown")})

examples.sort(key=lambda example: (
    GROUP_ORDER.index(example["group"]) if example["group"] in GROUP_ORDER else len(GROUP_ORDER),
    example["group"],
    example["order"],
    example["id"],
))
# The order was only ever about sorting; the manifest is already sorted, so it does not travel.
for example in examples:
    del example["order"]

# The index in examples/README.md is generated, so it cannot drift from the metadata.
rows = []
for example in examples:
    if not rows or rows[-1][0] != example["group"]:
        rows.append((example["group"], []))
    summary = example["description"].split(". ")[0].rstrip(".")
    rows[-1][1].append(f"| [{example['title']}]({example['id']}) | {summary}. |")
index = EXAMPLES / "README.md"
head, _, rest = index.read_text(encoding="utf-8").partition("<!-- generated:start -->")
_, _, tail = rest.partition("<!-- generated:end -->")
sections = "\n\n".join(
    f"### {group}\n\n"
    + (f"{GROUP_DESCRIPTIONS[group]}\n\n" if group in GROUP_DESCRIPTIONS else "")
    + "| Example | What it shows |\n| --- | --- |\n"
    + "\n".join(lines)
    for group, lines in rows
)
index.write_text(f"{head}<!-- generated:start -->\n{sections}\n<!-- generated:end -->{tail}",
                 encoding="utf-8", newline="\n")

group_names = []
for example in examples:
    if example["group"] not in group_names:
        group_names.append(example["group"])
groups = [{"name": name, **({"description": GROUP_DESCRIPTIONS[name]} if name in GROUP_DESCRIPTIONS else {})}
          for name in group_names]

manifest = {"schema": "pulsar.logic.library/v1",
            "catalog": {"id": "logic-examples", "name": "Logic Lab Examples", "version": VERSION},
            "repository": REPOSITORY, "groups": groups, "examples": examples}
(ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                                    encoding="utf-8", newline="\n")
print(f"Generated {len(examples)} examples")
