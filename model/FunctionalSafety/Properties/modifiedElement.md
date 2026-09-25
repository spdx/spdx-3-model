SPDX-License-Identifier: Community-Spec-1.0

# modifiedElement

## Summary

Identifies an SPDX element modified as a result of a functional safety system
impact analysis.

## Description

modifiedElement identifies an SPDX element whose represented system item,
requirement, validation, test, design artifact, document, or other work product
is modified as a result of a functional safety system impact analysis.

When the modification is represented by a replacement SPDX element, the prior
element can be listed as modifiedElement, the replacement can be listed as
addedElement, and a relationship such as amendedBy can link the prior element
to the replacement where appropriate.

## Metadata

- name: modifiedElement
- Nature: ObjectProperty
- Range: /Core/Element
