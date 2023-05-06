SPDX-License-Identifier: Community-Spec-1.0

# ConjunctiveSet

## Summary

A license expression representing a set of licensing information where all elements apply.

## Description

A ConjunctiveSet indicates that _each_ of its subsidiary
license expressions apply. In other words, a ConjunctiveSet of two or
more licenses represents a licensing situation where _all_ of the specified
licenses are to be complied with.

It is represented in the SPDX License
Expression Syntax by the `AND` operator.
There is no order between the members of the ConjunctiveSet.

It is syntactically correct to specify a ConjunctiveSet where the
subsidiary license expressions may be "incompatible" according to a particular
interpretation of the corresponding Licenses. The SPDX License Expression
Syntax does not take into account interpretation of license texts, which is
left to the consumer of SPDX data to determine for themselves.

## Metadata

- name: ConjunctiveSet
- SubclassOf: LicenseExpression
- Instantiability: Concrete

## Properties

- member
  - type: LicenseExpression
  - minCount: 2

