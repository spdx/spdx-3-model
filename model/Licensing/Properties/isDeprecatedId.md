SPDX-License-Identifier: Community-Spec-1.0

# isDeprecatedId

## Summary

Specifies whether a license or additional text identifier has been marked as deprecated.

## Description

The isDeprecatedId property specifies whether an identifier
for a License or an Addition has been marked as deprecated.

If the property is not defined, then it is presumed to be false (i.e., not deprecated).

"Deprecated" in this context refers to deprecating the use of the
_identifier_, not the underlying license. In other words, even if a License's
author or steward has stated that a particular License generally should not be
used, that would _not_ mean that the License's identifier is "deprecated."
Rather, a License or Addition is typically marked as "deprecated"
when it is determined that use of another identifier is preferable.

## Metadata

- name: isDeprecatedId
- Nature: DataProperty
- Range: xsd:boolean
