SPDX-License-Identifier: Community-Spec-1.0

# SystemChangeImpactAnalysis

## Summary

Documents the impact analysis of one or more system changes.

## Description

SystemChangeImpactAnalysis represents an assessment of the impact of actual or
proposed changes to system elements. It is used when the subject of the
analysis is one or more additions, modifications, or removals from a system.

SystemChangeImpactAnalysis is distinct from SystemImpactAnalysis, which
assesses whether a trigger or other source affects a system and may conclude
that no change is required.

When a SystemImpactAnalysis identifies changes that need a separate
change-impact assessment, the SystemImpactAnalysis can be linked to the
SystemChangeImpactAnalysis using a /Core/Relationship with relationshipType
hasOutput, from the SystemImpactAnalysis to the SystemChangeImpactAnalysis.

The change-impact assessment can identify the elements considered and classify
elements as added, modified, or removed. An element can be linked using
impactedElement without also being classified as changed.

The /Core/rationale property, when used, explains the basis for the
change-impact conclusion. The changed-element properties identify the scope
being assessed; they do not replace the rationale.

## Metadata

- name: SystemChangeImpactAnalysis
- SubclassOf: /Core/Artifact
- Instantiability: Concrete

## Properties

- impactAnalysisProcess
  - type: /Core/Element
  - minCount: 0
- impactAnalysisStatus
  - type: SystemImpactAnalysisStatus
  - minCount: 0
  - maxCount: 1
- impactLevel
  - type: SystemImpactLevel
  - minCount: 0
- impactedElement
  - type: /Core/Element
  - minCount: 0
- addedElement
  - type: /Core/Element
  - minCount: 0
- modifiedElement
  - type: /Core/Element
  - minCount: 0
- removedElement
  - type: /Core/Element
  - minCount: 0
- /Core/rationale
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
