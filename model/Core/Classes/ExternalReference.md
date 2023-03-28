SPDX-License-Identifier: Community-Spec-1.0

# ExternalReference

## Summary

A reference to a resource outside the scope of SPDX-3.0 content.

## Description

An External Reference points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.

## Metadata

- name: ExternalReference
- SubclassOf: none
- Instantiability: Concrete

## Properties

- externalReferenceType
  - type: ExternalReferenceType
  - maxCount: 1
- locator
  - type: xsd:anyURI
- contentType
  - type: MediaType
  - maxCount: 1
- comment
  - type: xsd:string
  - maxCount: 1

