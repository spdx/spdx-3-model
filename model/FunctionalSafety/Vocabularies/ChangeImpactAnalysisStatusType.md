SPDX-License-Identifier: Community-Spec-1.0

# ChangeImpactAnalysisStatusType

## Summary

Specifies the lifecycle status of a functional safety change impact analysis.

## Description

ChangeImpactAnalysisStatusType provides common values for communicating whether
a ChangeImpactAnalysis is still in progress, complete, or represented by another
status value.

## Metadata

- name: ChangeImpactAnalysisStatusType

## Entries

- inProgress: The change impact analysis is being prepared, waiting on evidence, a decision, a test rerun, or other information, and is not ready for review.
- complete: The change impact analysis has documented its conclusions.
- other: The change impact analysis status is not represented by another value in this vocabulary.
