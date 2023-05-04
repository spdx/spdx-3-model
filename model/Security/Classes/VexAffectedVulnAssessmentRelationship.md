SPDX-License-Identifier: Community-Spec-1.0

# VexAffectedVulnAssessmentRelationship

## Summary

Connects a vulnerability and an element designating the element as a product
affected by the vulnerability.

## Description

VexAffectedVulnAssessmentRelationship connects a vulnerability and a number
of elements. The relationship marks these elements as products affected by the
vulnerability. This relationship corresponds to the VEX affected status.

When linking elements using a VexAffectedVulnAssessmentRelationship, the
following requirements must be observed:

- Elements linked with a VulnVexAffectedAssessmentRelationship are constrained
to the affects relationship type.

## Metadata

- name: VexAffectedVulnAssessmentRelationship
- SubclassOf: /Security/VexVulnAssessmentRelationship 
- Instantiability: Concrete

## Properties

- relationshipType
  - type: relationshipType
  - value: affects
- actionStatement
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- actionStatementTime
  - type: xsd:dateTime
  - minCount: 0
  - maxCount: 1
