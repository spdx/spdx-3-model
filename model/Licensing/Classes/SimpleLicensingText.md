SPDX-License-Identifier: Community-Spec-1.0

# SimpleLicensingText

## Summary

A license or addition that is not listed on the SPDX License List.

## Description

A SimpleLicensingText represents a License or Addition that is not listed on the SPDX License
List at https://spdx.org/licenses, and is therefore defined by an SPDX data
creator.

## Metadata

- name: SimpleLicensingText
- SubclassOf: AnyLicenseInfo
- Instantiability: Concrete

## Properties

- simpleLicensingText
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
