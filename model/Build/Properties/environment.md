SPDX-License-Identifier: Community-Spec-1.0

# environment

## Summary

Property describing the session in which a build is invoked.

## Description

environment is a map of environment variables and values that are set during a
build session, according to the buildType.

This is different from the [parameter](parameter.md) property in that it
describes the environment variables set before a build is invoked rather than
the variables provided to the builder.

## Metadata

- name: environment
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry

## Summary @zh-Hans

此属性描述调用构建的会话。

## Description @zh-Hans

`environment` 是在构建会话期间根据 `buildType` 设置的环境变量和值的映射。

这与 [`parameter`](parameter.md) 属性的不同之处在于，它描述的是在调用构建之前设置的环境变量，而不是提供给构建者的变量。
