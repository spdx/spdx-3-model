SPDX-License-Identifier: Community-Spec-1.0

# standardCompliance

## Summary

Captures a standard that an artifact is being complied with.

## Description

A free-form text that captures a standard that an artifact complies with.

This includes both published and unpublished standards, such as those developed
by ETSI, IEEE, IETF, ISO, and W3C, as well as national standards bodies.

The standard may, but is not necessarily required to, satisfy a legal or
regulatory requirement.

If the artifact is using a standard as a reference or guideline, but not
necessarily compliant with it, use the `standardName` property instead.

## Metadata

- name: standardCompliance
- Nature: DataProperty
- Range: xsd:string
