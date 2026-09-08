SPDX-License-Identifier: Community-Spec-1.0

# contentDuration

## Summary

Total duration of audio or video content in a software artifact.

## Description

contentDuration records the total playback duration of time-based content
in a software artifact.

The value shall be expressed as an ISO 8601 duration string.
For example, `PT30S` represents 30 seconds,
and `P1DT1H12M` represents 1 day, 1 hour, and 12 minutes.

## Metadata

- name: contentDuration
- Nature: DataProperty
- Range: xsd:duration
