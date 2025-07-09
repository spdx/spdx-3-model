SPDX-License-Identifier: Community-Spec-1.0

# Dataset

## Summary

The Dataset Profile provides additional metadata, based on Software Profile,
that is useful for datasets.

## Description

The Dataset namespace defines concepts related to dataset, including its
preparation process, its characteristics, and its access methods.

## Metadata

- id: https://spdx.org/rdf/3.0.1/terms/Dataset
- name: Dataset

## Profile conformance

For an element collection to be conformant with this profile,
the following has to hold:

1. for every `/Dataset/DatasetPackage` there MUST exist exactly one
   `/Core/Relationship` of type `hasConcludedLicense` having that element as its
   `from` property and a `/SimpleLicensing/AnyLicenseInfo` as its `to`
    property.
2. for every `/Dataset/DatasetPackage` there MUST exist exactly one
   `/Core/Relationship` of type `hasDeclaredLicense` having that element as its
   `from` property and a `/SimpleLicensing/AnyLicenseInfo` as its `to`
    property.

## Summary @zh-Hans

`Dataset` 配置文件基于 `Software` 配置文件提供了对数据集有用的附加元数据。

## Description @zh-Hans

`Dataset` 命名空间定义了与数据集相关的概念，包括其准备流程、特征和访问方法。

## Profile conformance @zh-Hans

元素集合要符合这个配置文件，必须满足以下条件：

1. 每一个 `/Dataset/DatasetPackage` 必须存在一个类型为 `hasConcludedLicense`
   的 `/Core/Relationship` 元素，此元素作为它的 `from` 属性，
   `/SimpleLicensing/AnyLicenseInfo` 作为它的 `to` 属性。
2. 每一个 `/Dataset/DatasetPackage` 必须存在一个类型为 `hasDeclaredLicense`
   的 `/Core/Relationship` 元素，此元素作为它的 `from` 属性，
   `/SimpleLicensing/AnyLicenseInfo` 作为它的 `to` 属性。
