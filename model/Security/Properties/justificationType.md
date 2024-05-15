SPDX-License-Identifier: Community-Spec-1.0

# justificationType

## Summary

Impact justification label to be used when linking a vulnerability to an element
representing a VEX product with a VexNotAffectedVulnAssessmentRelationship
relationship.

## Description

When stating that an element is not affected by a vulnerability, the
VexNotAffectedVulnAssessmentRelationship must include a justification from the
machine-readable labels catalog informing the reason the element is not impacted.

impactStatement which is a string with English prose can be used instead or as
complementary to the justification label, but one of both MUST be defined.

## Metadata

- name: justificationType
- Nature: ObjectProperty
- Range: VexJustificationType
