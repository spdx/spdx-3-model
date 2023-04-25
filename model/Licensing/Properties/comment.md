SPDX-License-Identifier: Community-Spec-1.0

# comment

## Summary

Identifies general comments about the License or LicenseException.

## Description

A comment for a License or LicenseException describes general factual
information about the License or LicenseException. It should not contain
information (or links to information) that includes any kind of interpretation
about the meaning or effect of the License or LicenseException, even if
written by the license author.

Examples of information for a comment may include the following:

* If the License's or LicenseException's identifier is deprecated, it may
  briefly explain the reason for deprecation.
* It may include the date of release, if identified, for licenses with multiple
  versions.
* It may include links to other official language translations for the license.
* For LicenseExceptions, it may include a reference to the License(s) with
  which this exception is typically used.

## Metadata

- name: comment
- Nature: DataProperty
- Range: xsd:string
