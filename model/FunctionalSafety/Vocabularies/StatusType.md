SPDX-License-Identifier: Community-Spec-1.0

# StatusType

## Summary

StatusType defines a controlled vocabulary of lifecycle states used to track the progression and maturity of engineering elements.

## Description

The StatusType enumeration provides standardized lifecycle states for engineering artifacts such as needs, requirements, designs, relationships, and verification items. It enables consistent tracking of an element's progression from initial conception through review, approval, and eventual obsolescence. By assigning a status, stakeholders can monitor work item maturity, enforce workflow rules, and facilitate traceability across system engineering phases.

## Metadata

- name: StatusType

## Entries

- draft: The element is in an initial or unreviewed state and has not yet undergone formal evaluation or approval.
- approved: The element has been formally reviewed, validated, and accepted by the appropriate stakeholders or governing process.
- deprecated: The element is officially superseded, obsolete, or no longer recommended for use, though it may be retained for reference or historical traceability.
