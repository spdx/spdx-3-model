SPDX-License-Identifier: Community-Spec-1.0

# licenseListVersion

## Summary

The version of the SPDX License List used in the license expression.

## Description

Recognizing that licenses are added to the SPDX License List with each subsequent version, the intent is to provide consumers with the version of the SPDX License List used. 
This anticipates that in the future, license expression might have used a version of the SPDX License List that is older than the then current one.
The specified version of the SPDX License List must include all listed licenses and exceptions referenced in the expression.

## Metadata

- name: licenseListVersion
- Nature: DataProperty
- Range: xsd:string

