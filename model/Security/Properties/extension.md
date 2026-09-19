SPDX-License-Identifier: Community-Spec-1.0

# extension

## Summary

Extension specifies the type or category of the CertificateExtension.

## Description

Extension identifies which kind of extension this CertificateExtension represents by referencing an ExtensionType. This property determines the semantic meaning and expected structure of the extension value, allowing systems to interpret the additional information correctly. For example, if extension is set to subjectAlternativeName, the value field would contain comma-separated domain names or IP addresses associated with the certificate's subject. Similarly, if extension is set to keyUsage, the value would encode permitted cryptographic operations such as digital signature or key encipherment

## Metadata

- name: extension
- Nature: DataProperty
- Range: ExtensionType
