SPDX-License-Identifier: Community-Spec-1.0

# ElementCollection

## Summary

A collection of Elements, not necessarily with unifying context.

## Description

An ElementCollection is a collection of Elements, not necessarily with unifying
context.

Note that all ElementCollections must conform to the Core profile even if the
Core profile is not specified in the profileConformance property.

If the profileConformance property is not provided, "core" is to be assumed as
the default.

*Constraints*

- If the ElementCollection has at least 1 element, it must also have at least
  1 rootElement.
- The element must not be of type SpdxDocument.
- The rootElement must not be of type SpdxDocument.

## Metadata

- name: ElementCollection
- SubclassOf: Element
- Instantiability: Abstract

## Properties

- element
  - type: Element
  - minCount: 0
- rootElement
  - type: Element
  - minCount: 0
- profileConformance
  - type: ProfileIdentifierType

## Summary @zh-Hans

`Element`的集合，不一定具有统一的上下文。

## Description @zh-Hans

`ElementCollection`是`Element`的集合，不一定具有统一的上下文。

需要注意的是，所有`ElementCollection`都必须符合`Core`配置，即使在`profileConformance`属性中未指定`core`配置。

如果未提供`profileConformance`属性，则`core`将作为默认值。

*约束条件*

- 如果`ElementCollection`至少有一个元素，那么它还必须至少有一个`rootElement`。
- `Element`不能是`SpdxDocument`类型。
- `rootElement`不能是`SpdxDocument`类型。
