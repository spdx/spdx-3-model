SPDX-License-Identifier: Community-Spec-1.0

# OrLaterOperator

## Summary

Portion of a LicenseExpression representing this version, or any later version,
of the indicated License.

## Description

An OrLaterOperator indicates that this portion of the LicenseExpression
represents either (1) the specified version of the corresponding License, or
(2) any later version of that License. It is represented in the SPDX License
Expression Syntax by the `+` operator.

It is context-dependent, and unspecified by SPDX, as to what constitutes a
"later version" of any particular License. Some Licenses may not be versioned,
or may not have clearly-defined ordering for versions. The consumer of SPDX
data will need to determine for themselves what meaning to attribute to a
"later version" operator for a particular License.

## Metadata

- name: OrLaterOperator
- SubclassOf: LicenseExpression
- Instantiability: Concrete

## Properties

- license
  - type: License
  - minCount: 1
  - maxCount: 1
