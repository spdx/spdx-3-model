SPDX-License-Identifier: Community-Spec-1.0

# DisjunctiveCryptographicSet

## Summary

Represents a set of `CryptographicAlgorithm` instances where one or more elements apply.

## Description

A DisjunctiveCryptographicSet of two or more `CryptographicAlgorithm` instances represents a logical grouping of multiple `CryptographicAlgorithm` instances in a selection list. It is represented in the SPDX Cryptographic Algorithm List Expression Syntax by the `OR` operator.

## Metadata

- name: DisjunctiveCryptographicSet
- SubclassOf: CryptographicAlgorithm
- Instantiability: Concrete

## Properties

- member
  - type: CryptographicAlgorithm
  - minCount: 2
