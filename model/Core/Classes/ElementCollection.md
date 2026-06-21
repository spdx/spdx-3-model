SPDX-License-Identifier: Community-Spec-1.0

# ElementCollection

## Summary

A collection of Elements, not necessarily with unifying context.

## Description

An ElementCollection is a collection of Elements, not necessarily with unifying
context.

An ElementCollection shall conform to the Core profile, regardless of whether
the Core profile is explicitly specified in the profileConformance property.

If the profileConformance property is omitted, it shall be evaluated as a list
containing the "core" profile identifier.

The inclusion of a profile identifier within the profileConformance property
shall constitute a declaration that all constituent elements conform to the
restrictions specified by that profile.

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
