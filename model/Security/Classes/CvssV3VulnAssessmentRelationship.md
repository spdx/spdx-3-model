SPDX-License-Identifier: Community-Spec-1.0

# CvssV3VulnAssessmentRelationship

## Summary

Provides a CVSS version 3 assessment for a vulnerability.

## Description

A CvssV3VulnAssessmentRelationship relationship describes the determined score,
severity, and vector of a vulnerability using version [3.0](https://www.first.org/cvss/v3.0/specification-document) or [3.1](https://www.first.org/cvss/v3.1/specification-document) of the Common
Vulnerability Scoring System (CVSS). It is intended to communicate the results of using a CVSS calculator.

**Constraints**

- The value of severity must be one of 'NONE', 'LOW', 'MEDIUM', 'HIGH' or 'CRITICAL'.
- The relationship type must be set to `hasAssessmentFor`.

**Syntax**

```json
{
  "@type": "CvssV3VulnAssessmentRelationship",
  "@id": "urn:spdx.dev:cvssv3-cve-2020-28498",
  "relationshipType": "hasAssessmentFor",
  "score": 6.8,
  "severity": "MEDIUM",
  "vectorString": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:N/A:N",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "assessedElement": "urn:npm-elliptic-6.5.2",
  "externalRefs": [
    {
      "@type": "ExternalRef",
      "externalRefType": "securityAdvisory",
      "locator": "https://nvd.nist.gov/vuln/detail/CVE-2020-28498"
    },
    {
      "@type": "ExternalRef",
      "externalRefType": "securityAdvisory",
      "locator": "https://snyk.io/vuln/SNYK-JS-ELLIPTIC-1064899"
    },
    {
      "@type": "ExternalRef",
      "externalRefType": "securityFix",
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
  "from": "urn:spdx.dev:cvssv3-cve-2020-28498",
  "to": "urn:spdx.dev:agent-snyk",
  "startTime": "2021-03-08T16:06:50Z"
}
```

## Metadata

- name: CvssV3VulnAssessmentRelationship
- SubclassOf: VulnAssessmentRelationship
- Instantiability: Concrete

## Properties

- score
  - type: xsd:decimal
  - minCount: 1
  - maxCount: 1
- severity
  - type: CvssSeverityType
  - minCount: 1
  - maxCount: 1
- vectorString
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
