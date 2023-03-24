SPDX-License-Identifier: Community-Spec-1.0

# ExternalMap

## Summary

A map of Element identifiers that are used within a Document but defined external to that Document.

## Description

An External Map is a map of Element identifiers that are used within a Document
but defined external to that Document.
The external map provides details about the externally-defined Element
such as its provenance, where to retrieve it, and how to verify its integrity.


## Metadata

- name: ExternalMap
- SubclassOf: none
- Instantiability: Concrete


## Properties

- externalId
  - type: xsd:anyURI
  - minCount: 1
  - maxCount: 1
- verifiedUsing
  - type: IntegrityMethod
- locationHint
  - type: xsd:anyURI
  - maxCount: 1

