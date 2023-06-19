SPDX-License-Identifier: Community-Spec-1.0

# DisjunctiveLicenseSet

## Summary

Portion of an AnyLicenseInfo representing a set of licensing information
where only any one of the elements applies.

## Description

A DisjunctiveLicenseSet indicates that _only one_ of its subsidiary
AnyLicenseInfos is required to apply. In other words, a
DisjunctiveLicenseSet of two or more licenses represents a licensing
situation where _only one_ of the specified licenses are to be complied with.
A consumer of SPDX data would typically understand this to permit the recipient
of the licensed content to choose which of the corresponding license they
would prefer to use. It is represented in the SPDX License Expression Syntax
by the `OR` operator.

## Metadata

- name: DisjunctiveLicenseSet
- SubclassOf: Licensing/AnyLicenseInfo
- Instantiability: Concrete

## Properties

- member
  - type: Licensing/AnyLicenseInfo
  - minCount: 2
