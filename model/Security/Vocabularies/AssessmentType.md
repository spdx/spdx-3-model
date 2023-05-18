SPDX-License-Identifier: Community-Spec-1.0

# AssessmentType

## Summary

Specifies the type of assessment data a hasAssessmentFor relationship contains.

## Description

Vulnerabilities and elements linked with a hasAssessmentFor express a security
assessment. The type of assessment must be noted on the assessmentType property
of a relationship subclassed from VulnAssessmentRelationship.

## Metadata

- name: AssessmentType

## Entries

- cvss2: Common Vulnerability Scoring System v2
- cvss3: Common Vulnerability Scoring System v3
- epss: Exploit Prediction Scoring System
- exploitCatalog: Known exploits catalog
- ssvc: Stakeholder-Specific Vulnerability Categorization
- vex: Vulnerability Exploitability eXchange
