SPDX-License-Identifier: Community-Spec-1.0

# observationProcedure

## Summary

Description of the methodology, protocol, or proxy utilized to perform
the Observation.

## Description

The `observationProcedure` property captures the specific technique or set of
steps used to arrive at the `observedValue`.
It is particularly critical when the `observationType` is `calculated` or
`estimated`, as it enables the author to record the proxy data, algorithms,
or formulas utilized.

For example, to comply with Regulation (EU) 2024/1689 (AI Act) Annex XI
Section 1.2(e), an author estimating energy consumption could use
this property to state: "Energy consumption estimated based on computational
resources utilized: total floating point operations (FLOPs) multiplied by the
Thermal Design Power (TDP) of the training hardware."

## Metadata

- name: observationProcedure
- Nature: DataProperty
- Range: xsd:string
