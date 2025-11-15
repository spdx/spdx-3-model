SPDX-License-Identifier: Community-Spec-1.0

# SoftwareArtifact

## Summary

A distinct article or unit related to Software.

## Description

A software artifact is a distinct article or unit related to software
such as a package, a file, or a snippet.

## Metadata

- name: SoftwareArtifact
- SubclassOf: /Core/Artifact
- Instantiability: Abstract

## Properties

- primaryPurpose
  - type: SoftwarePurpose
  - minCount: 0
  - maxCount: 1
- additionalPurpose
  - type: SoftwarePurpose
  - minCount: 0
- copyrightText
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- attributionText
  - type: xsd:string
  - minCount: 0
- contentIdentifier
  - type: ContentIdentifier
  - minCount: 0
- artifactSize
  - type: xsd:nonNegativeInteger
  - minCount: 0
  - maxCount: 1
