SPDX-License-Identifier: Community-Spec-1.0

# Threats and Control

## Summary

Enables to model Threats and Controls as different assessment targets.

## Description

The Threats and Controls namespace defines elements and relationships to outline threats, assess threats and controls.

The profile enables to communicate the context and conditions under which the evaluation of Threats are performed. The
approach envisions to convey both the resulting protective design and the intended deployment in which Vulnerabilities
can be evaluated in context.

TODO:

- Provide definitions on Threat-Analysis, Threat-Model, Threat-Modeling, Threat Catalog and differentiate these.

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

