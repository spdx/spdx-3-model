SPDX-License-Identifier: Community-Spec-1.0

# EvaluationResultType

## Summary

Specifies the outcome of an evaluation or verification process.

## Description

EvaluationResultType categorizes whether a requirement or condition was met,
not met, or could not be clearly determined.

This classification helps to communicate the status of an evaluation clearly,
so it is transparent when a result is definitive and when more information
is needed before a decision can be made.

## Metadata

- name: EvaluationResultType

## Entries

- pass: Indicates a successful evaluation where the requirement or condition is clearly met.
- fail: Indicates a failed evaluation where the requirement or condition is not met.
- inconclusive: Inconclusive refers to a result or outcome from a verification, test, or analysis that cannot be clearly classified as either positive (successful, pass) or negative (failed, reject). An inconclusive result means there was not enough clear evidence, data, or signal to make a definitive determination, and further investigation or additional testing is necessary. An inconclusive result always shall need a comment on it.
