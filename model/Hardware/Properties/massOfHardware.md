SPDX-License-Identifier: Community-Spec-1.0

# massOfHardware

## Summary

The physical mass of a hardware component.

## Description

This property specifies the mass of a physical hardware element. The value must be expressed using the `Core/UnitOfMeasure` type, which requires both a `quantity` and a `unitQUDT`. The `quantity` must denote a mass quantity, and the `unitQUDT` must be a unit of mass from the QUDT vocabulary, specifically constrained to the quantity kind `http://qudt.org/vocab/quantitykind/Mass`.

## Metadata

- name: massOfHardware
- Nature: ObjectProperty
- Range: /Core/UnitOfMeasure
