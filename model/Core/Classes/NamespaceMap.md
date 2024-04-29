SPDX-License-Identifier: Community-Spec-1.0

# NamespaceMap

## Summary

A mapping between prefixes and namespace partial URIs.

## Description

A namespace map allows the creator of a collection of Elements that could be serialized to suggest 
a set of shorter identifiers ("prefixes") for particular namespace portions 
of ElementIDs to be used in SPDX content serialization in order to provide a more
human-readable and smaller serialized representation of the Elements.

For details of how NamespaceMap content is to be serialized please refer to general SPDX serialization guidance at https://spdx.github.io/spdx-3-model/serialization/readme.md and the various serialization format specific .md filed under https://spdx.github.io/spdx-3-model/serialization/ (TODO: update the URLs as soon as the context is publicly available)

Namespace maps support a variety of relevant use cases such as:

1) An SPDX content producer wishing to provide clarity of their serialization of an SPDX 2.X simple style collection where all content is newly minted and a single prefix-namespace is used.  The consumer of SPDX content wishes to preserve the name space mapping provided by such a producer.  In this case, the consumer would record the namespace map prefixes in the NamespaceMap such that subsequent serializations could reproduce the prefixes / namespaces in the native serialization format.

2) An SPDX content producer wishing to maintain consistent prefix use and understanding across multiple different serialization formats of the produced content.
   For example, an SBOM producer wishes to share/publish the SBOM as JSON-LD and XML. The producer can specify the preferred prefix mappings in the native serialization format using information from a single Namespacemap accessible local to the producer.

3) An SPDX content consumer/producer wishing to maintain consistent prefix use while round tripping from SPDX content received, deserialized, modified/extended in some way, and then reserialized in the same serialization form.
   In this case the prefix-namespace mappings utilized in the content are transformed from the original native namespace/prefix into the in memory NamespaceMap then transformed from the NamespaceMap back into the resultant serialization native namespace / prefix format.

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
