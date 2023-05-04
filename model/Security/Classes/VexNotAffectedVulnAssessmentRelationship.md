SPDX-License-Identifier: Community-Spec-1.0

# VexNotVulnAffectedAssessmentRelationship

## Summary

Links a vulnerability and one or more elements designating the latter as products
not affected by the vulnerability.

## Description

VexNotVulnAffectedAssessmentRelationship connects a vulnerability and a number
of elements desigating them as products not affected by the vulnerability.
This relationship corresponds to the VEX not_affected status.

When linking elements using a VexNotVulnAffectedAssessmentRelationship, the
following requirements must be observed:

- Relating elements with a VexNotVulnAffectedAssessmentRelationship is restricted
to the doesNotAffect relationship type.
- The from: end of the relationship must be a /Security/Vulnerability classed
element.
- Both impactStatement and justification properties have a cardinality of
0..1 making them optional. Nevertheless, to produce a valid VEX not_affected
statement, one of them MUST be defined. This is specfied in the Minimum Elements
for VEX.

## Metadata

- name: VulnVexNotAffectedAssessmentRelationship
- SubclassOf:  /Security/VexVulnAssessmentRelationship
- Instantiability: Concrete

## Properties

- relationshipType
  - type: relationshipType
  - value: doesNotAffect
- justification
  - type: justification
  - minCount: 0
  - maxCount: 1
- impactStatement
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- impactStatementTime
  - type: xsd:dateTime
  - minCount: 0
  - maxCount: 1
