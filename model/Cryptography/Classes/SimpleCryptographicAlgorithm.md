SPDX-License-Identifier: Community-Spec-1.0

# SimpleCryptographicAlgorithm

## Summary

The class that represents a cryptographic algorithm.

## Description

SimpleCryptographicAlgorithm is an abstract class that defines a cryptographic algorithm used in SPDX documents.

This class is commonly used with the following relationships:

- providesAlgorithm: The `from` Element providesAlgorithm `to` CryptographicAlgorithm during a LifecycleScopedRelationship.
- usesAlgorithm: The `from` Element uses the `to` CryptographicAlgorithm during a LifecycleScopedRelationship.
- supportsAlgorithm: The `from` Element supportsAlgorithm `to` CryptographicAlgorithm during a LifecycleScopedRelationship.

## Metadata

- name: SimpleCryptographicAlgorithm
- SubclassOf: CryptographicAlgorithm
- Instantiability: Abstract

## Properties

- cryptoClass
  - type: CryptoClassType
  - minCount: 1
  - maxCount: 1
- cryptoSubClass
  - type: CryptoSubClassType
  - minCount: 0
  - maxCount: 1
- grammarExpressionReference
  - type: /Core/DictionaryEntry
  - minCount: 0
- parameter
  - type: /Core/DictionaryEntry
- pqcClass
  - type: PqcClassType
  - minCount: 0
  - maxCount: 1
- reference
  - type: xsd:anyURI
  - minCount: 1
- specifiedKeySize
  - type: /Core/PositiveIntegerRange
  - minCount: 0
  
## External properties restrictions

- /Core/Element/name
  - minCount: 1
