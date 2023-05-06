SPDX-License-Identifier: Community-Spec-1.0

# DisjunctiveSet

## Summary

A license expression representing a set of licensing information where one of the elements applies.

## Description

A DisjunctiveSet indicates that _at least one_ of its subsidiary
license expressions applies. In other words, a
DisjunctiveSet of two or more licenses represents a licensing
situation where _at least one_ of the specified licenses are to be complied with.
A consumer of SPDX data would typically understand this to permit the recipient
of the licensed content to choose which of the corresponding license they
would prefer to use.

It is represented in the SPDX License Expression Syntax
by the `OR` operator.
There is no order between the members of the DisjunctiveSet.

## Metadata

- name: DisjunctiveSet
- SubclassOf: LicenseExpression
- Instantiability: Concrete

## Properties

- member
  - type: LicenseExpression
  - minCount: 2

