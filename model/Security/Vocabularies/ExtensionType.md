SPDX-License-Identifier: Community-Spec-1.0

# ExtensionType

## Summary

ExtensionType specifies the category or purpose of an Extension within a Certificate.

## Description

ExtensionType defines an enumerated set of recognized extension types that can be included in a Certificate. Each ExtensionType represents a specific standardized use case for adding additional metadata or configuration to a certificate. These types follow common standards such as X.509 and help establish the certificate's intended usage, security constraints, and trust characteristics. When a Certificate includes an extension, the extensionType identifies what kind of additional information is being conveyed, enabling systems to properly interpret and validate the certificate according to its defined policies and intended purpose.
Metadata

## Metadata

- name: ExtensionType

## Entries

- basicConstraints: Specifies whether a certificate can be used as a CA certificate or not.
- keyUsage: Specifies the allowed uses of the public key in the certificate.
- extendedKeyUsage: Specifies additional purposes for which the public key can be used.
- subjectAlternativeName: Allows inclusion of additional names to identify the entity associated with the certificate.
- authorityKeyIdentifier: Identifies the public key of the CA that issued the certificate.
- subjectKeyIdentifier: Identifies the public key associated with the entity the certificate was issued to.
- authorityInformationAccess: Contains CA issuers and OCSP information.
- certificatePolicies: Defines the policies under which the certificate was issued and can be used.
- crlDistributionPoints: Contains one or more URLs where a Certificate Revocation List (CRL) can be obtained.
- signedCertificateTimestamp: Shows that the certificate has been publicly logged, which helps prevent the issuance of rogue certificates by a CA. Log ID, timestamp and signature as proof.
- custom: a ExtensionType not defined in any other ExtensionType.
