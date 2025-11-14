SPDX-License-Identifier: Community-Spec-1.0

# ElementCollection

## Summary

A collection of Elements, not necessarily with unifying context.

## Description

An ElementCollection is a collection of Elements, not necessarily with unifying
context.

Note that all ElementCollections shall conform to the Core profile even if the
Core profile is not specified in the profileConformance property.

If the profileConformance property is not provided, "core" is to be assumed as
the default.

*Constraints*

- If the ElementCollection has at least 1 element, it shall also have at least
  1 rootElement.
- The element shall not be of type SpdxDocument.
- The rootElement shall not be of type SpdxDocument.

## Metadata

- name: ElementCollection
- SubclassOf: Element
- Instantiability: Abstract

## Properties

- element
  - type: Element
  - minCount: 0
- rootElement
  - type: Element
  - minCount: 0
- profileConformance
  - type: ProfileIdentifierType
