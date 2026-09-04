SPDX-License-Identifier: Community-Spec-1.0

# ChangeImpactAnalysis

## Summary

Describes a functional safety change impact analysis.

## Description

ChangeImpactAnalysis represents the documented analysis of a change trigger
against safety-relevant SPDX elements.

A ChangeImpactAnalysis can be linked to the ChangeTrigger that caused it using
a /Core/Relationship with relationshipType causedBy. This keeps the source or
reason for the change separate from the analysis that determines impact.

The analysis can reference the process or specification used to perform the
impact analysis, communicate its current status, indicate its impact level,
identify the agent that approved it, and identify elements that were impacted,
added, removed from the analyzed context, verified again, or otherwise reviewed.

The affected elements can be requirements, validations, tests, design artifacts,
safety analyses, code, documents, or any other SPDX element relevant to the
safety lifecycle. Detailed engineering, quality-system, or regulatory records
can remain in their authoritative systems while SPDX communicates the
machine-readable change impact graph.

## Metadata

- name: ChangeImpactAnalysis
- SubclassOf: /Core/Artifact
- Instantiability: Concrete

## Properties

- impactAnalysisProcess
  - type: /Core/Element
  - minCount: 0
- impactAnalysisStatus
  - type: ChangeImpactAnalysisStatusType
  - minCount: 0
  - maxCount: 1
- impactLevel
  - type: ChangeImpactLevelType
  - minCount: 0
  - maxCount: 1
- approvedBy
  - type: /Core/Agent
  - minCount: 0
- impactedElement
  - type: /Core/Element
  - minCount: 0
- addedElement
  - type: /Core/Element
  - minCount: 0
- removedElement
  - type: /Core/Element
  - minCount: 0
- /Core/rationale
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
