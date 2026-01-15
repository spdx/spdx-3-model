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

The key for the DictionaryEntry is the string used in the license expression
and the value is target Element, which must be a CustomLicense,
CustomLicenseAddition, or SimpleLicensingText.

## Metadata

- name: customIdToLicense
- Nature: ObjectProperty
- Range: /Core/ElementMap
