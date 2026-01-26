SPDX-License-Identifier: Community-Spec-1.0

# ProfileIdentifierType

## Summary

Enumeration of the valid profiles.

## Description

There are a set of profiles that have been defined by a profile team.

A profile consists of a namespace that may add properties and classes to the
Core profile unique to the domain covered by the profile.

The profile may also contain additional restrictions on existing properties and
classes defined in other profiles.

If the creator of an SPDX collection of elements includes a profile in the list
of profileConformance, they are claiming that all contained elements conform
to all restrictions defined for that profile.

## Metadata

- name: ProfileIdentifierType

## Entries

- core: the element follows the Core profile specification
- software: the element follows the Software profile specification
- simpleLicensing: the element follows the SimpleLicensing profile specification
- expandedLicensing: the element follows the ExpandedLicensing profile specification
- security: the element follows the Security profile specification
- build: the element follows the Build profile specification
- ai: the element follows the AI profile specification
- dataset: the element follows the Dataset profile specification
- extension: the element follows the Extension profile specification
- lite: the element follows the Lite profile specification
