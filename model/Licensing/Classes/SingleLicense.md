SPDX-License-Identifier: Community-Spec-1.0

# SingleLicense

## Summary

A license expression representing a single license.

## Description

A SingleLicense is a license expression that indicates there is a single license.

## Metadata

- name: SingleLicense
- SubclassOf: LicenseExpression
- Instantiability: Concrete

## Properties

- license
  - type: License
  - minCount: 1
  - maxCount: 1

