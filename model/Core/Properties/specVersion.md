SPDX-License-Identifier: Community-Spec-1.0

# specVersion

## Summary

Provides a reference number that can be used to understand how to parse and interpret an Element.

## Description

The specVersion provides a reference number that can be used to understand how to parse and interpret an Element.
It will enable both future changes to the specification and to support backward compatibility.
The major version number shall be incremented when incompatible changes between versions are made
(one or more sections are created, modified or deleted).
The minor version number shall be incremented when backwards compatible changes are made.

Here, parties exchanging information in accordance with the SPDX specification need to provide 
100% transparency as to which SPDX specification version such information is conforming to.

The specVersion is a string that is following the specification of [Semantic Versioning 2.0.0](https://semver.org/).

## Metadata

- name: specVersion
- Nature: DataProperty
- Range: xsd:string

## Format

- pattern: ^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$
