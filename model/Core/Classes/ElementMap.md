SPDX-License-Identifier: Community-Spec-1.0

# ElementMap

## Summary

A key with an Element.

## Description

The class used for implementing mapping a string key to an Element.

Each ElementMap contains a key-value pair which maps the key to its
associated Element.

To implement a dictionary, this class is to be used in a collection with
unique keys.

## Metadata

- name: ElementMap
- Instantiability: Concrete

## Properties

- key
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- elementValue
  - type: Element
  - minCount: 1
  - maxCount: 1
