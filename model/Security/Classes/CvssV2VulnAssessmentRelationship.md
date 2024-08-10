SPDX-License-Identifier: Community-Spec-1.0

# CvssV2VulnAssessmentRelationship

## Summary

Provides a CVSS version 2.0 assessment for a vulnerability.

## Description

A CvssV2VulnAssessmentRelationship relationship describes the determined score
and vector of a vulnerability as defined in
[A Complete Guide to the Common Vulnerability Scoring System Version 2.0](https://www.first.org/cvss/v2/guide).

It is intended to communicate the results of using a CVSS calculator.

*Constraints*

- The relationship type must be set to `hasAssessmentFor`.

*Example*

```json
{
  "type": "CvssV2VulnAssessmentRelationship",
  "spdxId": "urn:spdx.dev:cvssv2-cve-2020-28498",
  "relationshipType": "hasAssessmentFor",
  "security_score": "4.3",
  "security_vectorString": "(AV:N/AC:M/Au:N/C:P/I:N/A:N)",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "security_assessedElement": "urn:npm-elliptic-6.5.2",
  "externalRef": [
    {
      "type": "ExternalRef",
      "externalRefType": "securityAdvisory",
      "locator": "https://nvd.nist.gov/vuln/detail/CVE-2020-28498"
    },
    {
      "type": "ExternalRef",
      "externalRefType": "securityAdvisory",
      "locator": "https://snyk.io/vuln/SNYK-JS-ELLIPTIC-1064899"
    },
    {
      "type": "ExternalRef",
      "externalRefType": "securityFix",
      "locator": "https://github.com/indutny/elliptic/commit/441b742"
    }
  ],
  "suppliedBy": ["urn:spdx.dev:agent-my-security-vendor"],
  "publishedTime": "2023-05-06T10:06:13Z"
},
{
  "type": "Relationship",
  "spdxId": "urn:spdx.dev:vulnAgentRel-1",  
  "relationshipType": "publishedBy",  
  "from": "urn:spdx.dev:cvssv2-cve-2020-28498",
  "to": ["urn:spdx.dev:agent-snyk"],
  "startTime": "2021-03-08T16:06:50Z"
}
```

## Metadata

- name: CvssV2VulnAssessmentRelationship
- SubclassOf: VulnAssessmentRelationship
- Instantiability: Concrete

## Properties

- score
  - type: xsd:decimal
  - minCount: 1
  - maxCount: 1
- vectorString
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
