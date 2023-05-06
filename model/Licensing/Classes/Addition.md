SPDX-License-Identifier: Community-Spec-1.0

# Addition

## Summary

Abstract class for additional text intended to be added to a License, but
which is not itself a standalone License.

## Description

An Addition represents text which is intended to be added to a License
as additional text, but which is not itself intended to be a standalone
License.

It may be an exception which is listed on the SPDX Exceptions List
(ListedLicenseException), or may be any other additional text (as an exception
or otherwise) which is defined by an SPDX data creator (CustomAddition).

## Metadata

- name: Addition
- SubclassOf: LicensingText
- Instantiability: Abstract

## Properties

