SPDX-License-Identifier: Community-Spec-1.0

# subjectPublicKey

## Summary

The public key bound to the certificate's subject.

## Description

This property links a Certificate to the public key component of the key pair associated with the certificate's subject. The public key is used by verifiers to validate digital signatures or encrypt data intended for the subject. The corresponding private key must be securely held by the subject.

## Metadata

- name: subjectPublicKey
- Nature: ObjectProperty
- Range: Key
