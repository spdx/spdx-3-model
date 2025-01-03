SPDX-License-Identifier: Community-Spec-1.0

# ExternalIdentifier

## Summary

A reference to a resource identifier defined outside the scope of SPDX-3.0 content that uniquely identifies an Element.

## Description

An ExternalIdentifier is a reference to a resource outside the scope of SPDX-3.0 content
that provides a unique key within an established domain that can uniquely identify an Element.

## Metadata

- name: ExternalIdentifier
- SubclassOf: none
- Instantiability: Concrete

## Properties

- externalIdentifierType
  - type: ExternalIdentifierType
  - minCount: 1
  - maxCount: 1
- identifier
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- comment
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- identifierLocator
  - type: xsd:anyURI
  - minCount: 0
- issuingAuthority
  - type: xsd:string
  - minCount: 0
  - maxCount: 1

## Summary @zh-Hans

SPDX 3.0内容范围之外定义的资源标识符的引用，唯一地标识一个`Element`。

## Description @zh-Hans

`ExternalIdentifier`是一个引用，指向一个在SPDX 3.0内容范围之外定义的资源，提供一个在特定领域内的唯一键，可以唯一标识一个`Element`。
