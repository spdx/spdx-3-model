SPDX-License-Identifier: Community-Spec-1.0

# VulnAssessmentRelationship

## Summary

Abstract ancestor class for all vulnerability assessments

## Description

VulnAssessmentRelationship is the ancestor class common to all vulnerability
assessment relationships. It factors out the common properties shared by them.

## Metadata

- name: VulnAssessmentRelationship
- SubclassOf: /Core/Relationship
- Instantiability: Abstract

## Properties

- assessmentType
  - type: AssessmentType
  - minCount: 1
  - maxCount: 1
- assessedElement
  - type: /Core/Element
  - minCount: 0
  - maxCount: 1
- publishedTime
  - type: /Core/DateTime
  - minCount: 0
  - maxCount: 1
- suppliedBy
  - type: /Core/Identity
  - minCount: 0
  - maxCount: 1
- modifiedTime
  - type: /Core/DateTime
  - minCount: 0
  - maxCount: 1
- withdrawnTime
  - type: /Core/DateTime
  - minCount: 0
  - maxCount: 1

## External properties restrictions

- /Core/Relationship/to
  - minCount: 1
