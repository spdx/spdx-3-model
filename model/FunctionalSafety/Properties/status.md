SPDX-License-Identifier: Community-Spec-1.0

# status

## Summary

Indicates the current lifecycle state or maturity level of an engineering element.

## Description

The status property records the current progression state of an element throughout the system engineering lifecycle. By referencing the `StatusType` enumeration, it enables standardized tracking of work item maturity (e.g., Draft, Approved, Deprecated) across Needs, Requirements, and other artifacts. This property supports workflow enforcement, auditability, and impact analysis by clearly indicating whether an artifact is under development, formally accepted, superseded, or pending review from a context. The status value may evolve as the element undergoes validation, stakeholder review, or lifecycle transitions.

## Metadata

- name: status
- Nature: ObjectProperty
- Range: StatusType
