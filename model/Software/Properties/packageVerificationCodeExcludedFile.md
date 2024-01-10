SPDX-License-Identifier: Community-Spec-1.0

# packageVerificationCodeExcludedFile

## Summary

Files which are excluded from the PackageVerificationCode integrity method.

## Description

Files which are excluded from the PackageVerificationCode integrity method.
See the PackageVerificationCode description for how this property is used in the integrity method algorithm.
The packageVerificationCodeExcludedFile is a relative filename with the root of the package archive or directory.

In general, every filename is preceded with a ./, see http://www.ietf.org/rfc/rfc3986.txt for syntax.

## Metadata

- name: packageVerificationCodeExcludedFile
- Nature: DataProperty
- Range: xsd:string
