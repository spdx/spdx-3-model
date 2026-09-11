SPDX-License-Identifier: Community-Spec-1.0

# PromptRoleType

## Summary

A controlled vocabulary for classifying the role of a prompt within an AI
system interaction.

## Description

PromptRoleType defines the two fundamental roles a prompt can serve in an
AI system:

- **User prompts** originate from the consumer of the AI system (human or
  automated agent) and are scoped to a single query or instruction.
- **System prompts** originate from the system's owner, maintainer, or
  administrator and govern the AI system's overall behavior for every query.

This distinction is fundamental for documenting the provenance and scope of
prompts, especially in multi-turn, agentic, or RAG-based AI systems where
both role types may be represented separately.

## Metadata

- name: PromptRoleType

## Entries

- system: A prompt provided by the system's owner, maintainer, or administrator to inform the system's overall behavior for every query or instruction. Sometimes referred to as "instructions" in agentic contexts.
- user: A prompt provided by a user (human or AI agent) of the AI system, associated with a single query or instruction.
