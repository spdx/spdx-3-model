SPDX-License-Identifier: Community-Spec-1.0

# standardAdditionTemplate

## Summary

Identifies the full text of a LicenseAddition, in SPDX templating format.

## Description

A standardAdditionTemplate contains a license addition template which describes
sections of the LicenseAddition text which can be varied.

See the Legacy Text Template format section of the
[SPDX License List Matching Guidelines](../../../annexes/license-matching-guidelines-and-templates.md)
for format information.

It is recommended to use [licenseXml](./licenseXml.md) instead, as it can
capture all the text and metadata associated with a license.

## Metadata

- name: standardAdditionTemplate
- Nature: DataProperty
- Range: xsd:string
