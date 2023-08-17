SPDX-License-Identifier: Community-Spec-1.0

# licenseListVersion

## Summary

An optional field for creators of the SPDX Element to provide the version of the SPDX License List used when the SPDX Element was created.

## Description

Recognizing that licenses are added to the SPDX License List with each subsequent version, the intent is to provide recipients of the SPDX Element with the version of the SPDX License List used. This anticipates that in the future, an SPDX Element might have used a version of the SPDX License List that is older than the then current one.

## Metadata

- name: licenseListVersion
- Nature: DataProperty
- Range: xsd:string

