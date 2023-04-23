SPDX-License-Identifier: Community-Spec-1.0

# licenseId

## Summary

A licenseId provides a short, unique identifier to refer to a License or
LicenseException.

## Description

A licenseId contains a human-readable, short-form license identifier for a
License or LicenseException. It may include only letters, numbers, period
(".") and hyphen ("-") characters.

For a ListedLicense or ListedLicenseException, the licenseId will be as
specified on the [SPDX License List](https://spdx.org/licenses) for the
particular license or exception.

For a CustomLicense, the licenseId must begin with the prefix `LicenseRef-`
and must be unique within the applicable SPDX namespace.

When used within a license expression, the licenseId can optionally include
a reference to an external document in the form
`DocumentRef-[docrefIdString]:LicenseRef-[idString]`, where docRefIdString
is an spdxId for an external document reference.

## Metadata

- name: licenseId
- Nature: DataProperty
- Range: xsd:string
