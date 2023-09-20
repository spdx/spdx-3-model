SPDX-License-Identifier: Community-Spec-1.0

# X-Collection

## Summary

A collection of Elements that respresents a serialization of SPDX data.

## Description

The X-Collection provides a convenient way to store information about SPDX data which has been serialized as a complete
unit (e.g., all SPDX data within a single JSON-LD file).
Information we wish to preserve about the serialization itself are store as properties of this class.

NOTE: This class is not intended to be serialized within the SPDX data it is representing.  It can, however, be serialized in a subsequent serialization to communicate a prior serialization namespace.
It is intended to be utilized within a system to handle the following use cases:

1) An SPDX content producer wishing to provide clarity of their serialization of an SPDX 2.X simple style collection where all content is newly minted and a single prefix-namespace is used.  The consumer of SPDX content wishes to preserve the name space mapping provided by such a producer.  In this case, the consumer would record the namespace map prefixes in the NamespaceMap such that subsequent serializations could reproduce the prefixes / namespaces in the native serialization format.
2) An SPDX content producer wishing to maintain consistent prefix use and understanding across multiple different serialization formats of the produced content.
   For example, an SBOM producer wishes to share/publish the SBOM as JSON-LD and XML. The producer can specify the preferred prefix mappings in the native serialization format using the information from a single Namespace stored in memory.
3) An SPDX content consumer/producer wishing to maintain consistent prefix use while round tripping from SPDX content received, deserialized, modified/extended in some way, and then reserialized in the same serialization form.
   In this case the prefix-namespace mappings utilized in the content are transformed from the original native namespace/prefix into the in memory NamespaceMap then transformed from the NamespaceMap back into the resultant serialization native namespace / prefix format.


## Metadata

- name: X-collection
- SubclassOf: ElementCollection
- Instantiability: Concrete

## Properties

- namespaceMap
  - type: NamespaceMap
