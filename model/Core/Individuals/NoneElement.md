SPDX-License-Identifier: Community-Spec-1.0

# NoneElement

## Summary

An Individual Value for Element representing a set of Elements with 
cardinality (number/count) of zero.

## Description

NoneLicenseElement should be used if the SPDX creator desires to assert that 
there are NO elements for the given context of use.

For example, a Relationship with `from`=Element1, `relationshipType`="ancestorOf", 
and `to`=NONE is explicitly expressing an assertion that Element1 has no descendents.

## Metadata

- name: NoneElement
- type: Element

## Property Values

- name: "NONE"
