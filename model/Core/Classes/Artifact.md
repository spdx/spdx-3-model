SPDX-License-Identifier: Community-Spec-1.0

# Artifact

## Summary

A distinct article or unit within the digital domain.

## Description

An artifact is a distinct article or unit within the digital domain,
such as an electronic file, a software package, a device or an element of data.

## Metadata

- name: Artifact
- SubclassOf: Element
- Instantiability: Abstract

## Properties

- originatedBy
  - type: Agent
  - minCount: 0
- suppliedBy
  - type: Agent
  - minCount: 0
  - maxCount: 1
- builtTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1
- releaseTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1
- validUntilTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1
- standardName
  - type: xsd:string
  - minCount: 0
- supportLevel
  - type: SupportType
  - minCount: 0

## Summary @zh-Hans

数字领域内的特定文章或单位。

## Description @zh-Hans

`Artifact`是数字领域中的特定文章或单位，如电子文件、软件包、设备或数据元素。
