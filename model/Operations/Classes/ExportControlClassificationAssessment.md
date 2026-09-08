SPDX-License-Identifier: Community-Spec-1.0

# ExportControlClassificationAssessment

## Summary

Assessment of an Element for export control classification.

## Description

Assessment of an Element for export control classification
according to the classification schema of one or multiple countries.

## Metadata

- name: ExportControlClassificationAssessment
- SubclassOf: /Core/Artifact
- Instantiability: Concrete

## Properties

- assessor
  - type: /Core/Agent
  - maxCount: 1
- assessedElement
  - type: /Core/Element
  - minCount: 1
  - maxCount: 1
- assessmentContext
  - type: Project
  - maxCount: 1
- assessmentResult
  - type: ExportControlClassification
  - minCount: 1
- assessmentTime
  - type: /Core/DateTime
  - maxCount: 1
