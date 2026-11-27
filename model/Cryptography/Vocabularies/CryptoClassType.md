SPDX-License-Identifier: Community-Spec-1.0

# CryptoClassType

## Summary

The cryptographic algorithm enumeration.

## Description

Specifies the type of a cryptographic algorithm.

## Metadata

- name: CryptoClassType

## Entries

- cryptographicHashFunction: Cryptographic algorithms that hash bytes.
- symmetricKeyAlgorithm: Symmetric-key algorithms transform data in a way that is fundamentally difficult to undo without knowledge of a secret key. The key is "symmetric" because the same key is used for a cryptographic operation and its inverse.
- asymmetricKeyAlgorithm: Asymmetric-key algorithms, commonly known as public-key algorithms, use two related keys (i.e., a key pair) to perform their functions: a public key and a private key.
- messageAuthenticationCode: These algorithms provide data origin authentication and integrity protection.
- keyDerivationFunction: These functions derive one or more secret keys from a master secret, password, or other entropy source through a process of stretching or compression.
- randomNumberGenerator: These mechanisms produce sequences of bits or numbers that lack any predictable pattern and are used to ensure the unpredictability of cryptographic keys and nonces. They include both hardware-based true random number generators and deterministic algorithms that expand a small entropy seed into a larger sequence.
