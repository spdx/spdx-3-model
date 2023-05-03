SPDX-License-Identifier: Community-Spec-1.0

# CvssV2VulnAssessmentRelationship

## Summary

Provides a CVSS version 2.0 assessment for a vulnerability.

## Description

A CvssV2VulnAssessmentRelationship relationship describes the characteristics and impact of a vulnerability using version 2.0 of the Common Vulnerability Scoring System
(CVSS) as defined on [https://www.first.org/cvss/v2/guide](https://www.first.org/cvss/v2/guide). 

## Metadata

- name: CvssV2VulnAssessmentRelationship
- SubclassOf: /Security/VulnAssessmentRelationship
- Instantiability: Concrete

## Properties

- score
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- severity
  - type: CvssV2SeverityType
  - minCount: 1
  - maxCount: 1
- vector
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
