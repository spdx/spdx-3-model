SPDX-License-Identifier: Community-Spec-1.0

# Element

## Summary

Base domain class from which all other SPDX-3.0 domain classes derive.

## Description

An Element is a representation of a fundamental concept either directly inherent
to the Bill of Materials (BOM) domain or indirectly related to the BOM domain
and necessary for contextually characterizing BOM concepts and relationships.
Within SPDX-3.0 structure this is the base class acting as a consistent,
unifying, and interoperable foundation for all explicit
and inter-relatable content objects.

## Metadata

- name: Element
- SubclassOf: none
- Instantiability: Abstract

## Properties

- spdxId
  - type: xsd:anyURI
  - minCount: 1
  - maxCount: 1
- name
  - type: xsd:string
  - maxCount: 1
- summary
  - type: xsd:string
  - maxCount: 1
- description
  - type: xsd:string
  - maxCount: 1
- comment
  - type: xsd:string
  - maxCount: 1
- creationInfo
  - type: CreationInfo
  - minCount: 1
  - maxCount: 1
- verifiedUsing
  - type: IntegrityMethod
- externalRef
  - type: ExternalRef
  - minCount: 0
- externalIdentifier
  - type: ExternalIdentifier
  - minCount: 0
- extension
  - type: /Extension/Extension
  - minCount: 0

## Summary @zh-Hans

派生所有其他SPDX 3.0域类的基础域类。

## Description @zh-Hans

`Element`是一个基本概念的表示，它可以直接与物料清单（BOM）域相关，也可以与BOM域间接相关，是在上下文中表征BOM概念和关系所必需的。
在SPDX 3.0结构中，`Element`是作为所有显式和相互关联的内容对象的一致、统一和互操作基础的基类。
