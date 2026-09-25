SPDX-License-Identifier: Community-Spec-1.0

# AnalysisTrigger

## Summary

Identifies the source that starts a functional safety system impact analysis.

## Description

AnalysisTrigger represents the information, event, report, or external record
that starts a functional safety SystemImpactAnalysis.

An AnalysisTrigger can represent a field incident, lab finding, customer report,
regulatory event, configuration change, environmental change, business decision,
or other source that may require safety-relevant review.

An AnalysisTrigger does not assert that a change is required. It records why a
SystemImpactAnalysis is opened so the analysis can determine whether affected
elements need to be added, removed, revised, verified, or left unchanged.

When the source is already represented by a more specific SPDX Artifact, that
existing element can be used as input to the SystemImpactAnalysis. For example,
a CVE can be represented using /Security/Vulnerability, which is a subclass of
/Core/Artifact and can carry an externalIdentifier with externalIdentifierType
`cve`.

The authoritative record for the trigger can be referenced using inherited
/Core/externalRef or /Core/externalIdentifier values. For example, the trigger
can point to an FAA report, CAPA record, QMS record, Jira issue, ServiceNow
ticket, or other externally managed record without duplicating that system's
contents in SPDX.

A SystemImpactAnalysis can be linked to the AnalysisTrigger using a
/Core/Relationship with relationshipType `hasInput`, from the
SystemImpactAnalysis to the AnalysisTrigger.

## Metadata

- name: AnalysisTrigger
- SubclassOf: /Core/Artifact
- Instantiability: Concrete
