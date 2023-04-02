SPDX-License-Identifier: Community-Spec-1.0

# ExternalIdentifierType

## Summary

Specifies the type of an external identifier.

## Description

ExteralIdentifierType specifies the type of an external identifier.

## Metadata

- name: ExternalIdentifierType

## Entries

- cpe22: https://cpe.mitre.org/files/cpe-specification_2.2.pdf
- cpe23: https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7695.pdf
- email: TODOdescription
- gitoid: gitoid stands for Git Object ID. A gitoid of typeblob is a unique hash of a software artifact. Git relies on a Merkle Tree to index stored objects. See https://git-scm.com/book/en/v2/Git-Internals-Git-Objects. GitBOM is an amalgam of the terms "Git" and "SBOM". GitBOM is a minimalistic schema to describe software dependency graphs using a Merkle Tree, and is inspired by Git. A gitoid may refer to either the software artifact or its GitBOM document; this ambiguity exists because the GitBOM document is itself an artifact, and the gitoid of that artifact is its valid locator.
- other: Used when the type doesn't match any of the other options.
- pkgUrl: https://github.com/package-url/purl-spec
- swhid: https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html
- swid: https://www.ietf.org/archive/id/draft-ietf-sacm-coswid-21.html#section-2.3
- urlScheme: TODOdescription

