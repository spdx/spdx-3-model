SPDX-License-Identifier: Community-Spec-1.0

# Payload

## Summary

A payload is a byte sequence that can be parsed into a set of SPDX elements.

## Description

SPDX element values can be serialized into a byte sequence called a payload
for transmission or storage. A payload includes header properties (non-element values)
and element content. Non-element values are valid only within a payload; they can be
serialized into and parsed from the payload data but are not present in logical elements
before serialization or after parsing. Serialization must be lossless: parsing a payload
must yield the identical information that was used to produce it.

There are many possible serialization formats:
* OWL ontology formats - RDF, JSON-LD, Turtle
* general-purpose - XML, JSON
* human-oriented - YAML, Tag-Value text, Spreadsheet
* machine-optimized production oriented - CBOR, Protobuf, Avro, Dataframes

A serialization specification for each supported format defines how header properties and
element values are serialized:
* the required element property contains serialized element values.
* the optional namespaceMap and creationInfoMap properties support compaction of the serialized
data for efficiency and improved readability; if they are not present the serialized element values
are not compacted.

Use case analysis suggests additional header properties that have not yet been approved:
* rootElement [0..*] - hints for where to start processing after parsing element values
* dataLicense [0..1] - moved from per-element CreationInfo to a per-document property

## Metadata

- name: Payload
- SubclassOf: none
- Instantiability: Concrete

## Properties

- namespaceMap
  - type: NamespaceMap
  - minCount: 0

- creationInfoMap
  - type: CreationInfoMap
  - minCount: 0

- element
  - type: Element
  - minCount: 1

