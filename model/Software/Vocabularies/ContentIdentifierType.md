SPDX-License-Identifier: Community-Spec-1.0

# ContentIdentifierType

## Summary

Specifies the type of a content identifier.

## Description

ContentIdentifierType specifies the type of a content identifier.

## Metadata

- name: ContentIdentifierType

## Entries

- gitoid: [Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid) stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) and a gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent the software [Artifact ID](https://github.com/omnibor/spec/blob/main/spec/SPEC.md#artifact-id) or the [OmniBOR Identifier](https://github.com/omnibor/spec/blob/main/spec/SPEC.md#omnibor-identifier) for the software artifact's associated [OmniBOR Document](https://github.com/omnibor/spec/blob/main/spec/SPEC.md#omnibor-document).
- swhid: SoftWare Hash IDentifier, persistent intrinsic identifiers for digital artifacts. The syntax of the identifiers is defined in the [SWHID specification](https://www.swhid.org/specification/v1.1/4.Syntax) and in the case of filess they typically look like `swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`.
