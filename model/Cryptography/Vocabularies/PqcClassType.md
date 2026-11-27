SPDX-License-Identifier: Community-Spec-1.0

# PqcClassType

## Summary

The post-quantum cryptographic algorithm enumeration.

## Description

Specifies the type of a post-quantum cryptographic algorithm.

## Metadata

- name: PqcClassType

## Entries

- latticeBased: Security based on hard lattice problems, such as Learning With Errors, Ring-LWE and Module-LWE, or NTRU lattices.
- codeBased: Security based on the hardness of decoding random linear error-correcting codes, such as Goppa codes or quasi-cyclic codes.
- multivariate: Security based on the difficulty of solving systems of multivariate quadratic equations over finite fields.
- hashBased: Security based on the properties of cryptographic hash functions, such as preimage and collision resistance. Includes stateful and stateless schemes.
- isogenyBased: Security based on the difficulty of finding isogenies between elliptic curves.
- mpcInTheHead: Signatures built with the "MPC-in-the-Head" or zero-knowledge proof paradigm.
