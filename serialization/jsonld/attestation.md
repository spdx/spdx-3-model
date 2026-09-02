# Attestation with SPDX 3 JSON Documents

SPDX JSON Documents can be used as an [in-toto][in-toto] attestation predicate
(version 1.2.0 or later) by using the predicate type
https://spdx.dev/Document/v3. The predicate data is the JSON content of the
SPDX document.

## Example

```jsonc
{
    // Standard attestation fields:
    "_type": "https://in-toto.io/Statement/v0.1",
    "subject": [{ ... }],

    // Predicate:
    "predicateType": "https://spdx.dev/Document/v3",
    "predicate": {
        "@context": "https://spdx.org/rdf/3.0/spdx-context.jsonld",
        "@graph": [
            ...
        ]
    }
}
```

[in-toto]: https://in-toto.io/
