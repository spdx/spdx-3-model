SPDX-License-Identifier: Community-Spec-1.0

# VexAffectedVulnAssessmentRelationship

## Summary

Connects a vulnerability and an element designating the element as a product
affected by the vulnerability.

## Description

VexAffectedVulnAssessmentRelationship connects a vulnerability and a number
of elements. The relationship marks these elements as products affected by the
vulnerability. This relationship corresponds to the VEX affected status.

**Constraints**

When linking elements using a VexAffectedVulnAssessmentRelationship, the
following requirements must be observed:

- Elements linked with a VulnVexAffectedAssessmentRelationship are constrained
to the affects relationship type.

## Metadata
- name: VexAffectedVulnAssessmentRelationship
- SubclassOf: /Security/VexVulnAssessmentRelationship 
- Instantiability: Concrete

## Properties
- relationshipType
  - type: relationshipType
  - value: affects
- actionStatement
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- actionStatementTime
  - type: xsd:dateTime
  - minCount: 0

## Syntax

=== "JSON"

    ```json
    {
      "@type": "VexAffectedVulnAssessmentRelationship",
      "@id": "urn:spdx.dev:vex-affected-1",
      "relationshipType": "affects",
      "from": "urn:spdx.dev:vuln-cve-2020-28498",
      "to": "urn:product-acme-application-1.3",
      "assessedElements": "urn:npm-elliptic-6.5.2",
      "actionStatement": "Upgrade to version 1.4 of ACME application.",
      "creationInfo": {
        "@type": "CreationInformation",
        "created": "2021-03-09T21:02:13Z",
        "createdBy": ["urn:spdx.dev:agent-jason-doe"]
      }
    }
    ```
