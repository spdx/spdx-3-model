SPDX-License-Identifier: Community-Spec-1.0

# SimpleLicensing

## Summary

Additional metadata relating to software licensing.

## Description

The SimpleLicensing profile provides classes and properties to express licenses
as a [license expression](../../annexes/SPDX-license-expressions.md) string.

It also provides the base abstract class, AnyLicenseInfo, used for references
to license information.

The SimpleLicensingText class provides a place to record any license text found
that does not match a license on the
[SPDX License List](https://spdx.org/licenses/).

The ExpandedLicensing profile can be used to represent the complete parsed
license expressions.

## Metadata

- id: https://spdx.org/rdf/3.0.1/terms/SimpleLicensing
- name: SimpleLicensing
