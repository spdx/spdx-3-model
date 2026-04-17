SPDX-License-Identifier: Community-Spec-1.0

# BulkHardware

## Summary

Products or commodities produced as a bulk unit are called bulk products. Commodities are often sold in bulk.

## Description

Products or commodities produced as a bulk unit are called bulk products. Commodities are often sold in bulk based on a batch or bulk ID number associated with the bulk unit.
Bulk units defined in the QUDT Units standards.

## Metadata

- name: BulkHardware
- SubclassOf: Hardware
- Instantiability: Concrete

## Properties

- bulkQuantity
  - type: /Core/UnitOfMeasure
  - minCount: 1
  - maxCount: 1
  
## External properties restrictions

- /Core/Element/description
  - minCount: 1
- /Hardware/Hardware/serialNumber
  - maxCount: 0
