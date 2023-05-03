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

