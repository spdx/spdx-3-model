SPDX-License-Identifier: Community-Spec-1.0

# Snippet

## Summary

Describes a certain part of a file.

## Description

A Snippet describes a certain part of a file and can be used when the file is
known to have some content that has been included from another original source.

Snippets are useful for denoting when part of a file may have been originally
created under another license or copied from a place with a known
vulnerability.

## Metadata

- name: Snippet
- SubclassOf: /Software/SoftwareArtifact

## Properties

- byteRange
  - type: /Core/PositiveIntegerRange
  - minCount: 0
  - maxCount: 1
- lineRange
  - type: /Core/PositiveIntegerRange
  - minCount: 0
  - maxCount: 1
- snippetFromFile
  - type: File
  - minCount: 1
  - maxCount: 1
