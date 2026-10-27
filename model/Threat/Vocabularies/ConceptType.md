SPDX-License-Identifier: Community-Spec-1.0

# ConceptType

## Summary

The ConceptType expresses the type of an existing concept.

## Description

An object in Threats & Controls may be associated to one or more ConceptReferences. The ConceptType defines the
currently supported types.

## Metadata

- name: ConceptType

## Entries

- securityRequirement: an externally defined security requirement. Using this reference type a Threat may be linked
  to a security requirement defined in a standard or norm.
- attackPattern: represents an attack pattern (such as CAPEC); see https://capec.mitre.org/data/index.html
- attackTactic: represents an attack tactic (compare MITRE ATT&CK); see https://attack.mitre.org/
- attackTechnique: represents an attack technique (compare MITRE ATT&CK); see https://attack.mitre.org/
- attackProcedure: represents an attack procedure
- weakness: represents a weakness (such as CWEs) that may be exploited; see https://cwe.mitre.org/data/index.html
- securityControl: represents a security control
- defenseTechnique: represents a technique establishing a defense
- mitigation: an activity to reduce the potential impact
- counterMeasure: a derived measure to address a potenital threat
