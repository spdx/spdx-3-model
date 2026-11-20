SPDX-License-Identifier: Community-Spec-1.0

# CertificateExtension

## Summary

CertificateExtension represents an extension added to a certificate to provide additional metadata or configuration about the certificate.

## Description

CertificateExtension specifies an extension field contained within a Certificate, typically following standards like X.509. Certificate extensions are used to convey additional information about the certificate that is not captured in the standard certificate fields. Common extensions include Subject Alternative Names (allowing additional domain names to be associated with the certificate), Key Usage (specifying permitted cryptographic operations), Extended Key Usage (defining specific purposes like server authentication or code signing), Basic Constraints (indicating whether the certificate is a CA certificate), and Subject Key Identifier (providing a way to identify the public key associated with this certificate). Each extension contains an OID or name identifier and an encoded value specific to that extension type.

## Metadata

- name: CertificateExtension
- Instantiability: Concrete

## Properties

- extension
  - type: ExtensionType
  - minCount: 1
  - maxCount: 1
- oid
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- /Core/value
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
