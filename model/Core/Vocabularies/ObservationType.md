SPDX-License-Identifier: Community-Spec-1.0

# ObservationType

## Summary

Specifies the methodological nature of how an Observation was derived.

## Description

The `ObservationType` enumeration provides categorization for the method
used to obtain a measurement. This allowing auditors and downstream users
to easily distinguish between direct measurements and derived approximations.

## Metadata

- name: ObservationType

## Entries

- calculated: The quantitative value was derived mathematically or algorithmically by applying a defined process or tool to other explicit inputs (e.g., deriving energy consumption from GPU hours and thermal design power).
- estimated: The quantitative value is a broad approximation or inference where exact inputs may not be fully known, or precise calculation is infeasible.
- measured: The quantitative value was obtained via direct physical measurement, hardware profiling, or direct reading from a sensor or system.
- simulated: The quantitative value was generated through a software model simulating physical or computational environments.
