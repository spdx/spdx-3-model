SPDX-License-Identifier: Community-Spec-1.0

# SystemImpactAnalysis

## Summary

Describes a functional safety system impact analysis.

## Description

SystemImpactAnalysis represents the documented analysis of one or more analysis
triggers against safety-relevant SPDX elements.

A SystemImpactAnalysis can be linked to one or more AnalysisTrigger elements
using a /Core/Relationship with relationshipType `hasInput`, from the
SystemImpactAnalysis to each AnalysisTrigger. This keeps the source or reason
for the analysis separate from the analysis that determines impact.

The analysis can reference the process or specification used to perform the
impact analysis, communicate its current status, indicate its impact category,
and identify elements that were impacted, added, removed from the analyzed
context, verified again, or otherwise reviewed.

The analysis may determine that no actual change is required. In that case, the
analysis can record its impact category, rationale, affected elements, and
completion status without adding or removing elements.

The affected elements can be requirements, validations, tests, design artifacts,
safety analyses, code, documents, or any other SPDX element relevant to the
safety lifecycle. Detailed engineering, quality-system, or regulatory records
can remain in their authoritative systems while SPDX communicates the
machine-readable system impact graph.

When the analysis requires downstream verification, the verification work can
be represented with RequirementVerification, EvaluationResult, and
EvidenceRelationship elements. A newly required verification can be listed as an
addedElement so the analysis communicates both the affected element and the
follow-up verification that must be completed. A SystemImpactAnalysis should use
the `complete` status only when required downstream verification, evidence, and
decisions are represented, or when the analysis rationale explains why no
downstream work is required.

The /Core/rationale property describes the overall reason, scope, or conclusion
for the SystemImpactAnalysis. When a more detailed decision record is needed,
each per-element decision can be linked from the analysis with a /Core/Relationship
using relationshipType `hasOutput`, such as `SystemImpactAnalysis hasOutput Decision`.
The Decision can then use `hasInput` to identify the specific impacted, added, or
removed Element it decides on.

If a SystemImpactAnalysis uses the `duplicate` status, that status describes
the lifecycle state of the analysis itself. A separate decision record, when
used, can capture the agent or process decision that closed the analysis as a
duplicate and can link to the analysis that already covers the trigger or scope.

## Metadata

- name: SystemImpactAnalysis
- SubclassOf: /Core/Artifact
- Instantiability: Concrete

## Properties

- impactAnalysisProcess
  - type: /Core/Element
  - minCount: 0
- impactAnalysisStatus
  - type: SystemImpactAnalysisStatusType
  - minCount: 0
  - maxCount: 1
- impactLevel
  - type: SystemImpactLevelType
  - minCount: 0
  - maxCount: 1
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
