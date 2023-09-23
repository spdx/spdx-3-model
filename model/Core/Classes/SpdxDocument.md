SPDX-License-Identifier: Community-Spec-1.0

# SpdxDocument

## Summary

Describes an instance of SPDX data serialized using a specific format.

## Description

SpdxDocument is metadata about a byte sequence (payload) that can be parsed into a set of element values.
It includes the SpdxIds of elements included in the payload, and information used to locate and verify the payload.

## Metadata

- name: SpdxDocument
- SubclassOf: Element
- Instantiability: Concrete

## Properties

- element
  - type: Element
  - minCount: 1

- locationHint
  - type: anyURI
  - minCount: 0

- verifiedUsing
  - type: IntegrityMethod
  - minCount: 0


