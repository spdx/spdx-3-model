SPDX-License-Identifier: Community-Spec-1.0

# ContentIdentifier

## Summary

A canonical, unique, immutable identifier

## Description

A ContentIdentifier is a canonical, unique, immutable identifier of the content of a software artifact, such as a package, a file, or a snippet.
It can be used for verifying its identity and integrity.

## Metadata

- name: ContentIdentifier
- SubclassOf: /Core/IntegrityMethod
- Instantiability: Concrete

## Properties

- contentIdentifierType
  - type: ContentIdentifierType
  - minCount: 1
  - maxCount: 1
- contentIdentifierValue
  - type: xsd:string
  - minCount: 1
  - maxCount: 1

