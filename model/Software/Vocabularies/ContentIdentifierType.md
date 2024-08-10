SPDX-License-Identifier: Community-Spec-1.0

# ContentIdentifierType

## Summary

Specifies the type of a content identifier.

## Description

ContentIdentifierType specifies the type of a content identifier.

## Metadata

- name: ContentIdentifierType

## Entries

- gitoid: [Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid), stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). A gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent either an [Artifact Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-identifier-types) for the software artifact or an [Input Manifest Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#input-manifest-identifier) for the software artifact's associated [Artifact Input Manifest](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-input-manifest); this ambiguity exists because the Artifact Input Manifest is itself an artifact, and the gitoid of that artifact is its valid identifier. Gitoids calculated on software artifacts (Snippet, File, or Package Elements) should be recorded in the SPDX 3.0 SoftwareArtifact's contentIdentifier property. Gitoids calculated on the Artifact Input Manifest (Input Manifest Identifier) should be recorded in the SPDX 3.0 Element's externalIdentifier property. See [OmniBOR Specification](https://github.com/omnibor/spec/), a minimalistic specification for describing software [Artifact Dependency Graphs](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-dependency-graph-adg).
- swhid: [SoftWare Hash IDentifier](https://www.swhid.org/), persistent intrinsic identifiers for digital artifacts, such as files, trees (also known as directories or folders), commits, and other objects typically found in version control systems. The syntax of the identifiers is defined in the [ISO/IEC 18670 SoftWare Hash IDentifier (SWHID) Specification V1.2](https://www.iso.org/standard/89985.html) and they typically look like `swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`.
