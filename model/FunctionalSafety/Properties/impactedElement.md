SPDX-License-Identifier: Community-Spec-1.0

# impactedElement

## Summary

Identifies an SPDX element considered by a system impact analysis.

## Description

impactedElement identifies an SPDX element that is within the scope of a
system impact analysis.

The element may or may not ultimately require a change. More specific
properties such as addedElement, modifiedElement, or removedElement can be used
when the analysis outcome is known.

## Metadata

- name: impactedElement
- Nature: ObjectProperty
- Range: /Core/Element
