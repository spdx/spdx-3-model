SPDX-License-Identifier: Community-Spec-1.0

# ExportControlClassification

## Summary

The Element for export control classification.

## Description

The result of the export control classification assessment, including exporting country, weight and comment. 

## Metadata

- name: ExportControlClassification
- Instantiability: Concrete

## Properties

- exportingCountry
  - type: /Core/CountryCodeAlpha3
  - minCount: 1
  - maxCount: 1
- exportControlSpecification
  - type: /Core/Specification
  - minCount: 1
  - maxCount: 1
- exportClassification
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- weight
  - type: xsd:positiveInteger
  - maxCount: 1
- /Core/comment
  - type: xsd:string
  - maxCount: 1
