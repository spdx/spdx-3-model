SPDX-License-Identifier: Community-Spec-1.0

# SystemImpactAnalysisStatusType

## Summary

Specifies the lifecycle status of a functional safety system impact analysis.

## Description

SystemImpactAnalysisStatusType provides common values for communicating whether
a SystemImpactAnalysis has been opened, is still in progress, is complete, has
been stopped, is a duplicate of another analysis, or is represented by another
status value.

## Metadata

- name: SystemImpactAnalysisStatusType

## Entries

- new: The system impact analysis has been opened, but substantive analysis work has not yet started.
- inProgress: The system impact analysis is being prepared, waiting on evidence, a decision, a test rerun, or other information, and is not complete.
- complete: The system impact analysis has documented its conclusions, and any required downstream verification, evidence, or decision records are either represented or the analysis rationale explains why no downstream work is required.
- stopped: The system impact analysis was intentionally stopped before completion.
- duplicate: The system impact analysis is closed because another system impact analysis covers the same trigger or scope.
- other: The system impact analysis status is not represented by another value in this vocabulary.
