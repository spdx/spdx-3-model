SPDX-License-Identifier: Community-Spec-1.0

# IntegrityMethod

## Summary

Provides an independently reproducible mechanism that permits verification of a specific Element.

## Description

An IntegrityMethod provides an independently reproducible mechanism that permits verification
of a specific Element that correlates to the data in this SPDX document. This identifier enables
a recipient to determine if anything in the original Element has been changed and eliminates
confusion over which version or modification of a specific Element is referenced.

Please note that different profiles may also provide additional methods for verifying the integrity of specific subclasses of Elements.

## Metadata

- name: IntegrityMethod
- Instantiability: Abstract

## Properties

- comment
  - type: xsd:string
  - maxCount: 1

## Summary @zh-Hans

提供一个独立可复现的机制，允许验证特定的`Element`。

## Description @zh-Hans

`IntegrityMethod`提供一个独立可复现的机制，允许验证与此SPDX文档中数据相关的特定`Element`。这一标识符使接收方能够确定原始`Element`是否有任何更改，并消除对特定`Element`的哪个版本或修改项被引用的困惑。

请注意，其他配置文件可能还会提供额外的方法用于验证特定`Element`子类的完整性。

