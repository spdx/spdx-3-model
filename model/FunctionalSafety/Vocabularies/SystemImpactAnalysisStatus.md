SPDX-License-Identifier: Community-Spec-1.0

# SystemImpactAnalysisStatus

## Summary

Specifies the lifecycle status of a system impact analysis.

## Description

SystemImpactAnalysisStatus provides common values for communicating the
lifecycle state of a SystemImpactAnalysis or SystemChangeImpactAnalysis.

## Metadata

- name: SystemImpactAnalysisStatus

## Entries

- new: The analysis has been opened, but substantive analysis work has not yet started.
- inProgress: The analysis is underway or waiting for evidence, decisions, tests, or other information; it is not complete.
- complete: The analysis has completed and documented its conclusion.
- stopped: The analysis was intentionally stopped before completion.
- duplicate: The analysis was closed because it duplicates another analysis.
- other: The analysis status is not represented by another value in this vocabulary.
