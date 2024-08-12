SPDX-License-Identifier: Community-Spec-1.0

# LicenseExpression

## Summary

An SPDX Element containing an SPDX license expression string.

## Description

A LicenseExpression enables the representation, in a single string, of a
combination of one or more licenses, together with additions such as license
exceptions.

The syntax for a LicenseExpression string is set forth in the corresponding
Annex of this specification
(["SPDX license expressions"](../../../annexes/spdx-license-expressions.md)).
A LicenseExpression string is not valid if it does not conform to the grammar
set forth in that annex.

The ExpandedLicensing profile can be used to represent the complete parsed
license expression as a combination of license objects.

## Metadata

- name: LicenseExpression
- SubclassOf: AnyLicenseInfo
- Instantiability: Concrete

## Properties

- licenseExpression
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- licenseListVersion
  - type: /Core/SemVer
  - maxCount: 1
- customIdToUri
  - type: /Core/DictionaryEntry
  - minCount: 0
