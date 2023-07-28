SPDX-License-Identifier: Community-Spec-1.0

# customIdToUri

## Summary

Maps a LicenseRef or AdditionRef string for a Custom License or a Custom License Addition to its URI ID.

## Description

Within a License Expression, references can be made to a Custom License or a Custom License Addition.
The License Expression syntax dictates any refence starting with a "LicenseRef-" or "AdditionRef-" refers to license or addition text not found in the SPDX list of licenses.
These custom licenses must be a CustomLicense, a CustomLicenseAddtion, or a SimpleLicensingText which are identified with a unique URI identifier.
The key for the DictionaryEntry is the string used in the license expression and the value is the URI for the corrosponding CustomLicense, CustomLicenseAddition, or SimpleLicensingText.


## Metadata

- name: customIdToUri
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry
