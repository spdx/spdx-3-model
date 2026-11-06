SPDX-License-Identifier: Community-Spec-1.0

# CertificateLifecycleEnum

## Summary

An enumeration defining the possible lifecycle states of a digital certificate.

## Description

The CertificateLifecycleEnum defines the various states that a digital certificate may occupy throughout its lifecycle. This enumeration provides a standardized vocabulary for describing the status of a certificate from issuance through termination. The states include: pre-activation (issued but not authorized), active (authorized for use), deactivated (not for new protection but may process existing protected information), suspended (temporarily unusable), revoked (invalidated before expiration), and destroyed (permanently removed). This enumeration enables precise tracking and reporting of certificate status within security and compliance systems.

## Metadata

- name: CertificateLifecycleEnum

## Entries

- preActivation: The certificate has been issued by the issuing certificate authority (CA) but has not been authorized for use.
- active: The certificate may be used to cryptographically protect information, cryptographically process previously protected information, or both.
- deactivated: Certificates in the deactivated state shall not be used to apply cryptographic protection but, in some cases, may be used to process cryptographically protected information.
- suspended: The use of a certificate may be suspended for several possible reasons.
- revoked: A revoked certificate is a digital certificate that has been invalidated by the issuing certificate authority (CA) before its scheduled expiration date.
- destroyed: The certificate has been destroyed.
