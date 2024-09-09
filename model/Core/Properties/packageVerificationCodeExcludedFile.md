SPDX-License-Identifier: Community-Spec-1.0

# packageVerificationCodeExcludedFile

## Summary

The relative file name of a file to be excluded from the
`PackageVerificationCode`.

## Description

A relative filename with the root of the package archive or directory
referencing a file to be excluded from the `PackageVerificationCode`.

In general, every filename is preceded with a `./`, see
[RFC 3986 Uniform Resource Identifier (URI): Generic Syntax](https://datatracker.ietf.org/doc/rfc3986)
for syntax.

## Metadata

- name: packageVerificationCodeExcludedFile
- Nature: DataProperty
- Range: xsd:string
