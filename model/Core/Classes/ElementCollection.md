SPDX-License-Identifier: Community-Spec-1.0

# ElementCollection

## Summary

A collection of Elements, not necessarily with unifying context.

## Description

An ElementCollection is a collection of Elements, not necessarily with unifying context.

Note that all ElementCollections must conform to the core profile even if the core profile is no specified in the profileConformance property.
If the profileConformance property is not provided, core is to be assumed as the default.

## Metadata

- name: ElementCollection
- SubclassOf: Element
- Instantiability: Abstract

## Properties

- element
  - type: Element
  - minCount: 1
- rootElement
  - type: Element
  - minCount: 1
- imports
  - type: ExternalMap
- profileConformance
  - type: ProfileIdentifierType
