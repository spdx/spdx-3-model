SPDX-License-Identifier: Community-Spec-1.0

# impactAnalysisStatus

## Summary

Identifies the lifecycle status of a functional safety change impact analysis.

## Description

impactAnalysisStatus identifies whether a ChangeImpactAnalysis is new, still
in progress, complete, a duplicate of another analysis, or uses another
lifecycle status.

This allows an SPDX document to communicate intermediate versions of a change
impact analysis before the analysis is fully complete.

## Metadata

- name: impactAnalysisStatus
- Nature: DataProperty
- Range: ChangeImpactAnalysisStatusType
