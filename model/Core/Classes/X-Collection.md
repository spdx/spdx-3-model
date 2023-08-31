SPDX-License-Identifier: Community-Spec-1.0

# X-Collection

## Summary

Assembles a collection of Elements that does not contain any other X Collection Elements.

## Description

An X collection Element is a collection of Elements that does not contain any other X Collection Elements.

In this way it can be thought of as an outer shell collection of SPDX content without 
self-recursion that can be used as a content aggregation target for serialization.


## Metadata

- name: X-collection
- SubclassOf: ElementCollection
- Instantiability: Concrete

## Properties

- namespaceMap
  - type: NamespaceMap
