SPDX-License-Identifier: Community-Spec-1.0

# SoftwareService

## Summary

Software provided as a service over a network.

## Description

SoftwareService represents a service based on software components offered for access online over a network.

The primary provider of the SoftwareService is the [/Core/suppliedBy](../../Core/Properties/suppliedBy.md) property. Any additional providers can use a relationship of relationship type [availableFrom](../../Core/Vocabularies/RelationshipType.md).

The [serviceHostingCountry](../Properties/serviceHostingCountry.md) property can be used to capture any countries from which the service is provided.

**Note**
SPDX 3.1 does not define tenancy or tenant-isolation semantics for a SoftwareService. Implementations may describe these characteristics using the inherited extension property. Absence of this information means unspecified and shall not be interpreted as single-tenancy.

Future SPDX versions may define optional Service profile classes and properties for these concepts.

## Properties

- /Core/additionalInformation
  - type: /Core/DictionaryEntry
- /Core/additionalInformationSpecification
  - type: /Core/Specification
- serverAuthenticationProtocol
  - type: AuthenticationProtocolType
- serverKeyValidationProtocol
  - type: KeyValidationProtocolType
  - minCount: 0
- serviceHostingCountry
  - type: /Core/CountryCodeAlpha3
  - minCount: 0

## Metadata

- name: SoftwareService
- SubclassOf: /Core/Artifact
- Instantiability: Concrete
