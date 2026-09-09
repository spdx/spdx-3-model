SPDX-License-Identifier: Community-Spec-1.0

# agentCapability

## Summary

Describes a specific domain task or goal the agent is designed to perform,
optionally noting the autonomy level at which it is exercised.

## Description

A free-form string identifying a user-facing task ability of the AI agent.
Since autonomy can vary by capability, the description may also state the
level of automation at which that capability operates (e.g., full automation
versus requiring human approval), optionally referencing
[/Core/IsoAutomationLevel](../../Core/Vocabularies/IsoAutomationLevel.md).

*Examples*

```text
environment-perception: monitors incoming support tickets and extracts
customer intent without human intervention (full automation)
```

```text
state-reasoning: assesses progress toward the current goal and decides
whether to replan without external intervention (full automation)
```

```text
goal-decomposition: breaks a high-level objective into an ordered sequence
of sub-goals without external intervention (full automation)
```

```text
action-selection: chooses and initiates the next action toward the goal,
pausing for human approval before any irreversible action (conditional
automation)
```

```text
peer-delegation: assigns sub-goals to specialized peer agents and
reconciles their outcomes, escalating conflicting results to a human
reviewer (conditional automation)
```

## Metadata

- name: agentCapability
- Nature: ObjectProperty
- Range: xsd:string
