SPDX-License-Identifier: Community-Spec-1.0

# ChangeTrigger

## Summary

Identifies the source or reason that initiates a functional safety change impact
analysis.

## Description

ChangeTrigger represents the information, event, report, or external record
that initiates a functional safety change impact analysis.

A ChangeTrigger can represent a field incident, lab finding, customer report,
regulatory event, configuration change, environmental change, business decision,
or other source that may require safety-relevant review.

When the source is already represented by a more specific SPDX Artifact, that
existing element can be used as input to the ChangeImpactAnalysis. For example,
a CVE can be represented using /Security/Vulnerability, which is a subclass of
/Core/Artifact and can carry an externalIdentifier with externalIdentifierType
`cve`.

The authoritative record for the trigger can be referenced using inherited
/Core/externalRef or /Core/externalIdentifier values. For example, the trigger
can point to an FAA report, CAPA record, QMS record, Jira issue, ServiceNow
ticket, or other externally managed record without duplicating that system's
contents in SPDX.

A ChangeImpactAnalysis can be linked to the ChangeTrigger using a
/Core/Relationship with relationshipType `hasInput`, from the
ChangeImpactAnalysis to the ChangeTrigger.

## Metadata

- name: ChangeTrigger
- SubclassOf: /Core/Artifact
- Instantiability: Concrete
