SPDX-License-Identifier: Community-Spec-1.0

# Measurement

## Summary

An Observation whose result is a number with a unit of measure.

## Description

A `Measurement` records a numeric result, such as an amount of energy,
a duration, a mass, or a count.
The result is given by the `observedValue` property, by the `lowerBound` and
`upperBound` properties, or by all three.

The unit of each value shall have the same dimension as the observed property
(for example, <http://qudt.org/vocab/unit/KiloW-HR> for an energy).
Counts use the unit <http://qudt.org/vocab/unit/COUNT>.
There are no QUDT units for tokens, words, or images: these are counts,
and the thing counted is identified by the observed property.

Uncertainty and ranges:

- `standardUncertainty` is one standard deviation of the value
  (standard uncertainty as defined in JCGM 100, Guide to the Expression of
  Uncertainty in Measurement).
  It is not a ± bound.
- `lowerBound` and `upperBound` give a range, for example for an estimate or
  for a size that is disclosed only as a range.
  `coverageProbability` gives the probability that the true value lies in
  the range.
  If it is absent, the bounds are the plausible minimum and maximum.

The `observationStatistic` property states which statistic of the observed
property the value is, such as a total, a mean, or a percentile.
For a percentile, the `percentileRank` property gives which one.

A value "per" an amount of something else (a rate) is recorded using the
`referenceQuantity` property for the amount and the `referenceProperty`
property for what that amount is of.
For example, an `observedValue` of 0.3 W·h with a `referenceQuantity` of
1000 <http://qudt.org/vocab/unit/COUNT> and a `referenceProperty` of
`/Dataset/DatasetObservablePropertyType/tokenCount` means 0.3 W·h per 1000
tokens.
A rate per unit of time may instead use a rate unit, such as
<http://qudt.org/vocab/unit/W> for an average power.

A Measurement that is the total of other Measurements shall set
`observationStatistic` to `total`, and shall link to these Measurements using
a `hasInput` relationship.
Consumers should use a published total rather than adding up values
themselves, because the values may overlap.
For example, greenhouse gas emissions from aircraft transport are reported
separately but are also included in fossil emissions.

Negative values are allowed when the observed property allows them,
for example for greenhouse gas removals.

*Constraints*

- Either `observedValue`, or both `lowerBound` and `upperBound`,
  shall be present.
- The `quantity` of each value shall be a decimal number, optionally in
  exponent notation (for example, `3.8e25`).
- `standardUncertainty` shall not be negative.
  Its unit shall be the unit of `observedValue` (absolute uncertainty) or
  <http://qudt.org/vocab/unit/PERCENT> (relative uncertainty).
- `lowerBound`, `observedValue`, and `upperBound` shall use the same unit,
  and `lowerBound` ≤ `observedValue` ≤ `upperBound`.
- `coverageProbability` shall only be present with both bounds.
- `percentileRank` shall be present if and only if `observationStatistic` is
  `percentile`.
- `referenceQuantity` and `referenceProperty` shall be both present or both
  absent, and the quantity of `referenceQuantity` shall be greater than 0.

*Example*

The provider of an image dataset declares its licence and the number of
images in it.
The EU AI Act requires providers of general-purpose AI models to document
the number of data points used for training (Annex XI, Section 1,
point 2(c)).
If only a range is to be disclosed (for example, "1 million to 1 billion
images"), `lowerBound` and `upperBound` are given instead of `observedValue`.

```json
{
  "@context": "https://spdx.org/rdf/3.1/spdx-context.jsonld",
  "@graph": [
    {
      "type": "CreationInfo",
      "@id": "_:creationinfo",
      "specVersion": "3.1",
      "created": "2026-10-27T00:00:00Z",
      "createdBy": ["https://example.com/spdx/acme"]
    },
    {
      "type": "Organization",
      "spdxId": "https://example.com/spdx/acme",
      "creationInfo": "_:creationinfo",
      "name": "Acme AI"
    },
    {
      "type": "SpdxDocument",
      "spdxId": "https://example.com/spdx/doc-street-images",
      "creationInfo": "_:creationinfo",
      "profileConformance": ["core", "software", "dataset", "simpleLicensing"],
      "rootElement": ["https://example.com/spdx/street-images"],
      "element": [
        "https://example.com/spdx/street-images",
        "https://example.com/spdx/license-cc-by-4.0",
        "https://example.com/spdx/rel-declared-license",
        "https://example.com/spdx/obs-image-count"
      ]
    },
    {
      "type": "dataset_DatasetPackage",
      "spdxId": "https://example.com/spdx/street-images",
      "creationInfo": "_:creationinfo",
      "name": "Acme street images",
      "software_packageVersion": "2.0",
      "software_downloadLocation": "https://example.com/data/street-images-2.0.tar",
      "software_primaryPurpose": "data",
      "builtTime": "2026-09-01T00:00:00Z",
      "originatedBy": ["https://example.com/spdx/acme"],
      "releaseTime": "2026-09-15T00:00:00Z",
      "dataset_datasetType": ["image"]
    },
    {
      "type": "simplelicensing_LicenseExpression",
      "spdxId": "https://example.com/spdx/license-cc-by-4.0",
      "creationInfo": "_:creationinfo",
      "simplelicensing_licenseExpression": "CC-BY-4.0"
    },
    {
      "type": "Relationship",
      "spdxId": "https://example.com/spdx/rel-declared-license",
      "creationInfo": "_:creationinfo",
      "from": "https://example.com/spdx/street-images",
      "relationshipType": "hasDeclaredLicense",
      "to": ["https://example.com/spdx/license-cc-by-4.0"]
    },
    {
      "type": "Measurement",
      "spdxId": "https://example.com/spdx/obs-image-count",
      "creationInfo": "_:creationinfo",
      "originatedBy": ["https://example.com/spdx/acme"],
      "subject": "https://example.com/spdx/street-images",
      "observedProperty": "https://spdx.org/rdf/3/terms/Dataset/DatasetObservablePropertyType/imageCount",
      "observationType": "measured",
      "observationStatistic": "total",
      "observationProcedure": "Distinct image files, after removing exact duplicates by SHA-256 hash.",
      "observedValue": {
        "type": "UnitOfMeasure",
        "quantity": "4012553",
        "unitQUDT": "http://qudt.org/vocab/unit/COUNT"
      }
    }
  ]
}
```

The size of the dataset in bytes is recorded using the `/Software/byteSize`
property, not a Measurement.

## Metadata

- name: Measurement
- SubclassOf: Observation
- Instantiability: Concrete

## Properties

- coverageProbability
  - type: xsd:decimal
  - minCount: 0
  - maxCount: 1
- lowerBound
  - type: UnitOfMeasure
  - minCount: 0
  - maxCount: 1
- observationStatistic
  - type: ObservationStatisticType
  - minCount: 0
  - maxCount: 1
- observedValue
  - type: UnitOfMeasure
  - minCount: 0
  - maxCount: 1
- percentileRank
  - type: xsd:decimal
  - minCount: 0
  - maxCount: 1
- referenceProperty
  - type: xsd:anyURI
  - minCount: 0
  - maxCount: 1
- referenceQuantity
  - type: UnitOfMeasure
  - minCount: 0
  - maxCount: 1
- standardUncertainty
  - type: UnitOfMeasure
  - minCount: 0
  - maxCount: 1
- upperBound
  - type: UnitOfMeasure
  - minCount: 0
  - maxCount: 1

## SPARQL

- value_or_bounds
  - message: A Measurement shall have an observedValue, or both a lowerBound and an upperBound
  - query: <<<

        SELECT $this WHERE {
            FILTER NOT EXISTS { $this <Core/observedValue> ?v . }
            FILTER NOT EXISTS {
                $this <Core/lowerBound> ?l .
                $this <Core/upperBound> ?u .
            }
        }

- quantity_is_number
  - message: The quantity of each value of a Measurement shall be a decimal number, optionally in exponent notation
  - query: <<<

        SELECT $this WHERE {
            $this <Core/observedValue>|<Core/standardUncertainty>|<Core/lowerBound>|<Core/upperBound>|<Core/referenceQuantity> ?m .
            ?m <Core/quantity> ?q .
            FILTER (!regex(str(?q), "^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)([eE][+-]?[0-9]+)?$"))
        }

- uncertainty_not_negative
  - message: The standardUncertainty of a Measurement shall not be negative
  - query: <<<

        SELECT $this WHERE {
            $this <Core/standardUncertainty>/<Core/quantity> ?q .
            FILTER (<http://www.w3.org/2001/XMLSchema#double>(?q) < 0)
        }

- uncertainty_unit
  - message: The unit of standardUncertainty shall be the unit of observedValue or PERCENT
  - query: <<<

        SELECT $this WHERE {
            $this <Core/standardUncertainty>/<Core/unitQUDT> ?uu .
            $this <Core/observedValue>/<Core/unitQUDT> ?vu .
            FILTER (str(?uu) != str(?vu) && str(?uu) != "http://qudt.org/vocab/unit/PERCENT")
        }

- bounds_unit
  - message: The lowerBound, observedValue, and upperBound of a Measurement shall use the same unit
  - query: <<<

        SELECT $this WHERE {
            $this <Core/lowerBound>|<Core/observedValue>|<Core/upperBound> ?a .
            $this <Core/lowerBound>|<Core/observedValue>|<Core/upperBound> ?b .
            ?a <Core/unitQUDT> ?ua .
            ?b <Core/unitQUDT> ?ub .
            FILTER (str(?ua) != str(?ub))
        }

- bounds_order
  - message: A Measurement shall satisfy lowerBound <= observedValue <= upperBound
  - query: <<<

        SELECT $this WHERE {
            {
                $this <Core/lowerBound>/<Core/quantity> ?lo .
                $this <Core/observedValue>/<Core/quantity> ?hi .
            } UNION {
                $this <Core/observedValue>/<Core/quantity> ?lo .
                $this <Core/upperBound>/<Core/quantity> ?hi .
            } UNION {
                $this <Core/lowerBound>/<Core/quantity> ?lo .
                $this <Core/upperBound>/<Core/quantity> ?hi .
            }
            FILTER (<http://www.w3.org/2001/XMLSchema#double>(?lo) > <http://www.w3.org/2001/XMLSchema#double>(?hi))
        }

- coverage_probability
  - message: The coverageProbability of a Measurement shall be greater than 0 and less than or equal to 1, and shall only be given with both bounds
  - query: <<<

        SELECT $this WHERE {
            $this <Core/coverageProbability> ?p .
            FILTER (
                ?p <= 0 || ?p > 1 ||
                NOT EXISTS { $this <Core/lowerBound> ?l . $this <Core/upperBound> ?u . }
            )
        }

- percentile_rank
  - message: The percentileRank of a Measurement shall be present if and only if its observationStatistic is percentile, and shall be between 0 and 1
  - query: <<<

        SELECT $this WHERE {
            {
                $this <Core/observationStatistic> <Core/ObservationStatisticType/percentile> .
                FILTER NOT EXISTS { $this <Core/percentileRank> ?p . }
            } UNION {
                $this <Core/percentileRank> ?p .
                FILTER (
                    ?p < 0 || ?p > 1 ||
                    NOT EXISTS { $this <Core/observationStatistic> <Core/ObservationStatisticType/percentile> . }
                )
            }
        }

- reference_pair
  - message: The referenceQuantity and referenceProperty of a Measurement shall be both present or both absent, and the referenceQuantity shall be greater than 0
  - query: <<<

        SELECT $this WHERE {
            {
                $this <Core/referenceQuantity> ?r .
                FILTER NOT EXISTS { $this <Core/referenceProperty> ?p . }
            } UNION {
                $this <Core/referenceProperty> ?p .
                FILTER NOT EXISTS { $this <Core/referenceQuantity> ?r . }
            } UNION {
                $this <Core/referenceQuantity>/<Core/quantity> ?q .
                FILTER (<http://www.w3.org/2001/XMLSchema#double>(?q) <= 0)
            }
        }
