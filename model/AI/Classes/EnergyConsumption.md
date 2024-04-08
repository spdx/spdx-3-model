SPDX-License-Identifier: Community-Spec-1.0

# EnergyConsumption

## Summary

The class that contains properties to describe energy consumption incurred by an AI model in different stages of its lifecycle.

## Description

The class used for denoting the training energy consumption, inference energy consumption and fine tuning energy consumption of the AI model(s) used in an AI system.

## Metadata

- name: EnergyConsumption
- Instantiability: Concrete

## Properties

- trainingEnergyConsumption
  - type: EnergyConsumptionDescription
- finetuningEnergyConsumption
  - type: EnergyConsumptionDescription
- inferenceEnergyConsumption
  - type: EnergyConsumptionDescription
