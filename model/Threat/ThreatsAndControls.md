SPDX-License-Identifier: Community-Spec-1.0

# Threats and Control

## Summary

Enables to model Threats, Threat Assessments and Controls.

## Description

The Threats and Controls namespace defines elements and relationships to outline threats, assess threats and 
high-level controls.

## Metadata

- id: https://spdx.org/rdf/3.1/terms/ThreatsAndControls
- name: ThreatsAndControls


## Profile conformance (see Licensing as reference)

For an element collection to be conformant with this profile,
the following has to hold:

1. for every `/Threat/Threat` there shall exist one or more
   `/Core/Relationship` of type `basedOn` having that element as
   its `from` property and a `/Threat/TreatReference` or `/Core/Requirement` as its `to`
   property.

