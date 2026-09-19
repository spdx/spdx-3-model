SPDX-License-Identifier: Community-Spec-1.0

# CertificateAnnotationState

## Summary

A record representing the lifecycle state of a certificate at a specific point in time.

## Description

The CertificateAnnotationState class represents an annotation that records the lifecycle state of a certificate at a specific point in time. It combines the certificate's status (as defined in CertificateLifecycleEnum) with a timestamp (annotationTime) to provide a historical record of the certificate's status. This allows for tracking when a certificate entered a specific state, such as Active, Revoked, or Suspended.

## Metadata

- name: CertificateAnnotationState
- SubclassOf: /Core/Annotation
- Instantiability: Concrete

## Properties

- certificateState
  - type: CertificateLifecycleEnum
  - minCount: 1
- annotationTime
  - type: /Core/DateTime
  - minCount: 1
  - maxCount: 1
