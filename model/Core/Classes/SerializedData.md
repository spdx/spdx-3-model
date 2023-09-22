SPDX-License-Identifier: Community-Spec-1.0

# SerializedData

## Summary

Defines the structure of a serialized data instance (Payload) for non-RDF serialization formats.

## Description

SPDX Element values can be serialized into a sequence of bytes for transmission or storage,
using one of many data formats such as XML, JSON, text (in a human-friendly format
such as YAML or Tag-Value), Spreadsheet, or a machine-optimized production format such as
CBOR or Protobuf. Serialization must be lossless: regardless of data format, parsing
a serialized instance must result in the identical Element values that were used to
produce it.

The "element" property contains the serialized element values and is the only required
property.

NamespaceMap and CreationInfoMap support compaction of the serialized data; if they are
not present the element values are not compacted.

## Metadata

- name: SerializedData
- SubclassOf: none
- Instantiability: Concrete

## Properties

- namespaces
  - type: NamespaceMap
  - minCount: 0

- creationInfos
  - type: CreationInfoMap
  - minCount: 0

- element
  - type: Element
  - minCount: 1

