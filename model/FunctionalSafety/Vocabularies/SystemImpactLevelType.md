SPDX-License-Identifier: Community-Spec-1.0

# SystemImpactLevelType

## Summary

Specifies the assessed impact category from a functional safety system impact
analysis.

## Description

SystemImpactLevelType provides common values for communicating the category of
impact determined by a SystemImpactAnalysis.

The impact category can be used to communicate the expected verification response
without embedding organization-specific change-control rules in SPDX.
If no assertion is made about impact, the optional impactLevel property
can be omitted.

## Metadata

- name: SystemImpactLevelType

## Entries

- noCriticalImpact: No critical safety, security, quality, availability, or customer-satisfaction impact was identified.
- safetyImpact: A safety-relevant impact was identified.
- securityImpact: A security-relevant impact was identified.
- safetyAndSecurityImpact: Both safety-relevant and security-relevant impacts were identified.
- qualityImpact: A quality impact was identified.
- availabilityImpact: An availability impact was identified.
- customerSatisfactionImpact: A customer-satisfaction impact was identified.
- other: The impact category is not represented by another value in this vocabulary.
