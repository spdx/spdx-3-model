SPDX-License-Identifier: Community-Spec-1.0

# agentMemoryMode

## Summary

Indicates the memory category or storage mechanism used by the AI agent.

## Description

A free-form string indicating the type of memory store or storage mechanism used by the agent to retain and recall information across interactions or reasoning steps.

Memory modes in AI agents can be classified along two complementary dimensions:

By cognitive function (from cognitive science and BDI agent models):

- `episodic`: Records of past events, interactions, or task executions that provide experiential context for future reasoning.
- `semantic`: Factual or conceptual knowledge stored in a form suitable for retrieval and inference (e.g., vector embeddings, knowledge graphs).
- `procedural`: Encoded skills, plans, or behavioral patterns that guide the agent's execution strategy.
- `working`: Short-lived, context-scoped information used within a single reasoning session or conversation turn.

By storage location (from language agent architectures, e.g., CoALA 2023):

- `in-context`: Information retained within the active context window of the underlying language model.
- `in-weights`: Knowledge encoded in model parameters through pretraining or fine-tuning; not updated at runtime.
- `in-cache`: Precomputed key-value attention caches enabling efficient reuse of prior computations.
- `external`: Information persisted in an external store (database, file system, vector store) and retrieved on demand.

Multiple values may be declared when an agent employs more than one memory mechanism. Values are free-form strings; the examples above are recommended conventions.

## Metadata

- name: agentMemoryMode
- Nature: DataProperty
- Range: xsd:string
