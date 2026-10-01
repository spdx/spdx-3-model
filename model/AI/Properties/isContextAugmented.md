SPDX-License-Identifier: Community-Spec-1.0

# isContextAugmented

## Summary

Indicates whether the prompt content has been automatically augmented or
enhanced with external supporting content intended to ground the model's
response in specific facts or knowledge.

`true` if the prompt is augmented with external context, `false` otherwise.

## Description

Specifies whether an automated grounding mechanism is employed during prompt
construction. This technique (which may include Retrieval-Augmented Generation,
API results, or database lookups) is used to improve the accuracy and relevance
of responses from foundation models by programmatically providing them
with up-to-date or domain-specific supporting content.

Allowed values:

- `true`: The prompt includes automatically sourced external context or
  supporting content.
- `false`: The prompt is constructed directly without automated external
  augmentation.

## Metadata

- name: isContextAugmented
- Nature: DataProperty
- Range: xsd:boolean
