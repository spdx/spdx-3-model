SPDX-License-Identifier: Community-Spec-1.0

# Lite

## Summary

The SPDX Lite profile defines a subset of the SPDX specification, from the point of view of use cases in some industries. SPDX Lite aims at the balance between the SPDX standard and actual workflows in some industries.

## Description

The SPDX Lite profile consists of mandatory fields from the Document Creation and Package Information sections and other basic information.

The mandatory part of the Package information in SPDX Lite is basic but useful for complying with licenses. It is easy to understand licensing information by reading an SPDX Lite file. It is easy to create manually an SPDX Lite file by anyone who does not have enough knowledge about licensing information, so that tools are not necessarily required to create an SPDX Lite file.

SPDX Lite has affinity with SPDX tools due to its containing the mandatory part of the Document Creation and Package Information in the SPDX Lite definition.

An SPDX Lite document can be used in parallel with SPDX documents in software supply chains.

## Metadata

- id: https://rdf.spdx.org/v3/Lite
- name: Lite

## External properties restrictions

- /Software/Package
  - /Core/Element/name
    - minCount: 1
  - /Software/Package/packageVersion
    - minCount: 1
  - /Software/Package/packageUrl
    - minCount: 1
  - /Software/SoftwareArtifact/concludedLicense
    - minCount: 1
  - /Software/SoftwareArtifact/declaredLicense
    - minCount: 1	
  - /Software/SoftwareArtifact/copyrightText

- TODO - add other class restrictions
