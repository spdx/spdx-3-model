SPDX-License-Identifier: Community-Spec-1.0

# Dataset

## Summary

The Dataset Profile provides additional metadata, based on Software Profile,
that is useful for datasets.

## Description

The Dataset namespace defines concepts related to dataset, including its
preparation process, its characteristics, and its access methods.

## Metadata

- id: https://spdx.org/rdf/3.0.0/terms/Dataset
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
