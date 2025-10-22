SPDX-License-Identifier: Community-Spec-1.0

# customIdToUri

## Summary

Maps a LicenseRef or AdditionRef string for a Custom License or a Custom
License Addition to its URI ID.

## Description

Within a License Expression, references can be made to a Custom License or a
Custom License Addition.

The [License Expression syntax](../../../annexes/spdx-license-expressions.md)
dictates any reference starting with a
"LicenseRef-" or "AdditionRef-" refers to license or addition text not found in
the official [SPDX License List](https://spdx.org/licenses/).

These custom licenses shall be a CustomLicense, a CustomLicenseAddition, or a
SimpleLicensingText which are identified with a unique URI identifier.

The key for the DictionaryEntry is the string used in the license expression
and the value is the URI for the corresponding CustomLicense,
CustomLicenseAddition, or SimpleLicensingText.

## Metadata

- name: customIdToUri
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry

## Summary @zh-Hans

将自定义许可证或自定义许可证附加信息的`LicenseRef`或`AdditionRef`字符串映射到其URI ID上。

## Description @zh-Hans

在许可证表达式中，可以引用自定义许可证或自定义许可证附加内容。

[License Expression syntax](https://github.com/spdx/spdx-3-model/blob/main/annexes/spdx-license-expressions.md)规定，任何以 “LicenseRef-”或 “AdditionRef-”开头的引用都是指官方[SPDX许可证列表](https://spdx.org/licenses/)中没有的许可证或附加内容。

这些自定义许可证必须是一个`CustomLicense`、`CustomLicenseAddition`或`SimpleLicensingText`，它们都有一个唯一的URI标识符。

`DictionaryEntry`的关键是许可证表达式中使用的字符串，值则是对应的`CustomLicense`、`CustomLicenseAddition`或`SimpleLicensingText`的URI。
