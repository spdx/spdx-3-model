SPDX-License-Identifier: Community-Spec-1.0

# removedElement

## Summary

Identifies an SPDX element removed from the analyzed safety context by a
functional safety change impact analysis.

## Description

removedElement identifies an SPDX element that no longer applies in the
analyzed safety context as a result of a functional safety change impact
analysis.

The removed element may remain historically valid in a prior model or release.
Use a relationship such as amendedBy between the old element and a replacement
element when the change impact analysis results in a revised requirement,
validation, test, design artifact, or other SPDX element.

## Metadata

- name: removedElement
- Nature: ObjectProperty
- Range: /Core/Element
