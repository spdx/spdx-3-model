SPDX-License-Identifier: Community-Spec-1.0

# Security

## Summary

The Security profile describes vulnerabilities and assessments of how they affect software and other elements.

## Description

The Security profile defines concepts for sharing vulnerability information
alongside the elements it applies to. It lets suppliers, consumers, and security
teams identify a vulnerability, record who found, reported, published, or fixed
it, and exchange assessments of its impact on specific products and components.

A `Vulnerability` identifies the weakness itself, for example by its CVE or
GHSA identifier. Assessments are expressed as relationships from a
`Vulnerability` to the affected elements. The `VulnAssessmentRelationship`
subclasses carry severity scores (CVSS version 2, 3, and 4), exploit prediction
(EPSS), exploit catalog listings such as CISA KEV, and SSVC decisions. The
`VexVulnAssessmentRelationship` subclasses carry Vulnerability Exploitability
eXchange (VEX) statements, saying whether a product is affected, not affected,
fixed, or under investigation, with a justification where one applies.

Security information can be combined with the Software, Build, and other
profiles to describe exposure across a supply chain, and can be published in the
same document as the elements it describes or separately, for example as a
standalone VEX document that refers to elements of an existing SBOM.

## Metadata

- id: https://spdx.org/rdf/3/terms/Security
- name: Security
