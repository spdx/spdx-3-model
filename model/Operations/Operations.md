SPDX-License-Identifier: Community-Spec-1.0

# Operations

## Summary

The Operations profile defines fields for describing the business context of the software that cannot (or not yet) be directly extracted from the source repository. Operations include technical operations and business operations.

## Description

The intention of the Operations profile is to provide a common base rather for alignment of tool and infrastructure interfaces and development than for exchanging the data between organizations along the software supply chain. In a first phase it shall focus on business operations. The managed information is expected to be mainly kept within the organizations but in some cases might also be necessary input for processing and determining relevant parameters for the later exchange in the supply chain (e.g. Export Control Classification Number).

The information about an Element shall describe facts about the distribution and business context of the Element brought into the market, that could consist of several deliverables. The relation between Element and Deliverable targets can be one to many.

The information about deliverables shall provide more detailed information about the software item already in early phases of the product lifecycle, where the content may still be a planning or intended value that can be replaced and updated by real values in further phases (e.g. used programming language, used frameworks).

The Operations assessment descriptions are patterns for business relevant assessments like an ExportControl assessment to manage all necessary inputs for such an assessment from all over the SPDX model.

## Metadata

- id: https://spdx.org/rdf/3.1/terms/Operations
- name: Operations
