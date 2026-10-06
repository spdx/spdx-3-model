SPDX-License-Identifier: Community-Spec-1.0

# Control

## Summary

Mechanisms or processes that reduce the probability of a threat occurring or minimize its consequences.

## Description

Controls are proactive measures, systems, tools, strategies, or protocols implemented to neutralize or reduce threats (
hazards) that could negatively impact an organization, system, project such as financial losses, data breaches, or
operational failures.

A Control can be described by concepts intending to establish protection:

* Security Requirements,
* Mitigations,
* Countermeasures,
* Operational Procedures,
* Defense Techniques.

Controls can be linked to existing elements in an SPDX document. I.e. an SBOM may be linked to a Control using
a ReferenceRelationship with relationship type 'establishedBy'.

## Metadata

- name: Control
- SubclassOf: /Core/Element
- Instantiability: Concrete

## Properties

- genericProtection
  - type: Assessment
  - minCount: 0
- type
  - type: ControlType
  - minCount: 0
- attribution
  - type: ControlAttribution
  - minCount: 0

