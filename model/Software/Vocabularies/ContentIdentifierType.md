SPDX-License-Identifier: Community-Spec-1.0

# ContentIdentifierType

## Summary

Specifies the type of a content identifier.

## Description

ContentIdentifierType specifies the type of a content identifier.

## Metadata

- name: ContentIdentifierType

## Entries

- gitoid: https://www.iana.org/assignments/uri-schemes/prov/gitoid Gitoid stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) and a gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent the software [Artifact ID](https://github.com/omnibor/spec/blob/main/spec/SPEC.md#artifact-id) or the [OmniBOR Identifier](https://github.com/omnibor/spec/blob/main/spec/SPEC.md#omnibor-identifier) for the software artifact's associated [OmniBOR Document](https://github.com/omnibor/spec/blob/main/spec/SPEC.md#omnibor-document); this ambiguity exists because the OmniBOR Document is itself an artifact, and the gitoid of that artifact is its valid identifier. Omnibor is a minimalistic schema to describe software [Artifact Dependency Graphs](https://github.com/omnibor/spec/blob/main/spec/SPEC.md#artifact-dependency-graph-adg). Gitoids calculated on software artifacts (Snippet, File, or Package Elements) should be recorded in the SPDX 3.0 SoftwareArtifact's ContentIdentifier property. Gitoids calculated on the OmniBOR Document (OmniBOR Identifiers) should be recorded in the SPDX 3.0 Element's ExternalIdentifier property. 
- swhid: SoftWare Hash IDentifier, persistent intrinsic identifiers for digital artifacts. The syntax of the identifiers is defined in the [SWHID specification](https://www.swhid.org/specification/v1.1/4.Syntax) and they typically look like `swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`.

