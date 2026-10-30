SPDX-License-Identifier: Community-Spec-1.0

# observedPresence

## Summary

Result of a PresenceObservation.

## Description

The `observedPresence` property gives the result of a `PresenceObservation`:
`yes` if what is identified by `observedProperty` was found, or `no` if it
was not found by the method used.

The value `noAssertion` shall not be used.

## Metadata

- name: observedPresence
- Nature: ObjectProperty
- Range: PresenceType
