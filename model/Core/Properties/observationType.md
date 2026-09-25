SPDX-License-Identifier: Community-Spec-1.0

# observationType

## Summary

Categorization of the methodological nature of an Observation.

## Description

The `observationType` property indicates the method by which a quantitative
value was derived. This property shall reference a valid entry from the
`ObservationType` enumeration.

The application of this property enables
systems and auditors to determine whether a metric was derived via direct
physical measurement, algorithmic calculation, estimation, or simulation.

## Metadata

- name: observationType
- Nature: ObjectProperty
- Range: ObservationType
