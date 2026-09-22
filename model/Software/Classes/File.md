SPDX-License-Identifier: Community-Spec-1.0

# File

## Summary

Refers to any object that stores content on a computer.

## Description

Refers to any object that stores content on a computer.
The type of content can optionally be provided in the contentType property.

The fileKind property can be set to `directory` to indicate the file represents
a directory and all content stored in that directory.

The fileKind property can be set to `symlink` to indicate the file represents a link to another file or directory, it does not represent the file or directory referenced by the symlink.

## Metadata

- name: File
- SubclassOf: /Software/SoftwareArtifact

## Properties

- /Core/contentType
  - type: /Core/MediaType
  - minCount: 0
  - maxCount: 1
- fileKind
  - type: FileKindType
  - minCount: 0
  - maxCount: 1

## External properties restrictions

- /Core/Element/name
  - minCount: 1
