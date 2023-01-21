SPDX-License-Identifier: Community-Spec-1.0

# Hash

## Summary

A mathematically calculated representation of a grouping of data.

## Description

A hash is a grouping of characteristics unique to the result
of applying a mathematical algorithm
that maps data of arbitrary size to a bit string (the hash)
and is a one-way function, that is,
a function which is practically infeasible to invert.
This is commonly used for integrity checking of data.

## Metadata

- name: Hash
- SubclassOf: IntegrityMethod

## Properties

- algorithm
  - type: HashAlgorithm
  - minCount: 1
  - maxCount: 1
- hashValue
  - type: xsd:string
  - minCount: 1
  - maxCount: 1

