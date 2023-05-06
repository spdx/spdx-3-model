SPDX-License-Identifier: Community-Spec-1.0

# WithOperator

## Summary

A license expression representing a License which has additional text applied to it.

## Description

A WithOperator indicates that the designated license is subject to the designated addition.

It is represented in the SPDX License Expression Syntax by the `WITH` operator.

## Metadata

- name: WithOperator
- SubclassOf: LicenseExpression
- Instantiability: Concrete

## Properties

- license
  - type: License
  - minCount: 1
  - maxCount: 1
- addition
  - type: Addition
  - minCount: 1
  - maxCount: 1
