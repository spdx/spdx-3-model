SPDX-License-Identifier: Community-Spec-1.0

# AssessmentRelationship

## Summary

Allows to provide individual assessments of Threats and Controls with respect to assets and capabilities. 

## Description

Allows to provide
- impact assessments for a Threat on one or more assets or capabilities
- protection assessments for a Control with respect to one or more assets or capabilities.

This relationship is restricted to the `impacts` or `protects` relationship type.

## Metadata

- name: AssessmentRelationship
- SubclassOf: /Core/Relationship
- Instantiability: Concrete

## Properties

- /Core/rationale
  - type: String
  - minCount: 1
  - maxCount: 1
- assessments
  - type: Assessment
  - minCount: 1
