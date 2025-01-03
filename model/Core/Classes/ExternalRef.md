SPDX-License-Identifier: Community-Spec-1.0

# ExternalRef

## Summary

A reference to a resource outside the scope of SPDX-3.0 content related to an Element.

## Description

An External Reference points to a general resource outside the scope of the SPDX-3.0 content
that provides additional context, characteristics or related information about an Element.

## Metadata

- name: ExternalRef
- SubclassOf: none
- Instantiability: Concrete

## Properties

- externalRefType
  - type: ExternalRefType
  - maxCount: 1
- locator
  - type: xsd:string
- contentType
  - type: MediaType
  - maxCount: 1
- comment
  - type: xsd:string
  - maxCount: 1

## Summary @zh-Hans

对SPDX 3.0内容范围之外与`Element`相关的资源的引用。

## Description @zh-Hans

`ExternalRef`指向SPDX 3.0内容范围之外的资源，提供关于`Element`的额外上下文、特征或相关信息。
