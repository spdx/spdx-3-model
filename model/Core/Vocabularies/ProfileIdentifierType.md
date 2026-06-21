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

- ai: The element follows the AI profile specification.
- build: The element follows the Build profile specification.
- core: The element follows the Core profile specification.
- dataset: The element follows the Dataset profile specification.
- expandedLicensing: The element follows the ExpandedLicensing profile specification. **DEPRECATED in SPDX 3.1.** Use "licensing" instead.
- extension: The element follows the Extension profile specification.
- functionalSafety: The element follows the FunctionalSafety profile specification.
- hardware: The element follows the Hardware profile specification.
- licensing: The element follows the Licensing profile specification.
- lite: The element follows the Lite profile specification.
- operations: The element follows the Operations profile specification.
- security: The element follows the Security profile specification.
- service: The element follows the Service profile specification.
- simpleLicensing: The element follows the SimpleLicensing profile specification. **DEPRECATED in SPDX 3.1.** Use "licensing" instead.
- software: The element follows the Software profile specification.
- supplyChain: The element follows the SupplyChain profile specification.
