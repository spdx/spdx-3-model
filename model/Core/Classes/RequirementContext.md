SPDX-License-Identifier: Community-Spec-1.0

# RequirementContext

## Summary

Context of the requirement relating it to a project and its structure.

## Description

The requirement context describes the the hierarchical level of the requirement within a project. It does not give any idea where this requirement ends up in the final full system. It defines the project as a context for the requirement, e.g. Zephyr, Xen, Linux, any Application, any Library etc.; don't make it optional, as requirements levels without the context to the project will cause chaos in final systems. if not sure, don't use RequirementContext in your Requirement Class at all.

## Metadata

- name: RequirementContext
- SubclassOf: none

## Properties

- requirementNamespace
  - type:xsd:string
  - minCount: 0
  - maxCount: 1
<<<<<<< HEAD
- requirementHieratchyLevel
=======
- requirementHierarchyLevel
>>>>>>> 20a5242082bf8888c11507c5a1f27d4826129717
  - type: PositiveIntegerRange
  - minCount: 0
  - maxCount: 1
- contextOrigin
  - type: Specification
  - minCount: 0
  - maxCount: 1
