SPDX-License-Identifier: Community-Spec-1.0

# PositiveIntegerRange

## Summary

A tuple of two positive integers that define a range.

## Description

PositiveIntegerRange is a tuple of two positive integers that define a range.
"beginIntegerRange" must be less than or equal to "endIntegerRange".

## Metadata

- name: PositiveIntegerRange
- SubclassOf: none
- Instantiability: Concrete

## Properties

- beginIntegerRange
  - type: xsd:positiveInteger
  - minCount: 1
  - maxCount: 1
- endIntegerRange
  - type: xsd:positiveInteger
  - minCount: 1
  - maxCount: 1
