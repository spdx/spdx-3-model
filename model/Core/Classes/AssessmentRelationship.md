SPDX-License-Identifier: Community-Spec-1.0

# AssessmentRelationship

## Summary

Abstract ancestor class for all assessments

## Description

AssessmentRelationship is the ancestor class common to all assessment relationships. It factors out the common properties shared by them.

## Metadata

- name: AssessmentRelationship
- SubclassOf: Relationship
- Instantiability: Abstract

## Properties

- assessedElement
  - type: Element
  - minCount: 0
  - maxCount: 1
- publishedTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1
- /Core/suppliedBy
  - type: Agent
  - minCount: 0
  - maxCount: 1
- modifiedTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1
- withdrawnTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1
