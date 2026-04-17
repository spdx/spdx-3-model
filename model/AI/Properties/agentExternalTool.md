SPDX-License-Identifier: Community-Spec-1.0

# agentExternalTool

## Summary

Identifies an external tool or service that the AI agent can invoke to extend
its capabilities.

## Description

Identifies an external tool, API, or service that the AI agent can invoke to
perform actions beyond its built-in model. Each entry maps a short,
human-readable tool identifier (the key) to a URI, package URL, or other
reference that locates the tool's definition or specification (the value).

External tools enable agents to retrieve information, transform data, execute
operations, or interact with external systems. Examples include: web search
APIs, code execution sandboxes, database query interfaces, translation
services, and domain-specific utilities such as medical literature search.

*Examples*

```text
web-search: https://serpapi.com/
```

```text
code-interpreter: pkg:pypi/jupyter-kernel-gateway@2.0.0
```

```text
pubmed-query: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
```

## Metadata

- name: agentExternalTool
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry
