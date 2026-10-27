SPDX-License-Identifier: Community-Spec-1.0

# Observation

## Summary

An act of observing, measuring, calculating, estimating, or declaring
a property of an Element.

## Description

An `Observation` records one result about one Element, together with how,
when, and by whom the result was obtained.

`Observation` is abstract.
The subclass to use depends on the type of the result:

- `Measurement`: a number with a unit, including a count
  (for example, 4.2 kWh, or 4012553 images).
- `PresenceObservation`: yes or no
  (for example, whether a dataset contains personal data).
- `CategoryObservation`: a term from a code list
  (for example, an energy efficiency class).

The Element observed (the feature of interest) is given by the `subject`
property.
What was observed is identified by the IRI given in the `observedProperty`
property.

The kind of Element given as `subject` determines what the result means:

- If the subject is an `Action`, the result is the actual result for that
  execution (for example, the energy consumed by one training run).
- If the subject is a `DefinedProcess`, the result is a nominal or typical
  result for an execution of that process.
  A `Measurement` of a process shall be a rate (for example, energy per
  1000 tokens), unless its `observationProcedure` states that the value is
  per execution.
- Otherwise, the result is about the Element itself (for example, the number
  of images in a dataset, or a training energy value stated in the model card
  of an AI model).

Any characteristic that depends on running something, such as energy, time,
or emissions, should be observed on the `Action` (or `DefinedProcess`)
that ran it, when that is known.

The `startTime` and `endTime` properties give the interval that the result
covers.
If they are absent and the subject is an `Action`, the interval is that of
the subject.
The `created` property of the `CreationInfo` gives when the result was
produced, which may be later than the interval.
For example, an estimate made in May about a training run in March has
`startTime` and `endTime` in March and `created` in May.

If SPDX defines a dedicated property for a characteristic
(for example, `/Software/byteSize`), that property shall be used,
and the characteristic shall not be recorded as an Observation.

The absence of an Observation means that the result is unknown.
An Observation shall not be created when there is no result.

Each Observation records one result.
Several properties, or several statistics of one property, are recorded as
several Observations.
Raw data, such as each sample of a time series, should not be recorded as
Observations; a file that contains the raw data may be linked using
a `hasEvidence` relationship.

The following are recorded using existing properties and relationships:

- The Agent that made the observation: the `originatedBy` property,
  which is required.
- The instrument or software used, such as a power meter or a tokenizer:
  a `usesTool` relationship from the Observation.
- A published method that was followed: a `conformsTo` relationship from the
  Observation to a `Specification`.
- Inputs to a calculated or estimated result, such as other Observations or
  a datasheet: a `hasInput` relationship from the Observation.
  The subject should not also be given as an input.
- Details of the method that are not identified otherwise:
  the `observationProcedure` property.

This class aligns with the observation concept of the W3C Semantic Sensor
Network Ontology (SOSA/SSN) and ISO 19156 (Observations, measurements and
samples).

## Metadata

- name: Observation
- SubclassOf: Action
- Instantiability: Abstract

## Properties

- confidence
  - type: xsd:decimal
  - minCount: 0
  - maxCount: 1
- observationProcedure
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- observationType
  - type: ObservationType
  - minCount: 0
  - maxCount: 1
- observedProperty
  - type: xsd:anyURI
  - minCount: 1
  - maxCount: 1
- subject
  - type: Element
  - minCount: 1
  - maxCount: 1

## SPARQL

- confidence_range
  - message: The value of confidence shall be greater than 0 and less than or equal to 1
  - query: <<<

        SELECT $this WHERE {
            $this <Core/confidence> ?c .
            FILTER (?c <= 0 || ?c > 1)
        }
