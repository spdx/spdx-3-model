SPDX-License-Identifier: Community-Spec-1.0

# EnergyConsumption

## Summary

A class for describing the energy consumption incurred by an AI model in
different stages of its lifecycle.

## Description

A class to denote the known or estimated energy consumption of an AI model
during its training, fine-tuning, and inference stages.

**Syntax**

```json
{
  "type": "ai_EnergyConsumption",
  "ai_trainingEnergyConsumption": [
    {
      "type": "ai_EnergyConsumptionDescription",
      "ai_energyQuantity": 36.5,
      "ai_energyUnit": "kilowattHour"
    }
  ],
  "ai_inferenceEnergyConsumption": [
    {
      "type": "ai_EnergyConsumptionDescription",
      "ai_energyQuantity": 0.042,
      "ai_energyUnit": "kilowattHour"
    }
  ]
}
```

## Metadata

- name: EnergyConsumption
- Instantiability: Concrete

## Properties

- finetuningEnergyConsumption
  - type: EnergyConsumptionDescription
- inferenceEnergyConsumption
  - type: EnergyConsumptionDescription
- trainingEnergyConsumption
  - type: EnergyConsumptionDescription
