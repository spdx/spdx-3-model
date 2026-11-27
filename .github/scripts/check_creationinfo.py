# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Check individuals' CreationInfo in a generated ontology against releases.

Released CreationInfo shall not change. For each release tag of
spdx/spdx-3-model, compare creationInfo_* records with
https://spdx.org/rdf/{version}/spdx-model.ttl.

usage: python check_creationinfo.py GENERATED_TTL
"""

import re
import subprocess
import sys
from collections import defaultdict

from rdflib import Graph, URIRef

REPO = "https://github.com/spdx/spdx-3-model"
ONTOLOGY = "https://spdx.org/rdf/{}/spdx-model.ttl"
CREATION_INFO = "https://spdx.org/rdf/{}/creationInfo_"
KEYS = ("specVersion", "created", "createdBy")


def released():
    # release tags only, e.g. 3.0.1 (not 3.1-rc1)
    out = subprocess.run(["git", "ls-remote", "--tags", REPO], capture_output=True, text=True, check=True).stdout
    return set(re.findall(r"refs/tags/([0-9.]+)$", out, re.MULTILINE))


def records(g, version):
    # {name: [specVersion, created, createdBy]}; values joined by |, term IRIs as /Core/X
    prefix = CREATION_INFO.format(version)
    out = defaultdict(lambda: defaultdict(set))
    for s, p, o in g:
        key = str(p).rsplit("/", 1)[-1]
        if str(s).startswith(prefix) and key in KEYS:
            value = re.sub(r"^.*/terms(/[^/]+/[^/]+)$", r"\1", str(o)) if isinstance(o, URIRef) else str(o)
            out[str(s)[len(prefix):]][key].add(value)
    return {name: ["|".join(sorted(r[k])) for k in KEYS] for name, r in out.items()}


def main(generated):
    gen = Graph().parse(generated)
    errors = []
    for version in sorted(released()):
        rel, ours = records(Graph().parse(ONTOLOGY.format(version), format="turtle"), version), records(gen, version)
        for name in sorted(rel.keys() | ours.keys()):
            if rel.get(name) != ours.get(name):
                errors.append(f"{name}: generated {ours.get(name)}, released in {version} {rel.get(name)}")
        print(f"checked {version}: {len(rel)} released, {len(ours)} generated")
    for e in errors:
        print(f"error: {e} ({', '.join(KEYS)})")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
