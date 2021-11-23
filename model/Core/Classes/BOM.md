SPDX-License-Identifier: Community-Spec-1.0

# BOM

## Summary

A container for a grouping of SPDX-3.0 content characterizing details
(provenence, composition, licensing, etc.) about a product.

## Description

An BOM is a container for a grouping of SPDX-3.0 content
characterizing details about a product.
This could include details of the content and composition of the product,
provenence details of the product and/or
its composition, licensing information, known quality or security issues, etc.

## Metadata

- name: BOM
- SubclassOf: ContextualCollection
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

