# Asset

## Summary

An item of value to stakeholders.

## Description

An asset may be tangible (e.g., a physical item such as hardware, firmware, computing platform, network device, or other
technology component) or intangible (e.g., humans, data, information, software, capability, function, service,
trademark, copyright, patent, intellectual
property, image, or reputation).

Assets can be linked to existing elements in an SPDX document. I.e. an SBOM may be linked to an asset using
a ReferenceRelationship with relationship type 'constitutedBy'.

## Metadata

- name: Asset
- SubclassOf: /Core/Element
- Instantiability: Concrete

## Properties

- genericDemand
  - type: Assessment
  - minCount: 0

