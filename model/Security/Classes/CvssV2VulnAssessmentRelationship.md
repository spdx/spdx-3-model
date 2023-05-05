SPDX-License-Identifier: Community-Spec-1.0

# CvssV2VulnAssessmentRelationship

## Summary

Provides a CVSS version 2.0 assessment for a vulnerability.

## Description

A CvssV2VulnAssessmentRelationship relationship describes the determined score, severity, and vector of a vulnerability using version 2.0 of the Common Vulnerability Scoring System
(CVSS) as defined on [https://www.first.org/cvss/v2/guide](https://www.first.org/cvss/v2/guide). It is intented to communicate the results of using a CVSS calculator.

## Metadata

- name: CvssV2VulnAssessmentRelationship
- SubclassOf: /Security/VulnAssessmentRelationship
- Instantiability: Concrete

## Properties

- score
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- severity
  - type: CvssV2SeverityType
  - minCount: 0
  - maxCount: 1
- vector
  - type: xsd:string
  - minCount: 0
  - maxCount: 1

## Syntax

=== "JSON"

    ```json
    {
      "@type": "CvssV2VulnAssessmentRelationship",
      "@id": "urn:spdx.dev:cvssv2-cve-2020-28498",
      "relationshipType": "hasCvssV2AssessmentFor",
      "severity": "medium",
      "score": "4.3",
      "vector": "(AV:N/AC:M/Au:N/C:P/I:N/A:N)",
      "from": "urn:spdx.dev:vuln-cve-2020-28498",
      "to": "urn:product-acme-application-1.3",
      "assessedElements": "urn:npm-elliptic-6.5.2",
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
      ]
    },
    {
      "@type": "Relationship",
      "@id": "urn:spdx.dev:vulnAgentRel-1",  
      "relationshipType": "foundBy",  
      "from": "urn:spdx.dev:cvssv2-cve-2020-28498",
      "to": ["urn:spdx.dev:agent-snyk"],
      "startTime": "2021-03-08T16:06:50Z"
    }
    ```
