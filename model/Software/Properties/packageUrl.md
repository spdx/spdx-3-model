SPDX-License-Identifier: Community-Spec-1.0

# packageUrl

## Summary

Provides a place for the SPDX data creator to record the package URL string
(in accordance with the Package URL specification) for a software Package.

## Description

A package URL (commonly pronounced and referred to as "purl") is an attempt to standardize package representations
in order to reliably identify and locate software packages.
A packageUrl is a URL string which represents a package in a
mostly universal and uniform way across programming languages, package
managers, packaging conventions, tools, APIs and databases.

A packageUrl is composed of seven components:

```text
scheme:type/namespace/name@version?qualifiers#subpath
```

The definition for each component can be found in the corresponding
[Annex](../../../annexes/pkg-url-specification.md) of this document.
Known type definitions can be found in the
Package URL [type definitions](https://github.com/package-url/purl-spec/blob/b33dda1cf4515efa8eabbbe8e9b140950805f845/PURL-TYPES.rst).

Components are designed such that they form a hierarchy from the most
significant on the left to the least significant components on the right.

## Metadata

- name: packageUrl
- Nature: DataProperty
- Range: xsd:anyURI

## Summary @zh-Hans

为SPDX数据创建者提供了一个记录软件包的包URL字符串（按照包URL规范）的地方。

## Description @zh-Hans

包URL(`packageUrl`)（通常发音并被称为“purl”）是试图标准化包表示的方法，以便可靠地识别和定位软件包。

包URL是一个URL字符串，它以一种大致通用和统一的方式跨编程语言、包管理器、打包约定、工具、API和数据库来表示一个软件包。

包URL由七个组成部分构成：

```plain
scheme:type/namespace/name@version?qualifiers#subpath
```

每个组件的定义可以在本规范的相应附录([Annex](../../../annexes/pkg-url-specification.md))中找到。
已知类型的类型定义([type definitions](https://github.com/package-url/purl-spec/blob/b33dda1cf4515efa8eabbbe8e9b140950805f845/PURL-TYPES.rst))可以在包URL类型定义中找到。

组件的设计方式是，它们从最左边的最重要的组件到最右边的最不重要的组件形成一个层次结构。
