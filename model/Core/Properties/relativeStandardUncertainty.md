SPDX-License-Identifier: Community-Spec-1.0

# relativeStandardUncertainty

## Summary

Relative standard uncertainty of the observation,
expressed as a dimensionless percentage.

## Description

The `relativeStandardUncertainty` property captures the statistical dispersion
or relative error bound associated with an observed value.

The value of this property shall be expressed as a dimensionless percentage.
For example, a `relativeStandardUncertainty` value of `15.0` alongside an
observed value of 181 kilometers indicates a relative uncertainty of ±15%.

**The value of this property shall be a non-negative decimal.**

Authors should utilize this property when the uncertainty scales
proportionally with the measured value, and use `standardUncertainty`
when the uncertainty is a fixed constant.

This property conceptually aligns with the `qudt:relativeStandardUncertainty`
property defined in the QUDT ontology, as well as the ISO/IEC Guide 98-3
(Guide to the Expression of Uncertainty in Measurement).

## Metadata

- name: relativeStandardUncertainty
- Nature: DataProperty
- Range: xsd:decimal
