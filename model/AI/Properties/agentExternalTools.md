SPDX-License-Identifier: Community-Spec-1.0

# agentExternalTools

## Summary

Lists the external tools or services that the AI agent invokes to accomplish actions within or outside the system.

## Description
Identifies the means through which the agent extends its capabilities by calling external tools, APIs, or services. These tools represent actionable integrations that allow the agent to retrieve information, perform transformations, or execute operations beyond its built-in model capabilities. Examples include general-purpose APIs (e.g., Google Search, OpenAI API), specialized utilities (e.g., translation services like DeepL), and domain-specific tools (e.g., PubMed query service, arXiv retriever).  

If the agent does not use external tools, set the value to NONE. If it is unclear or not disclosed whether tools are used, set to NOASSERTION.

## Metadata

- name: agentExternalTools
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry
