SPDX-License-Identifier: Community-Spec-1.0

# SystemImpactAnalysis

## Summary

Documents the analysis of one or more triggers to determine system impact.

## Description

SystemImpactAnalysis represents the documented analysis of one or more sources
that may affect a system.

A SystemImpactAnalysis can be linked to one or more source elements using a
/Core/Relationship with relationshipType hasInput, from the
SystemImpactAnalysis to each source. A source may be an AnalysisTrigger or a
more specific SPDX Artifact. For example, a vulnerability can be represented
using /Security/Vulnerability, a subclass of /Core/Artifact, with its CVE
identifier represented using externalIdentifier.

An analysis can have multiple input sources, and one source can be used as
input to multiple analyses, such as analyses for different product
configurations.

The analysis records its process, lifecycle status, assessed impact category,
and rationale. Its input relationships identify the sources that prompted it.
The /Core/rationale property, when used, explains the basis for the analysis
conclusion.

A SystemImpactAnalysis may conclude that no change is required. If the analysis
leads to changes that require a separate accomplishment summary, a
SystemChangeAccomplishmentSummary can be linked as an output using a
/Core/Relationship with relationshipType hasOutput. Not every
SystemImpactAnalysis requires a SystemChangeAccomplishmentSummary.

SystemImpactAnalysis assesses the effect of a trigger or source. It does not
describe the accomplishment and supporting evidence for specific system
changes; those are documented by SystemChangeAccomplishmentSummary.

## Metadata

- name: SystemImpactAnalysis
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
- /Core/rationale
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
