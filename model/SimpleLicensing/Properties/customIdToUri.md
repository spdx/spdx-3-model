SPDX-License-Identifier: Community-Spec-1.0

# customIdToUri

## Summary

Maps a LicenseRef or AdditionRef string for a Custom License or a Custom
License Addition to its URI ID.

## Description

Within a License Expression, references can be made to a Custom License or a
Custom License Addition.

The [License Expression syntax](../../../annexes/SPDX-license-expressions.md)
dictates any reference starting with a
"LicenseRef-" or "AdditionRef-" refers to license or addition text not found in
[the official SPDX License List](https://spdx.org/licenses/).

These custom licenses must be a CustomLicense, a CustomLicenseAddition, or a
SimpleLicensingText which are identified with a unique URI identifier.

The key for the DictionaryEntry is the string used in the license expression
and the value is the URI for the corresponding CustomLicense,
CustomLicenseAddition, or SimpleLicensingText.

## Metadata

- name: customIdToUri
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry
