SPDX-License-Identifier: Community-Spec-1.0

# addedElement

## Summary

Identifies an SPDX element added as a result of a functional safety system
impact analysis.

## Description

addedElement identifies an SPDX element introduced as a result of a functional
safety system impact analysis.

Use addedElement only for elements newly introduced into the analyzed safety
context. Use modifiedElement for elements changed by the analysis outcome, and
use removedElement for elements that no longer apply in that context.

## Metadata

- name: addedElement
- Nature: ObjectProperty
- Range: /Core/Element
