SPDX-License-Identifier: Community-Spec-1.0

# ListedCryptographicAlgorithm

## Summary

Represents the cryptographic algorithm that is found in the cryptographic algorithm list.

## Description

ListedCryptographicAlgorithm is a class that defines a cryptographic algorithm used in SPDX documents.
This class is commonly used with the following relationships:

- providesAlgorithm: The `from` Element providesAlgorithm `to` CryptographicAlgorithm during a LifecycleScopedRelationship.
- usedAlgorithm: The `from` Element usedAlgorithm `to` CryptographicAlgorithm during a LifecycleScopedRelationship.
- supportsAlgorithm: The `from` Element supportsAlgorithm `to` CryptographicAlgorithm during a LifecycleScopedRelationship.

## Metadata

- name: ListedCryptographicAlgorithm
- SubclassOf: SimpleCryptographicAlgorithm
- Instantiability: Concrete

## Properties

- cryptographicExpressionListVersion
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
