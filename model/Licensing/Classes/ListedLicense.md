SPDX-License-Identifier: Community-Spec-1.0

# ListedLicense

## Summary

A license that is listed on the SPDX License List.

## Description

A ListedLicense represents a License that is listed on the SPDX License List
at https://spdx.org/licenses.

**TBD** whether to define the meaning and purpose for each of the properties

## Metadata

- name: ListedLicense
- SubclassOf: License
- Instantiability: Concrete

## Properties

- listVersionAdded
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- deprecatedVersion
  - type: xsd:string
  - minCount: 0
  - maxCount: 1

