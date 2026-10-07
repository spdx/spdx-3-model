SPDX-License-Identifier: Community-Spec-1.0

# DecisionStatusType

## Summary

Specifies the lifecycle status of a decision.

## Description

DecisionStatusType provides common values for communicating whether a Decision
has been requested, is proposed, is being prepared, has been recorded, has been
superseded, has been withdrawn, was entered in error, or is represented by
another status value.

## Metadata

- name: DecisionStatusType

## Entries

- proposed: The decision has been proposed but is not yet recorded as the active decision.
- requested: A decision has been requested, but the decision has not yet been proposed or recorded.
- inProgress: The decision is being evaluated or prepared.
- recorded: The decision has been made and recorded.
- superseded: The decision has been replaced by a newer decision.
- withdrawn: The decision has been withdrawn and is no longer active.
- enteredInError: The decision record was created in error and should not be used.
- other: The decision status is not represented by another value in this vocabulary.
