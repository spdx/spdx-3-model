SPDX-License-Identifier: Community-Spec-1.0

# ExternalMap

## Summary

A map of Element identifiers that are used within an SpdxDocument but defined
external to that SpdxDocument.

## Description

An external map is a map of Element identifiers that are used within an
SpdxDocument but defined external to that SpdxDocument.
The external map provides details about the externally-defined Element
such as its provenance, where to retrieve it, and how to verify its integrity.

## Metadata

- name: ExternalMap
- SubclassOf: none
- Instantiability: Concrete

## Properties

- externalSpdxId
  - type: xsd:anyURI
  - minCount: 1
  - maxCount: 1
- verifiedUsing
  - type: IntegrityMethod
- locationHint
  - type: xsd:anyURI
  - maxCount: 1
- definingArtifact
  - type: Artifact
  - maxCount: 1

## Summary @zh-Hans

在`SpdxDocument`中使用但在`SpdxDocument`外部定义的`Element`标识符的映射。

## Description @zh-Hans

`ExternalMap`是在`SpdxDocument`中使用但在`SpdxDocument`外部定义的`Element`标识符的映射。
`ExternalMap`提供了关于外部定义的`Element`的详细信息，例如其来源、如何检索它以及如何验证其完整性。
