SPDX-License-Identifier: Community-Spec-1.0

# DefinedProcess

## Summary

Class that describes a process.

## Description

Processes are composed of systematic task(s) required to achieve a goal.

## Metadata

- name: DefinedProcess
- SubclassOf: Artifact
- Instantiability: Abstract

## Properties

- processReadiness
  - type: ProcessReadinessType
  - minCount: 0
  - maxCount: 1
- processVersion
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- rationale
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
