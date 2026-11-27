SPDX-License-Identifier: Community-Spec-1.0

# CustomCryptographicAlgorithm

## Summary

The class that represents a cryptographic algorithm that is `NOT` found in the SPDX Cryptographic Algorithm List.

## Description

`CustomCryptographicAlgorithm` represents a cryptographic algorithm that is `NOT` found in the SPDX Cryptographic Algorithm List.

This class is commonly used with the following relationships:

- providesAlgorithm: The `from` Element providesAlgorithm `to` CryptographicAlgorithm during a LifecycleScopeType.
- usesAlgorithm: The `from` Element uses the `to` CryptographicAlgorithm during a LifecycleScopedRelationship.
- supportsAlgorithm: The `from` Element supportsAlgorithm `to` CryptographicAlgorithm during LifecycleScopeType.

## Metadata

- name: CustomCryptographicAlgorithm
- SubclassOf: SimpleCryptographicAlgorithm
- Instantiability: Concrete
