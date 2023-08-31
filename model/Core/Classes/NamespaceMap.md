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
Any serialization of the collection content SHOULD (rather than MUST) utilize the namespace map content unless the single 
serialization payload is intended to contain multiple peer collections each with their own namespace map.
In this case the serializer MUST do one of the following:
1) Diverge from the exact provided namespace mappings and utilize deconflicted mappings where appropriate.
   This could be fully new prefix mappings as if the suggested namespace maps had not been provided.
3) Use full ElementID IRIs instead of prefixed ElementID IRIs.


Namespace maps support a variety of relevant use cases such as:

1) An SPDX content producer wishing to provide clarity of their serialization of an SPDX 2.X simple style collection where all content is newly minted and a single prefix-namespace is used.
2) An SPDX content producer wishing to maintain consistent prefix use and understanding across multiple different serializations of the produced content.
   For example, an SBOM producer wishes to share/publish the SBOM as json-ld, XML and YAML. The producer can specify the preferred prefix mappings they plan to use in all serializations, maintain usage consistency themselves across those serializations and provide clarity to the consumer of the SBOM in any of those serializations independent of which serialization form was received.
3) An SPDX content consumer/producer wishing to maintain consistent prefix use while round tripping from SPDX content received, deserialized, modified/extended in some way, and then reserialized in the same serialization form.
   In this case the prefix-namespace mappings utilized in the content are preserved across serializations as native SPDX content. 
4) An SPDX content consumer/producer wishing to maintain consistent prefix use while trans-serializing SPDX content received in one serialization form, deserialized, and then reserialized into a different serialization form.
   In this case the prefix-namespace mappings utilized in the content are preserved across serializations as native SPDX content. 
5) An SPDX content producer wishing to serialize/share together multiple collections of SPDX content each with their own namespace map in a way any consumer of the content would be able to separate out the multiple collections including their namespace map suggestions.
   This would involve the conflicted mappings issue briefly characterized above this list of use cases.
6) An SPDX content consumer wishing to maintain consistent prefix use while receiving serialized content that does not include a namespace map but does utilize prefixes, and at some future point reserializing that content.
   The consumer can simply "wrap" the received content in a collection with a namespace map and specify the prefix to namespace mappings that were actually implemented in the received content.
7) It should be possible to derive and maintain namespace mapping provenance for content.

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
