SPDX-License-Identifier: Community-Spec-1.0

# VulnAssessmentRelationship

## Summary

Provides various type of assessment information for a vulnerability.

## Description

`VulnAssessmentRelationship` is an abstract subclass that captures the common elements among vulnerability assessment relationships.

## Metadata

- name: VulnAssessmentRelationship
- SubclassOf: /Core/Relationship
- Instantiability: Abstract

## Properties

- assessedElement
  - type: Element
  - minCount: 1
  - maxCount: 1
