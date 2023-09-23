SPDX-License-Identifier: Community-Spec-1.0

# Payload

## Summary

A Payload is a sequence of bytes that can be parsed into a set of SPDX elements.

## Description

SPDX element values can be serialized into a byte sequence called a payload
for transmission or storage. Serialization must be lossless: parsing a payload
must yield the identical elements that were used to produce it.

There are many possible serialization formats, including the OWL ontology
formats RDF, JSON-LD, and Turtle, and general-purpose formats including XML, JSON,
human-friendly text such as YAML or Tag-Value, and machine-optimized
production formats such as CBOR or Protobuf.

A serialization specification for each supported format defines how element and
non-element values are serialized:
* the required element property contains serialized element values.
* the optional namespaceMap and creationInfoMap properties support compaction of the serialized
data for efficiency and improved readability; if they are not present the element values
are not compacted.

Non-element values are used only within a payload. They can be read directly from the
payload but are not present in logical element values before serialization or after parsing.

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

