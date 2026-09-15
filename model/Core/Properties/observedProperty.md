SPDX-License-Identifier: Community-Spec-1.0

# observedProperty

## Summary

URI that identifies the specific dimension, characteristic, or metric being
quantified.

## Description

The `observedProperty` property specifies the characteristic being measured
during an `Observation`.

The value is constrained to the QUDT `quantityKind` vocabulary
(for example, `http://qudt.org/vocab/quantitykind/Distance` or
`http://qudt.org/vocab/quantitykind/Energy`).
The QUDT ontology and specifications are available at <https://www.qudt.org/>.

## Metadata

- name: observedProperty
- Nature: DataProperty
- Range: anyURI
