SPDX-License-Identifier: Community-Spec-1.0

# AgentMemoryMode

## Summary

The type of memory store or storage mechanism used by the AI agent.

## Description

Classifies how an AI agent retains and recalls information across interactions
or reasoning steps. Multiple values may be declared when an agent employs more
than one memory mechanism.

## Metadata

- name: AgentMemoryMode

## Entries

- episodic: Records of past events, interactions, or task executions that provide experiential context for future reasoning.
- semantic: Factual or conceptual knowledge stored for retrieval and inference (e.g., vector embeddings, knowledge graphs).
- procedural: Encoded skills, plans, or behavioral patterns that guide the agent's execution strategy.
- working: Short-lived, context-scoped information used within a single reasoning session or conversation turn.
- inContext: Information retained within the active context window of the underlying language model.
- inWeights: Knowledge encoded in model parameters through pretraining or fine-tuning; not updated at runtime.
- inCache: Precomputed key-value attention caches enabling efficient reuse of prior computations.
- external: Information persisted in an external store (database, file system, vector store) and retrieved on demand.
