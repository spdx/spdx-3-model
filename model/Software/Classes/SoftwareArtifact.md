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

- additionalPurpose
  - type: SoftwarePurpose
  - minCount: 0
- attributionText
  - type: xsd:string
  - minCount: 0
- byteSize
  - type: xsd:nonNegativeInteger
  - minCount: 0
  - maxCount: 1
- contentDuration
  - type: xsd:duration
  - minCount: 0
  - maxCount: 1
- contentIdentifier
  - type: ContentIdentifier
  - minCount: 0
- copyrightText
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- itemCount
  - type: xsd:nonNegativeInteger
  - minCount: 0
  - maxCount: 1
- primaryPurpose
  - type: SoftwarePurpose
  - minCount: 0
  - maxCount: 1
- tokenCount
  - type: xsd:nonNegativeInteger
  - minCount: 0
  - maxCount: 1
- downloadLocation
  - type: xsd:anyURI
  - minCount: 0
  - maxCount: 1
