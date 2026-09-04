SPDX-License-Identifier: Community-Spec-1.0

# FunctionalSafety

## Summary

The FunctionalSafety profile is designed to provide a standardized way of documenting and
sharing information about artifacts created, verified and maintained during the safety lifecycle of a system.

## Description

The FunctionalSafety profile's namespace defines a set of concepts and data elements related to artifacts and their dependencies or links
to each other that are part of a safety related system's safety conformance documentation.

These artifacts include the outputs of the safety engineering phases regarding planning, requirements analysis, system/software architecture, implementation, safety analysis and the verification tasks. The artifacts can be used to compile a standardized safety case document.

## Safety Relevance Assertion Profile

The FunctionalSafety profile can represent a Safety Relevance Assertion Profile
(SRAP) as a change impact delta without introducing a dedicated SRAPAssessment
class.

When new information may require safety-relevant review, ChangeTrigger
identifies the source, reason, event, report, or external record that initiates
the analysis. The trigger element can carry Core externalRef or
externalIdentifier values for external records such as CVEs, field incidents,
lab findings, customer reports, regulatory events, configuration changes,
environmental changes, or business decisions.

The ChangeImpactAnalysis can be connected to the ChangeTrigger using a Core
Relationship. The specific relationshipType for connecting the trigger and
analysis should be selected through the Core relationship vocabulary discussion
rather than fixed by RequirementVerification.

ChangeImpactAnalysis documents the analysis of the trigger against the safety
lifecycle. It can reference the process used for the impact analysis, communicate
the analysis status, indicate the impact level, identify approval, and identify
elements that were considered, added, or removed from the analyzed context by
the analysis.
These elements can include requirements, validations, tests, design artifacts,
safety analyses, code, documents, or other safety-lifecycle elements.

A RequirementVerification with verificationMethod set to assessment can
describe how an affected requirement is reassessed or reverified after the
ChangeImpactAnalysis identifies that verification is needed.

The impactAnalysisStatus value can communicate that the analysis is pending
before the engineering conclusion is ready. When a verification or assessment
has been completed, the resulting EvaluationResult records the outcome using
EvaluationResultType values. An inconclusive result should be used when the
evaluation was performed but cannot be clearly classified as pass or fail.
Evidence can be linked using EvidenceRelationship. A Core Bundle can carry the
change impact delta, such as the ChangeTrigger, ChangeImpactAnalysis, old
requirement, revised requirement, relationship between them, affected validation
or test elements, verification, result, and evidence. Elements that have not
changed can be referenced from the prior model rather than retransmitted.

For CVE-driven change analysis, the Security profile should continue to represent
vulnerability and VEX status. FunctionalSafety adds the safety context and
impact analysis result, including any SafetyContextRelationship that identifies
the relevant safety function or requirement and safety integrity level.

## Metadata

- id: https://spdx.org/rdf/3/terms/FunctionalSafety
- name: FunctionalSafety
