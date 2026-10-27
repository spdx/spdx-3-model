SPDX-License-Identifier: Community-Spec-1.0

# AIInferenceProcess

## Summary

Process definition specifying how an artificial intelligence model is run
to perform inference.

## Description

The `AIInferenceProcess` describes how an artificial intelligence model is
deployed and run to perform inference, such as the serving software,
hardware, numeric precision, and batch size.
It does not represent a period of time or the use of computational
resources; an execution is represented by an `AIInferenceAction`.

The model used should be recorded as an input of the process.

A `/Core/Measurement` whose `subject` is the process records a nominal or
typical value for running the model in this way.
Such a value shall be a rate, given using the `referenceQuantity` and
`referenceProperty` properties (for example, energy per 1000 tokens).
Values of a process are only comparable if the conditions are known,
so the conditions that affect the value should be stated in the process
description or in the `observationProcedure` of the Measurement.

A required threshold, such as a maximum energy per 1000 tokens, is not an
Observation: it is a `/Core/Requirement` whose subject is the process,
and a Measurement that shows it is met may be linked as evidence.

*Example*

A benchmark run of a model is measured: it consumed 4.2 kW·h of energy in
IT equipment, and processed 14 million tokens.
The energy per 1000 tokens is calculated from these, and recorded on the
process: 4200 W·h ÷ 14000000 tokens × 1000 = 0.3 W·h per 1000 tokens.

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
      "spdxId": "https://example.com/spdx/doc-llm-energy",
      "creationInfo": "_:creationinfo",
      "profileConformance": ["core", "software", "ai"],
      "rootElement": ["https://example.com/spdx/acme-llm-8b"],
      "element": [
        "https://example.com/spdx/acme-llm-8b",
        "https://example.com/spdx/serving",
        "https://example.com/spdx/rel-serving-model",
        "https://example.com/spdx/bench-run-42",
        "https://example.com/spdx/rel-run-model",
        "https://example.com/spdx/codecarbon",
        "https://example.com/spdx/obs-energy",
        "https://example.com/spdx/rel-energy-tool",
        "https://example.com/spdx/obs-tokens",
        "https://example.com/spdx/obs-energy-per-1k-tokens",
        "https://example.com/spdx/rel-rate-inputs"
      ]
    },
    {
      "type": "ai_AIPackage",
      "spdxId": "https://example.com/spdx/acme-llm-8b",
      "creationInfo": "_:creationinfo",
      "name": "acme-llm-8b",
      "software_packageVersion": "1.2.0",
      "software_downloadLocation": "https://example.com/models/acme-llm-8b-1.2.0",
      "software_primaryPurpose": "model",
      "suppliedBy": "https://example.com/spdx/acme",
      "releaseTime": "2026-09-01T00:00:00Z"
    },
    {
      "type": "ai_AIInferenceProcess",
      "spdxId": "https://example.com/spdx/serving",
      "creationInfo": "_:creationinfo",
      "name": "acme-llm-8b production serving",
      "description": "vLLM 0.9 on 1 NVIDIA H100 80GB SXM; FP8 weights; maximum batch size 32.",
      "version": "1.0"
    },
    {
      "type": "Relationship",
      "spdxId": "https://example.com/spdx/rel-serving-model",
      "creationInfo": "_:creationinfo",
      "from": "https://example.com/spdx/serving",
      "relationshipType": "hasInput",
      "to": ["https://example.com/spdx/acme-llm-8b"]
    },
    {
      "type": "ai_AIInferenceAction",
      "spdxId": "https://example.com/spdx/bench-run-42",
      "creationInfo": "_:creationinfo",
      "name": "Energy benchmark run 42",
      "description": "Run of the production serving configuration on ShareGPT prompts.",
      "originatedBy": ["https://example.com/spdx/acme"],
      "startTime": "2026-09-20T09:00:00Z",
      "endTime": "2026-09-20T15:00:00Z"
    },
    {
      "type": "Relationship",
      "spdxId": "https://example.com/spdx/rel-run-model",
      "creationInfo": "_:creationinfo",
      "from": "https://example.com/spdx/bench-run-42",
      "relationshipType": "hasInput",
      "to": ["https://example.com/spdx/acme-llm-8b"]
    },
    {
      "type": "Tool",
      "spdxId": "https://example.com/spdx/codecarbon",
      "creationInfo": "_:creationinfo",
      "name": "CodeCarbon 2.8.3"
    },
    {
      "type": "Measurement",
      "spdxId": "https://example.com/spdx/obs-energy",
      "creationInfo": "_:creationinfo",
      "originatedBy": ["https://example.com/spdx/acme"],
      "subject": "https://example.com/spdx/bench-run-42",
      "observedProperty": "https://spdx.org/rdf/3/terms/Core/ObservablePropertyType/energyConsumptionItEquipment",
      "observationType": "measured",
      "observationStatistic": "total",
      "observationProcedure": "GPU energy from NVML and CPU energy from RAPL, sampled every 15 s.",
      "observedValue": {
        "type": "UnitOfMeasure",
        "quantity": "4.2",
        "unitQUDT": "http://qudt.org/vocab/unit/KiloW-HR"
      },
      "standardUncertainty": {
        "type": "UnitOfMeasure",
        "quantity": "3",
        "unitQUDT": "http://qudt.org/vocab/unit/PERCENT"
      }
    },
    {
      "type": "LifecycleScopedRelationship",
      "spdxId": "https://example.com/spdx/rel-energy-tool",
      "creationInfo": "_:creationinfo",
      "from": "https://example.com/spdx/obs-energy",
      "relationshipType": "usesTool",
      "to": ["https://example.com/spdx/codecarbon"]
    },
    {
      "type": "Measurement",
      "spdxId": "https://example.com/spdx/obs-tokens",
      "creationInfo": "_:creationinfo",
      "originatedBy": ["https://example.com/spdx/acme"],
      "subject": "https://example.com/spdx/bench-run-42",
      "observedProperty": "https://spdx.org/rdf/3/terms/Dataset/DatasetObservablePropertyType/tokenCount",
      "observationType": "measured",
      "observationStatistic": "total",
      "observationProcedure": "Input and output tokens, counted by the model's own tokenizer from the server logs.",
      "observedValue": {
        "type": "UnitOfMeasure",
        "quantity": "1.4e7",
        "unitQUDT": "http://qudt.org/vocab/unit/COUNT"
      }
    },
    {
      "type": "Measurement",
      "spdxId": "https://example.com/spdx/obs-energy-per-1k-tokens",
      "creationInfo": "_:creationinfo",
      "originatedBy": ["https://example.com/spdx/acme"],
      "subject": "https://example.com/spdx/serving",
      "observedProperty": "https://spdx.org/rdf/3/terms/AI/AIObservablePropertyType/inferenceEnergyConsumption",
      "observationType": "calculated",
      "observationStatistic": "mean",
      "observationProcedure": "IT equipment energy of benchmark run 42, divided by the number of tokens processed.",
      "observedValue": {
        "type": "UnitOfMeasure",
        "quantity": "0.3",
        "unitQUDT": "http://qudt.org/vocab/unit/W-HR"
      },
      "standardUncertainty": {
        "type": "UnitOfMeasure",
        "quantity": "3",
        "unitQUDT": "http://qudt.org/vocab/unit/PERCENT"
      },
      "referenceQuantity": {
        "type": "UnitOfMeasure",
        "quantity": "1000",
        "unitQUDT": "http://qudt.org/vocab/unit/COUNT"
      },
      "referenceProperty": "https://spdx.org/rdf/3/terms/Dataset/DatasetObservablePropertyType/tokenCount"
    },
    {
      "type": "Relationship",
      "spdxId": "https://example.com/spdx/rel-rate-inputs",
      "creationInfo": "_:creationinfo",
      "from": "https://example.com/spdx/obs-energy-per-1k-tokens",
      "relationshipType": "hasInput",
      "to": [
        "https://example.com/spdx/obs-energy",
        "https://example.com/spdx/obs-tokens"
      ]
    }
  ]
}
```

## Metadata

- name: AIInferenceProcess
- SubclassOf: /Core/DefinedProcess
- Instantiability: Concrete
