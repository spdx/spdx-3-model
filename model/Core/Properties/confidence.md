SPDX-License-Identifier: Community-Spec-1.0

# confidence

## Summary

Probability that the result of an Observation is correct.

## Description

The `confidence` property gives the probability, as judged by the observer,
that the result of an Observation is correct.
For example, a classifier that reports a result with a score of 0.87 has
a `confidence` of 0.87.

The value shall be greater than 0 and less than or equal to 1.

This property is not an uncertainty of a numeric value.
For the uncertainty of a `Measurement`, use `standardUncertainty`,
or `lowerBound` and `upperBound`.

## Metadata

- name: confidence
- Nature: DataProperty
- Range: xsd:decimal
