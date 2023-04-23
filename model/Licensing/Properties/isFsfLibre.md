SPDX-License-Identifier: Community-Spec-1.0

# isFsfLibre

## Summary

isFsfLibre specifies whether the License is listed as free by the
[Free Software Foundation (FSF)](https://fsf.org).

## Description

isFsfLibre specifies whether the FSF has listed this License as "free" in
their commentary on licenses, located at the time of this writing at
https://www.gnu.org/licenses/license-list.en.html.

A value of "true" indicates that the FSF has listed this License as _free_.

A value of "false" indicates that the FSF has listed this License as _not free.

If no isFsfLibre field is specified, this indicates that the SPDX data creator
is not making any assertions about whether the License is listed in the FSF's
commentary.

## Metadata

- name: isFsfLibre
- Nature: DataProperty
- Range: xsd:boolean
