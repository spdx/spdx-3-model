SPDX-License-Identifier: Community-Spec-1.0

# agentMemoryMode

## Summary

Describes the category of memory enabled for the agent.

## Description

A free-form string to indicate the purpose/structure of the memory store. Multiple values are allowed and can be indicated as a comma-separated string. Some examples include  episodic          (step/run-level logs and outcomes), semantic (vector embeddings / long-term knowledge), instruction/persona (system prompts, user profiles, norms), tool-history (tool I/O traces, function-call cache), rag-cache (retrieval cache / doc chunk cache),  working-cache (short-lived scratchpad persisted to store).


## Metadata
- name: agentMemoryMode
- Nature: DataProperty
- Range: xsd: anyURI
