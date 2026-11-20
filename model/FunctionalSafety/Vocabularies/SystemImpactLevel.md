SPDX-License-Identifier: Community-Spec-1.0

# SystemImpactLevel

## Summary

Specifies an assessed impact category from a system impact analysis.

## Description

SystemImpactLevel provides common values for communicating the category of
impact determined by a SystemImpactAnalysis or SystemChangeImpactAnalysis.

The impact category communicates the assessed result. It does not prescribe an
organization-specific change-control or verification response. If no impact
category is asserted, the optional impactLevel property can be omitted.

## Metadata

- name: SystemImpactLevel

## Entries

- noCriticalImpact: No critical safety, security, quality, availability, or customer-satisfaction impact was identified.
- safetyImpact: A safety-relevant impact was identified.
- securityImpact: A security-relevant impact was identified.
- qualityImpact: A quality impact was identified.
- availabilityImpact: An availability impact was identified.
- customerSatisfactionImpact: A customer-satisfaction impact was identified.
- other: The impact category is not represented by another value in this vocabulary.
