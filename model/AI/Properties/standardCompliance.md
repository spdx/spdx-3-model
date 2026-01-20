SPDX-License-Identifier: Community-Spec-1.0

# standardCompliance

## Summary

Standard that an artifact is being complied with.

## Description

A free-form text that captures a standard that an artifact complies with.

The standard may, but is not necessarily required to, satisfy a legal or
regulatory requirement.

If the artifact is using a standard as a reference or guideline, but not
necessarily compliant with it, use the `/Core/standardName` property instead.

For a detailed compliance information, please consider defining
a `Relationship` with "conformsTo" relationship type to a `Regulation`.

## Metadata

- name: standardCompliance
- Nature: DataProperty
- Range: xsd:string
