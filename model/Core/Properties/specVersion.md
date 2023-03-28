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

## Metadata

- name: specVersion
- Nature: DataProperty
- Range: SemVer

