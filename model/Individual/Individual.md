SPDX-License-Identifier: Community-Spec-1.0

# Individual

## Summary

A profile to be used when sharing individual SPDX Element.

## Description

Although most use cases involve sharing Elements inside a Collection, there are cases where a stand-alone SPDX element may be made available.
In those cases, the Element creationInfo property would be required to identify the Agent that created the element.

## Metadata

- id: https://rdf.spdx.org/v3/Individual
- name: Individual

## External properties restrictions

- /Core/Element/creationInfo
  - minCount: 1
