SPDX-License-Identifier: Community-Spec-1.0

# impactLevel

## Summary

Identifies the assessed impact category from an impact analysis.

## Description

impactLevel identifies the assessed impact category resulting from a
SystemImpactAnalysis or SystemChangeImpactAnalysis.

The impact category can help communicate the assessed result without embedding
organization-specific change-control rules in SPDX. If no impact category is
asserted, the optional impactLevel property can be omitted.

## Metadata

- name: impactLevel
- Nature: ObjectProperty
- Range: SystemImpactLevel
