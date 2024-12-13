SPDX-License-Identifier: Community-Spec-1.0

# AI

## Summary

The AI Profile is designed to provide a standardized way of documenting and
sharing information about AI software packages (i.e. systems).

## Description

The AI namespace defines a set of concepts and data elements related to AI
system and model artifacts. These artifacts are the tangible outputs of the AI
development process, such as software packages, models, and datasets.

## Metadata

- id: https://spdx.org/rdf/3.0.1/terms/AI
- name: AI

## Profile conformance

For an element collection to be conformant with this profile,
the following has to hold:

1. for every `/AI/AIPackage` there MUST exist exactly one `/Core/Relationship`
   of type `hasConcludedLicense` having that element as its `from` property
   and a `/SimpleLicensing/AnyLicenseInfo` as its `to` property.
2. for every `/AI/AIPackage` there MUST exist exactly one `/Core/Relationship`
   of type `hasDeclaredLicense` having that element as its `from` property
   and a `/SimpleLicensing/AnyLicenseInfo` as its `to` property.
