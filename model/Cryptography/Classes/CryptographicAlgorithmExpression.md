SPDX-License-Identifier: Community-Spec-1.0

# CryptographicAlgorithmExpression

## Summary

An SPDX Element containing an SPDX Cryptographic Algorithm Expression string.

## Description

A CryptographicAlgorithmExpression enables the representation, in a single string, of a combination of one or more Cryptographic Algorithms.
The syntax for a Cryptographic Algorithm Expression string is set forth in the corresponding Annex [Cryptographic Algorithm Expression](https://github.com/spdx/cryptographic-algorithm-list/tree/main/docs/SPDXCryptographicAlgorithmExpressions.md)
A CryptographicAlgorithmExpression string is valid only if it conforms to the Cryptographic Algorithm Expression grammar.

## Metadata

- name: CryptographicAlgorithmExpression
- SubclassOf: CryptographicAlgorithm
- Instantiability: Concrete

## Properties

- cryptographicAlgorithmExpression
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- cryptographicExpressionListVersion
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
