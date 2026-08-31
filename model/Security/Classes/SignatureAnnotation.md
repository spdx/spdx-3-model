SPDX-License-Identifier: Community-Spec-1.0

# SignatureAnnotation

## Summary

SignatureAnnotation represents a cryptographic signature associated with a Element providing verification information about the authenticity and integrity of signed content.

## Description

SignatureAnnotation captures metadata about a cryptographic signature applied to software, documents, or other elements. This annotation enables verification that the signed content has not been modified since signing and confirms the identity of the signer.

## Metadata

- name: SignatureAnnotation
- SubclassOf: /Core/Annotation
- Instantiability: Concrete

## Properties

- signatureStorage
  - type: /Core/Artifact
  - minCount: 0
  - maxCount: 1
- signatureValue
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- signatureAlgorithm
  - type: CryptographyAlgorithm
  - minCount: 1
  - maxCount: 1
- verifiedByKey
  - type: Key
  - minCount: 0
  - maxCount: 1
- signedByKey
  - type: Key
  - minCount: 0
  - maxCount: 1
- signedBy
  - type: /Core/Agent
  - minCount: 0
  - maxCount: 1
- signatureTime
  - type: /Core/DateTime
  - minCount: 0
  - maxCount: 1
- signatureFormat
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
