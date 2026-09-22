SPDX-License-Identifier: Community-Spec-1.0

# ProfileIdentifierType

## Summary

Enumeration of valid profile identifiers.

## Description

The ProfileIdentifierType provides the permitted values used to declare
conformance to an SPDX profile.

A profile consists of a namespace that may add properties and classes to the
Core profile unique to the domain covered by the profile.

The profile may also contain additional restrictions on existing properties and
classes defined in other profiles.

## Metadata

- name: ProfileIdentifierType

## Entries

- core: The element follows the Core profile specification.
- software: The element follows the Software profile specification.
- simpleLicensing: The element follows the SimpleLicensing profile specification.
- expandedLicensing: The element follows the ExpandedLicensing profile specification.
- security: The element follows the Security profile specification.
- build: The element follows the Build profile specification.
- ai: The element follows the AI profile specification.
- dataset: The element follows the Dataset profile specification.
- extension: The element follows the Extension profile specification.
- lite: The element follows the Lite profile specification.
- hardware: The element follows the Hardware profile specification.
- supplyChain: The element follows the SupplyChain profile specification.
- operations: The element follows the Operations profile specification.
- functionalSafety: The element follows the FunctionalSafety profile specification.
- service: The element follows the Service profile specification.
