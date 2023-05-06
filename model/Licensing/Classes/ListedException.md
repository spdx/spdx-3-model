SPDX-License-Identifier: Community-Spec-1.0

# ListedException

## Summary

A license exception that is listed on the SPDX Exceptions list.

## Description

A ListedException represents an exception to a License (in other words,
an exception to a license condition or an additional permission beyond those
granted in a License) which is listed on the SPDX Exceptions List at
https://spdx.org/licenses/exceptions-index.html.

## Metadata

- name: ListedException
- SubclassOf: Addition
- Instantiability: Concrete

## Properties

- listVersionAdded
  - type: LicenseListVersion
  - minCount: 0
  - maxCount: 1
- deprecatedVersion
  - type: LicenseListVersion
  - minCount: 0
  - maxCount: 1
