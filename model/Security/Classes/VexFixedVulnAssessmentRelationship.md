SPDX-License-Identifier: Community-Spec-1.0

# VexFixedVulnAssessmentRelationship

## Summary

Links a vulnerability and elements representing products (in the VEX sense) where
a fix has been applied and are no longer affected.

## Description

VexFixedVulnAssessmentRelationship links a vulnerability to a number of elements
representing VEX products where a vulnerability has been fixed and are no longer
affected. It represents the VEX fixed status.

When linking elements using a VexFixedVulnAssessmentRelationship, the following
requirements must be observed:

- Elements linked with a VulnVexFixedAssessmentRelationship are constrained to
using the fixedIn relationship type.
- The from: end of the relationship must be a /Security/Vulnerability classed
element.

## Metadata

- name: VexFixedVulnAssessmentRelationship
- SubclassOf:  /Security/VulnVexAssessmentRelationship
- Instantiability: Concrete

## Properties

- relationshipType
  - type: relationshipType
  - value: fixedIn
