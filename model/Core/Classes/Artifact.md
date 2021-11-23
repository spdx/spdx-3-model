SPDX-License-Identifier: Community-Spec-1.0

# Artifact

## Summary

A distinct article or unit within the digital domain.

## Description

An artifact is a distinct article or unit within the digital domain,
such as an electronic file, a software package, a device or an element of data.

## Metadata

- name: Artifact
- SubclassOf: Element; Agent
- Instantiability: Abstract
- Status: unstable


## Properties

- artifactURL
  - type: ArtifactURL
  - minCount: 0
  - maxCount: 1
- originatedBy
  - type: Identity
  - minCount: 0
  - maxCount: 1

