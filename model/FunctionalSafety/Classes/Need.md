SPDX-License-Identifier: Community-Spec-1.0

# Need

## Summary

A Need is condition, objective or capability desired by a Role or Element.

## Description

A Need represents the high-level intent expressed by Role or Element. It defines the problem space or desired capability before it is translated into verifiable system requirements.

This entity captures the natural language expression of the Need via the need property, ensuring the Role or Elements voice is preserved in the model.  Needs are distinct from System Requirements; needs express the underlying value or necessity that justifies the system's existence. Traceability from derived requirements back to Needs is essential to ensure alignment with stakeholder expectations with the RelationshipType 'satisfies'.

## Metadata

- name: Need
- SubclassOf: /Core/Element
- Instantiability: Concrete

## Properties

- need
  - type: xsd:string
  - minCount: 1
- status
  - type: StatusType
  - minCount: 0
  - maxCount: 1
- priority
  - type: /Core/DefinedType
  - minCount: 0
  - maxCount: 1

## External properties restrictions

- /Core/Element/name
  - minCount: 1
