SPDX-License-Identifier: Community-Spec-1.0

# PhysicalDocument

## Summary

Describes an instance of an SPDX document serialized using a specific format.

## Description

PhysicalDocument refers to a document that can be parsed into a set of SPDX element values.
It is the v3 physical interpretation of SPDX v2 Document, which has both physical and logical meanings.

The element property lists the elements serialized in a document; PhysicalDocument is the
"defining document" of those elements.
The downloadLocation and verifiedUsing properties allow the document containing an element
to be located and/or verified.

## Metadata

- name: PhysicalDocument
- SubclassOf: Artifact
- Instantiability: Concrete

## Properties

- element
  - type: Element
  - minCount: 1

- downloadLocation
  - type: anyURI
  - minCount: 0
  - maxCount: 1

- verifiedUsing
  - type: IntegrityMethod
  - minCount: 0


