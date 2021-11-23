SPDX-License-Identifier: Community-Spec-1.0

# Document

## Summary

A grouping of SPDX-3.0 content with no presumption of shared context.

## Description

A Document is a container for a grouping of SPDX-3.0 content with no presumption of shared context.

## Metadata

- name: Document
- SubclassOf: Element
- Instantiability: Concrete

## Properties

- namespace
  - type: URI
  - minCount: 1
  - maxCount: 1
- externalMap
  - type; ExternalMap
- element
  - type: Element
  - minCount: 1
- rootElement
  - type: Element
  - minCount: 1

