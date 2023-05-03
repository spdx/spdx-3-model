SPDX-License-Identifier: Community-Spec-1.0

# CvssV3VulnAssessmentRelationship

## Summary

Provides a CVSS version 3.x assessment for a vulnerability.

## Description

A CvssV2VulnAssessmentRelationship relationship describes the characteristics and impact of a vulnerability using version 3.1 of the Common Vulnerability Scoring System (CVSS) as defined on [https://www.first.org/cvss/v3.1/specification-document](https://www.first.org/cvss/v3.1/specification-document). 

## Metadata

- name: CvssV3VulnAssessmentRelationship
- SubclassOf: /Security/VulnAssessmentRelationship
- Instantiability: Concrete

## Properties

- score
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- severity
  - type: CvssV3SeverityType
  - minCount: 1
  - maxCount: 1
- vector
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
