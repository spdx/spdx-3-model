SPDX-License-Identifier: Community-Spec-1.0

# NamespaceMap

## Summary

A mapping between prefixes and namespace URIs.

## Description

A namespace map allows the creator of a collection of Elements to suggest 
a set of shorter identifiers ("prefixes") for particular namespace portions 
of ElementIDs to be used in SPDX content serialization in order to provide a more
human-readable and smaller serialized representation of the Elements.

The content of a namespace map are suggestions for consistency in serialization but are not normatively enforced.
When a serialization only contains the elements in "X", the collection content SHOULD (rather than MUST) utilize
the namespace map.
A serialization MAY choose to use the namespace map content.
A serialization MAY choose to use prefixes and namespaces other than the namespace map content.
A serialization MAY choose to use no prefixes at all and rather use the more verbose full ElementID IRIs.

If a serialization format supports prefixes or namespaces (e.g., JSON-LD context or XML XSD namespace), the namespace map
must be represented in that format "native" to the serialization.
If the serialization format does not support prefixes, then the full URI's for the elements must be used and the namespace map will not be preserved.
Any custom serialization format SHOULD implement namespaces in order to preserve the namespace map.

Namespace maps support a variety of relevant use cases such as:

1) An SPDX content producer wishing to provide clarity of their serialization of an SPDX 2.X simple style collection where all content is newly minted and a single prefix-namespace is used.  The consumer of SPDX content wishes to preserve the name space mapping provided by such a producer.  In this case, the consumer would record the namespace map prefixes in the NamespaceMap such that subsequent serializations could reproduce the prefixes / namespaces in the native serialization format.
2) An SPDX content producer wishing to maintain consistent prefix use and understanding across multiple different serialization formats of the produced content.
   For example, an SBOM producer wishes to share/publish the SBOM as JSON-LD, XML and YAML. The producer can specify the preferred prefix mappings in the native serialization format using information from a single Namespacemap accessible local to the producer.
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
