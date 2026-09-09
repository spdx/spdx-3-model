SPDX-License-Identifier: Community-Spec-1.0

# Observation

## Summary

Execution of a procedure to measure, estimate, or calculate a property
of an Element.

## Description

The `Observation` class represents the temporal event of quantifying a metric.

The Element being measured (the feature of interest) shall be linked to
the Observation via "hasInput" relationship ("Observation hasInput Element").

The specific dimension or characteristic being quantified shall be identified
by the `observedProperty` property, and the quantitative output shall be
recorded intrinsically via the `observedValue` property.

To bound the statistical dispersion of the `observedValue`, an Observation
instance may specify `standardUncertainty` or `relativeStandardUncertainty`,
but shall not use both simultaneously.
If `standardUncertainty` is specified, its value shall be interpreted
utilizing the exact same `unitQUDT` defined in the associated `observedValue`.

An Observation instance may use the "usesTool" relationship to identify
the tool that performed the observation.

## Metadata

- name: Observation
- SubclassOf: Action
- Instantiability: Concrete

## Properties

- observationProcedure
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- observationType
  - type: ObservationType
  - minCount: 0
  - maxCount: 1
- observedProperty
  - type: anyURI
  - minCount: 1
  - maxCount: 1
- observedValue
  - type: UnitOfMeasure
  - minCount: 1
  - maxCount: 1
- relativeStandardUncertainty
  - type: xsd:decimal
  - minCount: 0
  - maxCount: 1
- standardUncertainty
  - type: xsd:decimal
  - minCount: 0
  - maxCount: 1
