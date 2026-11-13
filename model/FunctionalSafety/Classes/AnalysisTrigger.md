SPDX-License-Identifier: Community-Spec-1.0

# AnalysisTrigger

## Summary

Identifies a source that prompts a system impact analysis.

## Description

AnalysisTrigger represents an event, finding, report, or condition that prompts
a system impact analysis.

Examples include a field incident, laboratory finding, customer report,
regulatory event, configuration change, environmental change, or business
decision.

An AnalysisTrigger does not assert that a change is required. It records why an
analysis is opened; the analysis determines whether the design needs to be
modified.

An externally managed record can be identified using the inherited
/Core/externalIdentifier and /Core/externalRef properties. For example, an
external issue can use its source-system key as externalIdentifier and its
resolvable URL as externalRef. The specific interpretation of those values
remains with the source system; this class does not define system-specific
identifier formats or duplicate the external record's contents.

If a source is already represented by a more specific SPDX Artifact, that
artifact can be used directly as input to the SystemImpactAnalysis instead of
creating an AnalysisTrigger for the same source.

A SystemImpactAnalysis can be linked to an AnalysisTrigger using a
/Core/Relationship with relationshipType hasInput, from the
SystemImpactAnalysis to the AnalysisTrigger.

## Metadata

- name: AnalysisTrigger
- SubclassOf: /Core/Artifact
- Instantiability: Concrete
