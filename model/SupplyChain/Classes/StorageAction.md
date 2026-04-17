SPDX-License-Identifier: Community-Spec-1.0

# StorageAction

## Summary

Records the storage of a product.

## Description

A StorageAction expresses the actual storage of product in a specific location.

## Metadata

- name: StorageAction
- SubclassOf: ModifyAction
- Instantiability: Concrete

## External properties restrictions

- /Core/Element/description
  - minCount: 1
- /Core/Action/actionLocation
  - minCount: 1
