# Glossary of Terms

## Domain

A specific sphere of activity or knowledge. For example, cyber security, software, bills of material, licensing, software security, etc

## Ontology

An explicit specification of concepts, terms, categories, relationships, etc. for a particular scoped domain forming a language or basis for communication and analysis of information within the scoped domain. SPDX 3.0 is an ontology targeted to support the scoped domain of bills of material.

## Class

A represention of a scope/set of individual instances of a particular “concept” (e.g., File, Person, ExternalReference, etc.). Each individual instance of a class has an IRI ID and is asserted as a member of a particular class via a type statement.

## Domain Class

A class representing a concept of primary focus within a given domain. In a graph or serialized set of instance content this would be the granularity of what would be a node in the graph or a top-level object in the serialization set. This is typically similar to the scoping seen in labeled property graphs. In SPDX 3.0, all domain classes are subclasses of Element.

## Non-domain Class

A class representing a concept of secondary or tertiary focus within a given domain that is a characterization of some aspect of a domain class. When structuring the graph for a domain use case it is desirable and more practical for the domain graph nodes to only consist of domain class instances and object properties. Any non-domain classes and datatype properties would be considered internal adornments on the domain objects. In SPDX 3.0, all defined classes that are not subclasses of Element are non-domain classes.

## Property

A representation of a relationship between a class (definition or instance) and some descriptive characterization of the class.

## Datatype property

A representation of a relationship between a class (definition or instance) and some literal (string, integer, boolean, etc.) descriptive characterization of the class.

## Object property

A representation of a relationship between a class (definition or instance) and some conceptual (class-based) descriptive characterization of the class. In other words, it is a relationship between one class and another class.

## Domain

The class at the root of a property relationship. In other words, the class being characterized.

## Range

The class or literal datatype of the value of a property relationship.

## Namespace

An explicit scoping within which concept classes and properties for a given domain are defined and referenced. Each namespace typically defines its own IRI prefix utilized in the IRI IDs of all concept classes and properties defined within it. In SPDX 3.0, the "core" namespace is the scoping within which all foundational BOM concept classes and properties are defined and managed.

## Core

The namespace which contains definitions and constraints for all concpet classes and properties which are common to all other domains within the targeted scope of SPDX.

## Constraint

An explicit conformance requirement specifying details of an SPDX-valid relationship between a property and a concept class including such details as the valid type of the property on that class, the cardinality (e.g., `0..1`, `1`, `1..*`, etc.) of the property on that class, the value of the property on that class, etc. In SPDX 3.0 these constraints are expressed using the W3C SHACL language. One example could be the requirement of a specific hash algorithm to be present.

## Shape

A formally defined set of constraints that explicitly specify the valid "shape" of particular data to support validation against SPDX conformance requirements. A Property Shape defines the set of constraints for a given property when applied to a particular concept class. A Node Shape defines the set of property shapes (and thus constraints) relevant for validation of instance data realization of a given concept class. In SPDX 3.0 these shapes are expressed using the W3C SHACL language.

## Validation

The action of checking or proving that instance data content conforms to the explicit semantics (meaning) and syntax (structure of classes and properties) of the SPDX language standard. In SPDX 3.0, automated validation of RDF-based serialized content can be accomplished with various freely available SHACL validation engines such as pyshacl. Custom validation engines could also implement automated validation of non-RDF-based serializations against the defined SHACL shapes within SPDX 3.0.

## Profile

An explicit scope of usage for SPDX targeting support for particular use cases and scenarios (e.g., core, software, licensing, build, etc.). A profile identifies which particular SPDX namespaces, concept classes and properties it leverages along with any custom specializations of shape constraints unique to its use. NOTE: A profile is NOT the same thing as a namespace. A namespace is a formal part of the language ontology and defines specific concept classes, properties and shape constraints unique for a particular domain scope. A profile represents usage and conformance documentation for the language ontology and references concept classes, properties and shape constraints defined within namespaces. For a given profile, there may exist a namespace closely aligned to the same usage scope but they are not the same thing and the profile will often leverage/reference concept classes, properties and shape constraints from more namespaces (e.g., core) than just the aligned namespace.

## Serialization

The process of translating an abstract logical data structure into a format that can be stored or transmitted and reconstructed later. This series of resulting bits, processed according to its particular serialization format rules, can then be used to create a semantically identical clone of the original content through the process of deserialization.

## Canonicalization

A process that takes data in any valid form (e.g., various serializations of SPDX like json-ld, yaml, xml, turtle, etc.) and transforms it into a single consistent normalized deterministic and reproducible form. Such a canonical form normalizes things like ordering, formatting, choices, etc.

