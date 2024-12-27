SPDX-License-Identifier: Community-Spec-1.0

# Build

## Summary

Class that describes a build instance of software/artifacts.

## Description

A build is a representation of the process in which a piece of software or
artifact is built. It encapsulates information related to a build process and
provides an element from which relationships can be created to describe the
build's inputs, outputs, and related entities (e.g. builders, identities,
etc.).

ExternalIdentifier of type "urlScheme" may be used to identify build logs.
In this case, the comment of the ExternalIdentifier should be "LogReference".

Note that buildStartTime and buildEndTime are optional, and may be omitted to
simplify creating reproducible builds.

## Metadata

- name: Build
- SubclassOf: /Core/Element
- Instantiability: Concrete

## Properties

- buildType
  - type: xsd:anyURI
  - minCount: 1
  - maxCount: 1
- buildId
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- configSourceEntrypoint
  - type: xsd:string
  - minCount: 0
- configSourceUri
  - type: xsd:anyURI
  - minCount: 0
- configSourceDigest
  - type: /Core/Hash
  - minCount: 0
- parameter
  - type: /Core/DictionaryEntry
  - minCount: 0
- buildStartTime
  - type: /Core/DateTime
  - minCount: 0
  - maxCount: 1
- buildEndTime
  - type: /Core/DateTime
  - minCount: 0
  - maxCount: 1
- environment
  - type: /Core/DictionaryEntry
  - minCount: 0

## Summary @zh-Hans

描述软件/工件构建实例的类。

## Description @zh-Hans

构建是软件或工件构建过程的体现。它封装了与构建过程相关的信息，并提供一个元素，可以从中创建关系来描述构建的输入、输出和相关实体（如构建者、身份等等）。

可以使用类型为 `urlScheme` 的 `ExternalIdentifier` 来标识构建日志。在这种情况下，`ExternalIdentifier` 的注释应该是 `LogReference`。

注意，`buildStartTime` 和 `buildEndTime` 是可选的，可以省略以简化可复现构建的创建。
