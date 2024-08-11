SPDX-License-Identifier: Community-Spec-1.0

# CvssV4VulnAssessmentRelationship

## Summary

Provides a CVSS version 4 assessment for a vulnerability.

## Description

A CvssV4VulnAssessmentRelationship relationship describes the determined score,
severity, and vector of a vulnerability as defined in
[Common Vulnerability Scoring System version 4.0: Specification Document](https://www.first.org/cvss/v4.0/specification-document).

It is intended to communicate the results of using a CVSS calculator.

*Constraints*

- The relationship type must be set to hasAssessmentFor.

*Example*

```json
{
  "type": "CvssV4VulnAssessmentRelationship",
  "spdxId": "urn:spdx.dev:cvssv4-cve-2021-44228",
  "relationshipType": "hasAssessmentFor",
  "security_severity": "medium",
  "security_score": "10.0",
  "security_vectorString": "CVSS:4.0/AV:N/AC:L/AT:N/AR:N/UI:N/VCH/VI:H/VA:H/SC:H/SI:H/SA:H/E:A",
  "from": "urn:spdx.dev:vuln-cve-2021-44228",
  "to": ["urn:product-acme-application-1.3"],
  "security_assessedElement": "urn:apache-log4j-2.14.1",
  "externalRef": [
    {
      "@type": "ExternalRef",
      "externalRefType": "securityAdvisory",
      "locator": "https://nvd.nist.gov/vuln/detail/CVE-2021-44228"
    },
    {
      "@type": "ExternalRef",
      "externalRefType": "securityAdvisory",
      "locator": "https://logging.apache.org/log4j/2.x/security.html"
    },
    {
      "@type": "ExternalRef",
      "externalRefType": "securityOther",
      "locator": "https://www.first.org/cvss/v4.0/examples#Apache-log4j-Vulnerability-CVE-2021-44228"
    },
  ],
  "suppliedBy": ["urn:spdx.dev:agent-my-security-vendor"],
  "publishedTime": "2023-10-05T23:09:13Z"
},
{
  "type": "Relationship",
  "spdxId": "urn:spdx.dev:vulnAgentRel-1",
  "relationshipType": "publishedBy",
  "from": "urn:spdx.dev:cvssv4-cve-2021-44228",
  "to": ["urn:spdx.dev:agent-apache.org"],
  "startTime": "2021-12-11T18:39:00Z"
}
```

## Metadata

- name: CvssV4VulnAssessmentRelationship
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
