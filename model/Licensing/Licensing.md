SPDX-License-Identifier: Community-Spec-1.0

# Licensing

## Summary

The Licensing Profile defines a minimum set of license information to facilitate compliance with typical license use cases.

## Description

The Licensing profile only contains the additional requirement that any Software Artifact must have a concludedLicense Relationship.

Classes and Property restrictions are defined in the SimpleLicensingProfile
(Classes and Properties associated with string license expressions) and in the ExpandedLicensingProfile (Classes and Properties used for a
fully parsed syntax tree of license expressions).

There are 2 relationship types related to licensing - declaredLicense and concludedLicense.

A declaredLicense identifies the license information actually found in the Software Artifact,
for example as detected by use of automated tooling.

This field is not intended to capture license information obtained from an
external source, such as a package's website. Such information can be
included, as needed, in the concludedLicense field.

A declaredLicense may be expressed differently in practice for different
types of Software Artifacts. For example:

* for Packages:
  * would include license info for the Package as a
    whole, found in the Package itself (e.g., LICENSE file,
    README file, metadata in the Package, etc.)
  * would not include any license information that is not in the Package
    itself (e.g., license information from the project’s website or from a
    third party repository or website)
* for Files:
  * would include license info found in the File itself (e.g., license
    header or notice, comments indicating the license, SPDX-License-Identifier expression)
  * would not include license info found in a different file (e.g., LICENSE
    file in the top directory of a repository)
* for Snippets:
  * would include license info found in the Snippet itself (e.g., license
    notice, comments, SPDX-License-Identifier expression)
  * would not include license info found elsewhere in the File or in a
    different File (e.g., comment at top of File if it is not within the
    Snippet, LICENSE file in the top directory of a repository)

A declaredLicense relationship to NoneLicense indicates that the
corresponding Package, File or Snippet contains no license information
whatsoever.

A declaredLicense relationship to NoAssertionLicense 
indicates that one of the following applies:
* the SPDX data creator has attempted to but cannot reach a reasonable
  objective determination;
* the SPDX data creator has made no attempt to determine this field; or
* the SPDX data creator has intentionally provided no information (no meaning
  should be implied by doing so).
  
If a declaredLicense relationship is not present, no assumptions can be made
about whether or not a declaredLicense exists.
Note that a missing declaredLicense is not the same as a relationship to NoAssertionLicense
since the latter is a "known unknown" whereas no assumptions can be made
from a missing declaredLicense relationship.



A concludedLicense is the license identified by the SPDX data creator,
based on analyzing the license information in the Software Artifact
and other information to arrive at a reasonably objective
conclusion as to what license governs the Software Artifact.

A concludedLicense relationship to NoneLicense indicates that the
SPDX data creator has looked and did not find any license information for this
Software Artifact.

A concludedLicense relationship to NoAssertionLicense
indicates that one of the following applies:
* the SPDX data creator has attempted to but cannot reach a reasonable
  objective determination;
* the SPDX data creator has made no attempt to determine this field; or
* the SPDX data creator has intentionally provided no information (no
  meaning should be implied by doing so).
 
If a concludedLicense is not present, no assumptions can be made
about whether or not a concludedLicense exists.
Note that a missing concludedLicense is not the same as a relationship to a NoAssertionLicense
since the latter is a "known unknown" whereas no assumptions can be made
from a missing concludedLicense relationship.

A written explanation of a relationship to a NoAssertionLicense MAY be
provided in the comment field for the relationship.

If the concludedLicense for a Software Artifact is not the
same as its declaredLicense, a written explanation SHOULD be provided in
the concludedLicense relationship comment field.


## Metadata

- id: https://spdx.org/rdf/3.0.0/terms/Licensing
- name: Licensing


## Profile conformance

For an element collection to be conformant with this profile,
the following has to hold:

1. for every `/Software/SoftwareArtifact` there MUST exist exactly one `/Core/Relationship`
   of type `concludedLicense` having that element as its `from` property
   and an `/SimpleLicensing/AnyLicenseInfo` as its `to` property.


