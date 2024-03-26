SPDX-License-Identifier: Community-Spec-1.0

# IntegrityMethod

## Summary

Provides an independently reproducible mechanism that permits verification of a specific Element.

## Description

An IntegrityMethod provides an independently reproducible mechanism that permits verification
of a specific Element that correlates to the data in this SPDX document. This identifier enables
a recipient to determine if anything in the original Element has been changed and eliminates
confusion over which version or modification of a specific Element is referenced.

Please note that different profiles may also provide additional methods for verifying the integrity of specific subclasses of Elements.

## Metadata

- name: IntegrityMethod
- Instantiability: Abstract

## Properties

- comment
  - type: xsd:string
  - maxCount: 1

