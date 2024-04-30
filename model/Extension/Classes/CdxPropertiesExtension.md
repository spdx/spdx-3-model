SPDX-License-Identifier: Community-Spec-1.0

# CdxPropertiesExtension

## Summary

A type of extension consisting of a list of name value pairs.

## Description

This extension provides a more structured extension using a name-value
approach.

Unlike key-value stores, cdxProperties support duplicate names, each
potentially having different values.

This is intended to be compatible with the CycloneDX property `properties`.

## Metadata

- name: CdxPropertiesExtension
- SubclassOf: Extension
- Instantiability: Concrete

## Properties

- cdxProperty
  - type: CdxPropertyEntry
  - minCount: 1
