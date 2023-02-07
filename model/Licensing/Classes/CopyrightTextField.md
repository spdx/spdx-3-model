SPDX-License-Identifier: Community-Spec-1.0

# CopyrightTextField

## Summary

Base abstract class used for the copyrightText field that can take a value
of either a text value (via CopyrightText), NOASSERTION, or NONE.

## Description

A CopyrightTextField is the primary value that is used by a copyright text
field for a software Package, File or Snippet. It represents either actual
text (represented via a concrete CopyrightText), or the values NOASSERTION
or NONE.

**FIXME** The specific meanings of NOASSERTION or NONE are defined in the
copyrightText property description. (**INCORRECT** - change to NoAssertionText
or NoneText)

## Metadata

- name: CopyrightTextField
- SubclassOf: none
- Instantiability: Abstract

