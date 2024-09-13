SPDX-License-Identifier: Community-Spec-1.0

# NoneElement

## Summary

An Individual Value for Element representing a set of Elements with
cardinality (number/count) of zero.

## Description

NoneLicenseElement should be used if the SPDX creator desires to assert that
there are NO elements for the given context of use.

For example, a Relationship with
`relationshipType`="ancestorOf",
`from`=Element1,
and `to`=NoneElement
is explicitly expressing an assertion that
Element1 has no descendents.

## Metadata

- name: NoneElement
- type: Element
- IRI: https://spdx.org/rdf/3.0.1/terms/Core/None

## Property Values

- name: "NONE"
