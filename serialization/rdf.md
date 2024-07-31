# RDF serialization

SPDX data can be serialized in RDF. This can be saved in a variety of formats, like XML, JSON-LD, Turtle, etc.

1. The namespace for SPDX v3 is `https://spdx.org/rdf/3.0.0/terms`

1. IRIs for a namespace/profile are of the form: `https://spdx.org/rdf/3.0.0/terms/{Namespacename}`

1. IRIs for a class are of the form: `https://spdx.org/rdf/3.0.0/terms/{Namespacename}/{Classname}`

1. IRIs for a property are of the form: `https://spdx.org/rdf/3.0.0/terms/{Namespacename}/{Propertyname}`

1. IRIs for a vocabulary (an enumerated value list) are of the form: `https://spdx.org/rdf/3.0.0/terms/{Namespacename}/{Vocabularyname}`

1. IRIs for an enumerated value are of the form: `https://spdx.org/rdf/3.0.0/terms/{Namespacename}/{Vocabularyname}/{Entryname}`

1. IRIs for an individual value list are of the form: `https://spdx.org/rdf/3.0.0/terms/{Namespacename}/{Individualname}`

Please note that entries appearing in the License List are not under this namespace!

## Resources

1. The ontology is available at: https://spdx.org/rdf/3.0.0/spdx-model.ttl

1. The JSON-LD context definition is available at: https://spdx.org/rdf/3.0.0/spdx-context.jsonld

1. The JSON schema is available at: https://spdx.org/schema/3.0.0/spdx-json-schema.json
