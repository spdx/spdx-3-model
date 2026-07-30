SPDX-License-Identifier: Community-Spec-1.0

# ChangeAction

## Summary

An actual change to a product.

## Description

A ChangeAction represents an alteration made to a product. Such alterations may include intentional adjustments or repairs. A repair is a corrective modification that restores a product to a functional or acceptable state following a defect, failure, or damage. Common examples of repairs are replacing worn components, correcting misalignments, sealing leaks, or reestablishing intended performance characteristics. Firmware updates performed are included, as they may correct software defects, or improve performance, or add new capabilities.

## Metadata

- name: ChangeAction
- SubclassOf: ModifyAction
- Instantiability: Concrete

## External properties restrictions

- /Core/Element/description
  - minCount: 1
