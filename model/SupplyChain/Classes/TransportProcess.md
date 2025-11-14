SPDX-License-Identifier: Community-Spec-1.0

# TransportProcess

## Summary

A prescribed change to a product's location.

## Description

A TransportProcess is a process that will result in a change in location of a product, such as a component being moved from an assembly plant to a warehouse.

## Metadata

- name: TransportProcess
- SubclassOf: ModifyProcess
- Instantiability: Concrete

## Properties

- plannedTransportRoutes
  - type: xsd:string
  - minCount: 0
- forPickupLocation
  - type: /Core/Location
  - minCount: 0
- forDropoffLocation
  - type: /Core/Location
  - minCount: 0
