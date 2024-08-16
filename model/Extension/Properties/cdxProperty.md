SPDX-License-Identifier: Community-Spec-1.0

# cdxProperty

## Summary

Provides a map of a property names to a values.

## Description

This field provides a mapping of a name to a value.

This is intended to be compatible with the CycloneDX property `properties`.

Unlike key-value stores, CdxPropertiesExtension support duplicate names, each
potentially having different values.

## Metadata

- name: cdxProperty
- Nature: ObjectProperty
- Range: CdxPropertyEntry
