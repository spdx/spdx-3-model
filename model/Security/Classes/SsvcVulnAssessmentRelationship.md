SPDX-License-Identifier: Community-Spec-1.0

# SsvcVulnAssessmentRelationship

## Summary

Provides a SSVC assessment for a vulnerability.

## Description

A SsvcVulnAssessmentRelationship relationship can be used to prioritize vulnerability response using the Stakeholder-Specific Vulnerability Categorization (SSVC) as defined in the [CISA SSVC Guide](https://www.cisa.gov/sites/default/files/publications/cisa-ssvc-guide%20508c.pdf).

## Metadata

- name: SsvcVulnAssessmentRelationship
- SubclassOf: /Security/VulnAssessmentRelationship
- Instantiability: Concrete

## Properties

- decision
  - type: SsvcDecisionType
  - minCount: 1
  - maxCount: 1

## Syntax

=== "JSON"

    ```json
    {
      "@type": "SsvcVulnAssessmentRelationship",
      "@id": "urn:spdx.dev:ssvc-1",
      "relationshipType": "hasSsvcAssessmentFor",
      "decision": "act",
      "from": "urn:spdx.dev:vuln-cve-2020-28498",
      "to": "urn:product-acme-application-1.3",
      "assessedElement": "urn:npm-elliptic-6.5.2",
      "creationInfo": {
        "@type": "CreationInformation",
        "created": "2021-03-09T20:05:53Z",
        "createdBy": ["urn:spdx.dev:agent-john-doe"]
      }
    }
    ```