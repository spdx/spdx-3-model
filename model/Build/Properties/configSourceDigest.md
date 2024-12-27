SPDX-License-Identifier: Community-Spec-1.0

# configSourceDigest

## Summary

Property that describes the digest of the build configuration file used to
invoke a build.

## Description

configSourceDigest is the checksum of the build configuration file used by a
builder to execute a build, according to the buildType.

This Property uses the Core model's [Hash](../../Core/Classes/Hash.md) class.

## Metadata

- name: configSourceDigest
- Nature: ObjectProperty
- Range: /Core/Hash

## Summary @zh-Hans

此属性用于描述调用构建时所使用的构建配置文件的摘要。

## Description @zh-Hans

`configSourceDigest` 是构建者根据 `buildType` 执行构建时使用的构建配置文件的校验和。

这个属性使用了 `Core` 模型的 [`Hash`](../../Core/Classes/Hash.md) 类。
