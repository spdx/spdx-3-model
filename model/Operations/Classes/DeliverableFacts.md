SPDX-License-Identifier: Community-Spec-1.0

# DeliverableFacts

## Summary

A deliverable is a part of a product. The deliverable facts shall collect metadata that typically cannot be derived from the repository content.

## Description

The deliverable facts are collected and update in all deliverable lifecycle phases. So data could already collected in the architecture/design phase and then be updated along the furter development. The data might be needed to take design decisions and configure the environment. By having the structured explicit documentation, unnecessary iterations may be avoided.

## Metadata

- name: DeliverableFacts
- SubclassOf: Delivery
- Instantiability: Concrete

## Properties

- programmingLanguage
  - type: ProgrammingLanguageType
  - minCount: 1
- dependencyManager
  - type: DependencyManagerType
  - minCount: 1
- packageManager
  - type: PackageManagerType
  - minCount: 1
- environmentFramework
  - type: EnvironmentFrameworkType
  - minCount: 1
- applicationCategory
  - type: ApplicationCategoryType
  - minCount: 1
  - maxCount: 1
- applicationType
  - type: ApplicationType
  - minCount: 1
  - maxCount: 1
- distributionMethod
  - type: DistributionMethodType
  - minCount: 1
  - maxCount: n
- operatingSystem
  - type: OperatingSystemType
  - minCount: 1
  - maxCount: 1
- consistsOf
  - type: /Core/Artifact
  - minCount: 1
- developedBy
  - type: /Core/Agent
  - minCount: 1
- contact
  - type: /Core/Agent
  - minCount: 1
- linkToArchitecture
  - type: xsd:anyURI
  - minCount: 1
  - maxCount: 1
- osmConcept
  - type: xsd:anyURI
  - minCount: 1
  - maxCount: 1
- fossComplianceBundleStorage
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- reviews
  - type: xsd:anyURI
  - minCount: 1
- deliverableComment
  - type: xsd:string
  - maxCount: 1
- supplierDeliverableFacts
  - type: Delivery
  - minCount: 0
