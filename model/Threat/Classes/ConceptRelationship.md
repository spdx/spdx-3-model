SPDX-License-Identifier: Community-Spec-1.0

# ConceptRelationship

## Summary

Enables to model conceptual relationships between Threats and Controls with other elements.

## Description

The relationship can be used to describe a Threat or a Control using other elements or concepts. 

This relationship is restricted to the `basedOn`, `relatedTo`, and `excludes` relationship type.

## Metadata

- name: ConceptRelationship
- SubclassOf: /Core/Relationship
- Instantiability: Concrete

## Properties

- /Core/rationale
  - type: String
  - minCount: 1
  - maxCount: 1
- scope
  - type: ScopeType
  - minCount: 0
  - maxCount: 1
