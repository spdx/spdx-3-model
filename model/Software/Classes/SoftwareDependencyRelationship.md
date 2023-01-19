SPDX-License-Identifier: Community-Spec-1.0

# SoftwareDependencyRelationship

## Description

TODO

## Metadata

- name: SoftwareDependencyRelationship
- SubclassOf: /Core/LifecycleScopedRelationship
- Instantiability: Concrete

## Properties

- softwareLinkage
  - type: SoftwareDependencyLinkType
  - minCount: 0
  - maxCount: 1
- conditionality
  - type: DependencyConditionalityType
  - minCount: 0
  - maxCount: 1
