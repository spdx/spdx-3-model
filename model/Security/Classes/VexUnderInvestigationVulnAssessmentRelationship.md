SPDX-License-Identifier: Community-Spec-1.0

# VexUnderInvestigationVulnAssessmentRelationship

## Summary

Designates elements as products where the impact of a vulnerability is being
investigated.

## Description

VexUnderInvestigationVulnAssessmentRelationship links a vulnerability to a
number of products stating the vulnerability's impact on them is being
investigated. It represents the VEX under_investigation status.

**Constraints**

When linking elements using a VexUnderInvestigationVulnAssessmentRelationship
the following requirements must be observed:

- Elements linked with a VexUnderInvestigationVulnAssessmentRelationship are
constrained to using the underInvestigationFor relationship type.
- The from: end of the relationship must ve a /Security/Vulnerability classed
element.

## Metadata

- name: VexUnderInvestigationVulnAssessmentRelationship
- SubclassOf:  /Security/VexVulnAssessmentRelationship
- Instantiability: Concrete

## Properties

- relationshipType
  - type: relationshipType
  - value: underInvestigationFor

## Syntax

=== "JSON"

    ```json
    {
      "@type": "VexUnderInvestigationVulnAssessmentRelationship",
      "@id": "urn:spdx.dev:vex-underInvestigation-1",
      "relationshipType": "underInvestigationFor",
      "from": "urn:spdx.dev:vuln-cve-2020-28498",
      "to": "urn:product-acme-application-1.3",
      "assessedElement": "urn:npm-elliptic-6.5.2",
      "creationInfo": {
        "@type": "CreationInformation",
        "created": "2021-03-09T21:02:13Z",
        "createdBy": ["urn:spdx.dev:agent-jason-doe"]
      }
    }
    ```