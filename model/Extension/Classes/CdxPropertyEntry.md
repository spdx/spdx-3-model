SPDX-License-Identifier: Community-Spec-1.0

# CdxPropertyEntry

## Summary

A property name with an associated value.

## Description

Each CdxPropertyEntry  contains a name-value pair which maps the name to its associated value.
Unlike key-value stores, cdxProperties support duplicate names, each potentially having different values.
This class can be used to implement CycloneDX compatible properties.

## Metadata

- name: CdxPropertyEntry
- Instantiability: Concrete

## Properties

- cdxPropName
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- cdxPropValue
  - type: xsd:string
  - maxCount: 1
