SPDX-License-Identifier: Community-Spec-1.0

# WithAdditionOperator

## Summary

Portion of an AnyLicenseInfo representing a License which has additional
text applied to it.

## Description

A WithAdditionOperator indicates that the designated License is subject to the
designated LicenseAddition, which can be a license exception on the
[SPDX License Exceptions](https://spdx.org/licenses/exceptions-index.html)
(ListedLicenseException) or may be other additional text
(CustomLicenseAddition). It is represented in the SPDX License Expression
Syntax by the `WITH` operator.

## Metadata

- name: WithAdditionOperator
- SubclassOf: /SimpleLicensing/AnyLicenseInfo
- Instantiability: Concrete

## Properties

- subjectAddition
  - type: LicenseAddition
  - minCount: 1
  - maxCount: 1
- subjectExtendableLicense
  - type: ExtendableLicense
  - minCount: 1
  - maxCount: 1

## Summary @zh-Hans

`AnyLicenseInfo`的一部分，表示`License`, 其中应用了附加文本。

## Description @zh-Hans

附加信息操作符（`WithAdditionOperator`）表示指定的`License`受限于指定的许可证附加信息（`LicenseAddition`），可能是[SPDX License Exceptions](https://spdx.org/licenses/exceptions-index.html)中列出的许可证例外情况（已列许可证例外情况`ListedLicenseException`），或可能是其他附加文本（自定义许可证附加信息`CustomLicenseAddition`）。在SPDX许可证表达式语法中通过`WITH`运算符表示。
