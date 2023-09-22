SPDX-License-Identifier: Community-Spec-1.0

# NamespaceMap

## Summary

Defines equivalence between a prefix string and a namespace IRI

## Description

In the logical model all SpdxIds (Element unique identifiers) are full IRIs.  In serialized data these IRIs
can be decomposed into a namespace IRI followed by a local ID, and the namespace IRI replaced with a short
prefix string for brevity.  When parsing serialized data into Element values this mapping
is reversed, replacing prefix strings with namespace IRIs.

Example (from https://github.com/spdx/spdx-spec/blob/development/v2.3.1/examples/SPDXRdfExample-v2.3.spdx.rdf.xml):

The full IRI
"http://spdx.org/spdxdocs/spdx-example-444504E0-4F89-41D3-9A0C-0305E82C3301#SPDXRef-DoapSource"
can be decomposed into:

Namespace: "http://spdx.org/spdxdocs/spdx-example-444504E0-4F89-41D3-9A0C-0305E82C3301#"  
Local ID: "SPDXRef-DoapSource"

If NamespaceMap assigns the string "st" to this namespace, then the full IRI is serialized as "st:SPDXRef-DoapSource",
making the serialized data much more compact and readable.

## Metadata

- name: NamespaceMap
- SubclassOf: none
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
