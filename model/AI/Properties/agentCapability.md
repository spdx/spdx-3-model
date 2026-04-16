SPDX-License-Identifier: Community-Spec-1.0

# agentCapability

## Summary

Describes the agent’s functional capability, its purpose,
and the tool/integration used to realize each capability.

## Description

Provides a structured description of what the agent can do
(e.g., search, web scraping, summarization, code execution),
stating for each capability its purpose and which tool or service
it invokes to accomplish the action.

Use concise entries—one capability per item.

If no capabilities are defined, may set to "NONE";
if it is unknown or undisclosed, may set to "NOASSERTION".

Recommended notation:
`<capability>: <purpose> -> <tool references>`

*Examples*

```text
search: retrieve web results -> Google Search API; SerpAPI
```

```text
web-scrape: extract page content -> Playwright crawler; internal-scraper://v1
```

```text
summarize: condense retrieved docs -> OpenAI API (summarize endpoint)
```

```text
code-execute: run Python snippets -> file:///opt/agent/sandbox; exec-service://python
```

## Metadata

- name: agentCapability
- Nature: DataProperty
- Range: xsd:string
