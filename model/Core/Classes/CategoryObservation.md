SPDX-License-Identifier: Community-Spec-1.0

# CategoryObservation

## Summary

An Observation whose result is a term from a code list.

## Description

A `CategoryObservation` records a result that is one term of a code list,
such as an energy efficiency class or a test verdict.
The `observedProperty` property identifies what was classified, and the
`observedCategory` property gives the IRI of the resulting term.

The term may come from an SPDX vocabulary (for example,
`/FunctionalSafety/EvaluationResultType`) or from a code list published by
another organization.

The `confidence` property may give the probability that the result is
correct, for example for the output of a classifier.

*Example*

```json
{
  "type": "CategoryObservation",
  "spdxId": "https://example.com/spdx/obs-energy-class",
  "creationInfo": "_:creationinfo",
  "originatedBy": ["https://example.com/spdx/test-lab"],
  "subject": "https://example.com/spdx/display-x1",
  "observedProperty": "https://example.com/terms/energyEfficiencyClass",
  "observationType": "measured",
  "observationProcedure": "Measured according to Commission Delegated Regulation (EU) 2019/2013.",
  "observedCategory": "https://example.com/terms/energyEfficiencyClass/B"
}
```

## Metadata

- name: CategoryObservation
- SubclassOf: Observation
- Instantiability: Concrete

## Properties

- observedCategory
  - type: xsd:anyURI
  - minCount: 1
  - maxCount: 1
