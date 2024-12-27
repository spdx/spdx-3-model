SPDX-License-Identifier: Community-Spec-1.0

# buildId

## Summary

A buildId is a locally unique identifier used by a builder to identify a unique
instance of a build produced by it.

## Description

A buildId is a locally unique identifier to identify a unique instance of a
build, according to the buildType.

This identifier differs based on build toolchain, platform, or naming
convention used by an organization or standard.

## Metadata

- name: buildId
- Nature: DataProperty
- Range: xsd:string

## Summary @zh-Hans

`buildId` 是本地唯一标识符，用于构建者标识其产生的唯一构建实例。

## Description @zh-Hans

`buildId` 是一个本地唯一标识符，根据 `buildType` 标识唯一构建实例。

这个标识符根据构建工具、平台或者一个组织或标准使用的命名规则，而有所不同。
