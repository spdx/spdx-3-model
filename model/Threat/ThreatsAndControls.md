SPDX-License-Identifier: Community-Spec-1.0

# Threats and Control

## Summary

Enables to model Threats and Controls as different assessment targets.

## Description

The Threats and Controls namespace defines elements and relationships to outline and assess threats and controls.

The profile enables to communicate the context and conditions under which the evaluation of Threats are performed. The
approach envisions to convey both the resulting protective design and the intended deployment in which Vulnerabilities
can be evaluated in context.

The current approach is regarded to be result of a threat analysis or threat modeling endeavor. While the model does 
not capture the analysis or modeling process itself, it conveys and enables the resulting evaluation context, such that
the vulnerabilities can be assessed in the same fashion by the supplier and the consumers of an SPDX document. Rather
that a Threat Model the Threats and Controls namespace defines a Threat and Control harness, within which the hard- 
and/or software described can be evaluated.

## Metadata

- id: https://spdx.org/rdf/3/terms/ThreatsAndControls
- name: ThreatsAndControls

## Profile conformance (see Licensing as reference)

For an element collection to be conformant with this profile,
the following has to hold:

1. for every `/Threat/Threat` there shall exist one or more
   `/Core/Relationship` of type `basedOn` having that element as
   its `from` property and a `/Threat/TreatReference` or `/Core/Requirement` as its `to`
   property.