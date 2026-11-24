SPDX-License-Identifier: Community-Spec-1.0

# Cryptography

## Summary

The Cryptography profile documents cryptographic algorithms, algorithm expressions, keys, certificates, and signature metadata for representing cryptographic capabilities, requirements, and artifacts in SPDX documents and Cryptographic Bill of Materials (CBOM) use cases.

## Description

The Cryptography profile provides a common vocabulary for describing the cryptographic capabilities, algorithm requirements, and cryptographic artifacts associated with software, documents, devices, and other SPDX elements.

It supports the representation of cryptographic algorithms listed in the SPDX Cryptographic Algorithm List as well as user-defined custom cryptographic algorithms. The profile also supports algorithm parameters, parameter option sets, and SPDX Cryptographic Algorithm Expressions, enabling authors to describe algorithm alternatives, required algorithm combinations, and other complex cryptographic profiles using operators such as `AND` and `OR`.

In addition to algorithms, the profile describes concrete cryptographic artifacts such as cryptographic keys and certificates, including key type information, certificate identities, validity periods, certificate extensions, and certificate lifecycle-state annotations. It also supports metadata about cryptographic signatures, including signature algorithm, signature value or storage location, signer information, signing keys, verification keys, signature time, and signature format.

When combined with SPDX relationships such as `supportsAlgorithm`, `usedAlgorithm`, and `providesAlgorithm`, the profile can express which algorithms a system supports, uses, or provides. This enables Cryptographic Bill of Materials (CBOM) generation, cryptographic conformance assessment, dependency analysis, and supply-chain transparency for cryptographic components, policies, and implementations.

## Metadata

- id: https://spdx.org/rdf/3/terms/Cryptography
- name: Cryptography
