SPDX-License-Identifier: Community-Spec-1.0

# isDeprecatedAdditionId

## Summary

Specifies whether an additional text identifier has been marked as deprecated.

## Description

The isDeprecatedAdditionId property specifies whether an identifier for a
LicenseAddition has been marked as deprecated. If the property is not defined,
then it is presumed to be false (i.e., not deprecated).

If the LicenseAddition is included on the
[SPDX License Exceptions](https://spdx.org/licenses/exceptions-index.html),
then the `deprecatedVersion` property indicates on which version release of the
Exceptions List it was first marked as deprecated.

"Deprecated" in this context refers to deprecating the use of the
_identifier_, not the underlying license addition. In other words, even if a
LicenseAddition's author or steward has stated that a particular
LicenseAddition generally should not be used, that would _not_ mean that the
LicenseAddition's identifier is "deprecated." Rather, a LicenseAddition
operator is typically marked as "deprecated" when it is determined that use of
another identifier is preferable.

## Metadata

- name: isDeprecatedAdditionId
- Nature: DataProperty
- Range: xsd:boolean
