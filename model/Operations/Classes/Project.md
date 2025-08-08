SPDX-License-Identifier: Community-Spec-1.0

# Project

## Summary

Temporary endeavor with a beginning and an end and that must be used to create a unique product, service or result.
(based on PMBOK (Project Management Body of Knowledge) 3rd edition)

## Description

Temporary endeavor with a beginning and an end and that must be used to create a unique product, service or result.
(based on PMBOK (Project Management Body of Knowledge) 3rd edition)

## Metadata

- ProjectTitle
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- ProjectInformation
  - type: Core/Element/comment
  - minCount: 0
- ProjectContract
  - type: xsd:anyURI
  - minCount: 1
  - maxCount: 1
- ProjectSponsor
  - type: Core/Agent
  - maxCount: 1
- ProjectOwner
  - type: Core/Agent
  - minCount: 1
  - maxCount: 1
- ApplicationType
  - type: ApplicationType
  - minCount: 1
  - maxCount: 1
- DistributionMethod
  - type: DistributionMethodType
  - minCount: 1
- SCRMConcept
  - type: xsd:anyURI
  - maxCount: 1
- ComplianceBundleStorage
  - type: xsd:anyURI
  - maxCount: 1
- StartTime
  - type: /Core/DateTime
  - minCount: 1
  - maxCount: 1
- endTime
  - type: /Core/DateTime
  - maxCount: 1
