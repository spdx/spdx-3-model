SPDX-License-Identifier: Community-Spec-1.0

# concludedLicense

## Summary

Identifies the license that that SPDX data creator has concluded as governing
the software Package, File or Snippet.

## Description

A concludedLicense is the license identified by the SPDX data creator,
based on analyzing the license information in the software Package, File
or Snippet and other information to arrive at a reasonably objective
conclusion as to what license governs it.

If a concludedLicense has a NONE value (NoneLicense), this indicates that the
SPDX data creator has looked and did not find any license information for this
software Package, File or Snippet.

If a concludedLicense has a NOASSERTION value (NoAssertionLicense), this
indicates that one of the following applies:
* the SPDX data creator has attempted to but cannot reach a reasonable
  objective determination;
* the SPDX data creator has made no attempt to determine this field; or
* the SPDX data creator has intentionally provided no information (no
  meaning should be implied by doing so).

A written explanation of a NOASSERTION value (NoAssertionLicense) MAY be
provided in the licenseComment field.

If the concludedLicense for a software Package, File or Snippet is not the
same as its declaredLicense, a written explanation SHOULD be provided in
the licenseComment field.

If the declaredLicense for a software Package, File or Snippet is a choice
of more than one license (e.g. a license expression combining two licenses
through use of the `OR` operator), then the concludedLicense may either
retain the license choice or identify which license was chosen.

## Metadata

- name: concludedLicense
- Nature: ObjectProperty
- Range: /Licensing/LicenseField
