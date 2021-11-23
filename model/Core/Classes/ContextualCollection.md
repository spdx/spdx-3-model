SPDX-License-Identifier: Community-Spec-1.0

# ContextualCollection

## Summary

A container for a grouping of SPDX-3.0 content with a specific shared context.

## Description

A Contextual Collection is a container for a grouping of SPDX-3.0 content with a specific shared context.

## Metadata

- name: ContextualCollection
- SubclassOf: Artifact
- Instantiability: Concrete

## Properties

- element
  - type: Element
  - minCount: 1
  - maxCount: *
- rootElement
  - type: Element
  - minCount: 1
  - maxCount: 1

