SPDX-License-Identifier: Community-Spec-1.0

# SoftwareDependencyRelationship

## Description

TODO

## Metadata

- name: SoftwareDependencyRelationship
- SubclassOf: Core:Relationship
- Instantiability: Concrete

## Properties

- linkType
  - type: DependencyLinkType
  - minCount: 1
  - maxCount: 1
- scope
  - type: DependencyScope
  - minCount: 1
  - maxCount: 1
- requirement
  - type: DependencyRequirement
  - minCount: 1
  - maxCount: 1
