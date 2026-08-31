SPDX-License-Identifier: Community-Spec-1.0

# Certificate

## Summary

Represents a certificate, (typically X.509 v3 ITU-T) that binds a public key to an identity.

## Description

This element describes a specific Certificate.
An certificate is a standardized document (often using the X.509 v3 ITU-T format) that binds a public key to an identity (user, service, device, or organization) using a signature from a trusted Certificate Authority (CA).

## Metadata

- name: Certificate
- SubclassOf: CryptographyArtifact
- Instantiability: Concrete

## Properties

- serialNumber
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- version
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- /Core/subject
  - type: /Core/Element
  - minCount: 1
- subjectPublicKey
  - type: Key
  - minCount: 1
  - maxCount: 1
- issuerAgent
  - type: /Core/Agent
  - minCount: 1
- notValidBefore
  - type: /Core/DateTime
  - minCount: 1
  - maxCount: 1
- notValidAfter
  - type: /Core/DateTime
  - minCount: 1
  - maxCount: 1
- certificateFormat
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- certificateExtension
  - type: CertificateExtension
  - minCount: 0
