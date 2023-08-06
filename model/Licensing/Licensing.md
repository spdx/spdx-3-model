SPDX-License-Identifier: Community-Spec-1.0

# Licensing

## Summary

The Licensing Profile defines a minimum set of license information required to comply with typical license compliance use cases.

## Description

The Licensing profile only contains the additional requirement that any Software Artifact must have a concludedLicense Relationship.

Classes and Property restrictions are defined in the SimpleLicensingProfile
(Classes and Properties associated with string license expressions) and in the ExpandedLicensingProfile (Classes and Properties used for a
fully parsed syntax tree of license expressions).

There are 2 licensing related relationship types - declaredLicense and concludedLicense.

A declaredLicense identifies the license information actually found in the Software Artifact,
for example as detected by use of automated tooling.

This field is not intended to capture license information obtained from an
external source, such as a package's website. Such information can be
included, as needed, in a concludedLicense field.

A declaredLicense may be expressed differently in practice for different
types of Software Artifacts. For example:

* for Packages:
  * would include license info describing the license of the Package as a
    whole, when it is found in the Package itself (e.g., LICENSE file,
    README file, metadata in the repository, etc.)
  * would not include any license information that is not in the Package
    itself (e.g., license information from the project’s website or from a
    third party repository or website)
* for Files:
  * would include license info found in the File itself (e.g., license
    header or notice, comments, SPDX-License-Identifier expression)
  * would not include license info found in a different file (e.g., LICENSE
    file in the top directory of a repository)
* for Snippets:
  * would include license info found in the Snippet itself (e.g., license
    notice, comments, SPDX-License-Identifier expression)
  * would not include license info found elsewhere in the File or in a
    different File (e.g., comment at top of File if it is not within the
    Snippet, LICENSE file in the top directory of a repository)

A declaredLicense is related to a NoneLicenseindicates that the
corresponding Package, File or Snippet contains no license information
whatsoever.

A declaredLicense related to aNoAssertionLicense
indicates that one of the following applies:
* the SPDX data creator has attempted to but cannot reach a reasonable
  objective determination;
* the SPDX data creator has made no attempt to determine this field; or
* the SPDX data creator has intentionally provided no information (no meaning
  should be implied by doing so).
  
If a declaredLicense relationship is not present, no conclusion can be drawn.
Note that a missing declaredLicense is not the same as a relationship to a NoAssertionLicense
since the latter is a "known unknown" whereas no conclusion can be drawn
from a missing declaredLicense relationship.



A concludedLicense is the license identified by the SPDX data creator,
based on analyzing the license information in the Software Artifact
and other information to arrive at a reasonably objective
conclusion as to what license governs it.

A concludedLicense related to a NoneLicense indicates that the
SPDX data creator has looked and did not find any license information for this
Software Artifact.

A concludedLicense related to a NoAssertionLicense
indicates that one of the following applies:
* the SPDX data creator has attempted to but cannot reach a reasonable
  objective determination;
* the SPDX data creator has made no attempt to determine this field; or
* the SPDX data creator has intentionally provided no information (no
  meaning should be implied by doing so).
 
If a concludedLicense is not present, no conclusion can be drawn.
Note that a missing or null concludedLicense is not the same as a relationship to a NoAssertionLicense
since the latter is a "known unknown" whereas no conclusion can be drawn
from a missing or null value.

A written explanation of a relationship to a NoAssertionLicense MAY be
provided in the comment field for the relationship.

If the concludedLicense for a Software Artifact is not the
same as its declaredLicense, a written explanation SHOULD be provided in
the concludedLicense relationship comment field.


## Metadata

- id: https://rdf.spdx.org/v3/Licensing
- name: Licensing
