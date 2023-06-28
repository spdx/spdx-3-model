SPDX-License-Identifier: Community-Spec-1.0

# SimpleCustomLicense

## Summary

A license that is not listed on the SPDX License List.

## Description

A SimpleCustomLicense represents a License that is not listed on the SPDX License
List at https://spdx.org/licenses, and is therefore defined by an SPDX data
creator.

## Metadata

- name: SimpleCustomLicense
- SubclassOf: AnyLicenseInfo
- Instantiability: Concrete

## Properties

- simpleCustomLicenseText
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
