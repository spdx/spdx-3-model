SPDX-License-Identifier: Community-Spec-1.0

# AI

## Summary

Additional metadata based on software profile, that is useful for ai applications and models.

## Description

The AI profile namespace defines concepts related to AI application and model artifacts.

## Metadata

- id: https://rdf.spdx.org/v3/AI
- name: AI

## Profile conformance 

For an element collection to be conformant with this profile,
the following has to hold:

1. for every `/AI/AIPackage` there MUST exist exactly one `/Core/Relationship`
   of type `concludedLicense` having that element as its `from` property
   and an `/SimpleLicensing/AnyLicenseInfo` as its `to` property.
2. for every `/AI/AIPackage` there MUST exist exactly one `/Core/Relationship`
   of type `declaredLicense` having that element as its `from` property
   and an `/SimpleLicensing/AnyLicenseInfo` as its `to` property.
