SPDX-License-Identifier: Community-Spec-1.0

# EvaluationResult

## Summary

EvaluationResult is the result of an evaluation.

## Description

EvaluationResult represents the documented outcome of assessing a work product, like a requirement, system, component, or process against specified criteria. It records whether the evaluated subject has met, failed, or yielded an inconclusive result based on the applied EvaluationResultType. The EvaluationResult captures the rationale behind the conclusion, providing necessary context and justification while referencing the specific RequirementVerification upon which the evaluation was based. This structure ensures clear traceability and supports compliance with standards for rigorous verification and validation processes.

An `EvaluationResult` with an evaluation value of "inconclusive" should have a value in its comment property.

A `rationale` is a detailed explanation or reasoning that supports the
`EvaluationResult`. It provides the underlying justification for why
an `evaluation` was deemed to have passed, failed, or been inconclusive.
This clarifies the decision-making process, citing evidence, criteria,
analysis methods, and any considerations of uncertainties or risks.

## Metadata

- name: EvaluationResult
- SubclassOf: /Core/Element
- Instantiability: Concrete

## Properties

- /Core/rationale
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- evaluation
  - type: EvaluationResultType
  - minCount: 1
  - maxCount: 1
- evaluationBasedOn
  - type: RequirementVerification
  - minCount: 1
  - maxCount: 1
