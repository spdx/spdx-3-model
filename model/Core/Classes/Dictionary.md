SPDX-License-Identifier: Community-Spec-1.0

# DictionaryEntry

## Summary

A key with an associated value.

## Description

The class used for implementing a generic string mapping (also known as associative arrays, dictionaries, and hash maps) in SPDX.  To implement a dictionary, this class would be used in a collection with unique keys. Each DictionaryEntry would contain a key-value pair which maps the key to its associated value.  Both the key and the value are strings.

## Metadata

- name: DictionaryEntry
- Instantiability: Concrete

## Properties

- key
  - type: xsd:string
  - maxCount: 1
- value
  - type: xsd:string
  - maxCount: 1

