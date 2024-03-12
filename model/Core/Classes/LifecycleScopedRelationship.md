SPDX-License-Identifier: Community-Spec-1.0

# LifecycleScopedRelationship

## Summary

Provide context for a relationship that occurs in the lifecycle.

## Description

Certain relationships are sensitive to where they occur in the lifecycle.  This parameter lets us avoid a proliferation of relationships, by parameterizing this context information for a relationship.

## Metadata

- name: LifecycleScopedRelationship
- SubclassOf: Relationship
- Instantiability: Concrete

## Properties

- scope
  - type: LifecycleScopeType
  - minCount: 0
  - maxCount: 1

