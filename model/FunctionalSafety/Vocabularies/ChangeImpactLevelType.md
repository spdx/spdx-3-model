SPDX-License-Identifier: Community-Spec-1.0

# ChangeImpactLevelType

## Summary

Specifies the assessed level of impact from a functional safety change impact
analysis.

## Description

ChangeImpactLevelType provides common values for communicating the degree of
impact determined by a ChangeImpactAnalysis.

The impact level can be used to communicate the expected verification response
without embedding organization-specific change-control rules in SPDX.

## Metadata

- name: ChangeImpactLevelType

## Entries

- none: No safety-relevant impact was identified.
- low: Limited safety-relevant impact was identified.
- medium: Bounded safety-relevant impact was identified.
- high: Broad safety-relevant impact was identified.
- critical: Critical safety-relevant impact was identified.
- other: The impact level is not represented by another value in this vocabulary.
- noAssertion: No assertion is made about the impact level.
