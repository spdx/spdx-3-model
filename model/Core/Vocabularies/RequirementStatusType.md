SPDX-License-Identifier: Community-Spec-1.0

# RequirementStatusType

## Summary

Provide an enumerated set of requirement statuses that can provide state to a requirement.

## Description

This enumeration summarizes common states that a requirement may pass through in it's lifecycle. The same requirement wording may have different states depending on the context of the product it is being included in.

## Metadata

- name: RequirementStatusType

## Entries

- draft: A requirement is considered a draft state and may be modified before being submitted for review.
- reviewable: A requirement is ready for formal review by stakeholders for a specific use.
- active: A requirement has been approved by stakeholder, and can be include in traceability.
- retired: A requirement is no longer active for a specific use.
- backlog: A requirement has been captured and logged, but not yet ready to become a formal requirement draft. A backlog requirement may still be incomplete or ambiguous.
