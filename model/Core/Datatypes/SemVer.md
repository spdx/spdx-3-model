SPDX-License-Identifier: Community-Spec-1.0

# SemVer

## Summary

A string constrained to the SemVer 2.0.0 specification.

## Description

A semantic version is a string that is following the specification of
[Semantic Versioning 2.0.0](https://semver.org/).

## Metadata

- name: SemVer
- SubclassOf: xsd:string

## Format

- pattern: ^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$
