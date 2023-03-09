SPDX-License-Identifier: Community-Spec-1.0

# NamespaceMap

## Summary

A mapping between prefixes and namespace URIs.

## Description

A namespace map allows the creator of a collection of Elements to use
memorable identifiers ("prefixes") instead of URIs by defining a mapping between them.

## Metadata

- name: NamespaceMap
- Instantiability: Concrete

## Properties

- prefix
  - type: xsd:string
  - maxCount: 1
- namespace
  - type: anyURI
  - maxCount: 1

