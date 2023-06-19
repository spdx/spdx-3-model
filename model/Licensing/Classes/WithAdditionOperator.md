SPDX-License-Identifier: Community-Spec-1.0

# WithAdditionOperator

## Summary

Portion of an AnyLicenseInfo representing a License which has additional
text applied to it

## Description

A WithAdditionOperator indicates that the designated License is subject to the
designated LicenseAddition, which might be a license exception on the SPDX
Exceptions List (ListedLicenseException) or may be other additional text
(CustomLicenseAddition). It is represented in the SPDX License Expression
Syntax by the `WITH` operator.

## Metadata

- name: WithAdditionOperator
- SubclassOf: AnyLicenseInfo
- Instantiability: Concrete

## Properties

- subjectLicense
  - type: ExtendableLicense
  - minCount: 1
  - maxCount: 1
- subjectAddition
  - type: LicenseAddition
  - minCount: 1
  - maxCount: 1
