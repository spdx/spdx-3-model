SPDX-License-Identifier: Community-Spec-1.0

# LicenseExpression

## Summary

An SPDX Element containing an SPDX license expression string.

## Description

Often a single license can be used to represent the licensing terms of a source code or binary file, but there are situations where a single license identifier is not sufficient. A common example is when software is offered under a choice of one or more licenses (e.g., GPL-2.0-only OR BSD-3-Clause). Another example is when a set of licenses is needed to represent a binary program constructed by compiling and linking two (or more) different source files each governed by different licenses (e.g., LGPL-2.1-only AND BSD-3-Clause).

SPDX License Expressions provide a way for one to construct expressions that more accurately represent the licensing terms typically found in open source software source code. A license expression could be a single license identifier found on the SPDX License List; a user defined license reference denoted by the LicenseRef-idString; a license identifier combined with an SPDX exception; or some combination of license identifiers, license references and exceptions constructed using a small set of defined operators (e.g., AND, OR, WITH and +). We provide the definition of what constitutes a valid an SPDX License Expression in this section.

## Metadata

- name: ExtendableLicense
- SubclassOf: AnyLicenseInfo
- Instantiability: Concrete

## Properties
- licenseExpression
  - type: xsd:string
  - minCount: 1
  - maxCount: 1