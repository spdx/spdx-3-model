SPDX-License-Identifier: Community-Spec-1.0

# impactLevel

## Summary

Identifies the assessed level of impact from a functional safety change impact
analysis.

## Description

impactLevel identifies the assessed level of impact resulting from a
ChangeImpactAnalysis.

The impact level can help communicate the expected verification response. For
example, a low-impact change may require targeted test reruns, while a
high-impact change may require broader re-verification or safety-case review.

## Metadata

- name: impactLevel
- Nature: DataProperty
- Range: ChangeImpactLevelType
