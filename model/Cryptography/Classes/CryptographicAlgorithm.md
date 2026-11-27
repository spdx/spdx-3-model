SPDX-License-Identifier: Community-Spec-1.0

# CryptographicAlgorithm

## Summary

The base class that represents a cryptographic algorithm.

## Description

CryptographicAlgorithm is an abstract class that defines a cryptographic algorithm used in SPDX documents.
This class is commonly used with the following relationships:

- providesAlgorithm: The `from` Element provides Algorithm `to` CryptographicAlgorithm during a LifecycleScopedRelationship. The `from` must provide all valid branches that is defined in the `to` CryptographicAlgorithm.
- usedAlgorithm: The `from` Element usedAlgorithm `to` CryptographicAlgorithm during a LifecycleScopedRelationship.
- supportsAlgorithm: The `from` Element supportsAlgorithm `to` CryptographicAlgorithm during a LifecycleScopedRelationship. The `from` must support all valid branches that is defined in the `to` CryptographicAlgorithm.

## Metadata

- name: CryptographicAlgorithm
- SubclassOf: /Core/Element
- Instantiability: Abstract
