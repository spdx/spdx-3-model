SPDX-License-Identifier: Community-Spec-1.0

# standardCompliance

## Summary

A standard with which the artifact complies.

## Description

A free-form textual description that captures a standard with which the
artifact complies.

The standard may, but is not necessarily required to, satisfy a legal or
regulatory requirement.

If the artifact is using a standard as a reference or guideline, but not
necessarily compliant with it, use the `/Core/standardName` property instead.

For a detailed compliance information, please consider defining
a `/Core/Relationship` with "conformsTo" relationship type to
a `/Core/Regulation`.

## Metadata

- name: standardCompliance
- Nature: DataProperty
- Range: xsd:string
