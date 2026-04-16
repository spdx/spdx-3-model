SPDX-License-Identifier: Community-Spec-1.0

# agentMemoryMode

## Summary

Describes the category of memory enabled for the agent.

## Description

A free-form string to indicate the purpose/structure of the memory store.

Examples of possible values:

- `episodic`: Step/run-level logs and outcomes.
- `semantic`: Vector embeddings / long-term knowledge.
- `instruction/persona`: System prompts, user profiles, norms.
- `tool-history`: Tool I/O traces, function-call cache.
- `rag-cache`: Retrieval cache / doc chunk cache.
- `working-cache`: Short-lived scratchpad persisted to store.

## Metadata

- name: agentMemoryMode
- Nature: DataProperty
- Range: xsd:string