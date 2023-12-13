SPDX-License-Identifier: Community-Spec-1.0

# vectorString

## Summary

Specifies the CVSS vector string for a vulnerability.

## Description

Specifies any combination of the CVSS Base, Temporal, Threat, Environmental, and/or Supplemental vector string values for a vulnerability. Supports vectorStrings specified in all CVSS versions.

**Constraints**

String values for the vectorString range must only include the abbreviated form of metric names specified in CVSS specifications, e.g. [https://www.first.org/cvss/v4.0/specification-document#Vector-String](https://www.first.org/cvss/v4.0/specification-document#Vector-String)

## Metadata

- name: vectorString
- Nature: DataProperty
- Range: xsd:string

