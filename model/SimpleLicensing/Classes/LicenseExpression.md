SPDX-License-Identifier: Community-Spec-1.0

# LicenseExpression

## Summary

An SPDX Element containing an SPDX license expression string.

## Description

A LicenseExpression enables the representation, in a single string, of a
combination of one or more licenses, together with additions such as license
exceptions.

The syntax for a licenseExpression string is set forth in the corresponding
Annex of this document
(["SPDX license expressions"](../../../annexes/spdx-license-expressions.md)).
A licenseExpression string is not valid if it does not conform to the grammar
set forth in that Annex.

The ExpandedLicensing profile can be used to represent the complete parsed
license expression as a combination of license objects.

## Metadata

- name: LicenseExpression
- SubclassOf: AnyLicenseInfo
- Instantiability: Concrete

## Properties

- licenseExpression
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- licenseListVersion
  - type: /Core/SemVer
  - maxCount: 1
- customIdToUri
  - type: /Core/DictionaryEntry
  - minCount: 0

## Summary @zh-Hans

一个包含SPDX许可证表达式字符串的SPDX元素。

## Description @zh-Hans

一个`LicenseExpression`可以在单个字符串中表示一个或多个许可证的组合，以及许可证例外情况等附加内容。

`licenseExpression`字符串的语法在本规范的相应附件（[“SPDX 许可证表达式”](../../../annexes/spdx-license-expressions.md)）中规定。如果一个`licenseExpression`字符串不符合该附件中规定的语法，则该字符串无效。

`ExpandedLicensing`配置文件可用于将完整解析的许可证表达式表示为许可证对象的组合。
