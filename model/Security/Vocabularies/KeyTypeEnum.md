SPDX-License-Identifier: Community-Spec-1.0

# KeyTypeEnum

## Summary

Defines the classification of a cryptographic key.

## Description

This enumeration lists of cryptographic key types, distinguishing between symmetric and asymmetric key types and indicating the key's role within a cryptographic system.

## Metadata

- name: KeyTypeEnum

## Entries

- symmetricKey: A symmetric encryption key used for encrypting and decrypting data using a single secret, as opposed to an asymmetric pair (public/private).
- privateKey: A private cryptographic key that is kept confidential by its owner. It can be used in conjunction with the corresponding public key to create digital signatures or decrypt messages encrypted with the associated public key.
- publicKey: A public cryptographic key paired with a private key for use in encryption and decryption operations, where only the holder of the matching private key can decrypt data encrypted using this public key.
