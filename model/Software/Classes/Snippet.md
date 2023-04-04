SPDX-License-Identifier: Community-Spec-1.0

# Snippet

## Summary

Describes a certain part of a file.

## Description

A Snippet describes a certain part of a file and can be used when the file is known to have some content
that has been included from another original source. Snippets are useful for denoting when part of a file
may have been originally created under another license or copied from a place with a known vulnerability.

## Metadata

- name: Snippet
- SubclassOf: /Core/Artifact

## Properties

- contentIdentifier
  - type: xsd:anyURI
  - minCount: 0
  - maxCount: 1
- snippetPurpose
  - type: SoftwarePurpose
  - minCount: 0
- byteRange
  - type: positiveIntegerRange
  - minCount: 0
  - maxCount: 1
- lineRange
  - type: positiveIntegerRange
  - minCount: 0
  - maxCount: 1

