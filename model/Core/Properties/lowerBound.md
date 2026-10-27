SPDX-License-Identifier: Community-Spec-1.0

# lowerBound

## Summary

Lowest plausible value of the result of a Measurement.

## Description

The `lowerBound` property gives the lowest plausible value of the observed
property.
It is used together with `upperBound`, for example for an estimate,
or for a size that is disclosed only as a range.

It shall use the same unit as `observedValue` and `upperBound`.

## Metadata

- name: lowerBound
- Nature: ObjectProperty
- Range: UnitOfMeasure
