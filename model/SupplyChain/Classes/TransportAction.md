SPDX-License-Identifier: Community-Spec-1.0

# TransportAction

## Summary

An actual change to a product's location.

## Description

A TransportAction expresses the change in location of a product, such as a component being moved from an assembly plant to a warehouse.

## Metadata

- name: TransportAction
- SubclassOf: ModifyAction
- Instantiability: Concrete

## Properties

- transportRoute
  - type: xsd:string
  - minCount: 0
- pickupLocation
  - type: /Core/Location
  - minCount: 1
- dropoffLocation
  - type: /Core/Location
  - minCount: 0
