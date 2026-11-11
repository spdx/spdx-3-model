SPDX-License-Identifier: Community-Spec-1.0

# referenceQuantity

## Summary

Amount that the value of a Measurement is per.

## Description

The `referenceQuantity` property gives the denominator of a rate:
the value of the `Measurement` is per this amount.
The `referenceProperty` property identifies what the amount is of.

For example, an `observedValue` of 0.3 W·h with a `referenceQuantity` of
1000 <http://qudt.org/vocab/unit/COUNT> and a `referenceProperty` of
`/Dataset/DatasetObservablePropertyType/tokenCount` means 0.3 W·h per 1000
tokens.
A functional unit of one kilogram of a product is a `referenceQuantity` of
1 <http://qudt.org/vocab/unit/KiloGM> with a `referenceProperty` of
<http://qudt.org/vocab/quantitykind/Mass>.

The quantity shall be greater than 0.
It shall be given together with `referenceProperty`.

## Metadata

- name: referenceQuantity
- Nature: ObjectProperty
- Range: UnitOfMeasure
