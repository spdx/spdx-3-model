SPDX-License-Identifier: Community-Spec-1.0

# Need

## Summary

A Need is condition, objective or capability desired by a Role.

## Description

A Need represents the high-level intent expressed by Role during the Needs Analysis phase of the life cycle. It defines the problem space or desired capability before it is translated into verifiable system requirements.

This entity captures the natural language expression of the Need via the statement property, ensuring the Role's voice is preserved in the model. Role Needs are distinct from System Requirements; while requirements must be technically verifiable, needs express the underlying value or necessity that justifies the system's existence. Traceability from derived requirements back to Needs is essential to ensure alignment with stakeholder expectations with the RelationshipType 'satisfies'.

## Metadata

- name: Need
- SubclassOf: /Core/Element
- Instantiability: Concrete

## Properties

- statement
  - type: xsd:string
  - minCount: 1

## External properties restrictions

- /Core/Element/name
  - minCount: 1
