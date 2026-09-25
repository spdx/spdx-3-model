SPDX-License-Identifier: Community-Spec-1.0

# Decision

## Summary

Describes a recorded decision.

## Description

A Decision represents a determination made by an Agent or organization after
considering one or more inputs. It can be used by any profile that needs to
communicate an outcome such as approving, conditionally approving, rejecting,
deferring, delegating, requesting information or change, recording no action,
or closing a work item.

Decision is modeled as an Action so existing Relationship entries can describe
its context. A process or analysis that produces a Decision can link to it using
`hasOutput`; for example, a ChangeImpactAnalysis can use
`ChangeImpactAnalysis hasOutput Decision` to record that the analysis produced
one or more decisions. Use `hasInput` relationships from the Decision to the
specific Element or Elements the decision applies to, such as a requirement,
vulnerability, evidence record, ticket, or other record. Use `hasOutput`
relationships from the Decision to any Element produced by the decision, such
as a follow-up work item, closure record, revised requirement, or evidence
artifact.

Because Decision is an Action, the inherited `originatedBy` property identifies
the Agent that recorded or issued the decision. The `rationale` property can be
used to explain why the decision was made.

## Metadata

- name: Decision
- SubclassOf: Action
- Instantiability: Concrete

## Properties

- decisionType
  - type: DecisionType
  - minCount: 1
  - maxCount: 1
- decisionStatus
  - type: DecisionStatusType
  - minCount: 0
  - maxCount: 1
- rationale
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
