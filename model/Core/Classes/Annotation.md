SPDX-License-Identifier: Community-Spec-1.0

# Annotation

## Summary

An assertion made in relation to one or more elements.

## Description

An Annotation is an assertion made in relation to one or more elements.

## Metadata

- name: Annotation
- SubclassOf: Element
- Instantiability: Concrete

## Properties

- annotationType
  - type: annotationTypeVocab
  - minCount: 1
  - maxCount: 1
- contentType
  - type: mediaType
- statement
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- subject
  - type: Element
  - minCount: 1

