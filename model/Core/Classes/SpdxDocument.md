SPDX-License-Identifier: Community-Spec-1.0

# SpdxDocument

## Summary

A collection of SPDX Elements that could potentially be serialized.

## Description

The SpdxDocument provides a convenient way to express information about
collections of SPDX Elements that could potentially be serialized as complete
units (e.g., all in-scope SPDX data within a single JSON-LD file).

SpdxDocument is independent of any particular serialization format or instance.

Information we wish to preserve about a specific instance of serialization of
this SPDX content is NOT expressed using the SpdxDocument but rather using an
associated Artifact representing a particular instance of SPDX data physical
serialization.

Any instance of serialization of SPDX data MUST NOT contain more than one
SpdxDocument element definition.

## Metadata

- name: SpdxDocument
- SubclassOf: ElementCollection
- Instantiability: Concrete

## Properties

- import
  - type: ExternalMap
- namespaceMap
  - type: NamespaceMap
- dataLicense
  - type: /SimpleLicensing/AnyLicenseInfo
  - maxCount: 1

## Summary @zh-Hans

可序列化的SPDX `Element`的集合。

## Description @zh-Hans

`SpdxDocument`提供了一种便捷的方式来表达SPDX `Element`集合的信息，这些集合可以作为完整单元被序列化（例如，单个JSON-LD文件中的所有范围内的SPDX数据）。

`SpdxDocument`与任何特定的序列化格式或实例无关。

希望保留的关于该SPDX内容的特定序列化实例的信息不通过`SpdxDocument`表达，而是通过一个表示特定SPDX数据物理序列化实例的关联`Artifact`来表达。

任何SPDX数据的序列化实例都不得包含多个`SpdxDocument`元素定义。
