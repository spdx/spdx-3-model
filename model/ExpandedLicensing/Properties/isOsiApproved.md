SPDX-License-Identifier: Community-Spec-1.0

# isOsiApproved

## Summary

Specifies whether the License is listed as approved by the
[Open Source Initiative (OSI)](https://opensource.org).

## Description

isOsiApproved specifies whether the
[Open Source Initiative (OSI)](https://opensource.org)
has listed this License as "approved" in their list of OSI Approved Licenses,
located at the time of this writing at
[OSI Approved Licenses](https://opensource.org/licenses).

A value of "true" indicates that the license is in the list of licenses that
OSI publishes as approved.

A value of "false" indicates that the license is explicitly not in the
corresponding list of OSI licenses (e.g., OSI has stated publicly that a
license is not approved).

If the isOsiApproved field is not specified, the SPDX data creator makes no
assertions about whether the License is approved by the OSI.

## Metadata

- name: isOsiApproved
- Nature: DataProperty
- Range: xsd:boolean
