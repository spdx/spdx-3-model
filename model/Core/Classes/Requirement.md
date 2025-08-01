SPDX-License-Identifier: Community-Spec-1.0

# Requirement

## Summary

A distinct unit representing a requirement as it is used by systems, software and hardware engineering.

## Description

A requirement element is a distinct article or unit defining an expectation, need, behaviour, design intent etc. of an item that already exists or is to be created based on this requirement.

## Metadata

- name: Requirement
- SubclassOf: /Core/Element

## Properties

- requirementUID
  - type: ContentIdentifier
  - minCount: 0
  - maxCount: 1
- devLifeCycleStage
  - type: LifecycleScopeType
  - minCount: 0
  - maxCount: *
- requirementText
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- requirementContext
  - type: RequirementContext
  - minCount: 0
  - maxCount: 1
- requirementNote
  - type: xsd:string
  - minCount: 0
  - maxCount: *

