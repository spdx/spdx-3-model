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

- assessedElement
  - type: /Software/SoftwareArtifact
  - minCount: 0
  - maxCount: 1
- publishedTime
  - type: /Core/DateTime
  - minCount: 0
  - maxCount: 1
- /Core/suppliedBy
  - type: /Core/Agent
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
