SPDX-License-Identifier: Community-Spec-1.0

# approvedBy

## Summary

Identifies an Agent that approved a functional safety change impact analysis.

## Description

approvedBy identifies an Agent that has approved the ChangeImpactAnalysis.

Approval is separate from authorship or creation information. CreationInfo can
identify who created the SPDX element, while approvedBy can identify the safety,
quality, or regulatory authority that approved the analysis result.

## Metadata

- name: approvedBy
- Nature: ObjectProperty
- Range: /Core/Agent
