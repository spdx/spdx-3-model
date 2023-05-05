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
- /Licensing/concludedLicense
  - type: /Licensing/LicenseField
  - minCount: 0
  - maxCount: 1
- /Licensing/declaredLicense
  - type: /Licensing/LicenseField
  - minCount: 0
  - maxCount: 1
- /Licensing/copyrightText
  - type: /Licensing/CopyrightTextField
  - minCount: 0
  - maxCount: 1
- /Licensing/attributionText
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
