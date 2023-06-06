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

- contentIdentifier
  - type: xsd:anyURI
  - minCount: 0
  - maxCount: 1
- primaryPurpose
  - type: SoftwarePurpose
  - minCount: 0
  - maxCount: 1
- additionalPurpose
  - type: SoftwarePurpose
  - minCount: 0
- concludedLicense
  - type: /Licensing/AnyLicenseInfo
  - minCount: 0
  - maxCount: 1
- declaredLicense
  - type: /Licensing/AnyLicenseInfo
  - minCount: 0
  - maxCount: 1
- copyrightText
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- attributionText
  - type: xsd:string
  - minCount: 0
  - maxCount: 1

