SPDX-License-Identifier: Community-Spec-1.0

# promptPattern

## Summary

Identifies the structured reasoning strategy (e.g., Chain-of-Thought, Self-Consistency, Tree-of-Thought) that guides the underlying FM towards the desired output.

## Description

Prompt patterns are structured reasoning patterns that are used to make the prompts effective for the task that the Foundation Model (FM) (e.g., large language model) is attempting to accomplish. For instance, chain-of-thought, or checklists.

A prompt can also use a non-standard pattern or simple instructions. In such cases, one can state the promptPattern as simple or no assertion. The field is a freeform string.

If multiple promptPatterns are used, all the prompt patterns can be recorded.

Examples include:

- Chain-of-Thought – Sequential step-by-step reasoning.
- Self-Consistency – Multiple reasoning paths with consensus selection.
- Tree-of-Thought – Branching exploration of reasoning paths.

## Metadata

- name: promptPattern
- Nature: DataProperty
- Range: xsd:string
