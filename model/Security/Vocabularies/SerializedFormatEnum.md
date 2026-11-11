SPDX-License-Identifier: Community-Spec-1.0

# SerializedFormatEnum

## Summary

Enumeration of serialization formats for cryptographic artifacts.

## Description

A SerializedFormatEnum value describes the serialization format of a CryptographyArtifact, such as PEM or DER. These values help systems correctly parse and handle serializedArtifact content.

## Metadata

- name: SerializedFormatEnum

## Entries

- pem: PEM (originally “Privacy Enhanced Mail”) is the most common format for X.509 certificates, CSRs, and cryptographic keys.
- der: (Distinguished Encoding Rules) is a binary encoding for X.509 certificates and private keys.
