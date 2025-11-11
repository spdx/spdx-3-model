# RDF serialization

## Namespace and IRIs

SPDX data can be serialized in RDF.
This can be saved in a variety of formats, like XML, JSON-LD, Turtle, etc.

IRIs for SPDX 3 are versioned based on the major and minor version numbers of
the SPDX specification. The patch (third-level) version number is omitted
because there are no changes to the data model between patch versions.

1. The namespace for SPDX vX.Y.Z is
  `https://spdx.org/rdf/X.Y/terms`

1. IRIs for a namespace/profile are of the form:
  `https://spdx.org/rdf/X.Y/terms/{Namespacename}`

1. IRIs for a class are of the form:
  `https://spdx.org/rdf/X.Y/terms/{Namespacename}/{Classname}`

1. IRIs for a property are of the form:
  `https://spdx.org/rdf/X.Y/terms/{Namespacename}/{Propertyname}`

1. IRIs for a vocabulary (an enumerated value list) are of the form:
  `https://spdx.org/rdf/X.Y/terms/{Namespacename}/{Vocabularyname}`

1. IRIs for an enumerated value are of the form:
  `https://spdx.org/rdf/X.Y/terms/{Namespacename}/{Vocabularyname}/{Entryname}`

1. IRIs for an individual value list are of the form:
  `https://spdx.org/rdf/X.Y/terms/{Namespacename}/{Individualname}`

Please note that entries appearing in the
[SPDX License List](https://spdx.org/licenses/) are not under this namespace!

## Resources

1. The ontology is available at:
  `https://spdx.org/rdf/X.Y/spdx-model.ttl`

1. The JSON-LD context definition is available at:
  `https://spdx.org/rdf/X.Y/spdx-context.jsonld`

1. The JSON schema is available at:
  `https://spdx.org/schema/X.Y/spdx-json-schema.json`
