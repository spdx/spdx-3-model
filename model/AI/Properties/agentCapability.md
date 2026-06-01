SPDX-License-Identifier: Community-Spec-1.0

# agentCapability

## Summary

Captures all agents used in the system and describes their functional capabilities.

## Description

A free-form string that identifies and describes a specific functional capability of an agent used in the system, what it can do, what goal it serves, or what class of task it is designed to handle. Each value should capture one distinct capability across all agents present in the system.

*Examples*

```text
web-search
```

```text
document-summarization: condenses retrieved documents into structured outputs
```

```text
code-execution: runs Python snippets in a sandboxed environment
```

```text
multi-step-reasoning: decomposes complex queries into sub-tasks and plans execution order
```

```text
Orchestrator : delegates sub-tasks to specialized agents and aggregates results
```

## Metadata

- name: agentCapability
- Nature: DataProperty
- Range: xsd:string
