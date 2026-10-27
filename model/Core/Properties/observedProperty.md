SPDX-License-Identifier: Community-Spec-1.0

# observedProperty

## Summary

IRI that identifies what was observed by an Observation.

## Description

The `observedProperty` property identifies the property of the subject that
an `Observation` observed, such as an amount of energy, a number of tokens,
or whether personal data is present.

The unit of a result does not identify what was observed:
for example, an energy in kilowatt-hours may be consumed by accelerators only
or by a whole facility, and a count may be of tokens or of images.

The value should be chosen as follows:

- If a QUDT quantity kind fully identifies the observed property for the
  subject, its IRI shall be used (for example,
  <http://qudt.org/vocab/quantitykind/Temperature> for the temperature of
  a shipment).
- Otherwise, an entry of an SPDX observable property vocabulary should be
  used, if one fits.
  These are `ObservablePropertyType`,
  `/AI/AIObservablePropertyType`, and
  `/Dataset/DatasetObservablePropertyType`.
- Otherwise, an IRI from another published vocabulary may be used.

A QUDT quantity kind does not fully identify the observed property if the
same subject could have two different Observations of that quantity kind.
For example, a training run may have both its accelerator energy and its
facility energy observed, so <http://qudt.org/vocab/quantitykind/Energy> is
not specific enough.

The QUDT ontologies and specifications are available at
<https://www.qudt.org/>.

## Metadata

- name: observedProperty
- Nature: DataProperty
- Range: xsd:anyURI
