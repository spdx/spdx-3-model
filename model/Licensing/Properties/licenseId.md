SPDX-License-Identifier: Community-Spec-1.0

# licenseId

## Summary

Provides a short, unique identifier to refer to a License.

## Description

A licenseId contains a human-readable, short-form license identifier for a
License. It may only include letters, numbers, period (".") and hyphen ("-")
characters.

For a ListedLicense, the licenseId will be as specified on the
[SPDX License List](https://spdx.org/licenses) for the particular license.

For a CustomLicense, the short-form license identifer must begin with the
prefix `LicenseRef-` and must be unique within the applicable SPDX namespace.
The short-form license ID may be preceded by an SPDX namespace or a
fully-qualified URI prefix.

## Metadata

- name: licenseId
- Nature: DataProperty
- Range: xsd:string
