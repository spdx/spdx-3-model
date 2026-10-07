SPDX-License-Identifier: Community-Spec-1.0

# unitQUDT

## Summary

Measurement unit defined in accordance with the QUDT (Quantity, Unit,
Dimension, and Type) ontologies, applicable to measurement criteria based
on product type, region, and use.

Measurement unit defined in accordance with the QUDT (Quantity, Unit,
Dimension, and Type) ontologies, applicable to measurement criteria based on
product type, region, and use.

## Description

This property specifies a measurement unit conforming to the QUDT
(Quantity, Unit, Dimension, and Type) ontologies.
The QUDT ontologies provide a standard framework for the representation of
physical quantities, measurement units, dimensions, and associated data types.

The value shall be an Internationalized Resource Identifier (IRI) identifying
a member of the QUDT `unit` vocabulary (for example,
<http://qudt.org/vocab/unit/M> or <http://qudt.org/vocab/unit/KiloW-HR>).
The QUDT ontologies and technical specifications are available at
<https://www.qudt.org/>.

## Metadata

- name: unitQUDT
- Nature: DataProperty
- Range: xsd:anyURI
