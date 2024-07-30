SPDX-License-Identifier: Community-Spec-1.0

# ContentIdentifierType

## Summary

Specifies the type of a content identifier.

## Description

ContentIdentifierType specifies the type of a content identifier.

## Metadata

- name: ContentIdentifierType

## Entries

- gitoid: [gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid), stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). A gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent the software [Artifact ID](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-id) or the [Input Manifest Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#input-manifest-identifier) for the software artifact's associated [Artifact Input Manifest](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-input-manifest).
- swhid: SoftWare Hash IDentifier, persistent intrinsic identifiers for digital artifacts. The syntax of the identifiers is defined in the [SWHID specification](https://www.swhid.org/specification/v1.1/4.Syntax) and in the case of filess they typically look like `swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`.
