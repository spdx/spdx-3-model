SPDX-License-Identifier: Community-Spec-1.0

# VexNotAffectedVulnAssessmentRelationship

## Summary

Links a vulnerability and one or more elements designating the latter as products
not affected by the vulnerability.

## Description

VexNotAffectedVulnAssessmentRelationship connects a vulnerability and a number
of elements designating them as products not affected by the vulnerability.
This relationship corresponds to the VEX not_affected status.

*Constraints*

When linking elements using a VexNotVulnAffectedAssessmentRelationship, the
following requirements must be observed:

- Relating elements with a VexNotAffectedVulnAssessmentRelationship is
  restricted to the doesNotAffect relationship type.
- The from: end of the relationship must be a /Security/Vulnerability classed
  element.
- Both impactStatement and justificationType properties have a cardinality of
  0..1 making them optional. Nevertheless, to produce a valid VEX not_affected
  statement, one of them MUST be defined. This is specified in the Minimum
  Elements for VEX.

*Example*

```json
{
  "type": "VexNotAffectedVulnAssessmentRelationship",
  "spdxId": "urn:spdx.dev:vex-not-affected-1",
  "relationshipType": "doesNotAffect",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "security_assessedElement": "urn:npm-elliptic-6.5.2",
  "security_justificationType": "componentNotPresent",
  "security_impactStatement": "Not using this vulnerable part of this library.",
  "suppliedBy": ["urn:spdx.dev:agent-jane-doe"],
  "publishedTime": "2021-03-09T11:04:53Z"
}
```

## Metadata

- name: VexNotAffectedVulnAssessmentRelationship
- SubclassOf: VexVulnAssessmentRelationship
- Instantiability: Concrete

## Properties

- justificationType
  - type: VexJustificationType
  - minCount: 0
  - maxCount: 1
- impactStatement
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- impactStatementTime
  - type: /Core/DateTime
  - minCount: 0
  - maxCount: 1
