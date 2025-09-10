SPDX-License-Identifier: Community-Spec-1.0

# SoftwareService

## Summary

Software provided as a service over a network.

## Description

SoftwareService represents a service based on software components offered for access online over a network.

## Properties

- provider
  - type: /Core/Agent
  - minCount: 1
- serverAuthenticationProtocol
  - type: AuthenticationProtocolType
  - minCount: 0
- serviceHostingCountry
  - type: /Core/CountryCodeAlpha3
  - minCount: 0

## Metadata

- name: SoftwareService
- SubclassOf: /Core/Element
- Instantiability: Concrete
