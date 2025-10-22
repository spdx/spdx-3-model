SPDX-License-Identifier: Community-Spec-1.0

# obsoletedBy

## Summary

Specifies the licenseId that is preferred to be used in place of a deprecated
License or LicenseAddition.

## Description

An obsoletedBy value for a deprecated License or LicenseAddition specifies
the licenseId of the replacement License or LicenseAddition that is preferred
to be used in its place. It shall use the same format as specified for a
licenseId.

The License's or LicenseAddition's comment value may include more information
about the reason why the licenseId specified in the obsoletedBy value is
preferred.

## Metadata

- name: obsoletedBy
- Nature: DataProperty
- Range: xsd:string

## Summary @zh-Hans

指定了用于替代已弃用的许可证（`License`）或者许可证附加内容（`LicenseAddition`）的首选的licenseId。

## Description @zh-Hans

对于已弃用的许可证（`License`）或者许可证附加内容（`LicenseAddition`），`obsoletedBy` 值指定用于替代许可证（`License`）或者许可证附加内容（`LicenseAddition`）的首选许可证Id。应使用与为的licenseId指定的格式相同的格式。

许可证（`License`）或者许可证附加内容（`LicenseAddition`）的注释值可能包含关于在`obsoletedBy`值中首选指定的licenseId的原因的更多信息。
