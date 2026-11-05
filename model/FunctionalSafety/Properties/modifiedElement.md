SPDX-License-Identifier: Community-Spec-1.0

# modifiedElement

## Summary

Identifies an SPDX element modified by a system change under analysis.

## Description

modifiedElement identifies an existing SPDX element modified by an actual or
proposed system change assessed by a SystemChangeImpactAnalysis.

When a modification is represented by a replacement SPDX element, the prior
element can be listed as modifiedElement, the replacement can be listed as
addedElement, and a relationship such as amendedBy can link the prior element
to the replacement where appropriate.

## Metadata

- name: modifiedElement
- Nature: ObjectProperty
- Range: /Core/Element
