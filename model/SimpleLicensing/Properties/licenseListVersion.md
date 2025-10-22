SPDX-License-Identifier: Community-Spec-1.0

# licenseListVersion

## Summary

The version of the SPDX License List used in the license expression.

## Description

Recognizing that licenses are added to the
[SPDX License List](https://spdx.org/licenses/) with each
subsequent version, the intent is to provide consumers with the version of the
SPDX License List used.

This anticipates that in the future, license expression can used a
version of the SPDX License List that is older than the then current one.

The specified version of the SPDX License List shall include all listed licenses
and exceptions referenced in the expression.

## Metadata

- name: licenseListVersion
- Nature: DataProperty
- Range: /Core/SemVer

## Summary @zh-Hans

许可证表达式中使用的SPDX许可证列表版本。

## Description @zh-Hans

由于[SPDX许可证列表](https://spdx.org/licenses/)会随着每个后续版本的增加而增补，因此需要向消费者提供所使用的SPDX许可证列表版本。

这样做的目的是为了避免将来许可表达使用的SPDX许可列表版本早于当前版本。

指定版本的SPDX许可证列表必须包括表达式中引用的所有列出的许可证和例外情况。
