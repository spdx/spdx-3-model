SPDX-License-Identifier: Community-Spec-1.0

# ElementCollection

## Summary

A collection of Elements, not necessarily with unifying context.

## Description

An Element Collection is a collection of Elements, not necessarily with unifying context.

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

