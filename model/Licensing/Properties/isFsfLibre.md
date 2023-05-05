SPDX-License-Identifier: Community-Spec-1.0

# isFsfLibre

## Summary

Specifies whether the License is listed as free by the
[Free Software Foundation (FSF)](https://fsf.org).

## Description

isFsfLibre specifies whether the [Free Software Foundation FSF](https://fsf.org)
has listed this License as "free" in their commentary on licenses, located at
the time of this writing at https://www.gnu.org/licenses/license-list.en.html.

A value of "true" indicates that the FSF has listed this License as _free_.

A value of "false" indicates that the FSF has listed this License as _not free_.

If the isFsfLibre field is not specified, the SPDX data creator makes no
assertions about whether the License is listed in the FSF's commentary.

## Metadata

- name: isFsfLibre
- Nature: DataProperty
- Range: xsd:boolean
