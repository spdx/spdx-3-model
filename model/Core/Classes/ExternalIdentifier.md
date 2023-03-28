SPDX-License-Identifier: Community-Spec-1.0

# ExternalIdentifier

## Summary

A reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.

## Description

An ExternalIdentifier is a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.

## Metadata

- name: ExternalIdentifier
- Instantiability: Concrete


## Properties

- externalIdentifierType
  - type: ExternalIdentifierType
  - minCount: 1
  - maxCount: 1
- identifier
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- comment
  - type: xsd:string
  - minCount: 0
  - maxCount: 1

