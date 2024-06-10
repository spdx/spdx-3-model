SPDX-License-Identifier: Community-Spec-1.0

# licenseExpression

## Summary

A string in the license expression format.

## Description

A licenseExpression enables the representation, in a single string, of a
combination of one or more licenses, together with additions such as license
exceptions.

The syntax for a LicenseExpression string is set forth in the Annex D
of the SPDX Specification
(["SPDX license expressions"](../../../annexes/SPDX-license-expressions.md)).
A LicenseExpression string is not valid if it does not conform to the grammar
set forth in that annex.

The ExpandedLicensing profile can be used to represent the complete parsed
license expression as a combination of license objects.

## Metadata

- name: licenseExpression
- Nature: DataProperty
- Range: xsd:string
