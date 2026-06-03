SPDX-License-Identifier: Community-Spec-1.0

# agentCapability

## Summary

Describes a specific domain task or goal the agent is designed to perform,
independent of its implementation mechanism.

## Description

A free-form string that identifies a user-facing task ability of the AI agent:
what it can accomplish for an integrator or end-user, regardless of the
architectural pattern used to fulfill it. Each value should capture one
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
- Nature: DataProperty
- Range: xsd:string
