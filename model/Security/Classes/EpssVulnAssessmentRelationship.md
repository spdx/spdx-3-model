SPDX-License-Identifier: Community-Spec-1.0

# EpssVulnAssessmentRelationship

## Summary

Provides a EPSS assessment for a vulnerability.

## Description

A EpssVulnAssessmentRelationship relationship describes the likelihood that a vulnerability will be exploited in the wild using the Exploit Prediction Scoring System (EPSS) as defined on [https://www.first.org/epss/model](https://www.first.org/epss/model).

## Metadata

- name: EpssVulnAssessmentRelationship
- SubclassOf: /Security/VulnAssessmentRelationship
- Instantiability: Concrete

## Properties

- probability
  - type: xsd:nonNegativeInteger
  - minCount: 1
  - maxCount: 1
- severity
  - type: xsd:string
  - minCount: 0
  - maxCount: 1

## Syntax

=== "JSON"

    ```json
    {
      "@type": "EpssVulnAssessmentRelationship",
      "@id": "urn:spdx.dev:epss-1",
      "relationshipType": "hasEpssAssessmentFor",
      "probability": 80,
      "from": "urn:spdx.dev:vuln-cve-2020-28498",
      "to": "urn:product-acme-application-1.3",
      "creationInfo": {
        "@type": "CreationInformation",
        "created": "2021-03-09T11:04:53Z",
        "createdBy": ["urn:spdx.dev:agent-jane-doe"]
      }
    }
    ```
