SPDX-License-Identifier: Community-Spec-1.0

# ChangeImpactAnalysisStatusType

## Summary

Specifies the lifecycle status of a functional safety change impact analysis.

## Description

ChangeImpactAnalysisStatusType provides common values for communicating whether
a ChangeImpactAnalysis is pending further information, still being developed,
ready for review, complete, approved, or superseded.

## Metadata

- name: ChangeImpactAnalysisStatusType

## Entries

- draft: The change impact analysis is being prepared and is not ready for review.
- pending: The change impact analysis is waiting on evidence, a decision, a test rerun, or other information before a conclusion can be reached.
- reviewable: The change impact analysis is ready for review by stakeholders.
- complete: The change impact analysis has documented its conclusions.
- approved: The change impact analysis has been approved by the appropriate authority.
- superseded: The change impact analysis has been replaced by a newer analysis.
- other: The change impact analysis status is not represented by another value in this vocabulary.
- noAssertion: No assertion is made about the change impact analysis status.
