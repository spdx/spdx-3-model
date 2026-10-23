SPDX-License-Identifier: Community-Spec-1.0

# signatureFormat

## Summary

The container format used to encode the signature.

## Description

The signatureFormat property specifies the signature container format used to encode the signature data. This identifies the structure and encoding of how the signature is packaged, enabling appropriate parsing and verification tools to be selected.

Common signature formats include:

- PGP - Pretty Good Privacy format, commonly used for OpenPGP RFC 4880 signatures with support for radix64 encoding
- CMS/PKCS#7 - Cryptographic Message Syntax format, used for S/MIME and code signing with ASN.1 DER encoding
- JSON Web Signature (JWS) - A compact, URL-safe format for signing JSON data, used in modern web APIs
- Detached signature - A format where the signature exists separately from signed content, common in package managers like RPM and apt
- XMLDSig - Digital signatures for XML documents, used in web services and document signing

## Metadata

- name: signatureFormat
- Nature: DataProperty
- Range: xsd:string
