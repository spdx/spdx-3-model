# Signing SPDX 3 JSON Documents

SPDX JSON Documents may be signed using [ITU-T X.590 JSON Signature Schema (JSS)][JSS].
The signature must be placed in a `signatures` property at the top level of the
document. For the structure of the signature, see the [JSS][JSS] specification.

SPDX does not currently allow sub-objects of the document to be signed (e.g.
individual objects in the `@graph` list). Only the complete document can be
signed.

## Example

```jsonc
{
    "@context": "https://spdx.org/rdf/3.0/spdx-context.jsonld",
    "@graph": [
        ...
    ],
    "signatures": [
        {
            "hash_algorithm": "sha-256",
            "algorithm": "Ed25519",
            "public_key": "MCowBQYDK2VwAyEAubMonBfU9pvIbj5RCiWQLD45Jvu6mKr+kQXjvjW8ZkU=",
            "value": "QxWYpg2iH5ebWQJDxzzHLYC4frs8SRmdE5hjAFyl8OWqFhXZYue5rzce5BUKEK3LjEeqrRvXultNquqVCnJ1Ag"
        }
    ]
}
```

[JSS]: https://www.itu.int/epublications/en/publication/itu-t-x-590-2023-10-json-signature-scheme-jss/en
