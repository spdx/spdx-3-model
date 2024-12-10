SPDX-License-Identifier: Community-Spec-1.0

# profileConformance

## Summary

Describes one a profile which the creator of this ElementCollection intends to
conform to.

## Description

Describes a profile to which the creator of this ElementCollection intends to
conform.

The profileConformance will apply to all Elements contained within the
collection as well as the collection itself.

Conformance to a profile is defined by the additional restrictions documented
in the profile specific documentation and schema files.

Use of this property allows the creator of an ElementCollection to communicate
to consumers their intent to adhere to the profile additional restrictions.

The profileConformance has a default value of "core" if no other
profileConformance is specified since all ElementCollections and Element must
adhere to the Core profile.

## Metadata

- name: profileConformance
- Nature: ObjectProperty
- Range: ProfileIdentifierType
