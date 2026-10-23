SPDX-License-Identifier: Community-Spec-1.0

# standardUncertainty

## Summary

Absolute standard uncertainty of the observation.

## Description

The `standardUncertainty` property captures the statistical dispersion or absolute error bound associated with an observed value.

For example, a `standardUncertainty` value of `0.5` alongside an observed value of 181 kilometers indicates an absolute uncertainty of ±0.5 kilometers.

**The value of this property shall be a non-negative decimal.**

Authors should utilize this property when the uncertainty is a fixed constant,
and use `relativeStandardUncertainty` when the uncertainty scales
proportionally with the measured value.

This property conceptually aligns with the `qudt:standardUncertainty`
property defined in the QUDT ontology, as well as the ISO/IEC Guide 98-3
(Guide to the Expression of Uncertainty in Measurement).

## Metadata

- name: standardUncertainty
- Nature: DataProperty
- Range: xsd:decimal
