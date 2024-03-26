SPDX-License-Identifier: Community-Spec-1.0

# energyConsumption

## Summary

Indicates the amount of energy consumed to train the AI model.

## Description

A free-form text captures known or estimated energy consumption for the training of the AI model.

In case not known, the estimation could be based on information about computational resources used
(e.g. number of floating point operations – FLOPs), training time, type and quantity of processing units,
and other relevant details related to the training.

## Metadata

- name: energyConsumption
- Nature: DataProperty
- Range: xsd:string
