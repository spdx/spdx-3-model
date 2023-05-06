SPDX-License-Identifier: Community-Spec-1.0

# VexAffectedVulnAssessmentRelationship

## Summary

Connects a vulnerability and an element designating the element as a product
affected by the vulnerability.

## Description

VexAffectedVulnAssessmentRelationship connects a vulnerability and a number
of elements. The relationship marks these elements as products affected by the
vulnerability. This relationship corresponds to the VEX affected status.

**Constraints**

When linking elements using a VexAffectedVulnAssessmentRelationship, the
following requirements must be observed:

- Elements linked with a VulnVexAffectedAssessmentRelationship are constrained
to the affects relationship type.

**Syntax**

```json
{
  "@type": "VexAffectedVulnAssessmentRelationship",
  "@id": "urn:spdx.dev:vex-affected-1",
  "relationshipType": "affects",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "assessedElement": "urn:npm-elliptic-6.5.2",
  "actionStatement": "Upgrade to version 1.4 of ACME application.",
  "suppliedBy": ["urn:spdx.dev:agent-jane-doe"],
  "publishedTime": "2021-03-09T11:04:53Z"
}
```

## Metadata
- name: VexAffectedVulnAssessmentRelationship
- SubclassOf: VexVulnAssessmentRelationship 
- Instantiability: Concrete

## Properties
- actionStatement
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- actionStatementTime
  - type: xsd:dateTime
  - minCount: 0
