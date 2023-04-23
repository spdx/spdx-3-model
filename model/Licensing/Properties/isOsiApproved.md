#SPDX-License-Identifier: Community-Spec-1.0

# isOsiApproved

## Summary

isOsiApproved specifies whether the License is listed as approved by the
[Open Source Initiative (OSI)](https://opensource.org).

## Description

isOsiApproved specifies whether the OSI has listed this License as "approved"
in their list of OSI Approved Licenses, located at the time of this writing at
https://opensource.org/licenses/.

A value of "true" indicates that the OSI has listed this License as approved.

A value of "false" indicates that the OSI has not listed this License as
approved.

If no isOsiApproved field is specified, this indicates that the SPDX data
creator is not making any assertions about whether the License is approved
by the OSI.

## Metadata

- name: isOsiApproved
- Nature: DataProperty
- Range: xsd:boolean
