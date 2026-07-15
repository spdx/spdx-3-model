SPDX-License-Identifier: Community-Spec-1.0

# externalResources

## Summary

Identifies an external resource that the AI agent can access or invoke to extend its capabilities.

## Description

Identifies an external resources, API, service, knowledge base, or data sources, that the AI agent can invoke to
perform actions or retrieve information beyond its built-in model. Each entry maps a short, human-readable resource identifier (the key) to a URI, package URL, or other
reference that locates the resource's definition or specification (the value).

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

- name: externalResources
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry
