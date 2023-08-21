SPDX-License-Identifier: Community-Spec-1.0

# namespaces

## Summary

Provides a NamespaceMap representing the NamespaceMap used for the original serialization of an SpdxDocument.

## Description

This field is used for providing the ability to reproduce an original serialization for a given SPDX Document, especially if the serialization format does not natively support namespace mapping.

This purely optional field is not intended for implementing or representing the NameSpaceMap for all serializations where this SPDX document may be found.

## Metadata

- name: originalNamespaces
- Nature: DataProperty
- Range: NamespaceMap

