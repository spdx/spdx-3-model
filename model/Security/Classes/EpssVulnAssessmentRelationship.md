SPDX-License-Identifier: Community-Spec-1.0

# EpssVulnAssessmentRelationship

## Summary

Provides an EPSS assessment for a vulnerability.

## Description

An EpssVulnAssessmentRelationship relationship describes the likelihood or
probability that a vulnerability will be exploited in the wild using the Exploit
Prediction Scoring System (EPSS) as defined on 
[https://www.first.org/epss/model](https://www.first.org/epss/model).

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
