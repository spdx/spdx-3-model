SPDX-License-Identifier: Community-Spec-1.0

# OpenSourceProject

## Summary

Project in the Open Source Community that shares their workproducts for reuse under an Open Source license.

## Description

An Open Source Project is a collaborative endeavor to create workproducts where the source code is made publicly accessibe. 
The project is governed by an open source license that allows anyone to inspect, modify, enhance, and share the code.
An Open Source Project can serve as source for downstream derivatives in the context of a supply chain.
(The definition of an 'Open Source Project' is derived from the principles in the Open Source Definition (https://opensource.org/osd). The definition of 'Upstream Project' is based on the community-accepted meaning described in sources like Wikipedia (https://en.wikipedia.org/wiki/Upstream_(software_development)).)

## Metadata

- name: OpenSourceProject
- SubclassOf: /Project
- Instantiability: Concrete

## Properties

- projectUrl
  - type: /Software/Package/homePage
  - maxCount: 1
- codeRepository
  - type: xsd:anyURI
  - minCount: 1
  - maxCount: 1
- binaryRepoUrl
  - type: /Software/Package/downloadLocation
- containerRepoUrl
  - type: /Software/Package/downloadLocation
- dependencies
  - type: /Software/Sbom
  - maxCount: 1
- projectDocUrl
  - type: /Software/SoftwareArtifact
- technicalScope
  - type: /Core/Bundle/context
  - maxCount: 1
- technicalDomain
  - type: /Software/SoftwareArtifact/primaryPurpose
  - maxCount: 1
- projectSizeLoc
  - type: xsd:positiveInteger
  - maxCount: 1
- projectHealthMetadataUrl
  - type: /Software/Package/downloadLocation
- projectIssueTrackerUrl
  - type: /Software/Package/downloadLocation
  - maxCount: 1
- projectMailinglistUrl
  - type: /Software/Package/downloadLocation
  - maxCount: 1
- projectSocialMediaUrl
  - type: /Software/Package/downloadLocation
- projectInboundLicense
  - type: /SimpleLicensing/AnyLicenseInfo
  - maxCount: 1
- projectLicense
  - type: /SimpleLicensing/AnyLicenseInfo
  - minCount: 1
  - maxCount: 1
- hostFoundation
  - type: /projectSponsor
  - maxCount: 1
- hostCommunity
  - type: /projectSponsor
  - maxCount: 1
- steward
  - type: /projectOwner
  - minCount: 1
  - maxCount: 1
- projectCharter
  - type: /projectContract
  - maxCount: 1
- participationAgreements
  - type: /projectContract
- contributionProcess
  - type: /Core/DefinedProcess
  - maxCount: 1
