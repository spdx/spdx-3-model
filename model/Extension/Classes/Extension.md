SPDX-License-Identifier: Community-Spec-1.0

# Extension

## Summary

A characterization of some aspect of an Element that is associated with the Element in a generalized fashion.

## Description

An Extension is a characterization of some aspect of an Element that is associated with the Element in a generalized fashion.

Rather than being associated with a particular Element through the typical use of a purpose-specific object property an Extension is associated with the Element it characterizes using a single common generalized object property.

This approach serves multiple purposes:

1. Support profile-based extended characterization of Elements. Enables specification and expression of Element characterization extensions within any profile and namespace of SPDX without requiring changes to other profiles or namespaces and without requiring local subclassing of remote classes (which could inhibit ecosystem interoperability in some cases).

2. Support extension of SPDX by adopting individuals or communities with Element characterization details uniquely specialized to their particular context. Enables adopting individuals or communities to utilize SPDX expressive capabilities along with expressing more arcane Element characterization details specific to them and not appropriate for standardization across SPDX.

3. Support structured capture of expressive solutions for gaps in SPDX coverage from real-world use. Enables adopting individuals or communities to express Element characterization details they require that are not currently defined in SPDX but likely should be. Enables a practical pipeline that:

    - identifies gaps in SPDX that should be filled,
    - expresses solutions to those gaps in a way that allows the identifying adopters to use the extended solutions with SPDX and does not conflict with current SPDX,
    - can be clearly detected among the SPDX content exchange ecosystem,
    - provides a clear and structured definition of gap solution that can be used as submission for revision to SPDX standard

## Metadata

- name: Extension
- Instantiability: Abstract
