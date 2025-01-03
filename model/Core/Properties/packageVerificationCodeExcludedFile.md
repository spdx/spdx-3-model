SPDX-License-Identifier: Community-Spec-1.0

# packageVerificationCodeExcludedFile

## Summary

The relative file name of a file to be excluded from the
`PackageVerificationCode`.

## Description

A relative filename with the root of the package archive or directory
referencing a file to be excluded from the `PackageVerificationCode`.

Every filename is preceded with a `./`.

## Metadata

- name: packageVerificationCodeExcludedFile
- Nature: DataProperty
- Range: xsd:string

## Summary @zh-Hans

要从`PackageVerificationCode`中排除的文件的相对文件名。

## Description @zh-Hans

相对于包归档或目录的根目录的文件名，用于引用要从`PackageVerificationCode`中排除的文件。

通常，每个文件名前面都会加上`./`。关于语法，详见[RFC 3986统一资源标识符（URI）：通用语法](https://datatracker.ietf.org/doc/rfc3986/)。
