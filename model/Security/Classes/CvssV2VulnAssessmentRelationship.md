SPDX-License-Identifier: Community-Spec-1.0

# CvssV2VulnAssessmentRelationship

## Summary

Provides a CVSS version 2.0 assessment for a vulnerability.

## Description

A CvssV2VulnAssessmentRelationship relationship describes the determined score and vector of a vulnerability using version 2.0 of the Common Vulnerability Scoring System
(CVSS) as defined on [https://www.first.org/cvss/v2/guide](https://www.first.org/cvss/v2/guide). It is intented to communicate the results of using a CVSS calculator.

**Constraints**

The value of severity must be one of 'low', 'medium' or 'high'

**Syntax**

```json
{
  "@type": "CvssV2VulnAssessmentRelationship",
  "@id": "urn:spdx.dev:cvssv2-cve-2020-28498",
  "relationshipType": "hasCvssV2AssessmentFor",
  "score": 4.3,
  "vector": "(AV:N/AC:M/Au:N/C:P/I:N/A:N)",
  "severity": "low",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "assessedElement": "urn:npm-elliptic-6.5.2",
  "externalReferences": [
    {
      "@type": "ExternalReference",
      "externalReferenceType": "securityAdvisory",
      "locator": "https://nvd.nist.gov/vuln/detail/CVE-2020-28498"
    },
    {
      "@type": "ExternalReference",
      "externalReferenceType": "securityAdvisory",
      "locator": "https://snyk.io/vuln/SNYK-JS-ELLIPTIC-1064899"
    },
    {
      "@type": "ExternalReference",
      "externalReferenceType": "securityFix",
      "locator": "https://github.com/indutny/elliptic/commit/441b742"
    }
  ],
  "suppliedBy": ["urn:spdx.dev:agent-my-security-vendor"],
  "publishedTime": "2023-05-06T10:06:13Z"
},
{
  "@type": "Relationship",
  "@id": "urn:spdx.dev:vulnAgentRel-1",  
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
- severity
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- vector
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
