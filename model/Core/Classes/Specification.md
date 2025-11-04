SPDX-License-Identifier: Community-Spec-1.0

# Specification

## Summary

A specification is a detailed description of the design, requirements,
or features of a product, process, or system.

## Description

A specification (spec) is a detailed document that outlines the
design, requirements, or features for a product, process, or system.

Requirements, standards, specifications and processes
can be referenced in this class.

## Metadata

- name: Specification
- SubclassOf: Artifact
- Instantiability: Concrete
  
## Properties

- specType
  - type: SpecificationType
  - minCount: 0
  - maxCount: 1

## External properties restrictions

- /Core/Element/externalIdentifier
  - minCount: 1
