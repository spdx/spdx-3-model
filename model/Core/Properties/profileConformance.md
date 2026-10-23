SPDX-License-Identifier: Community-Spec-1.0

# profileConformance

## Summary

Identifies a profile to which the creator of this ElementCollection intends to
conform.

## Description

Identifies a profile to which the creator of this ElementCollection intends to
conform.

The profileConformance shall apply to all Elements contained within the
collection as well as the collection itself.

Conformance to a profile requires adherence to the additional restrictions
specified in the corresponding profile documentation.

This property enables the creator of an ElementCollection to declare
an intent to adhere to the restrictions specified for that profile.

The profileConformance has a default value of "core" if no other
profileConformance is specified since all ElementCollections and Elements shall
adhere to the Core profile.

## Metadata

- name: profileConformance
- Nature: ObjectProperty
- Range: ProfileIdentifierType
