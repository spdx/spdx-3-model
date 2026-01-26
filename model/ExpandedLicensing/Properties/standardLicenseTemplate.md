SPDX-License-Identifier: Community-Spec-1.0

# standardLicenseTemplate

## Summary

Identifies the full text of a License, in SPDX templating format.

## Description

A standardLicenseTemplate contains a license template which describes sections
of the License text which can be varied.

See the Legacy Text Template format section of the
[SPDX License List Matching Guidelines](../../../annexes/license-matching-guidelines-and-templates.md)
for format information.

It is recommended to use [licenseXml](./licenseXml.md) instead, as it can
capture all the text and metadata associated with a license.

## Metadata

- name: standardLicenseTemplate
- Nature: DataProperty
- Range: xsd:string
