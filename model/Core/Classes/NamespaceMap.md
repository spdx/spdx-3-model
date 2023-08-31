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
Any serialization of the collection content SHOULD (rather than MUST) utilize the namespace map content.
A serialization MAY choose to use the namespace map content.
A serialization MAY choose to use prefixes and namespaces other than the namespace map content.
A serialization MAY choose to use no prefixes at all and rather use the more verbose full ElementID IRIs.

If utilized the namespace map set of prefixes and namespaces MUST be implemented in a given serialization 
form (e.g., json-ld or xml) as specified in the binding rules specification for that serialization and 
utilizing the appropriate inherent or custom specified mechanism for that serialization.
The namespace map itself is also conveyed as native SPDX content to support clarity, transparency and 
consistency independent of any particular serialization form.

A given serialization payload (whether file or streaming) MUST NOT contain multiple namespace maps with conflicting mappings.
If a serializer wishes to include in one payload multiple peer collections each with their own namespace map then the serializer 
MUST EITHER diverge from the exact mappings and utilize deconflicted mappings where appropriate OR must not utilize prefixes and use full ElementID IRIs instead.

Namespace maps support a variety of relevant use cases such as:

1) An SPDX content producer wishing to provide clarity of their serialization of an SPDX 2.X simple style collection where all content is newly minted and a single prefix-namespace is used.
2) An SPDX content producer wishing to maintain consistent prefix use across multiple different serializations of the produced content
   For example, an SBOM producer wishes to share/publish the SBOM as json-ld, XML and YAML. The producer can specify the preferred prefix mappings they plan to use in all serializations, maintain consistency themselves across those serializations and provide clarity to the consumer of the SBOM in any of those serializations.
3) An SPDX content consumer/producer wishing to maintain consistent prefix use while round tripping from SPDX content received, deserialized, modified/extended in some way, and then reserialized in the same serialization form.
   In this case the prefix-namespace mappings utilized in the content are preserved across serializations as native SPDX content.
5) An SPDX content consumer/producer wishing to maintain consistent prefix use while trans-serializing SPDX content received in one serialization form, deserialized, and then reserialized into a different serialization form.
   In this case the prefix-namespace mappings utilized in the content are preserved across serializations as native SPDX content.
7) An SPDX content consumer wishing to maintain consistent prefix use while receiving serialized content that does not include a namespace map but does utilize prefixes, and at some future point reserializing that content.
   The consumer can simply "wrap" the received content in a collection with a namespace map and specify the prefix to namespace mappings that were actually implemented in the received content.

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
