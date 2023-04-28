SPDX-License-Identifier: Community-Spec-1.0

# isDeprecatedLicenseId

## Summary

Specifies whether a license or exception identifier has been marked as
deprecated.

## Description

The isDeprecatedLicenseId property specifies whether an identifier for a
License or LicenseException has been marked as deprecated. If the property
is not defined, then it is presumed to be false (i.e., not deprecated).

If the License or LicenseException is included on the SPDX License List, then
the `deprecatedVersion` property indicates on which version release of the
License List it was first marked as deprecated.

"Deprecated" in this context refers to deprecating the use of the
_identifier_, not the underlying license. In other words, even if a License's
author or steward has stated that a particular License generally should not be
used, that would _not_ mean that the License's identifier is "deprecated."
Rather, a License or LicenseException operator is typically marked as
"deprecated" when it is determined that use of another identifier is
preferable.

## Metadata

- name: isDeprecatedLicenseId
- Nature: DataProperty
- Range: xsd:boolean
