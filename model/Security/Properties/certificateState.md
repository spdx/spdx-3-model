SPDX-License-Identifier: Community-Spec-1.0

# certificateState

## Summary

The lifecycle state of the certificate at the time of the annotation.

## Description

This property specifies the state of the certificate as defined in the CertificateLifecycleEnum. It indicates the current status of the certificate, such as pre-activation, active, deactivated, suspended, revoked, or destroyed. The value represents the certificate's state at the time recorded by the annotationTime property.

## Metadata

- name: certificateState
- Nature: ObjectProperty
- Range: CertificateLifecycleEnum
