SPDX-License-Identifier: Community-Spec-1.0

# LiteRelationshipType

## Summary

Information about the relationship between two Elements.


## Description

Provides information about the relationship between two Elements.
For example, you can represent a relationship between two different Files,
between a Package and a File, between two Packages, or between one SPDXDocument and another SPDXDocument.


## Metadata

- name: LiteRelationshipType

## Entries
- contains: Every `to` Element is contained by the `from` Element
- describes: Every `to` Element is  described by the `from` Element.  This can be used to denote the root(s) of a tree of elements contained in an SBOM.

