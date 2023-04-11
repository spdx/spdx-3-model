SPDX-License-Identifier: Community-Spec-1.0

# metricsDecisionThresholds

## Summary

Captures the thresholds that were used for computation of the metrics described in the metrics field.

## Description

Each metric might be computed based on a decision threshold. 
For instance, precision or recall is typically computed by checking
if the probability of the outcome is larger than 0.5.
Each decision threshold should match with the metrics field defined in the AI Package.

## Metadata

- name: metricsDecisionThresholds
- Nature: DataProperty
- Range: xsd:string
