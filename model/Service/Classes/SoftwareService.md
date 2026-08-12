SPDX-License-Identifier: Community-Spec-1.0

# SoftwareService

## Summary

Software provided as a service over a network.

## Description

SoftwareService represents a service based on software components offered for access online over a network.
The primary provider of the SoftwareService is the /Core/suppliedBy.
Any additional providers can use a relationship of relationship type availableFrom.

## Properties

- serverAuthenticationProtocol
  - type: AuthenticationProtocolType
  - minCount: 0
- serviceHostingCountry
  - type: /Core/CountryCodeAlpha3
  - minCount: 0

## Metadata

- name: SoftwareService
- SubclassOf: /Core/Artifact
- Instantiability: Concrete
