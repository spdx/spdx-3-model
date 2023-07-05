# RDF Serialization

SPDX data can be serialized in RDF. This can be saved in a variety of formats, like XML, JSON-LD, Turtle, etc.

1. The namespace for SPDX v3 is `http://spdx.org/rdf/v3`

1. IRIs for a class are of the form: `http://spdx.org/rdf/v3/{Namespacename}/{Classname}`

1. IRIs for a property are of the form: `http://spdx.org/rdf/v3/{Namespacename}/{Propertyname}`

1. IRIs for an enumerated value are of the form: `http://spdx.org/rdf/v3/{Namespacename}/{Classname}/{Valuename}`


## JSON-LD
JSON-LD is a JSON-based format to encode RDF graphs. Its documentation can be found [here](https://www.w3.org/TR/json-ld11/).

The SPDX organization provides a context file that is to be used universally for all SPDX JSON-LD files of a given SPDX version.
The context is available under https://spdx.github.io/spdx-3-model/rdf/context.json (TODO: update the URL as soon as the context is publicly available)
and should be included in serialized files on top-level via
```json
"@context": "https://spdx.github.io/spdx-3-model/rdf/context.json"
```
Take special note that this context defines aliases for better compatibility with the SPDX model.
In particular, these are "spdxId" for "@id" and "type" for "@type".
Further custom namespace mapping can be included in the context in a separate object, see for example [here](json_ld/examples/spdx_document4.json).

The RDF graph of an instance of the SPDX model shall contain all Element nodes (i.e. objects that are subclasses of Element) as a list on top-level under the "@graph" key.
This means that all references to Element nodes have to use the URI of the referenced Element.
Inlining/Embedding of Element nodes into other nodes is not allowed.
On the other hand, non-Element nodes (like those of type "ExternalReference" or similar complex data classes) have to be inlined (TODO: we may want to make an exception for CreationInfo, depending on the outcome of the surrounding discussion).

An SPDX serialization in JSON-LD is considered valid if it validates against the OWL ontology which also includes SHACL shape restrictions.
The ontology is automatically generated from the [specification markdown files](https://github.com/spdx/spdx-3-model/tree/main/model) and can be found [here](https://github.com/spdx/spdx-3-model/blob/gh-pages/model.ttl).
The code that generates the ontology is located [here](https://github.com/spdx/spec-parser).  
