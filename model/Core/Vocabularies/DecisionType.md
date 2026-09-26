SPDX-License-Identifier: Community-Spec-1.0

# DecisionType

## Summary

Specifies the kind of decision that was made.

## Description

DecisionType provides common values for communicating the outcome represented by
a Decision. These values describe the decision itself, not the lifecycle status
of the activity or analysis that informed it.

## Metadata

- name: DecisionType

## Entries

- approve: The decision approves or accepts the input, proposed change, or requested outcome.
- approveConditionally: The decision approves or accepts the input, proposed change, or requested outcome subject to specified criteria, constraints, or actions being met.
- reject: The decision rejects the input, proposed change, or requested outcome.
- defer: The decision postpones the outcome for later consideration without assigning a specific requested action.
- delegate: The decision reassigns the authority and responsibility for evaluating and deciding the outcome to another entity.
- requestChange: The decision requests further change before the input or proposed outcome can be accepted.
- requestInformation: The decision pauses evaluation to request additional evidence, context, or clarification from the submitter or an external party.
- noAction: The decision records that no action is required.
- close: The decision closes the item, analysis, or work as complete.
- duplicate: The decision records that the item duplicates another item or decision.
- other: The decision type is not represented by another value in this vocabulary.
