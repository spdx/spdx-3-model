SPDX-License-Identifier: Community-Spec-1.0

# Project

## Summary

Temporary endeavor with a beginning and an end and that must be used to create a unique product, service or result.

## Description

Temporary endeavor with a beginning and an end and that must be used to create a unique product, service or result.

Based on the Project Management Body of Knowledge (PMBOK), 3rd edition.

## Metadata

- name: Project
- SubclassOf: /Core/Organization
- Instantiability: Abstract

## Properties

- projectTitle
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- projectInformation
  - type: /Core/description
  - minCount: 0
- projectContract
  - type: xsd:anyURI
  - minCount: 1
  - maxCount: 1
- projectSponsor
  - type: /Core/Agent
  - maxCount: 1
- projectOwner
  - type: Core/Agent
  - minCount: 1
  - maxCount: 1
- applicationType
  - type: ApplicationType
  - minCount: 1
  - maxCount: 1
- distributionMethod
  - type: DistributionMethodType
  - minCount: 1
  scrmConcept
  - type: xsd:anyURI
  - maxCount: 1
- complianceBundleStorage
  - type: xsd:anyURI
  - maxCount: 1
- projectStartTime
  - type: /Core/DateTime
  - minCount: 1
  - maxCount: 1
- projectEndTime
  - type: /Core/DateTime
  - maxCount: 1
