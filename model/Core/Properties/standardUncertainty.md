SPDX-License-Identifier: Community-Spec-1.0

# standardUncertainty

## Summary

Standard uncertainty of the value of a Measurement.

## Description

The `standardUncertainty` property gives the standard uncertainty of
the `observedValue` of a `Measurement`: an estimate of one standard deviation
of the value.
It is not a ± bound; a range is given using `lowerBound` and `upperBound`.

The unit determines how the quantity is read:

- If the unit is the unit of the `observedValue`, the uncertainty is absolute.
  For example, an uncertainty of 0.5 <http://qudt.org/vocab/unit/KiloM> for
  a value of 181 <http://qudt.org/vocab/unit/KiloM>.
- If the unit is <http://qudt.org/vocab/unit/PERCENT>, the uncertainty is
  relative to the value.
  For example, an uncertainty of 5 <http://qudt.org/vocab/unit/PERCENT> for
  a value of 36.5 <http://qudt.org/vocab/unit/MegaW-HR> means one standard
  deviation of 1.825 MW·h.
  A relative uncertainty cannot be used for a value of zero.

The quantity shall not be negative.

This property aligns with the standard uncertainty defined in JCGM 100
(Guide to the Expression of Uncertainty in Measurement) and with the
`qudt:standardUncertainty` property of QUDT.

## Metadata

- name: standardUncertainty
- Nature: ObjectProperty
- Range: UnitOfMeasure
