SPDX-License-Identifier: Community-Spec-1.0

# SpdxDocument

## Summary

Assembles a collection of Elements under a common string, the name of the document.

## Description

An SpdxDocument assembles a collection of Elements under a common string, the name of the document.
Commonly used when representing a unit of transfer of SPDX Elements.

## Metadata

- name: SpdxDocument
- SubclassOf: Bundle
- Instantiability: Concrete

## Properties

- name
  - type: xsd:string
  - minCount: 1
  - maxCount: 1

## External properties restrictions

- /Core/Element/name
  - minCount: 1

