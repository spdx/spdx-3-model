SPDX-License-Identifier: Community-Spec-1.0

# metrics

## Summary

This  field records the measurement of prediction quality including uncertainty, accuracy, characteristics of of tested population, Quality, Fairness, explainability, Robustness etc

## Description

The field describes the metrics used to evaluate the AI model used in the AI software. Its a text field where metrics are listed in a comma separated fashion in the following format metric_1: value, metric_2:value, etc. If there are multiple models, metrics are listed in a new line for each model.

## Metadata

- name: metrics
- Nature: DataProperty
- Range: xsd:string
