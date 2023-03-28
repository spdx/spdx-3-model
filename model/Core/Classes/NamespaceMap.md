SPDX-License-Identifier: Community-Spec-1.0

# NamespaceMap

## Summary

A mapping between prefixes and namespace URIs.

## Description

A namespace map allows the creator of a collection of Elements to use
shorter identifiers ("prefixes") instead of URIs to provide a more
human-readable and smaller serialized representation of the Elements.

## Metadata

- name: NamespaceMap
- Instantiability: Concrete

## Properties

- prefix
  - type: xsd:string
  - maxCount: 1
- namespace
  - type: xsd:anyURI
  - maxCount: 1

