# RDF Serialization

SPDX data can be serialized in RDF. This can be saved in a variety of formats, like XML, JSON-LD, Turtle, etc.

1. The namespace for SPDX v3 is `https://rdf.spdx.org/v3`

1. IRIs for a namespace/profile are of the form: `https://rdf.spdx.org/v3/{Namespacename}`

1. IRIs for a class are of the form: `https://rdf.spdx.org/v3/{Namespacename}/{Classname}`

1. IRIs for a property are of the form: `https://rdf.spdx.org/v3/{Namespacename}/{Propertyname}`

1. IRIs for a vocabulary (an enumerated value list) are of the form: `https://rdf.spdx.org/v3/{Namespacename}/{Vocabularyname}`

1. IRIs for an enumerated value are of the form: `https://rdf.spdx.org/v3/{Namespacename}/{Vocabularyname}/{Entryname}`

1. IRIs for an individual value list are of the form: `https://rdf.spdx.org/v3/{Namespacename}/{Individualname}`

Please note that entries appearing in the License List are not under this namespace!

