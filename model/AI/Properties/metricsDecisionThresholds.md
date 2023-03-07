SPDX-License-Identifier: Community-Spec-1.0

# metricsDecisionThresholds

## Summary

Field captures the thresholds that are being used for metric computation of the metrics described in the metrics field. Should match with the Metrics field and depends on the metrics field

## Description

Each metric might be computed based on a decision threshold (for instance precision or recall is typically computed by splitting checking if the probability of the outcome is >0.5). This field records the decision threshold in comma separated values. E.g., metric_1:decsion_threshold, metric_2:decision threshold. If there are multiple models each line represents each model’s metrics and decision threshold. 

## Metadata

- name: metricsDecisionThresholds
- Nature: DataProperty
- Range: xsd:string
