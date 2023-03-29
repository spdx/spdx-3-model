SPDX-License-Identifier: Community-Spec-1.0

# metricsDecisionThresholds

## Summary
Field that captures the thresholds being used for computation of those metrics described in the Metrics field. 

## Description

Each metric might be computed based on a decision threshold (for instance precision or recall is typically computed by splitting checking if the probability of the outcome is >0.5). This field records the decision threshold in comma separated values. E.g., metric_1:decsion_threshold, metric_2:decision threshold. If there are multiple models each line represents each model’s metrics and decision threshold. Each decision threshold should match with the metrics field defined in the AI Package.

## Metadata

- name: metricsDecisionThresholds
- Nature: DataProperty
- Range: xsd:string
