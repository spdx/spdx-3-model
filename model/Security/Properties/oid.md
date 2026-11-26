SPDX-License-Identifier: Community-Spec-1.0

# oid

## Summary

The Object Identifier (OID) that uniquely identifies the extension type.

## Description

This property holds the registered Object Identifier (OID) string that uniquely identifies the type or purpose of a certificate extension. OIDs are hierarchical numeric identifiers (e.g., '2.5.29.15' for Key Usage) assigned by standardization bodies or organizations.

For standard X.509 extensions, this OID corresponds to a well-known value; for custom extensions, it is a unique identifier registered within an organization's OID arc. This property enables precise, machine-readable identification of the extension beyond any human-readable name.

## Metadata

- name: oid
- Nature: DataProperty
- Range: xsd:string
