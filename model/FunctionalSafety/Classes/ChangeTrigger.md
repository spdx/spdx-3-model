SPDX-License-Identifier: Community-Spec-1.0

# ChangeTrigger

## Summary

Identifies the source or reason that initiates a functional safety change impact
analysis.

## Description

ChangeTrigger represents the information, event, report, or external record
that causes a functional safety change impact analysis to be performed.

A ChangeTrigger can represent a vulnerability, field incident, lab finding,
customer report, regulatory event, configuration change, environmental change,
business decision, or other source that may require safety-relevant review.

The authoritative record for the trigger can be referenced using inherited
/Core/externalRef or /Core/externalIdentifier values. For example, the trigger
can point to a CVE, FAA report, CAPA record, QMS record, Jira issue,
ServiceNow ticket, or other externally managed record without duplicating that
system's contents in SPDX.

A ChangeImpactAnalysis can be linked to the ChangeTrigger that caused it using
a /Core/Relationship with relationshipType causedBy.

## Metadata

- name: ChangeTrigger
- SubclassOf: /Core/Artifact
- Instantiability: Concrete

## Properties

- /Core/rationale
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
