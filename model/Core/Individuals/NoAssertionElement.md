SPDX-License-Identifier: Community-Spec-1.0

# NoAssertionElement

## Summary

An Individual Value for Element representing a set of Elements of unknown
identify or cardinality (number).

## Description

NoAssertionElement should be used if

- the SPDX creator has attempted to but cannot reach a reasonable objective
  determination; or
- the SPDX creator has made no attempt to determine this field; or
- the SPDX creator has intentionally provided no information (no meaning should
  be implied by doing so).

For example, a Relationship with `from`=Element1,
`relationshipType`="ancestorOf", and `to`=NOASSERTION is explicitly expressing
that no assertion is being made about any potential descendents of Element1.

## Metadata

- name: NoAssertionElement
- type: Element

## Property Values

- name: "NOASSERTION"
