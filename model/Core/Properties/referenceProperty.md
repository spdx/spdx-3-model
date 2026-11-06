SPDX-License-Identifier: Community-Spec-1.0

# referenceProperty

## Summary

IRI that identifies what the reference quantity of a Measurement is of.

## Description

The `referenceProperty` property identifies what the `referenceQuantity` of
a `Measurement` counts or measures, in the same way that `observedProperty`
identifies what was observed.
For example, `/Dataset/DatasetObservablePropertyType/tokenCount` for a rate
per 1000 tokens, or `/AI/AIObservablePropertyType/inferenceCount` for a rate
per inference.

It shall be given together with `referenceQuantity`.

## Metadata

- name: referenceProperty
- Nature: DataProperty
- Range: xsd:anyURI
