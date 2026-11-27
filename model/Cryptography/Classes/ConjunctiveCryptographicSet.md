SPDX-License-Identifier: Community-Spec-1.0

# ConjunctiveCryptographicSet

## Summary

Represents a set of `CryptographicAlgorithm` instances where all elements apply.

## Description

A ConjunctiveCryptographicSet of two or more `CryptographicAlgorithm` instances represents a logical grouping of multiple `CryptographicAlgorithm` instances. It is represented in the SPDX Cryptographic Algorithm List Expression Syntax by the `AND` operator.

## Metadata

- name: ConjunctiveCryptographicSet
- SubclassOf: CryptographicAlgorithm
- Instantiability: Concrete

## Properties

- member
  - type: CryptographicAlgorithm
  - minCount: 2
