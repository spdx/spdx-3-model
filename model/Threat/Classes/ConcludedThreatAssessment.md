SPDX-License-Identifier: Community-Spec-1.0

# ConcludedThreatAssessment

## Summary

The ConcludedThreatAssessment element concludes an evaluation of one or more threats while anticipating existing 
controls.

## Description

While the assessment of demand, impact, and protection against assets, capabilities, threats, and controls  
evaluate independent of further context information, the ConcludedThreatAssessment allows to evaluate the impact of a 
set of Threats in relation to an affected subject. The ConcludedThreatAssessment element may take the established 
controls into account.

## Metadata

- name: Control
- SubclassOf: /Core/Element
- Instantiability: Concrete

## Properties

- threat
  - type: Threat
  - minCount: 1
- control
  - type: Control
  - minCount: 0
- affectedSubject
  - type: /Core/Element
  - minCount: 1
- impact
  - type: Assessment
  - minCount: 1
