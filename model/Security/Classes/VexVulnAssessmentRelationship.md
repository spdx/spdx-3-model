SPDX-License-Identifier: Community-Spec-1.0

# VexVulnAssessmentRelationship

## Summary

Abstract ancestor class for all VEX relationships

## Description

VexVulnAssessmentRelationship is an abstract subclass that defined the common
properties shared by all the SPDX-VEX status relationships.

*Constraints*

When linking elements using a VexVulnAssessmentRelationship, the following
requirements must be observed:

- The to: end must point to elements representing the VEX *products*.

To specify a different element where the vulnerability was detected, the VEX
relationship can optionally specify *subcomponents* using the assessedElement
property.

VEX inherits information from the document level down to its statements. When a
statement is missing information it can be completed by reading the equivalent
field from the containing document. For example, if a VEX relationship is
missing data in its createdBy property, tools must consider the entity
listed in the CreationInfo section of the document as the VEX author.
In the same way, when a VEX relationship does not have a created property,
the document's date must be considered as authoritative.

## Metadata

- name: VexVulnAssessmentRelationship
- SubclassOf: VulnAssessmentRelationship
- Instantiability: Abstract

## Properties

- vexVersion
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- statusNotes
  - type: xsd:string
  - minCount: 0
  - maxCount: 1

## Summary @zh-Hans

所有VEX关系的抽象祖先类。

## Description @zh-Hans

`VexVulnAssessmentRelationship`是一个抽象子类，定义了所有SPDX-VEX状态关系共享的公共属性。

*约束条件*

使用`VexVulnAssessmentRelationship`关联元素时，必须遵循以下要求：

- `from:`端必须为一个`/Security/Vulnerability`类型的元素。
- `to:`端必须指向表示VEX产品的元素。

要指定检测到漏洞的其他元素，VEX关系可以选择使用`assessedElement`属性指定子组件。

VEX从文档级别继承信息到其语句。当语句缺少信息时，可通过读取包含文档中的等效字段来补充。例如，如果VEX关系的`createdBy`属性中缺失数据，工具将文档`CreationInfo`部分中列出的实体视为VEX作者。同理，当VEX关系没有`created`属性时，文档的日期应被视为权威信息。
