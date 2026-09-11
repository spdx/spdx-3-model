SPDX-License-Identifier: Community-Spec-1.0

# statement

## Summary

A condition, objective or capability required by a role to solve a problem.

## Description

The statement property captures the natural language articulation of a Need during the Needs Analysis phase. It represents the primary input for the Requirements Engineering process, preserving the role's original intent before transformation into verifiable system requirements.

While derived requirements must adhere to strict verification criteria, the statement within a Need may initially be qualitative or subjective. This property serves as the foundational traceability link, ensuring that downstream system capabilities can be traced back to the original role intent. The use of xsd:string accommodates the unstructured nature of early elicitation, allowing for the recording of raw role input prior to refinement.

## Metadata

- name: statement
- Nature: DataProperty
- Range: xsd:string
