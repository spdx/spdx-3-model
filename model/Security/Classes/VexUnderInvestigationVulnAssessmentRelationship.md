SPDX-License-Identifier: Community-Spec-1.0

# VexUnderInvestigationVulnAssessmentRelationship

## Summary

Designates elements as products where the impact of a vulnerability is being
investigated.

## Description

VexUnderInvestigationVulnAssessmentRelationship links a vulnerability to a
number of products stating the vulnerability's impact on them is being
investigated. It represents the VEX under_investigation status.

When linking elements using a VexUnderInvestigationVulnAssessmentRelationship
the following requirements must be observed:

- Elements linked with a VexUnderInvestigationVulnAssessmentRelationship are
constrained to using the underInvestigationFor relationship type.
- The from: end of the relationship must ve a /Security/Vulnerability classed
element.

## Metadata

- name: VexUnderInvestigationVulnAssessmentRelationship
- SubclassOf:  /Security/VexVulnAssessmentRelationship
- Instantiability: Concrete

## Properties

- relationshipType
  - type: relationshipType
  - value: underInvestigationFor
