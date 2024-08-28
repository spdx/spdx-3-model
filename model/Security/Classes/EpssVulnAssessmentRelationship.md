SPDX-License-Identifier: Community-Spec-1.0

# EpssVulnAssessmentRelationship

## Summary

Provides an EPSS assessment for a vulnerability.

## Description

An EpssVulnAssessmentRelationship relationship describes the likelihood or
probability that a vulnerability will be exploited in the wild, and the
percentile ranking of probability relative to all other vulnerabilities' EPSS
scores, using the Exploit Prediction Scoring System (EPSS) as defined at
[The EPSS Model](https://www.first.org/epss/model).

*Constraints*

- The relationship type must be set to hasAssessmentFor.
- The probability must be between 0 and 1.
- The percentile must be between 0 and 1.

*Example*

```json
{
  "type": "EpssVulnAssessmentRelationship",
  "spdxId": "urn:spdx.dev:epss-CVE-2020-28498",
  "relationshipType": "hasAssessmentFor",
  "security_probability": "0.00105",
  "security_percentile": "0.42356",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "suppliedBy": ["urn:spdx.dev:agent-jane-doe"],
  "publishedTime": "2023-10-05T00:00:30Z"
}
```

## Metadata

- name: EpssVulnAssessmentRelationship
- SubclassOf: VulnAssessmentRelationship
- Instantiability: Concrete

## Properties

- probability
  - type: xsd:decimal
  - minCount: 1
  - maxCount: 1
- percentile
  - type: xsd:decimal
  - minCount: 1
  - maxCount: 1

## External properties restrictions

- /Security/VulnAssessmentRelationship/publishedTime
  - minCount: 1
