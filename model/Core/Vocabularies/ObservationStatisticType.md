SPDX-License-Identifier: Community-Spec-1.0

# ObservationStatisticType

## Summary

Statistic of an observed property that the value of a Measurement is.

## Description

The `ObservationStatisticType` vocabulary states which statistic, over the
interval or population observed, the value of a `Measurement` is.

## Metadata

- name: ObservationStatisticType

## Entries

- maximum: The value is the largest value observed.
- mean: The value is the arithmetic mean of the values observed.
- median: The value is the median of the values observed.
- minimum: The value is the smallest value observed.
- other: The value is another statistic, described in the observation procedure.
- percentile: The value is the percentile given by the percentileRank property.
- total: The value is the sum over the whole interval or population observed, such as the total energy consumed by a training run.
