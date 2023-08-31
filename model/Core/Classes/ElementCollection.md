SPDX-License-Identifier: Community-Spec-1.0

# ElementCollection

## Summary

A collection of Elements, not necessarily with unifying context.

## Description

An SpdxCollection is a collection of Elements, not necessarily with unifying context.

## Metadata

- name: ElementCollection
- SubclassOf: Element
- Instantiability: Abstract

## Properties

- element
  - type: Element and NOT (X-Collection)
  - minCount: 1
- rootElement
  - type: Element and NOT (X-Collection)
  - minCount: 1
- imports
  - type: ExternalMap

