SPDX-License-Identifier: Community-Spec-1.0

# CreationInfo

## Summary

Provides information about the creation of the Element.

## Description

The CreationInfo provides information about who created the Element, and when
and how it was created.

The dateTime created is often the date of last change
(e.g., a git commit date), not the date when the SPDX data was created, as
doing so supports reproducible builds.

## Metadata

- name: CreationInfo
- Instantiability: Concrete

## Properties

- specVersion
  - type: SemVer
  - minCount: 1
  - maxCount: 1
- comment
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- created
  - type: DateTime
  - minCount: 1
  - maxCount: 1
- createdBy
  - type: Agent
  - minCount: 1
- createdUsing
  - type: Tool
  - minCount: 0

## Summary @zh-Hans

提供有关`Element`创建的信息。

## Description @zh-Hans

`CreationInfo`提供有关`Element`的创建者、创建时间和创建方式的信息。

创建的`dateTime`通常是最后一次修改的日期（例如Git提交日期），而不是SPDX数据创建的日期。这样能够支持可重复构建。
