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

- id: https://spdx.org/rdf/3.0.0/terms/Lite
- name: Lite

## Profile conformance

In addition to the following, please refer to the Annex for elements defined in other profiles that should be included as part of the Lite profile.

For a /Software/Package to be conformant with this profile,
the following has to hold:

1. The mincount for /Core/Element/name is 1
1. The mincount for /Software/Package/packageVersion is 1
1. The mincount for /Software/SoftwareArtifact/copyrightText is 1

1. for every `/Software/Package` there MUST exist exactly one `/Core/Relationship`
   of type `concludedLicense` having that element as its `from` property
   and an `/SimpleLicensing/AnyLicenseInfo` as its `to` property.
1. for every `/Software/Package` there MUST exist exactly one `/Core/Relationship`
   of type `declaredLicense` having that element as its `from` property
   and an `/SimpleLicensing/AnyLicenseInfo` as its `to` property.
