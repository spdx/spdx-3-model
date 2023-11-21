SPDX-License-Identifier: Community-Spec-1.0

# Dataset

## Summary

Everything having to do with datasets.

## Description

The Dataset namespace defines tbd.

## Metadata

- id: https://rdf.spdx.org/v3/Dataset
- name: Dataset

## Profile conformance 

For an element collection to be conformant with this profile,
the following has to hold:

1. for every `/Dataset/DatasetPackage` there MUST exist exactly one `/Core/Relationship`
   of type `concludedLicense` having that element as its `from` property
   and an `/SimpleLicensing/AnyLicenseInfo` as its `to` property.
2. for every `/Dataset/DatasetPackage` there MUST exist exactly one `/Core/Relationship`
   of type `declaredLicense` having that element as its `from` property
   and an `/SimpleLicensing/AnyLicenseInfo` as its `to` property.
