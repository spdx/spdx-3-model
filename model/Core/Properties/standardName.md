SPDX-License-Identifier: Community-Spec-1.0

# standardName

## Summary

The name of a standard applicable to an artifact.

## Description

A standard applicable as a reference or guideline for the
design, implementation, production, or evaluation of the artifact.

This property does not imply that the artifact complies with the standard.

For compliance with a standard, use
a [Relationship](../Classes/Relationship.md)
with "conformsTo" relationship type to
a [Specification](../Classes/Specification.md)
instead.

## Metadata

- name: standardName
- Nature: DataProperty
- Range: xsd:string
