SPDX-License-Identifier: Community-Spec-1.0

# DictionaryEntry

## Summary

A key with an associated value.

## Description

The class used for implementing a generic string mapping (also known as associative array, dictionary, or hash map) in SPDX.  Each DictionaryEntry contains a key-value pair which maps the key to its associated value.  To implement a dictionary, this class is to be used in a collection with unique keys.

## Metadata

- name: DictionaryEntry
- Instantiability: Concrete

## Properties

- key
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- value
  - type: xsd:string
  - maxCount: 1
