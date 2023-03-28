SPDX-License-Identifier: Community-Spec-1.0

# ExternalReferenceType

## Summary

Specifies the type of an external reference.

## Description

ExteralReferenceType specifies the type of an external reference.

## Metadata

- name: ExternalReferenceType

## Entries

- altDownloadLocation: A reference to an alternative download location.
- altWebPage: A reference to an alternative web page.
- other: Used when the type doesn't match any of the other options.
- securityAdvisory: A reference to the published security advisory (where advisory as defined per ISO 29147:2018). It may contain an impact statement whether a package (e.g. a product) is or is not affected by vulnerabilities.
- securityFix: A reference to the source code with a fix for the vulnerability (e.g., a GitHub commit). 
- securityOther: Used when the reference is security related but doesn't match any of the other types.

