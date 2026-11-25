SPDX-License-Identifier: Community-Spec-1.0

# percentileRank

## Summary

Which percentile the value of a Measurement is.

## Description

The `percentileRank` property gives which percentile of the observed property
the value of a `Measurement` is, as a decimal between 0 and 1.
For example, 0.99 means the 99th percentile (p99).

It shall be present if and only if `observationStatistic` is `percentile`.

## Metadata

- name: percentileRank
- Nature: DataProperty
- Range: xsd:decimal
