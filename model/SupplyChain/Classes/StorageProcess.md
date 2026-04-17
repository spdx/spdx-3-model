SPDX-License-Identifier: Community-Spec-1.0

# StorageProcess

## Summary

Prescribes the storage of a product.

## Description

A StorageProcess expresses the planned storage of product in an optionally-specified location.

## Metadata

- name: StorageProcess
- SubclassOf: ModifyProcess
- Instantiability: Concrete

## Properties

- plannedStorageLocation
  - type: /Core/Location
  - minCount: 0
