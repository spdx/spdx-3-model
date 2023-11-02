# JSON-LD
JSON-LD is a JSON-based format to encode RDF graphs. Its documentation can be found [here](https://www.w3.org/TR/json-ld11/).

The JSON-LD is an RDF format and follows the serialization rules of the [rdf SPDX serialization specification](rdf.md).

## SpdxDocument

The following SpdxDocument properties are mapped to native JSON-LD mechanisms defined within the JSON-LD syntax specifications.
Any properties not listed below should be serialized as part of the SpdxDocument element itself within
the JSON-LD serialized data.
Deserialization of any JSON-LD serialized SPDX content MUST expand the inverse of these native mappings such that the logical SpdxDocument element directly contains its full set of properties.

### namespaceMap

The namespaceMap uses the [term to IRI mapping](https://www.w3.org/TR/json-ld11/#example-11-term-expansion-from-context-definition) in the [JSON-LD context](https://www.w3.org/TR/json-ld11/#the-context).

### element

The [graph objects](https://www.w3.org/TR/json-ld11/#graph-objects) `@graph` lists the elements for the SpdxDocument.

The RDF graph of an instance of the SPDX model shall contain all Element nodes (i.e. objects that are subclasses of Element) as a list on top-level under the "@graph" key.
This means that all references to Element nodes have to use the URI of the referenced Element.
Inlining/Embedding of Element nodes into other nodes is not allowed.
On the other hand, non-Element nodes (like those of type "ExternalReference" or similar complex data classes) have to be inlined (TODO: we may want to make an exception for CreationInfo, depending on the outcome of the surrounding discussion).

## Context File

The SPDX organization provides a global JSON-LD @context file that MUST be used universally for all SPDX JSON-LD files of a given SPDX version.
The context is available under https://spdx.github.io/spdx-3-model/rdf/context.json (TODO: update the URL as soon as the context is publicly available)
and should be included in serialized files on top-level via
```json
"@context": "https://spdx.github.io/spdx-3-model/rdf/context.json"
```
Take special note that this context defines aliases for better compatibility with the SPDX model.
In particular, these are "spdxId" for "@id" and "type" for "@type".
Further custom namespace mapping can be included in the context in a separate object, see for example [here](json_ld/examples/spdx_document4.json).

## Validation

An SPDX serialization in JSON-LD is considered valid if it validates against the OWL ontology which also includes SHACL shape restrictions.
The ontology is automatically generated from the [specification markdown files](https://github.com/spdx/spdx-3-model/tree/main/model) and can be found [here](https://github.com/spdx/spdx-3-model/blob/gh-pages/model.ttl).
The code that generates the ontology is located [here](https://github.com/spdx/spec-parser).  
