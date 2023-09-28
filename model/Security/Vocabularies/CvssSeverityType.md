SPDX-License-Identifier: Community-Spec-1.0

# CvssSeverityType

## Summary

Specifies the CVSS severity type.

## Description

CvssSeverityType specifies the CVSS severity type, defined as the textual representation of the numeric CVSS score. The severity type entries are inclusive of and applicable to enumerations found in CVSS versions 3 and 4. The field can be used to document the base, temporal, threat, or environmental severity.

## Metadata

- name: CvssSeverityType

## Entries

- critical: When a CVSS score is between 9.0 - 10.0
- high: When a CVSS score is between 7.0 - 8.9
- medium: When a CVSS score is between 4 - 6.9
- low: When a CVSS score is between 0 - 3.9
- none: When a CVSS score is 0
- noAssertion: No assertion can be made about the severity of the CVSS score.