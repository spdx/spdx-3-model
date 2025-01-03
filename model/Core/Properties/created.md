SPDX-License-Identifier: Community-Spec-1.0

# created

## Summary

Identifies when the Element was originally created.

## Description

Created is a date that identifies when the Element was originally created.

The time stamp can serve as an indication as to whether the analysis needs to
be updated.

This is often the date of last change (e.g., a git commit date), not the date
when the SPDX data was created, as doing so supports reproducible builds.

## Metadata

- name: created
- Nature: DataProperty
- Range: DateTime

## Summary @zh-Hans

标识`Element`最初创建的时间。

## Description @zh-Hans

`created`是一个日期，用于标识`Element`最初创建的时间。

此时间戳可以用于指示分析是否需要更新。

`created`通常是最后一次修改的日期（例如Git提交日期），而不是SPDX数据创建的日期。这样能够支持可重复构建。
