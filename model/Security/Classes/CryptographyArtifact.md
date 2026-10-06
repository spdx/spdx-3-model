SPDX-License-Identifier: Community-Spec-1.0

# CryptographyArtifact

## Summary

An abstract base for concrete cryptographic data objects (e.g., keys, certificates, signatures) used in security operations.

## Description

A cryptographic artifact is any concrete piece of data that embodies or supports a cryptographic function, such as protecting confidentiality, integrity, or authenticity. In practice, it is a specific, handleable item (file, value, or record).

## Metadata

- name: CryptographyArtifact
- SubclassOf: /Core/Artifact
- Instantiability: Abstract

## Properties

- sourceElement
  - type: /Core/Element
  - minCount: 0
