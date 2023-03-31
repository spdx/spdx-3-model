SPDX-License-Identifier: Community-Spec-1.0

# LicenseField

## Summary

Base abstract class used for all fields that can take a value of either a
license expression, NOASSERTION, or NONE.

## Description

A LicenseField is the primary value that is used by a licensing field for a
software Package, File or Snippet. It represents either a license expression,
or the values NOASSERTION or NONE. The specific meanings of NOASSERTION or
NONE for the particular licensing field are defined in the corresponding
property description.

## Metadata

- name: LicenseField
- SubclassOf: none
- Instantiability: Abstract

## Properties
