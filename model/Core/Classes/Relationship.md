SPDX-License-Identifier: Community-Spec-1.0

# Relationship

## Summary

Describes a relationship between one or more elements.

## Description

A Relationship is a grouping of characteristics unique to an assertion
that one Element is related to one or more other Elements in some way.

To explicitly assert that no such relationships exist, the `to` property
should contain the NoneElement individual and no other elements.

A relationship that contains NoneElement and additional elements in the `to`
property is not valid.

To explicitly assert that no assertions are being made regarding the
existence of such relationships, the `to` property should contain the
NoAssertionElement individual.

## Metadata

- name: Relationship
- SubclassOf: Element
- Instantiability: Concrete

## Properties

- from
  - type: Element
  - minCount: 1
  - maxCount: 1
- to
  - type: Element
  - minCount: 1
- relationshipType
  - type: RelationshipType
  - minCount: 1
  - maxCount: 1
- completeness
  - type: RelationshipCompleteness
  - minCount: 0
  - maxCount: 1
- startTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1
- endTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1

## Summary @zh-Hans

描述一个或多个元素之间的关系。

## Description @zh-Hans

`Relationship`是一组特征，独特地断言一个`Element`以某种方式与一个或多个其他`Element`相关。

若要明确断言不存在这种关系，`to`属性应包含'NONE'个体而不包含其他元素。

在`to`属性中包含'NONE'和其他元素的`Relationship`是无效的。

若要明确断言不对这种关系的存在进行任何断言，则`to`属性应包含'NOASSERTION'个体。
