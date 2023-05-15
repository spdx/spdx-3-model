SPDX-License-Identifier: Community-Spec-1.0

# declaredLicense

## Summary

Identifies the license information actually found in the software Package,
File or Snippet, for example as detected by use of automated tooling.

## Description

A declaredLicense is the license identified in text in the software package,
file or snippet as the license declared by its authors.

This field is not intended to capture license information obtained from an
external source, such as a package's website. Such information can be
included, as needed, in a concludedLicense field.

A declaredLicense may be expressed differently in practice for different
types of artifacts. For example:

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

If a declaredLicense has a NONE value (NoneLicense), this indicates that the
corresponding Package, File or Snippet contains no license information
whatsoever.

If a declaredLicense has a NOASSERTION value (NoAssertionLicense), this
indicates that one of the following applies:
* the SPDX data creator has attempted to but cannot reach a reasonable
  objective determination;
* the SPDX data creator has made no attempt to determine this field; or
* the SPDX data creator has intentionally provided no information (no meaning
  should be implied by doing so).

## Metadata

- name: declaredLicense
- Nature: ObjectProperty
- Range: /Licensing/LicenseField
