SPDX-License-Identifier: Community-Spec-1.0

# evaluationBasedOn

## Summary

Indicates the specific RequirementVerification instance on which the EvaluationResult is based.

## Description

The evaluationBasedOn property represents the linkage to the particular RequirementVerification that serves as the foundation for generating an EvaluationResult. It connects the evaluation outcome to the defined process or activity that verified the requirement, enabling traceability and verification of the evaluation’s basis. This linkage is critical in systems engineering to ensure that evaluation conclusions clearly reference the verified requirements and their verification methods, supporting auditability, compliance, and quality control.

## Metadata

- name: evaluationBasedOn
- Nature: ObjectProperty
- Range: RequirementVerification
