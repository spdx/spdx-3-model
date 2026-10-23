SPDX-License-Identifier: Community-Spec-1.0

# Capability

## Summary

Expression of a system, product, function, or process ability to achieve a specific objective under stated conditions.

## Description

A capability may be a function unique to an asset, established by several assets, or shared by different assets.

Examples:

- Access Control System
  - Authentication
  - Authorization
  - Policy Enforcement
- Secret Store
- Public Key Infrastructure

Capabilities can be linked to existing elements in an SPDX document. I.e. a Bundle may be linked to a capability using
a ReferenceRelationship with relationship type 'constitutedBy'.

## Metadata

- name: Asset
- SubclassOf: /Core/Element
- Instantiability: Concrete

## Properties

- genericDemand
  - type: Assessment
  - minCount: 0

