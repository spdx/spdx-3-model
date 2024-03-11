SPDX-License-Identifier: Community-Spec-1.0

# SoftwareService

## Summary

Software provided as a service over a network.

## Description

SoftwareService represents software being licensed, delivered and accessed online over a network.

## Properties

- provider
  - type: Agent
  - minCount: 1
- serverAuthenticationProtocol
  - type: AuthenticationProtocolType
  - minCount: 0

## Metadata

- name: SoftwareService
- SubclassOf: Element
- Instantiability: Concrete
