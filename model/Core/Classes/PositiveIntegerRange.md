SPDX-License-Identifier: Community-Spec-1.0

# PositiveIntegerRange

## Summary

A tuple of two positive integers that define a range.

## Description

PositiveIntegerRange is a tuple of two positive integers that define a range.
"begin" must be less than or equal to "end".

## Metadata

- name: PositiveIntegerRange
- SubclassOf: owl:Thing
- Instantiability: Concrete

## Properties

- begin
  - type: xsd:positiveInteger
  - minCount: 1
  - maxCount: 1
- end
  - type: xsd:positiveInteger
  - minCount: 1
  - maxCount: 1

