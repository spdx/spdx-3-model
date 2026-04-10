SPDX-License-Identifier: Community-Spec-1.0

# Assumption

## Summary

A distinct unit representing a constraint associated with an item's use in a system.

## Description

An assumption element is a distinct unit that defines a design constraint.
This constraint is imposed by the intended design, the requirement context, or the operational context.
It ensures the item operates correctly within a system context.

## Metadata

- name: Assumption
- SubclassOf: /Core/Element

## Properties

- /Core/rationale
  - type: xsd:string
  - minCount: 0
  - maxCount: *
- assumptionStatement
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- assumptionUUID
  - type: /Core/ExternalIdentifier
  - minCount: 0
  - maxCount: 1
