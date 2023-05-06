SPDX-License-Identifier: Community-Spec-1.0

# obsoletedBy

## Summary

Specifies the identifier that is preferred to be used in place of a deprecated License or Addition.

## Description

An obsoletedBy value for a deprecated License or Addition specifies
the id of the replacement License or LicenseAddition that is preferred
to be used in its place. It should use the same format as specified for an id.

The License's or Addition's comment value may include more information
about the reason why the id specified in the obsoletedBy value is preferred.

## Metadata

- name: obsoletedBy
- Nature: DataProperty
- Range: xsd:anyURI

