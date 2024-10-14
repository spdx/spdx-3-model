SPDX-License-Identifier: Community-Spec-1.0

# CvssSeverityType

## Summary

Specifies the CVSS base, temporal, threat, or environmental severity type.

## Description

CvssSeverityType specifies the Common Vulnerability Scoring System (CVSS)
severity type, defined in the CVSS specifications as the textual representation
of the numeric CVSS score.

The severity type entries are inclusive of and applicable to enumerations found
in
[Common Vulnerability Scoring System v3.0: Specification Document](https://www.first.org/cvss/v3.0/specification-document#Qualitative-Severity-Rating-Scale)
and
[Common Vulnerability Scoring System version 4.0: Specification Document](https://www.first.org/cvss/v4.0/specification-document#Qualitative-Severity-Rating-Scale).

CvssSeverityType is a mandatory field because baseSeverity is required in the
[CVSS 3.0 schema](https://www.first.org/cvss/cvss-v3.0.json),
[CVSS 3.1 schema](https://www.first.org/cvss/cvss-v3.1.json), and
[CVSS 4.0 schema](https://www.first.org/cvss/cvss-v4.0.json).

The field can be used to document the base, temporal, threat, or environmental
severity.

## Metadata

- name: CvssSeverityType

## Entries

- critical: When a CVSS score is between 9.0 - 10.0
- high: When a CVSS score is between 7.0 - 8.9
- medium: When a CVSS score is between 4.0 - 6.9
- low: When a CVSS score is between 0.1 - 3.9
- none: When a CVSS score is 0.0
