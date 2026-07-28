SPDX-License-Identifier: Community-Spec-1.0

# OpenSourceProject

## Summary

Project in the Open Source Community that shares their workproducts for reuse under an Open Source license.

## Description

Project in the Open Source Community that shares their workproducts for reuse under an Open Source license. 

## Metadata

- name: OpenSourceProject
- SubclassOf: Project
- Instantiability: Concrete

## Properties

- technicalScope
  - type: /Core/Artifact/intendedUse
  - maxCount: 1
- participationAgreements
  - type: /Core/Specification
  - maxCount: 1
- projectUrl
  - type: xsd:anyURI
  - maxCount: 1
- projectDocUrl
  - type: xsd:anyURI
  - minCount: 0
- projectHealthMetadataUrl
  - type: /Core/Annotation
  - maxCount: 1
- projectIssueTrackerUrl
  - type: xsd:anyURI
  - minCount: 0
- projectMailinglistUrl
  - type: /Core/ExternalIdentifier
  - minCount: 0
- projectSocialMediaUrl
  - type: /Core/ExternalIdentifier
  - minCount: 0
- projectCharter
  - type: projectContract
  - maxCount: 1
- contributionProcess
  - type: /Core/DefinedProcess
