SPDX-License-Identifier: Community-Spec-1.0

# observationStatistic

## Summary

Statistic of the observed property that the value of a Measurement is.

## Description

The `observationStatistic` property states which statistic of the observed
property, over the interval or population observed, the value of
a `Measurement` is.
For example, the value may be the total energy consumed by a training run,
or the mean latency of inference requests.

If it is absent, the value is a single reading, or the statistic is given in
the `observationProcedure` property.

## Metadata

- name: observationStatistic
- Nature: ObjectProperty
- Range: ObservationStatisticType
