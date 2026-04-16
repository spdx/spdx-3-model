SPDX-License-Identifier: Community-Spec-1.0

# agentExternalTool

## Summary

Describes an external tool or a service that an AI agent invokes to accomplish
actions within or outside the system.

## Description

Identifies the means through which an agent extends its capabilities by
calling external tools, APIs, or services. These tools represent actionable
integrations that allow the agent to retrieve information, transform data,
or execute operations not possible with its built-in model alone.

Examples include general-purpose APIs (e.g., search, database lookup),
specialized utilities (e.g., translation services), and domain-specific tools
(e.g., medical publication query service).

If the agent does not use external tools, set the value to NONE.
If it is unclear or not disclosed whether tools are used, set to NOASSERTION.

## Metadata

- name: agentExternalTool
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry