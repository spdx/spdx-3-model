SPDX-License-Identifier: Community-Spec-1.0

# metricDecisionThreshold

## Summary

Captures the threshold that was used for computation of a metric described in the metric field.

## Description

Each metric might be computed based on a decision threshold. 
For instance, precision or recall is typically computed by checking
if the probability of the outcome is larger than 0.5.
Each decision threshold should match with a metric field defined in the AI Package.

## Metadata

- name: metricDecisionThreshold
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry
