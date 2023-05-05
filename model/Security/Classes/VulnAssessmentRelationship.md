SPDX-License-Identifier: Community-Spec-1.0

# VulnAssessmentRelationship

## Summary

Asbtract ancestor class for all vulnerability assessments

## Description

VulnAssessmentRelationship is the ancestor class common to all vulnerability
assessment relationships. It factors out the common properties shared by them.

## Metadata

- name: VulnAssessmentRelationship
- SubclassOf: /Core/Relationship
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
- modifiedTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1
- withdrawnTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1

