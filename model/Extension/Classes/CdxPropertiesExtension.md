SPDX-License-Identifier: Community-Spec-1.0
# CdxPropertiesExtension

## Summary
A type of extension consisting of a list of name value pairs.

## Description
This extension provides a more structured extension using a keyword / value approach.
This is intended to be compatible with the CycloneDX property `properties`.

See the `cdxProperties` definition for how to map the keys and values to CycloneDX.

## Metadata
- name: CdxPropertiesExtension
- SubclassOf: Extension
- Instantiability: Concrete

## Properties
- cdxProperties
  - type: /Core/DictionaryEntry
  - minCount: 0
