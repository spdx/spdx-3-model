SPDX-License-Identifier: Community-Spec-1.0

# VexStatusType

## Summary

Specifies the VEX status type.

## Description

VexStatusType specifies the type of Vulnerability Exploitability eXchange (VEX) status.

## Metadata

- name: VexStatusType

## Entries

- notAffected: This version is known not to be affected by the vulnerability. No remediation is required regarding this vulnerability.
- affected:  This version is known to be affected by the vulnerability.
- fixed: This version contains a fix for the vulnerability but may not be the recommended fixed version.
- underInvestigation: It is not known yet whether this version is or is not affected by the vulnerability. However, it is still under investigation - the result will be provided in a later release of the document.

