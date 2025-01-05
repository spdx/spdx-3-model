SPDX-License-Identifier: Community-Spec-1.0

# NamespaceMap

## Summary

A mapping between prefixes and namespace partial URIs.

## Description

A namespace map allows the creator of a collection of serializable Elements
to suggest shorter identifiers ("prefixes") for specific namespace portions
of Element IDs. This map is used in SPDX content serialization to provide
a more human-readable and smaller serialized representation of the Elements.

For details of how NamespaceMap content is to be serialized please refer to
the [Model and serializations](../../../serializations.md) clause
and the various serialization format-specific files within the
[spdx-3-model repository](https://github.com/spdx/spdx-3-model/tree/main/serialization).

Namespace maps support a variety of relevant use cases such as:

1. An SPDX content producer wishing to provide clarity of their serialization
    of an SPDX 2.X simple style collection where all content is newly minted
    and a single prefix-namespace is used. The consumer of SPDX content wishes
    to preserve the name space mapping provided by such a producer.

    In this case, the consumer would record the namespace map prefixes in the
    NamespaceMap such that subsequent serializations could reproduce the
    prefixes / namespaces in the native serialization format.

2. An SPDX content producer wishing to maintain consistent prefix use and
    understanding across multiple different serialization formats of the
    produced content.
  
    For example, an SBOM producer wishes to share/publish the SBOM as JSON-LD
    and XML. The producer can specify the preferred prefix mappings in the
    native serialization format using information from a single NamespaceMap
    accessible local to the producer.

3. An SPDX content consumer/producer wishing to maintain consistent prefix use
    while round tripping from SPDX content received, deserialized,
    modified/extended in some way, and then reserialized in the same
    serialization form.

    In this case the prefix-namespace mappings utilized in the content are
    transformed from the original native namespace/prefix into the in memory
    NamespaceMap then transformed from the NamespaceMap back into the resultant
    serialization native namespace / prefix format.

## Metadata

- name: NamespaceMap
- Instantiability: Concrete

## Properties

- prefix
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- namespace
  - type: xsd:anyURI
  - minCount: 1
  - maxCount: 1

## Summary @zh-Hans

前缀和命名空间部分URI之间的映射。

## Description @zh-Hans

`NamespaceMap`允许可序列化`Element`集合的创建者为`Element` ID的特定命名空间部分建议更短的标识符（前缀）。此映射在SPDX内容序列化中使用，提供更易读和更精简的`Element`序列化表示。

有关如何序列化`NamespaceMap`内容的详细信息，请参阅[模型和序列化](../../../serializations.md)以及[spdx-3-model存储库](https://github.com/spdx/spdx-3-model/tree/main/serialization)中各种序列化格式的文件。

`NamespaceMap`支持各种相关的用例，例如：

1. SPDX内容生产者希望使其SPDX 2.X简单样式集合的序列化清晰明确，其中所有内容都是新生成的，并且使用单一前缀-命名空间。SPDX内容消费者希望保留此类生产者提供的`NamespaceMap`。

    在这种情况下，消费者可以记录`NamespaceMap`中的前缀，以便后续序列化使用原生序列化格式复现前缀/命名空间。

2. SPDX内容生产者希望在生成内容的多种不同序列化格式中保持前缀使用和理解的一致性。

    例如，SBOM生产者希望以JSON-LD和XML格式共享/发布SBOM。该生产者可以使用从单个`NamespaceMap`中获取并在本地可访问的信息，以原生序列化格式指定首选前缀映射。

3. SPDX内容消费者/生产者希望在接收到的SPDX内容经过反序列化、以某种方式修改/扩展并以相同的序列化形式重新序列化的过程中，保持前缀使用的一致性。

    在这种情况下，内容中使用的前缀-命名空间映射从原始的原生命名空间/前缀格式转化为内存中的`NamespaceMap`，然后再从`NamespaceMap`转化为生成后的序列化原生命名空间/前缀格式。
