SPDX-License-Identifier: Community-Spec-1.0

# ExternalRef

## Summary

A reference to a resource outside the scope of SPDX-3.0 content.

## Description

An External Reference points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.

## Metadata

- name: ExternalRef
- SubclassOf: none
- Instantiability: Concrete

## Properties

- externalRefType
  - type: ExternalRefType
  - maxCount: 1
- locator
  - type: xsd:string
- contentType
  - type: MediaType
  - maxCount: 1
- comment
  - type: xsd:string
  - maxCount: 1

