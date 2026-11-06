SPDX-License-Identifier: Community-Spec-1.0

# coverageProbability

## Summary

Probability that the true value of a Measurement lies between its bounds.

## Description

The `coverageProbability` property gives the probability that the true value
lies between the `lowerBound` and the `upperBound` of a `Measurement`.
For example, a value of 0.95 means that the bounds are a 95% coverage
interval.

The value shall be greater than 0 and less than or equal to 1.
It shall only be given together with both bounds.
If it is absent, the bounds are the plausible minimum and maximum.

This property aligns with the coverage probability defined in JCGM 100:2008
(Guide to the Expression of Uncertainty in Measurement).

## Metadata

- name: coverageProbability
- Nature: DataProperty
- Range: xsd:decimal
