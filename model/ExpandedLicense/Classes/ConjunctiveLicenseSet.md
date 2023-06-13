SPDX-License-Identifier: Community-Spec-1.0

# ConjunctiveLicenseSet

## Summary

Portion of an AnyLicenseInfo representing a set of licensing information
where all elements apply.

## Description

A ConjunctiveLicenseSet indicates that _each_ of its subsidiary
AnyLicenseInfos apply. In other words, a ConjunctiveLicenseSet of two or
more licenses represents a licensing situation where _all_ of the specified
licenses are to be complied with. It is represented in the SPDX License
Expression Syntax by the `AND` operator.

It is syntactically correct to specify a ConjunctiveLicenseSet where the
subsidiary AnyLicenseInfos may be "incompatible" according to a particular
interpretation of the corresponding Licenses. The SPDX License Expression
Syntax does not take into account interpretation of license texts, which is
left to the consumer of SPDX data to determine for themselves.

## Metadata

- name: ConjunctiveLicenseSet
- SubclassOf: Licensing/AnyLicenseInfo
- Instantiability: Concrete

## Properties

- member
  - type: Licensing/AnyLicenseInfo
  - minCount: 2
