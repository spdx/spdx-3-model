SPDX-License-Identifier: Community-Spec-1.0

# EvidenceRelationship

## Summary

EvidenceRelationship defines the association between pieces of evidence and EvaluationResult.

## Description

EvidenceRelationship defines the association between pieces of evidence and EvaluationResult. This establishes traceability and contextual linkage between evidence items, supporting certification, verification, and audit activities.

## Metadata

- name: EvidenceRelationship
- SubclassOf: /Core/Relationship
- Instantiability: Concrete

## Properties

- evidenceUUID
  - type: ExternalIdentifier
  - minCount: 0
  - maxCount: 1
- evidenceCategories
  - type: EvidenceType
  - minCount: 0
