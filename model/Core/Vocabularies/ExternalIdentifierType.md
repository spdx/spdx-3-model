SPDX-License-Identifier: Community-Spec-1.0

# ExternalIdentifierType

## Summary

Specifies the type of an external identifier.

## Description

ExteralIdentifierType specifies the type of an external identifier.

## Metadata

- name: ExternalIdentifierType

## Entries

- cpe22: [Common Platform Enumeration Specification 2.2](https://cpe.mitre.org/files/cpe-specification_2.2.pdf)
- cpe23: [Common Platform Enumeration: Naming Specification Version 2.3](https://csrc.nist.gov/publications/detail/nistir/7695/final)
- cve: Common Vulnerabilities and Exposures identifiers, an identifier for a specific software flaw defined within the official CVE Dictionary and that conforms to the [CVE specification](https://csrc.nist.gov/glossary/term/cve_id).
- email: Email address, as defined in [RFC 3696](https://www.rfc-editor.org/info/rfc3986) Section 3.
- gitoid: [Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid>), stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). A gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent the software [Artifact ID](https://github.com/omnibor/spec/blob/main/spec/SPEC.md#artifact-id) or the [OmniBOR Identifier](https://github.com/omnibor/spec/blob/main/spec/SPEC.md#omnibor-identifier) for the software artifact's associated [OmniBOR Document](https://github.com/omnibor/spec/blob/main/spec/SPEC.md#omnibor-document); this ambiguity exists because the OmniBOR Document is itself an artifact, and the gitoid of that artifact is its valid identifier. Omnibor is a minimalistic schema to describe software [Artifact Dependency Graphs](https://github.com/omnibor/spec/blob/main/spec/SPEC.md#artifact-dependency-graph-adg). Gitoids calculated on software artifacts (Snippet, File, or Package Elements) should be recorded in the SPDX 3.0 SoftwareArtifact's ContentIdentifier property. Gitoids calculated on the OmniBOR Document (OmniBOR Identifiers) should be recorded in the SPDX 3.0 Element's ExternalIdentifier property.
- other: Used when the type doesn't match any of the other options.
- packageUrl: [package URL](https://github.com/package-url/purl-spec)
- securityOther: Used when there is a security related identifier of unspecified type.
- swhid: SoftWare Hash IDentifier, persistent intrinsic identifiers for digital artifacts, such as files, trees (also known as directories or folders), commits, and other objects typically found in version control systems. The syntax of the identifiers is defined in the [SWHID specification](https://www.swhid.org/specification/v1.1/4.Syntax) and they typically look like `swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`.
- swid: [Concise Software Identification tag](https://www.ietf.org/archive/id/draft-ietf-sacm-coswid-21.html#section-2.3)
- urlScheme: [Uniform Resource Identifier (URI) Schemes](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml). The scheme used in order to locate a resource.
