SPDX-License-Identifier: Community-Spec-1.0

# SafetyContextRelationship

## Summary

Provides functional safety context for an existing lifecycle-scoped relationship.

## Description

SafetyContextRelationship provides functional safety context for a relationship
between SPDX elements. It enables an existing relationship, such as a dependency
or requirement relationship, to carry a safety integrity level leveraging the existing
relationship types as needed for safety-related use case.

SafetyContextRelationship inherits lifecycle scope from
/Core/LifecycleScopedRelationship so the safety context can be interpreted for a
specific lifecycle phase, such as design, build, test, runtime, update, or
decommission.

## Metadata

- name: SafetyContextRelationship
- SubclassOf: /Core/LifecycleScopedRelationship
- Instantiability: Concrete

## Properties

- safetyIntegrityLevel
  - type: SafetyIntegrityLevelType
  - minCount: 0
  - maxCount: 1
