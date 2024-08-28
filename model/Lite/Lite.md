SPDX-License-Identifier: Community-Spec-1.0

# Lite

## Summary

The SPDX Lite profile defines a simple view of SPDX data,
from the point of view of use cases in some industries.

## Description


The SPDX Lite profile consists of mandatory and recommended information.

The mandatory data in SPDX Lite is basic but useful for complying with licenses.
It is easy to understand licensing information by reading an SPDX Lite file.

SPDX Lite aims at a balance between the full SPDX data model and actual workflows in some industries.

An SPDX Lite document can also be used in parallel with other SPDX documents in software supply chains.

## Metadata

- id: https://spdx.org/rdf/3.0.1/terms/Lite
- name: Lite

## Profile conformance

In addition to the following mandatory requirements,
please refer to the corresponding Annex for elements
that should be included as part of a document conforming to the Lite profile.

For a `/Software/Package` to be conformant with this profile, the following has to hold:

1. The mincount for `copyrightText` is 1
1. The mincount for `packageVersion` is 1
1. The mincount for `suppliedBy` is 1
1. At least one of `downloadLocation` or `packageUrl` must be present

Additionally:

1. for every `/Software/Package` there MUST exist exactly one
   `/Core/Relationship` of type `hasConcludedLicense` having that element as
   its `from` property and an `/SimpleLicensing/AnyLicenseInfo` as its `to`
   property.
1. for every `/Software/Package` there MUST exist exactly one
   `/Core/Relationship` of type `hasDeclaredLicense` having that element as its
   `from` property and an `/SimpleLicensing/AnyLicenseInfo` as its `to`
   property.
   
For a `/Core/SpdxDocument` to be conformant with this profile, the following has to hold:
1. The mincount for `element` is 1
1. The mincount for `rootElement` is 1

For a `/Software/Sbom` to be conformant with this profile, the following has to hold:
1. The mincount for `element` is 1
1. The mincount for `rootElement` is 1

Finally, for a `/Core/Agent` to be conformant with this profile, the following has to hold:

1. The mincount for `name` is 1
