SPDX-License-Identifier: Community-Spec-1.0

# ThreatReferenceType

## Summary

The reference type categorizes the different threat reference types.

## Description

A Threat may be associated to one or more ThreatReferences of different types. The ThreatReferenceType defines the
currently supported types.

## Metadata

- name: ThreatReferenceType

## Entries

- securityRequirement: an externally defined security requirement. Using this reference type a Threat may be linked
  to a security requirement defined in a standard or norm.
- attackPattern: represents an attack pattern (such as CAPEC); see https://capec.mitre.org/data/index.html
- attackTactic: represents an attack tactic (compare MITRE ATT&CK); see https://attack.mitre.org/
- attackTechnique: represents an attack technique (compare MITRE ATT&CK); see https://attack.mitre.org/
- attackProcedure: represents an attack procedure
- weakness: represents a weakness (such as CWEs) that may be exploited; see https://cwe.mitre.org/data/index.html

