SPDX-License-Identifier: Community-Spec-1.0

# CryptographyAlgorithm

## Summary

Represents a specific cryptographic algorithm (e.g., RSA, AES) and its configurable parameters.

## Description

Cryptographic algorithm originate from cryptographic artifact.
A cryptographic algorithm is a well-defined mathematical procedure or set of rules that performs cryptographic operations, such as encryption, decryption, hashing, digital signing, or key exchange, using inputs like plaintext, keys, and parameters to produce secure outputs.

Specifies a CryptographyAlgorithm includeing attributes set in the parameter: variant, key length, block size and mode of operation.

## Metadata

- name: CryptographyAlgorithm
- SubclassOf: CryptographyArtifact
- Instantiability: Concrete

## Properties

- cryptographyName
  - type: CryptographyNameType
  - minCount: 1
  - maxCount: 1
- cryptographicAlgorithmsListVerson
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- parameter
  - type: /Core/DictionaryEntry
  - minCount: 0
