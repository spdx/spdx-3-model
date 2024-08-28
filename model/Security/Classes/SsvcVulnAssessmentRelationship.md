SPDX-License-Identifier: Community-Spec-1.0

# SsvcVulnAssessmentRelationship

## Summary

Provides an SSVC assessment for a vulnerability.

## Description

An SsvcVulnAssessmentRelationship describes the decision made using the
Stakeholder-Specific Vulnerability Categorization (SSVC) decision tree as
defined by
[CISA Stakeholder-Specific Vulnerability Categorization Guide](https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc).

It is intended to communicate the results of using the CISA SSVC Calculator.

*Constraints*

- The relationship type must be set to hasAssessmentFor.

*Example*

```json
{
  "@type": "SsvcVulnAssessmentRelationship",
  "@id": "urn:spdx.dev:ssvc-1",
  "relationshipType": "hasAssessmentFor",
  "security_decisionType": "act",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "security_assessedElement": "urn:npm-elliptic-6.5.2",
  "suppliedBy": ["urn:spdx.dev:agent-jane-doe"],
  "publishedTime": "2021-03-09T11:04:53Z"
}
```

## Metadata

- name: SsvcVulnAssessmentRelationship
- SubclassOf: VulnAssessmentRelationship
- Instantiability: Concrete

## Properties

- decisionType
  - type: SsvcDecisionType
  - minCount: 1
  - maxCount: 1
