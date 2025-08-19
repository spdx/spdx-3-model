SPDX-License-Identifier: Community-Spec-1.0
# agentCapabilities
## Summary
Describes the agent’s functional capabilities, their purposes, and the tools/integrations used to realize each capability.
## Description
Provides a structured listing of what the agent can do (e.g., search, web scraping, summarization, code execution), stating for each capability its purpose and which tools/services or modules it invokes to accomplish the action. Use concise entries—one capability per item. If no capabilities are defined, set to NONE; if it is unknown or undisclosed, set to NOASSERTION.

Recommended notation: <capability>: <purpose> -> <tool references>

*Examples*

- search: retrieve web results -> Google Search API; SerpAPI
- web-scrape: extract page content -> Playwright crawler; internal-scraper://v1
- summarize: condense retrieved docs -> OpenAI API (summarize endpoint)
- code-execute: run Python snippets -> file:///opt/agent/sandbox; exec-service://python

## Metadata

- name: agentCapabilities
- Nature: DataProperty
- Range: xsd: string
