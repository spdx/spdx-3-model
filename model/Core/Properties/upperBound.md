SPDX-License-Identifier: Community-Spec-1.0

# upperBound

## Summary

Highest plausible value of the result of a Measurement.

## Description

The `upperBound` property gives the highest plausible value of the observed
property.
It is used together with `lowerBound`, for example for an estimate,
or for a size that is disclosed only as a range.

It shall use the same unit as `observedValue` and `lowerBound`.

## Metadata

- name: upperBound
- Nature: ObjectProperty
- Range: UnitOfMeasure
