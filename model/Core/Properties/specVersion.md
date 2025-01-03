SPDX-License-Identifier: Community-Spec-1.0

# specVersion

## Summary

Provides a reference number that can be used to understand how to parse and
interpret an Element.

## Description

The specVersion provides a reference number that can be used to understand how
to parse and interpret an Element.
It will enable both future changes to the specification and to support backward
compatibility.

The major version number shall be incremented when incompatible changes between
versions are made (one or more sections are created, modified or deleted).
The minor version number shall be incremented when backwards compatible changes
are made.
The patch version number shall be incremented when backward compatible bug
fixes are made.

Here, parties exchanging information in accordance with the SPDX specification
need to provide 100% transparency as to which SPDX specification version such
information is conforming to.

## Metadata

- name: specVersion
- Nature: DataProperty
- Range: SemVer

## Summary @zh-Hans

提供参考编号，用于理解如何解析和解释一个`Element`。

## Description @zh-Hans

`specVersion`提供参考编号，用于理解如何解析和解释一个`Element`。
它将允许将来对规范进行更改，并保持向后兼容性。

当版本之间存在不兼容的更改（一个或多个部分被创建、修改或删除）时，应增加主版本号。
当进行向后兼容的更改时，应增加次版本号。
当进行向后兼容的错误修复时，应增加修补版本号。

在此，根据SPDX规范交换信息的各方需要提供100%透明度，以明确该信息遵循哪一个SPDX规范版本。
