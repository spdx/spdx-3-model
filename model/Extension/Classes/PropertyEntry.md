SPDX-License-Identifier: Community-Spec-1.0

# PropertyEntry

## Summary

A property key with an associated extension value.

## Description

The class used for implementing a generic mapping (also known as associative array, dictionary, or hash map) of a key string value to an object value in SPDX.  Each PropertyEntry  contains a key-value pair which maps the key to its associated value.  This class can be used to implement CycloneDX compatible properties where `key` is equivalent to the `name` property in CycloneDX.

## Metadata

- name: PropertyEntry
- Instantiability: Concrete

## Properties

- /Core/key
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- value
  - type: owl:Thing
  - maxCount: 1
