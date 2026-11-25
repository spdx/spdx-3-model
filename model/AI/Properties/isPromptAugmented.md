SPDX-License-Identifier: Community-Spec-1.0

# isPromptAugmented

## Summary

Indicates whether the prompt has been automatically augmented with external
supporting content intended to ground the model's response in specific facts
or knowledge.

## Description

Specifies whether an automated grounding mechanism adds external supporting
content to the prompt before it is provided to an AI system. This content
supplements the prompt's instructions or directly accompanying content to
improve the accuracy and relevance of the response.

Grounding mechanisms may include retrieval-augmented generation, API calls,
or database lookups that supply up-to-date or domain-specific information.
Supporting content supplied elsewhere in the inference-time context does not
by itself constitute prompt augmentation.

Allowed values:

- `true`: The prompt includes automatically added external supporting content.
- `false`: The prompt has not been automatically augmented with external
  supporting content.

## Metadata

- name: isPromptAugmented
- Nature: DataProperty
- Range: xsd:boolean
