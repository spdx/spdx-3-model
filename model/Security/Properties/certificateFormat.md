SPDX-License-Identifier: Community-Spec-1.0

# certificateFormat

## Summary

certificateFormat is the format or encoding standard of this Certificate.

## Description

certificateFormat specifies the encoding format or standard used to represent this Certificate. Common certificate formats include X.509 (the most widely used standard for public key certificates), PEM (Privacy Enhanced Mail, base64-encoded DER format), DER (Distinguished Encoding Rules, a binary encoding format), PKCS#12 (Personal Information Exchange Syntax Standard), and PFX (Personal Information Exchange). This property helps tools and systems understand how to parse and validate the certificate data, as different formats have different encoding rules and structures.

## Metadata

- name: certificateFormat
- Nature: DataProperty
- Range: xsd:string
