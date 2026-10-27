SPDX-License-Identifier: Community-Spec-1.0

# signedByKey

## Summary

The cryptographic key used to create the signature.

## Description

The signedByKey property references the Key element that was used to generate the signature. When content is signed, the signer's private key is applied using the specified signature algorithm to produce the signature value. This property establishes the cryptographic identity of the signer by pointing to the specific key material used during the signing operation.

## Metadata

- name: signedByKey
- Nature: ObjectProperty
- Range: Key
