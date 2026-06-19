SPDX-License-Identifier: Community-Spec-1.0

# Project

## Summary

Temporary endeavor with a beginning and an end and that must be used to create a unique product, service or result.

## Description

Temporary endeavor with a beginning and an end and that must be used to create a unique product, service or result.

Based on the Project Management Body of Knowledge (PMBOK), 3rd edition.

`startTime` is the time at which a project starts or is planned to start.
`endTime` is the time at which a project ends or is planned to end.

## Metadata

- name: Project
- SubclassOf: /Core/Bundle
- Instantiability: Concrete

## Properties

- /Core/endTime
  - type: /Core/DateTime
  - maxCount: 1
- /Core/startTime
  - type: /Core/DateTime
  - minCount: 1
  - maxCount: 1
- /Core/intendedUse
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- docUrl
  - type: xsd:anyURI
  - minCount: 0
- homePageUrl
  - type: xsd:anyURI
  - minCount: 0
  - maxCount: 1
- projectIssueTrackerUrl
  - type: xsd:anyURI
  - minCount: 0
- mediaChannel
  - type: /Core/ExternalIdentifier
  - minCount: 0
- projectTitle
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- projectContract
  - type: xsd:anyURI
  - minCount: 1
  - maxCount: 1
- projectSponsor
  - type: /Core/Agent
- projectOwner
  - type: /Core/Agent
  - minCount: 1
  - maxCount: 1
