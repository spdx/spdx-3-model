SPDX-License-Identifier: Community-Spec-1.0

# customIdToLicense

## Summary

Maps a "LicenseRef-" string for a custom license or a "AdditionRef-" string for
a custom license addition to a `CustomLicense`, a `CustomLicenseAddition`, or a
`SimpleLicensingText`.

## Description

Within a license expression, references can be made to a custom license or a
custom license addition.

The [License Expression syntax](../../../annexes/spdx-license-expressions.md)
dictates any reference starting with a
"LicenseRef-" or "AdditionRef-" refers to license or addition text not found in
the official [SPDX License List](https://spdx.org/licenses/).

The key for the ElementMap is the string used in the license expression
and the elementValue is target Element, which must be a CustomLicense,
CustomLicenseAddition, or SimpleLicensingText.

The key for the ElementMap shall be matched against the license expression
in a case-insensitive manner.
This is required because the entire license expression string is itself
case-insensitive.

## Metadata

- name: customIdToLicense
- Nature: ObjectProperty
- Range: /Core/ElementMap
