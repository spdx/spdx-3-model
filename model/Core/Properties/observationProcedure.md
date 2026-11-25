SPDX-License-Identifier: Community-Spec-1.0

# observationProcedure

## Summary

Description of the method used to obtain the result of an Observation.

## Description

The `observationProcedure` property describes the method, formula, proxies,
or settings used to obtain the result of an `Observation`.
It should be given when the `observationType` is `calculated` or
`estimated`, and when the result depends on a procedure that is not
otherwise identified (for example, the tokenizer used to count tokens).

A tool used is identified using a `usesTool` relationship, and a published
method that was followed is identified using a `conformsTo` relationship to
a `Specification`.
This property is for details that these do not give.

For example, to comply with Regulation (EU) 2024/1689 (AI Act) Annex XI,
Section 1, point 2(e), a provider estimating the energy used to train a model
could state: "Estimated as total floating-point operations, divided by the
measured throughput of the training hardware, multiplied by its thermal
design power (TDP)."

## Metadata

- name: observationProcedure
- Nature: DataProperty
- Range: xsd:string
