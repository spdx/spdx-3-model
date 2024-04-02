# RDF/SHACL model

Quick notes on how the model description is translated into SHACL

# Class example

```ttl
<https://rdf.spdx.org/v3/Software/Snippet> a rdfs:Class,
                                             owl:Class,
                                             sh:NodeShape ;
    rdfs:comment "Describes a certain part of a file."@en ;
    rdfs:subClassOf <https://rdf.spdx.org/v3/Software/SoftwareArtifact> ;
    sh:property [
            sh:maxCount 1 ;
            sh:minCount 1 ;
            sh:nodeKind sh:IRI ;
            sh:class  <https://rdf.spdx.org/v3/Software/File> ;
            sh:path <https://rdf.spdx.org/v3/Software/snippetFromFile> ] .

```

for data properties, instead of `sh:class`, we'll have (a) `sh:datatype` and the type, and (b) `sh:nodeKind: sh:Literal`

for our datatypes, also add `sh:pattern`

we can omit `rdfs:Class`, since we have `owl:Class`

# Property examples

we can omit `rdf:Property`, since we have the `owl:` property type

future: add `rdfs:label "Start time"` (instead of `startTime`)

## Data property

```ttl
<https://rdf.spdx.org/v3/Core/name> a rdf:Property,
        owl:DatatypeProperty ;
    rdfs:comment "Identifies the name as designated by the creator."@en ;
    rdfs:range xsd:string .
```

## Object property

```ttl
<https://rdf.spdx.org/v3/Software/snippetFromFile> a rdf:Property,
        owl:ObjectProperty ;
    rdfs:comment "Defines the file that the snippet information applies to."@en ;
    rdfs:range <https://rdf.spdx.org/v3/Software/File> .
```

# Vocabulary example

```ttl
<https://rdf.spdx.org/v3/Core/HashAlgorithm> a rdfs:Class,
        owl:Class ;
    rdfs:comment "A mathematical algorithm that maps data to a bit string."@en .
```

## entry

```ttl
<https://rdf.spdx.org/v3/Core/HashAlgorithm/blake2b256> a owl:NamedIndividual,
        <https://rdf.spdx.org/v3/Core/HashAlgorithm> ;
    rdfs:label "blake2b256" ;
    rdfs:comment "blake2b algorithm with a digest size of 256 https://datatracker.ietf.org/doc/html/rfc7693#section-4"@en .
```

# Datatype example

```ttl
<https://rdf.spdx.org/v3/Core/MediaType> a rdfs:datatype ; 

```

