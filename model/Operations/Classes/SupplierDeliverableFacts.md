SPDX-License-Identifier: Community-Spec-1.0

# SupplierDeliverableFacts

## Summary

Relevant metadata for a deliverable from a supplier used in own deliverable.

## Description

The supplier relation can vary according to the terms and conditions agreed between customer and supplier. Based on that some of the necessary metadata may be provided in different ways. The details may be described in the defined fields. For Open Source components the information may be derived from the Open Source license and context and thus this factsheet is only relevant in a commercial supplier-customer-relationship.

## Metadata

- name: SupplierDeliverableFacts
- SubclassOf: Delivery
- Instantiability: Concrete

## Properties

- supplierName
  - type: /Core/Agent
  - minCount: 1
- deliverableFromSupplier
  - type: /Core/Artifact
  - minCount: 1
- fossTermsTowardsSupplier
  - type: /Core/Artifact
  - maxCount: 1
- distributionTermsFromSupplier
  - type: /Core/Artifact
  - maxCount: 1
- fossComplianceBundleConsumption
  - type: fossComplianceBundleProvisionType
  - minCount: 1
- supplierFossContact
  - type: /Core/Agent
  - minCount: 1
