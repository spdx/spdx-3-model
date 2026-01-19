SPDX-License-Identifier: Community-Spec-1.0

# EvaluationResult

## Summary

EvaluationResult is the result of an evaluation.

## Description

EvaluationResult represents the documented outcome of assessing a work product, like a requirement, system, component, or process against specified criteria. It records whether the evaluated subject has met, failed, or yielded an inconclusive result based on the applied EvaluationResultType. The EvaluationResult captures the rationale behind the conclusion, providing necessary context and justification while referencing the specific RequirementVerification upon which the evaluation was based. This structure ensures clear traceability and supports compliance with standards for rigorous verification and validation processes.

An EvaluationResult with an evaluation value of "inconclusive" should have a value in its comment property.

## Metadata

- name: EvaluationResult
- SubclassOf: /Core/Element
- Instantiability: Concrete

## Properties

- evaluation
  - type: EvaluationResultType
  - minCount: 1
  - maxCount: 1
- evaluationRationale
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- evaluationBasedOn
  - type: RequirementVerification
  - minCount: 1
  - maxCount: 1
