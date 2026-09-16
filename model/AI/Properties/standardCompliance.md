SPDX-License-Identifier: Community-Spec-1.0

# standardCompliance

## Summary

**DEPRECATED in SPDX 3.1.**
Use [/Core/Relationship](../../Core/Classes/Regulation.md)
with "conformsTo" relationship type instead.

A standard with which the artifact complies.

## Description

**NOTE:**
This property is deprecated and only included for backward compatibility.
New documents should use
a [/Core/Relationship](../../Core/Classes/Relationship.md)
with "conformsTo" relationship type to
a [/Core/Specification](../../Core/Classes/Specification.md)
instead.

A free-form textual description that captures a standard with which the
artifact complies.

The standard can, but is not necessarily required to, satisfy a legal or
regulatory requirement.

If the artifact is using a standard as a reference or guideline, but not
necessarily compliant with it, use the `/Core/standardName` property instead.

## Metadata

- name: standardCompliance
- Nature: DataProperty
- Range: xsd:string
