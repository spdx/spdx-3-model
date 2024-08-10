SPDX-License-Identifier: Community-Spec-1.0

# AnyLicenseInfo

## Summary

Abstract class representing a license combination consisting of one or more licenses.

## Description

AnyLicenseInfo is 
an bstract class representing a license combination consisting of one or more
licenses (optionally including additional text), which may be combined
according to the
[SPDX license expression syntax](../../../annexes/SPDX-license-expressions.md).

An AnyLicenseInfo is used by licensing properties of software artifacts.

It can be:

- a NoneLicense;
- a NoAssertionLicense;
- a single license (either on the
  [SPDX License List](https://spdx.org/licenses/) or
  [a custom-defined license](../../ExpandedLicensing/Classes/CustomLicense.md));
- a single license with an "or later" operator applied;
- the foregoing with additional text applied; or
- a set of licenses combined by applying "AND" and "OR" operators recursively.

## Metadata

- name: AnyLicenseInfo
- SubclassOf: /Core/Element
- Instantiability: Abstract
