SPDX-License-Identifier: Community-Spec-1.0

# verifiedByKey

## Summary

The cryptographic key used to verify the signature.

## Description

The verifiedByKey property references the Key element that was used during signature verification. When a signature is verified, the verifier applies the signature algorithm with this key (typically the signer's public key) to confirm that the signature value matches what would be expected for the signed content.

## Metadata

- name: verifiedByKey
- Nature: ObjectProperty
- Range: Key
