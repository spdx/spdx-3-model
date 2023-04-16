SPDX-License-Identifier: Community-Spec-1.0

# NoAssertionText

## Summary

Concrete class representing an absence of an assertion about the presence of
copyright text.

## Description

A NoAssertionText is the primary value that is used by a copyrightText field
that indicates that the SPDX data creator is making no assertion about whether
any copyright information is present, or what its contents are if it is
present.

If a copyrightText has a NOASSERTION value, this indicates that one of the
following applies:
* the SPDX data creator has made no attempt to determine this field; or
* the SPDX data creator has intentionally provided no information (no meaning
  should be implied from the absence of an assertion).

## Metadata

- name: NoAssertionText
- SubclassOf: CopyrightTextField
- Instantiability: Concrete

## Properties
