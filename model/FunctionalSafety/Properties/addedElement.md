SPDX-License-Identifier: Community-Spec-1.0

# addedElement

## Summary

Identifies an SPDX element added as a result of a functional safety system
impact analysis.

## Description

addedElement identifies an SPDX element introduced as a result of a functional
safety system impact analysis.

Use addedElement only for elements newly introduced into the analyzed safety
context. Use removedElement for elements that no longer apply in that context.
When a system impact analysis results in a modification, represent the modified
work product as a new SPDX element, and use relationships such as amendedBy
between the old and new elements where appropriate.

## Metadata

- name: addedElement
- Nature: ObjectProperty
- Range: /Core/Element
