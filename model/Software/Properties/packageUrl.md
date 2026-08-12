SPDX-License-Identifier: Community-Spec-1.0

# packageUrl

## Summary

Provides a place for the SPDX data creator to record the Package-URL
for a software Package.

## Description

A packageUrl property specifies a Package-URL (PURL).
The PURL shall be a valid Uniform Resource Identifier (URI) and
Uniform Resource Locator (URL) that identifies a software package independent
of its ecosystem or distribution channel, in accordance with
[ECMA-427](https://ecma-international.org/publications-and-standards/standards/ecma-427/).

The PURL contains a type component that defines the ecosystem-specific
structure and semantics for the remaining PURL components.

The registered PURL type definitions are maintained in the Package-URL type
registry available at <https://packageurl.org/docs/purl/purl-types>.

## Metadata

- name: packageUrl
- Nature: DataProperty
- Range: xsd:anyURI
