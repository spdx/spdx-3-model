SPDX-License-Identifier: Community-Spec-1.0

# contentDuration

## Summary

Total temporal duration of time-based content within a software artifact.

## Description

contentDuration records the total temporal extent or presentation duration
of time-based content within a software artifact.

The value shall be expressed as an ISO 8601 duration string.
A decimal fraction may be included on the lowest-order component,
using a full stop.
For example, `PT0.05S` represents 50 milliseconds,
and `P1DT1H12.5M` represents 1 day, 1 hour, 12 minutes, and 30 seconds.

## Metadata

- name: contentDuration
- Nature: DataProperty
- Range: xsd:duration
