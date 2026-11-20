SPDX-License-Identifier: Community-Spec-1.0

# SystemChangeAccomplishmentSummary

## Summary

Documents the accomplishment of a system change and its supporting assurance evidence.

## Description

SystemChangeAccomplishmentSummary represents a documented summary of an actual
or proposed system change, including the resulting system or software context,
the work performed, and evidence supporting the change.

The summary can bring together information commonly found in a Software
Accomplishment Summary (SAS), such as the following:

- System overview: system functions, allocation of functions to hardware and
  software, architecture, processors, hardware/software interfaces, and safety
  features.
- Software overview: software functions, safety-related behavior, and
  partitioning concepts.
- Certification considerations and applicable plans, such as the Plan for
  Software Aspects of Certification (PSAC), where relevant.
- Software life cycle: planning, development, verification, configuration
  management, quality assurance, and certification liaison activities.
- Software life cycle data and references to supporting lifecycle artifacts.
- Additional considerations relevant to the system, software, or certification
  authority.
- Supplier oversight, including relevant supplier processes and outputs.
- Software identification, including part numbers, versions, and release
  identifiers.
- Software characteristics, such as executable size, timing and memory
  margins, resource limitations, and how those characteristics are measured.
- Change history, including changes resulting from failures that may affect
  safety.
- Software status at release, including unresolved problem reports, errors,
  functional limitations, operational restrictions, potential safety effects,
  justifications, and mitigation actions.
- A compliance statement summarizing the methods used to demonstrate
  compliance with applicable plans and standards, including certification
  decisions and deviations.

Where a PSAC or equivalent approved system overview exists, the summary should
also identify areas that deviate from that overview.

The SAS concepts are guidance for organizing relevant information. This SPDX
class is intended for reuse across domains and does not itself assert
compliance with DO-178C or replace a domain-specific certification data item.
Supporting plans, lifecycle records, verification results, supplier evidence,
problem reports, and compliance records can be referenced using existing SPDX
elements and relationships.

SystemChangeAccomplishmentSummary is distinct from SystemImpactAnalysis,
which assesses whether a trigger or other source affects a system and may
conclude that no change is required. When a SystemImpactAnalysis identifies a
change requiring further assessment or documentation, it can be linked to the
SystemChangeAccomplishmentSummary using a /Core/Relationship with
relationshipType hasOutput, from the SystemImpactAnalysis to the
SystemChangeAccomplishmentSummary.

The summary can identify the elements considered and classify elements as
added, modified, or removed. An element can be linked using impactedElement
without also being classified as changed.

The /Core/rationale property, when used, explains the basis for the documented
change summary. The changed-element properties identify the scope being
documented; they do not replace the supporting accomplishment evidence.

## Metadata

- name: SystemChangeAccomplishmentSummary
- SubclassOf: /Core/Artifact
- Instantiability: Concrete

## Properties

- impactAnalysisProcess
  - type: /Core/Element
  - minCount: 0
- impactAnalysisStatus
  - type: SystemImpactAnalysisStatus
  - minCount: 0
  - maxCount: 1
- impactLevel
  - type: SystemImpactLevel
  - minCount: 0
- impactedElement
  - type: /Core/Element
  - minCount: 0
- addedElement
  - type: /Core/Element
  - minCount: 0
- modifiedElement
  - type: /Core/Element
  - minCount: 0
- removedElement
  - type: /Core/Element
  - minCount: 0
- /Core/rationale
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
