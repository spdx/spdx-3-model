SPDX-License-Identifier: Community-Spec-1.0

# CreationInfoMap

## Summary

Defines an abbreviation string for a CreationInfo instance

## Description

In the logical model all elements have a creationInfo property whose value is a CreationInfo
structure. In serialized data the structure can be replaced by a short identifier for brevity.
When parsing serialized data into Element values the mapping is reversed, replacing
the identifiers with full CreationInfo values.

## Metadata

- name: CreationInfoMap
- SubclassOf: none
- Instantiability: Concrete

## Properties

- ci
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- creationInfo
  - type: CreationInfo
  - minCount: 1
  - maxCount: 1
