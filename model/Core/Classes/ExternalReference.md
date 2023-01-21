SPDX-License-Identifier: Community-Spec-1.0

# ExternalReference

## Summary

A reference to a resource outside of the scope of SPDX-3.0 content.

## Description

An External Reference is a grouping of characteristics unique to the identity,
location and context of a resource outside of the scope of SPDX-3.0 content.

## Metadata

- name: ExternalReference
- SubclassOf: none
- Instantiability: Concrete

## Properties

- externalReferenceType
  - type: ExternalReferenceType
  - maxCount: 1
- locator
  - type: anyURI
- contentType
  - type: MediaType
  - maxCount: 1
- comment
  - type: xsd:string
  - maxCount: 1

