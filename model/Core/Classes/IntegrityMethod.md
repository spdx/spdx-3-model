SPDX-License-Identifier: Community-Spec-1.0

# IntegrityMethod

## Summary

Provides an independently reproducible mechanism that permits verification of a specific Element.

## Description

An IntegrityMethod provides an independently reproducible mechanism that permits verification
of a specific Element that correlates to the data in this SPDX document. This identifier enables
a recipient to determine if anything in the original Element has been changed and eliminates
confusion over which version or modification of a specific Element is referenced.

The recommended method to verify the integrity of `SoftwareArtifacts` Elements (including `Files`, `Snippets`, and `Packages`) is to use the SoftwareArtifact’s `contentIdentifier` property. 

## Metadata

- name: IntegrityMethod
- Instantiability: Abstract

## Properties

- comment
  - type: xsd:string
  - maxCount: 1

