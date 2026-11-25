SPDX-License-Identifier: Community-Spec-1.0

# observedValue

## Summary

Numeric result of a Measurement.

## Description

The `observedValue` property gives the result of a `Measurement` as
a quantity and a QUDT unit.
The unit shall have the same dimension as the observed property.

It may be absent if both `lowerBound` and `upperBound` are given.

## Metadata

- name: observedValue
- Nature: ObjectProperty
- Range: UnitOfMeasure
