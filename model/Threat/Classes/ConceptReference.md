SPDX-License-Identifier: Community-Spec-1.0

# ConceptReference

## Summary

Allows to reference concepts not part of the SPDX document to associate Threats and Controls with existing concepts.

## Description

A Threat or Control may be associated to one or more TypedReferences of different types. The ReferenceType defines the
currently supported types. I.e. you may reference concepts of an ontology.

## Metadata

- name: ConceptReference
- SubclassOf: /Core/Element
- Instantiability: Concrete

## Properties

- context
  - type: ConceptType
  - minCount: 1

