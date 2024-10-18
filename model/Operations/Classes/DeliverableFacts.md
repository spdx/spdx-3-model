SPDX-License-Identifier: Community-Spec-1.0

# DeliverableFacts

## Summary

A deliverable is a part of a product. The deliverable facts shall collect metadata that typically cannot be derived from the repository content.

## Description

The deliverable facts are collected and update in all deliverable lifecycle phases. So data could already collected in the architecture/design phase and then be updated along the furter development. The data might be needed to take design decisions and configure the environment. By having the structured explicit documentation, unnecessary iterations may be avoided.

## Metadata

- name: DeliverableFacts
- SubclassOf: tbd
- Instantiability: Concrete

## Properties

- programmingLanguage
  - type: tbd
  - minCount: 1
  - maxCount: n

- dependencyManager
  - type: tbd
  - minCount: 1
  - maxCount: n

- packageManager
  - type: tbd
  - minCount: 1
  - maxCount: n

- environmentFramework
  - type: tbd
  - minCount: 1
  - maxCount: n

- applicationCategory
  - type: tbd
  - minCount: 1
  - maxCount: 1

- applicationType
  - type: tbd
  - minCount: 1
  - maxCount: 1

- distributionMethod
  - type: tbd
  - minCount: 1
  - maxCount: 1

- operatingSystem
  - type: tbd
  - minCount: 1
  - maxCount: 1

- consistsOf
  - type: tbd
  - minCount: 1
  - maxCount: n

- developedBy
  - type: tbd
  - minCount: 1
  - maxCount: n

- contact
  - type: tbd
  - minCount: 1
  - maxCount: n

- linkToArchitecture
  - type: tbd
  - minCount: 1
  - maxCount: 1

- osmConcept
  - type: tbd
  - minCount: 1
  - maxCount: 1

- fossComplianceBundleStorage
  - type: tbd
  - minCount: 1
  - maxCount: 1

- reviews
  - type: tbd
  - minCount: 1
  - maxCount: n

- comment
  - type: tbd
  - minCount: 1
  - maxCount: n

[//]: the parts below should be a class that can be instantiated 0:n

- supplierDeliverableFacts
  - type: tbd
  - minCount: 1
  - maxCount: n

- supplierName
  - type: tbd
  - minCount: 1
  - maxCount: n

- deliverableFromSupplier
  - type: tbd
  - minCount: 1
  - maxCount: n

- fossTermsTowardsSupplier
  - type: tbd
  - minCount: 1
  - maxCount: n

- distributionTermsFromSupplier
  - type: tbd
  - minCount: 1
  - maxCount: n

- fossComplianceBundleConsumption
  - type: tbd
  - minCount: 1
  - maxCount: n

- supplierFossContact
  - type: tbd
  - minCount: 1
  - maxCount: n