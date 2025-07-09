SPDX-License-Identifier: Community-Spec-1.0

# Lite

## Summary

The SPDX Lite profile defines a simple view of SPDX data,
from the point of view of use cases in some industries.

## Description

The SPDX Lite profile consists of mandatory and recommended information.

The mandatory data in SPDX Lite is basic but useful for complying with licenses.
It is easy to understand licensing information by reading an SPDX Lite file.

SPDX Lite aims at a balance between the full SPDX data model and actual workflows in some industries.

An SPDX Lite document can also be used in parallel with other SPDX documents in software supply chains.

## Metadata

- id: https://spdx.org/rdf/3.0.1/terms/Lite
- name: Lite

## Profile conformance

In addition to the following mandatory requirements,
please refer to the corresponding Annex for elements
that should be included as part of a document conforming to the Lite profile.

For a `/Software/Package` to be conformant with this profile, the following has to hold:

1. The minCount for `copyrightText` is 1
2. The minCount for `packageVersion` is 1
3. The minCount for `suppliedBy` is 1
4. At least one of `downloadLocation` or `packageUrl` must be present

Additionally:

1. for every `/Software/Package` there MUST exist exactly one
   `/Core/Relationship` of type `hasConcludedLicense` having that element as
   its `from` property and a `/SimpleLicensing/AnyLicenseInfo` as its `to`
   property.
2. for every `/Software/Package` there MUST exist exactly one
   `/Core/Relationship` of type `hasDeclaredLicense` having that element as its
   `from` property and a `/SimpleLicensing/AnyLicenseInfo` as its `to`
   property.

For a `/Core/SpdxDocument` to be conformant with this profile, the following has to hold:

1. The minCount for `element` is 1
2. The minCount for `rootElement` is 1

For a `/Software/Sbom` to be conformant with this profile, the following has to hold:

1. The minCount for `element` is 1
2. The minCount for `rootElement` is 1

Finally, for a `/Core/Agent` to be conformant with this profile, the following has to hold:

1. The minCount for `name` is 1

## Summary @zh-Hans

SPDX Lite（SPDX 轻量版）配置文件从某些行业用例的角度定义了 SPDX 数据的简要视图。

## Description @zh-Hans

SPDX `Lite` 配置文件包括强制性和建议性信息。

SPDX `Lite` 中的强制性信息是基础性的，但有助于遵守许可证。
通过阅读 SPDX `Lite` 文件，可以轻松理解许可证信息。

SPDX `Lite` 力求在全量 SPDX 数据模型和某些行业的实际工作流程之间寻求一种平衡。

SPDX `Lite` 文档可以在软件供应链中与其他 SPDX 文档并行使用。

## Profile conformance @zh-Hans

除了以下强制性信息外，请参考相应的附录，了解符合 Lite 配置文件的文档应包含的元素。

一个 `/Software/Package` 类要符合此配置文件，必须满足以下条件：

1. `copyrightText` 的 `minCount` 为 1。
2. `packageVersion` 的 `minCount` 为 1。
3. `suppliedBy` 的 `minCount` 为 1。
4. 必须至少存在一个 `downloadLocation` 或 `packageUrl`。

此外：

1. 对于每个 `/Software/Package`，必须存在一个 `/Core/Relationship`，其类型为 `hasConcludedLicense`，该元素作为其 `from` 属性，`/SimpleLicensing/AnyLicenseInfo` 作为其 `to` 属性。
2. 对于每个 `/Software/Package`，必须存在一个 `/Core/Relationship`，其类型为 `hasDeclaredLicense`，该元素作为其 `from` 属性，`/SimpleLicensing/AnyLicenseInfo` 作为其 `to` 属性。

一个 `/Core/SpdxDocument` 类要符合这个配置文件，必须满足以下条件：

1. `element` 的 `minCount` 为 1。
2. `rootElement` 的 `minCount` 为 1。

一个 `/Software/Sbom` 类要符合这个配置文件，必须满足以下条件：

1. `element` 的 `minCount` 为 1。
2. `rootElement` 的 `minCount` 为 1。

最后，一个 `/Core/Agent` 类要符合这个配置文件，必须满足以下条件：

1. `name` 的 `minCount` 为 1。
