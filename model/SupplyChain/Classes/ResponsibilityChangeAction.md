SPDX-License-Identifier: Community-Spec-1.0

# ResponsibilityChangeAction

## Summary

ResponsibilityChangeAction refers to the transfer of responsibility from one party to another.

## Description

Changes of responsibility are recorded in this process. Responsibility Change refers to the transfer of rights, responsibilities, and/or control of an asset, property, business, or entity from one party to another. This change can occur in various contexts, including real estate, business acquisitions, intellectual property, and assets.

The `startTime` and `endTime` can be the same time.

## Metadata

- name: ResponsibilityChangeAction
- SubclassOf: /Core/Action
- Instantiability: Concrete

## Properties

- current
  - type: /Core/Agent
  - minCount: 1
  - maxCount: 1
- previous
  - type: /Core/Agent
  - minCount: 0
  - maxCount: 1
- responsibilityChangedOn
  - type: /Core/Element
  - minCount: 1
- responsibilityCategory
  - type: ResponsibilityType
  - minCount: 1
  - maxCount: 1

## External properties restrictions

- /Core/Action/endTime
  - minCount: 1
- /Core/Action/startTime
  - minCount: 1
