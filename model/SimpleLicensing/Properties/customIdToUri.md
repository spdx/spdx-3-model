SPDX-License-Identifier: Community-Spec-1.0

# customIdToUri

## Summary

**DEPRECATED in SPDX 3.1.**
Use [customIdToLicense](./customIdToLicense.md) instead.

Maps a "LicenseRef-" string for a custom license or a "AdditionRef-" string for
a custom license addition to its URI identifier.

**NOTE:**
This property is deprecated and only included for backward compatibility.
New documents should use [customIdToLicense](./customIdToLicense.md) instead.

## Description

Within a License Expression, references can be made to a Custom License or a
Custom License Addition.

The [License Expression syntax](../../../annexes/spdx-license-expressions.md)
dictates any reference starting with a
"LicenseRef-" or "AdditionRef-" refers to license or addition text not found in
the official [SPDX License List](https://spdx.org/licenses/).

These custom licenses shall be a CustomLicense, a CustomLicenseAddition, or a
SimpleLicensingText which are identified with a unique URI identifier.

The key for the DictionaryEntry is the string used in the license expression
and the value is the URI for the corresponding CustomLicense,
CustomLicenseAddition, or SimpleLicensingText.

## Metadata

- name: customIdToUri
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry
