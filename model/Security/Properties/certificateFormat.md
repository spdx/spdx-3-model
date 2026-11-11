SPDX-License-Identifier: Community-Spec-1.0

# certificateFormat

## Summary

certificateFormat is the format or encoding standard of this Certificate.

## Description

certificateFormat specifies the representation format or encoding used for the certificate value. Common certificate formats include X.509 (the most widely used standard for public key certificates), PEM (Privacy Enhanced Mail, base64-encoded DER format), DER (Distinguished Encoding Rules, a binary encoding format), PKCS#12 (Personal Information Exchange Syntax Standard), and PFX (Personal Information Exchange). Note that X.509 refers to the certificate structure, PEM and DER refer to encodings, and PKCS#12/PFX refer to container formats that may include certificates and related objects.

## Metadata

- name: certificateFormat
- Nature: DataProperty
- Range: xsd:string
