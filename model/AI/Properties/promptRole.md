SPDX-License-Identifier: Community-Spec-1.0

# promptRole

## Summary

Indicates whether a prompt is a user prompt (scoped to a single query) or a
system prompt (governing overall behavior for every query).

## Description

Specifies the role of a prompt within an AI interaction. Prompts are
categorized into two distinct roles:

- `user`: A user prompt is provided by a user (human or AI agent) of the AI
  system and is associated with a single query or instruction.
- `system`: A system prompt is provided by the system's owner, maintainer, or
  administrator to inform the system's overall behavior for every query or
  instruction. In agentic contexts, system prompts are sometimes referred to as
  "instructions."

This property is important for understanding provenance and scope: user prompts
describe individual interactions, while system prompts describe standing
configuration applied to all interactions. Both are distinct from the AI
system's static models, programming, and configuration files.

## Metadata

- name: promptRole
- Nature: ObjectProperty
- Range: PromptRoleType
