SPDX-License-Identifier: Community-Spec-1.0

# AnyLicenseInfo

## Summary

Abstract class representing a license combination consisting of one or more
licenses (optionally including additional text), which may be combined
according to the SPDX license expression syntax.

## Description

An AnyLicenseInfo is used by a licensing field for a software package,
file or snippet when its value is not NOASSERTION or NONE. It can be a
single license (either on the SPDX License List or a custom-defined license);
a single license with an "or later" operator applied; the foregoing with
additional text applied; or a set of licenses combined by applying "AND" and
"OR" operators recursively.

## Metadata

- name: AnyLicenseInfo
- SubclassOf: LicenseField
- Instantiability: Abstract

## Properties
