SPDX-License-Identifier: Community-Spec-1.0

# Artifact

## Summary

A distinct article or unit within the digital domain.

## Description

An artifact is a distinct article or unit within the digital domain,
such as an electronic file, a software package, a device or an element of data.

## Metadata

- name: Artifact
- SubclassOf: Element
- Instantiability: Abstract

## Properties

- originatedBy
  - type: Agent
  - minCount: 0
- suppliedBy
  - type: Agent
  - minCount: 0
  - maxCount: 1
- builtTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1
- releaseTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1
- validUntilTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1
- standard
  - type: xsd:string
  - minCount: 0 
