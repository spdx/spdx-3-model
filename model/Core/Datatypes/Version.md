SPDX-License-Identifier: Community-Spec-1.0

# Version

## Summary

A string following the SemVer 2.0.0 specification with the exceptions of the patch version being optional and extensions are not supported.

## Description

A version is a string of decimal numbers and dots assigned to a specific state
of software, a specification, a document, or an artifact.

The SPDX Version type follows [Semantic Versioning 2.0.0](https://semver.org/)
but differs in that the patch version is optional and
extensions are not supported.

If no patch version is present, the latest released patch version is assumed.

Note that this Datatype was named "SemVer" prior to the SPDX specification release 3.1.

## Metadata

- name: Version
- SubclassOf: xsd:string

## Format

- pattern: ^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))?$
