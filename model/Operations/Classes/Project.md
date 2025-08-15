SPDX-License-Identifier: Community-Spec-1.0

# Project

## Summary

Temporary endeavor with a beginning and an end and that must be used to create a unique product, service or result.

## Description

Temporary endeavor with a beginning and an end and that must be used to create a unique product, service or result.

Based on the Project Management Body of Knowledge (PMBOK), 3rd edition.

## Metadata

- name: Project
- SubclassOf: /Core/Bundle
- Instantiability: Concrete

## Properties

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
- projectStartTime
  - type: /Core/DateTime
  - minCount: 1
  - maxCount: 1
- projectEndTime
  - type: /Core/DateTime
  - maxCount: 1
