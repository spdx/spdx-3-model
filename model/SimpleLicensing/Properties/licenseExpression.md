SPDX-License-Identifier: Community-Spec-1.0

# licenseExpression

## Summary

A string in the license expression format.

## Description

A licenseExpression enables the representation, in a single string, of a
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

- name: licenseExpression
- Nature: DataProperty
- Range: xsd:string

## Summary @zh-Hans

许可证表达式格式的字符串。

## Description @zh-Hans

许可证表达式（`licenseExpression`）可在单个字符串中表示一个或多个许可证的组合，以及许可证例外情况等附加内容。

许可证表达式（`licenseExpression`）字符串的语法在本规范的相应附件（["SPDX 许可证表达式”](../../../annexes/spdx-license-expressions.md)）中规定。如果一个许可证表达式（`licenseExpression`）字符串不符合该附件中规定的语法，则该字符串无效。

`ExpandedLicensing`配置文件可用于将完整解析的许可证表达式表示为许可证对象的组合。
