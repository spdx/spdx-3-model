SPDX-License-Identifier: Community-Spec-1.0

# agentCapability

## Summary

Describes a specific domain task or goal the agent is designed to perform.

## Description

A free-form string that identifies a user-facing task ability of the AI agent:
what it can accomplish for a system. Each value should capture one
distinct task or goal. 

*Examples*

```text
web-search: search across web and retrieve information
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
multi-agent-coordination: delegates sub-tasks to specialized agents and aggregates results
```

## Metadata

- name: agentCapability
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry
