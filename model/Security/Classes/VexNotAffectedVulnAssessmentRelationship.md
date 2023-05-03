SPDX-License-Identifier: Community-Spec-1.0

# VexNotVulnAffectedAssessmentRelationship

## Summary

TODO

## Description

An VexNotVulnAffectedAssessment is TODO

## Metadata

- name: VexNotAffectedVulnAssessmentRelationship
- SubclassOf: /Security/VexVulnAssessmentRelationship
- Instantiability: Concrete

## Properties

- impact
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- justification
  - type: VexJustificationType
  - minCount: 1
  - maxCount: 1
