SPDX-License-Identifier: Community-Spec-1.0

# agentCapability

## Summary

Describes a functional capability that the AI agent can perform.

## Description

A free-form string that identifies and describes a specific functional
capability of the agent—what it can do, what goal it serves, or what class
of task it is designed to handle. Each value should capture one distinct
capability.

Capabilities reflect the agent's behavioral repertoire and may include, but
are not limited to: information retrieval, document summarization, code
generation and execution, data analysis, planning and task decomposition,
multi-step reasoning, multi-agent coordination, and domain-specific actions.

Use one `agentCapability` entry per distinct capability. Descriptions should
be concise and human-readable. External tools or services invoked to fulfill a
capability are recorded separately using the `agentExternalTool` property.

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
multi-agent-coordination: delegates sub-tasks to specialized agents and aggregates results
```

## Metadata

- name: agentCapability
- Nature: DataProperty
- Range: xsd:string
