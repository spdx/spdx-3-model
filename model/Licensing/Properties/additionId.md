SPDX-License-Identifier: Community-Spec-1.0

# additionId

## Summary

Provides a short, unique identifier to refer to a LicenseAddition.

## Description

An additionId contains a human-readable, short-form identifier for a
LicenseAddition. It may only include letters, numbers, period (".") and
hyphen ("-") characters.

For a ListedLicenseException, the licenseId will be as specified on the
[SPDX Exceptions List](https://spdx.org/licenses/exceptions-index.html) for the
particular exception.

For a CustomLicenseAddition, the short-form identifier must begin with the
prefix `AdditionRef-` and must be unique within the applicable SPDX namespace.
The short-form identifier may be preceded by an SPDX namespace or a
fully-qualified URI prefix.

## Metadata

- name: additionId
- Nature: DataProperty
- Range: xsd:string

