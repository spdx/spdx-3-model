SPDX-License-Identifier: Community-Spec-1.0

# PresenceObservation

## Summary

An Observation whose result is yes or no.

## Description

A `PresenceObservation` records whether something was found in, or is true
of, the subject.
The `observedProperty` property identifies what was looked for.

A result of `no` means that the method used did not find it.
It does not mean that it is certainly absent: the result is only as reliable
as the method.
A `PresenceObservation` with a result of `no` should therefore identify the
method, using the `observationProcedure` property or a `usesTool`
relationship.
If there is no result, no Observation shall be created.

A `PresenceObservation` can coexist with, and differ from, a value declared
for a dedicated property.
For example, a supplier may declare `/Dataset/hasSensitivePersonalInformation`
as `no` for a dataset, while a scanner reports `yes`.

The `confidence` property may give the probability that the result is
correct, for example for the output of a classifier.

*Constraints*

- The value of `observedPresence` shall not be `noAssertion`.

*Example*

```json
{
  "type": "PresenceObservation",
  "spdxId": "https://example.com/spdx/obs-pii-scan",
  "creationInfo": "_:creationinfo",
  "originatedBy": ["https://example.com/spdx/acme"],
  "subject": "https://example.com/spdx/street-images",
  "observedProperty": "https://example.com/terms/containsFaces",
  "observationType": "measured",
  "observationProcedure": "Face detector v2.1 run on every image; detection threshold 0.6.",
  "observedPresence": "yes",
  "confidence": "0.97"
}
```

## Metadata

- name: PresenceObservation
- SubclassOf: Observation
- Instantiability: Concrete

## Properties

- observedPresence
  - type: PresenceType
  - minCount: 1
  - maxCount: 1

## SPARQL

- presence_not_noassertion
  - message: The observedPresence of a PresenceObservation shall not be noAssertion
  - query: <<<

        SELECT $this WHERE {
            $this <Core/observedPresence> <Core/PresenceType/noAssertion> .
        }
