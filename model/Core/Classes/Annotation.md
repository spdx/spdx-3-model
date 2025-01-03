SPDX-License-Identifier: Community-Spec-1.0

# Annotation

## Summary

An assertion made in relation to one or more elements.

## Description

An Annotation is an assertion made in relation to one or more elements.

The `contentType` property describes the format of the `statement` property.

## Metadata

- name: Annotation
- SubclassOf: Element
- Instantiability: Concrete

## Properties

- annotationType
  - type: AnnotationType
  - minCount: 1
  - maxCount: 1
- contentType
  - type: MediaType
  - minCount: 0
  - maxCount: 1
- statement
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- subject
  - type: Element
  - minCount: 1
  - maxCount: 1

## Summary @zh-Hans

对一个或多个元素断言。

## Description @zh-Hans

`Annotation`是对一个或多个元素的断言。

`contentType`属性描述了`statement`属性的格式。

