SPDX-License-Identifier: Community-Spec-1.0

# SoftwareArtifact

## Summary

A distinct article or unit within the digital domain.

## Description

An artifact is a distinct article or unit within the digital domain,
such as an electronic file, a software package, a device or an element of data.

## Metadata

- name: SoftwareArtifact
- SubclassOf: /Core/Artifact
- Instantiability: Abstract

## Properties

- contentIdentifier
  - type: xsd:anyURI
  - minCount: 0
  - maxCount: 1
- purpose
  - type: SoftwarePurpose
  - minCount: 0
- /Core/Licensing/concludedLicense
  - type: /Core/Licensing/LicenseField
  - minCount: 0
  - maxCount: 1
- /Core/Licensing/declaredLicense
  - type: /Core/Licensing/LicenseField
  - minCount: 0
  - maxCount: 1
- /Core/Licensing/copyrightText
  - type: /Core/Licensing/CopyrightTextField
  - minCount: 0
  - maxCount: 1
- /Core/Licensing/attributionText
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
