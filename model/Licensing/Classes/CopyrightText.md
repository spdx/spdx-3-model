SPDX-License-Identifier: Community-Spec-1.0

# CopyrightText

## Summary

Concrete class representing copyright text that has actually been found.

## Description

A CopyrightText is the primary value that is used by a copyrightText field
that indicates copyright text being found, i.e. with a value other than
NONE or NOASSERTION.

## Metadata

- name: CopyrightText
- SubclassOf: CopyrightTextField
- Instantiability: Concrete

## Properties

- text
  - type: xsd:string
  - minCount: 1
  - maxCount: 1

