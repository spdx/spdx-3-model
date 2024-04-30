SPDX-License-Identifier: Community-Spec-1.0

# ListedLicenseException

## Summary

A license exception that is listed on the SPDX Exceptions list.

## Description

A ListedLicenseException represents an exception to a License (in other words,
an exception to a license condition or an additional permission beyond those
granted in a License) which is listed on the SPDX Exceptions List at
https://spdx.org/licenses/exceptions-index.html.

## Metadata

- name: ListedLicenseException
- SubclassOf: LicenseAddition
- Instantiability: Concrete

## Properties

- deprecatedVersion
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- listVersionAdded
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
