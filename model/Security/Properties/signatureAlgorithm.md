SPDX-License-Identifier: Community-Spec-1.0

# signatureAlgorithm

## Summary

The cryptographic algorithm used to create and verify the signature.

## Description

The signatureAlgorithm property references a CryptographyAlgorithm element that specifies the cryptographic method used to generate and verify the signature. This algorithm defines the mathematical operations applied to the hash of the content and the signer's private key to produce the signature value.

## Metadata

- name: signatureAlgorithm
- Nature: ObjectProperty
- Range: CryptographyAlgorithm
