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
- cve: An identifier for a specific software flaw defined within the official CVE Dictionary and that conforms to the CVE specification as defined by https://csrc.nist.gov/glossary/term/cve_id.
- email: https://datatracker.ietf.org/doc/html/rfc3696#section-3
- gitoid: https://www.iana.org/assignments/uri-schemes/prov/gitoid Gitoid stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) and a gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent the software [Artifact ID](https://github.com/omnibor/spec/blob/main/spec/SPEC.md#artifact-id) or the [OmniBOR Identifier](https://github.com/omnibor/spec/blob/main/spec/SPEC.md#omnibor-identifier) for the software artifact's associated [OmniBOR Document](https://github.com/omnibor/spec/blob/main/spec/SPEC.md#omnibor-document); this ambiguity exists because the OmniBOR Document is itself an artifact, and the gitoid of that artifact is its valid identifier. Omnibor is a minimalistic schema to describe software [Artifact Dependency Graphs](https://github.com/omnibor/spec/blob/main/spec/SPEC.md#artifact-dependency-graph-adg). Gitoids calculated on software artifacts (Snippet, File, or Package Elements) should be recorded in the SPDX 3.0 SoftwareArtifact's ContentIdentifier property. Gitoids calculated on the OmniBOR Document (OmniBOR Identifiers) should be recorded in the SPDX 3.0 Element's ExternalIdentifier property. 
- other: Used when the type doesn't match any of the other options.
- pkgUrl: https://github.com/package-url/purl-spec
- securityOther: Used when there is a security related identifier of unspecified type.
- swhid: https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html
- swid: https://www.ietf.org/archive/id/draft-ietf-sacm-coswid-21.html#section-2.3
- urlScheme: the scheme used in order to locate a resource https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml

