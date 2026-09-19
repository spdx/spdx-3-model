SPDX-License-Identifier: Community-Spec-1.0

# DecisionStatusType

## Summary

Specifies the lifecycle status of a decision.

## Description

DecisionStatusType provides common values for communicating whether a Decision
is proposed, recorded, superseded, withdrawn, or represented by another status
value.

## Metadata

- name: DecisionStatusType

## Entries

- proposed: The decision has been proposed but is not yet recorded as the active decision.
- recorded: The decision has been made and recorded.
- superseded: The decision has been replaced by a newer decision.
- withdrawn: The decision has been withdrawn and is no longer active.
- other: The decision status is not represented by another value in this vocabulary.
