SPDX-License-Identifier: Community-Spec-1.0

# VexFixedVulnAssessmentRelationship

## Summary

Links a vulnerability and elements representing products (in the VEX sense) where
a fix has been applied and are no longer affected.

## Description

VexFixedVulnAssessmentRelationship links a vulnerability to a number of elements
representing VEX products where a vulnerability has been fixed and are no longer
affected. It represents the VEX fixed status.

*Constraints*

When linking elements using a VexFixedVulnAssessmentRelationship, the following
requirements must be observed:

- Elements linked with a VulnVexFixedAssessmentRelationship are constrained to
  using the fixedIn relationship type.
- The from: end of the relationship must be a /Security/Vulnerability classed
  element.

*Example*

```json
{
  "type": "VexFixedVulnAssessmentRelationship",
  "spdxId": "urn:spdx.dev:vex-fixed-in-1",
  "relationshipType": "fixedIn",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "security_assessedElement": "urn:npm-elliptic-6.5.4",
  "suppliedBy": ["urn:spdx.dev:agent-jane-doe"],
  "publishedTime": "2021-03-09T11:04:53Z"
}
```

## Metadata

- name: VexFixedVulnAssessmentRelationship
- SubclassOf: VexVulnAssessmentRelationship
- Instantiability: Concrete
