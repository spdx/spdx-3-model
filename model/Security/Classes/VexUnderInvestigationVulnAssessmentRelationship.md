SPDX-License-Identifier: Community-Spec-1.0

# VexUnderInvestigationVulnAssessmentRelationship

## Summary

Designates elements as products where the impact of a vulnerability is being
investigated.

## Description

VexUnderInvestigationVulnAssessmentRelationship links a vulnerability to a
number of products stating the vulnerability's impact on them is being
investigated. It represents the VEX under_investigation status.

*Constraints*

When linking elements using a VexUnderInvestigationVulnAssessmentRelationship
the following requirements must be observed:

- Elements linked with a VexUnderInvestigationVulnAssessmentRelationship are
  constrained to using the underInvestigationFor relationship type.
- The from: end of the relationship must be a /Security/Vulnerability classed
  element.

*Example*

```json
{
  "type": "VexUnderInvestigationVulnAssessmentRelationship",
  "spdxId": "urn:spdx.dev:vex-underInvestigation-1",
  "relationshipType": "underInvestigationFor",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "security_assessedElement": "urn:npm-elliptic-6.5.2",
  "suppliedBy": ["urn:spdx.dev:agent-jane-doe"],
  "publishedTime": "2021-03-09T11:04:53Z"
}
```

## Metadata

- name: VexUnderInvestigationVulnAssessmentRelationship
- SubclassOf:  VexVulnAssessmentRelationship
- Instantiability: Concrete
