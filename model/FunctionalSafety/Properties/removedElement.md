SPDX-License-Identifier: Community-Spec-1.0

# removedElement

## Summary

Identifies an SPDX element removed by a system change under analysis.

## Description

removedElement identifies an existing SPDX element that an actual or proposed
system change documented by a SystemChangeAccomplishmentSummary removes from
the analyzed system context.

The removed element may remain historically valid in a prior model or release.
Use a relationship such as amendedBy between the old element and a replacement
element when the system change results in a revised requirement, validation,
test, design artifact, or other SPDX element.

## Metadata

- name: removedElement
- Nature: ObjectProperty
- Range: /Core/Element
