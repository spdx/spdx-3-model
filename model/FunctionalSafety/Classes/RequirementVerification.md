SPDX-License-Identifier: Community-Spec-1.0

# RequirementVerification

## Summary

RequirementVerification class defines the base properties of a verification.

## Description

RequirementVerification class describes the method of verification.
With this class it is possible to identify verification items, such as testcases, checklists or analysis frameworks, etc. It allows to add information for the verification preconditions (what needs to be present before even starting a verification task, run the test case etc.) and what are the postconditions (what has to have happened, what is the state of the item under verification, to be confident the verification task is completed).

Verification typically checks if a requirement has been implemented or refined by more details correctly by a subsequent work product (like a technical specification needs to be verified if it correctly refines a functional specification, or that code correctly implements the state machine defined in a software component design requirement).

A `rationale` is supporting information that adds more context on how
verification needs to be performed, justifies the chosen verification method,
etc.

## Metadata

- name: RequirementVerification
- SubclassOf: /Core/Element
- Instantiability: Concrete

## Properties

- /Core/rationale
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- verificationUUID
  - type: /Core/ExternalIdentifier
  - minCount: 0
  - maxCount: 1
- verificationMethod
  - type: VerificationType
  - minCount: 0
- verificationPrecondition
  - type: xsd:string
  - minCount: 0
- verificationPostcondition
  - type: xsd:string
  - minCount: 0
