SPDX-License-Identifier: Community-Spec-1.0

# notValidBefore

## Summary

notValidBefore is the date and time on which this Certificate becomes valid.

## Description

notValidBefore specifies the exact date and time when the Certificate begins its validity period. Before this timestamp, the Certificate should not be considered valid for its intended purpose, even if it has been signed by its issuer. This property is part of the Certificate's validity window, which spans from notValidBefore to notValidAfter.

## Metadata

- name: notValidBefore
- Nature: DataProperty
- Range: /Core/DateTime
