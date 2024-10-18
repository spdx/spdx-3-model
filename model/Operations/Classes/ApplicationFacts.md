SPDX-License-Identifier: Community-Spec-1.0

# ApplicationFacts

## Summary

The Application facts summarize the business context metadata of an application. An application may consist of one to n deliverables.

## Description

The Application Facts are collected all along the product lifecyle and contents may be updated when the product reaches a new phase.
```

## Metadata

- name: ApplicationFacts
- SubclassOf: tbd
- Instantiability: Concrete

## Properties

- productOwner
  - type: tbd
  - minCount: 1
  - maxCount: 1

- documentationLink
  - type: tbd
  - minCount: 1
  - maxCount: 1

- productAccessURL
  - type: tbd
  - minCount: 1
  - maxCount: 1

- commentComment
  - type: tbd
  - minCount: 1
  - maxCount: 1

- distributedDeliverables
  - type: tbd
  - minCount: 1
  - maxCount: n

- technicalDeploymnent
  - type: tbd
  - minCount: 1
  - maxCount: 1

- contact
  - type: tbd
  - minCount: 1
  - maxCount: 1

- scope
  - type: tbd
  - minCount: 1
  - maxCount: 1

- relationType
  - type: tbd
  - minCount: 1
  - maxCount: 1

- supplyChainContext
  - type: tbd
  - minCount: 1
  - maxCount: 1

- releaseCycles
  - type: tbd
  - minCount: 1
  - maxCount: 1

- fossComplianceBundelProvision
  - type: tbd
  - minCount: 1
  - maxCount: 1

- contractSetup
  - type: tbd
  - minCount: 1
  - maxCount: 1

- fossTermsTowardsCustomer
  - type: tbd
  - minCount: 1
  - maxCount: 1

- distributionTermsTowardsCustomer
  - type: tbd
  - minCount: 1
  - maxCount: 1

- customerFossContact
  - type: tbd
  - minCount: 1
  - maxCount: 1