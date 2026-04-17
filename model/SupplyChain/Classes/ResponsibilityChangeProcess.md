SPDX-License-Identifier: Community-Spec-1.0

# ResponsibilityChangeProcess

## Summary

ResponsibilityChangeProcess refers to the process of transferring responsibility from one party to another.

## Description

The process changes of responsibility are recorded in this process. Responsibility Change refers to the transfer of rights, responsibilities, and/or control of an asset, property, business, or entity from one party to another.

## Metadata

- name: ResponsibilityChangeProcess
- SubclassOf: /Core/DefinedProcess
- Instantiability: Concrete

## Properties

- plannedCurrent
  - type: /Core/Agent
  - minCount: 0
  - maxCount: 1
- plannedPrevious
  - type: /Core/Agent
  - minCount: 0
  - maxCount: 1
- plannedProductOfResponsibilityChange
  - type: /Core/Element
  - minCount: 0
- responsibilityCategory
  - type: ResponsibilityType
  - minCount: 1
  - maxCount: 1
